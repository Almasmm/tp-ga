"use client";

import { useEffect, useState } from "react";
import { AlertTriangle } from "lucide-react";
import { useSettings } from "../providers";
import { api } from "../lib/api";
import { num, pct } from "../lib/format";
import { Metric, PageHead, Panel, Progress, Source, State } from "../components/ui";

const POLL_MS = 3000;

function duration(s, en) {
  if (s === null || s === undefined || !Number.isFinite(s)) return "–";
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  if (h >= 24) return en ? `${Math.floor(h / 24)} d ${h % 24} h` : `${Math.floor(h / 24)} д ${h % 24} ч`;
  if (h > 0) return en ? `${h} h ${m} min` : `${h} ч ${m} мин`;
  return en ? `${m} min ${Math.floor(s % 60)} s` : `${m} мин ${Math.floor(s % 60)} с`;
}

/** Polls the state file of the runner; stops polling while the tab is hidden. */
function useMonitor() {
  const [res, setRes] = useState({ status: "loading", data: null, error: null });
  useEffect(() => {
    let alive = true;
    let timer;
    const tick = async () => {
      if (document.visibilityState === "visible") {
        try {
          const data = await api("/monitor/state");
          if (alive) setRes({ status: "ok", data, error: null });
        } catch (error) {
          if (alive) setRes((r) => ({ status: r.data ? "ok" : "error", data: r.data, error }));
        }
      }
      if (alive) timer = setTimeout(tick, POLL_MS);
    };
    tick();
    return () => {
      alive = false;
      clearTimeout(timer);
    };
  }, []);
  return res;
}

export default function MonitorPage() {
  const { t, lang } = useSettings();
  const en = lang === "en";
  const { status, data, error } = useMonitor();
  const s = data?.state;
  const overall = s?.overall ?? {};
  const phase = s?.phase_progress ?? {};
  const cpu = s?.system?.cpu_percent ?? [];

  return (
    <>
      <PageHead kicker={t("navResearch")} title={t("monitor")}>
        {en
          ? "Progress of the v0.4 run, read from the state file the runner rewrites every few seconds. The page cannot start, stop or change the run: stop it with Ctrl+C in its terminal."
          : "Ход прогона v0.4 по файлу состояния, который программа прогона перезаписывает каждые несколько секунд. Страница не может запустить, остановить или изменить прогон: останавливают его Ctrl+C в его терминале."}
      </PageHead>
      <State status={status} error={error}>
        {data && !data.available ? (
          <Panel><State status="empty" empty={en ? "No run is writing its state" : "Ни один прогон не пишет своё состояние"}
            emptyHint="tpga-exp run --config experiments/paper-v2.yaml" /></Panel>
        ) : s ? (
          <div className="stack">
            {data.stale && (
              <div className="state error" role="alert" style={{ padding: 16 }}>
                <AlertTriangle size={20} aria-hidden="true" />
                <span>{en
                  ? `The state was last written ${duration(data.age_s, en)} ago: the run has probably stopped. Restart the same command to resume.`
                  : `Состояние записано ${duration(data.age_s, en)} назад: прогон, вероятно, остановлен. Повторите ту же команду, чтобы продолжить.`}</span>
              </div>
            )}
            {s.message && <p className="meta" role="status">{s.message}</p>}
            <div className="grid grid-4">
              <Metric label={en ? "phase" : "фаза"} value={s.phase ?? "–"} />
              <Metric label={en ? "runs done (all phases)" : "запусков (все фазы)"} value={`${num(overall.done, 0, lang)} / ${num(overall.total, 0, lang)}`} />
              <Metric label={en ? "remaining in the phase" : "до конца фазы"} value={duration(phase.eta_s, en)} />
              <Metric label={en ? "errors" : "ошибки"} value={num(s.counts?.errors ?? 0, 0, lang)} source="logs/errors.jsonl" />
            </div>
            <Panel title={en ? "Progress" : "Прогресс"}>
              <div className="stack">
                <div>
                  <div className="row" style={{ justifyContent: "space-between" }}><span>{en ? "Phase" : "Фаза"} {s.phase}</span>
                    <span className="meta">{num(phase.done, 0, lang)} / {num(phase.total, 0, lang)} · {num(phase.rate_per_min, 1, lang)} {en ? "runs/min" : "запусков/мин"}</span></div>
                  <Progress value={phase.total ? phase.done / phase.total : 0} label={en ? "phase progress" : "прогресс фазы"} />
                </div>
                <div>
                  <div className="row" style={{ justifyContent: "space-between" }}><span>{en ? "All requested phases" : "Все запрошенные фазы"}</span>
                    <span className="meta">{duration(overall.elapsed_s, en)} {en ? "elapsed" : "прошло"}</span></div>
                  <Progress value={overall.total ? overall.done / overall.total : 0} label={en ? "overall progress" : "общий прогресс"} />
                </div>
              </div>
            </Panel>
            <Panel title={en ? "Runs in progress" : "Выполняются сейчас"} subtitle={en ? "One process per logical processor" : "Один процесс на логический процессор"}>
              {(s.workers ?? []).length === 0 ? <State status="empty" empty={en ? "No runs in progress" : "Нет выполняющихся запусков"} /> : (
                <div className="table-wrap" style={{ maxHeight: 420 }}>
                  <table>
                    <thead><tr>
                      <th className="num">CPU</th><th>{en ? "method" : "метод"}</th><th>{en ? "instance" : "задача"}</th><th className="num">seed</th>
                      <th className="num">{en ? "decoder calls" : "вызовы декодера"}</th><th className="num">{en ? "best gap" : "лучшее откл."}</th><th className="num">{en ? "running" : "идёт"}</th>
                    </tr></thead>
                    <tbody>
                      {s.workers.map((w, i) => (
                        <tr key={`${w.cpu}-${i}`}>
                          <td className="num">{w.cpu ?? "–"}</td><td>{w.method}</td><td>{w.instance}</td><td className="num">{w.seed ?? "–"}</td>
                          <td className="num">{w.budget ? `${Math.round((100 * (w.evals ?? 0)) / w.budget)} %` : "–"}</td>
                          <td className="num">{pct(w.best_gap, lang)}</td><td className="num">{duration(w.running_s, en)}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </Panel>
            <div className="grid grid-2">
              <Panel title={en ? "Recently finished" : "Недавно завершены"}>
                {(s.recent ?? []).length === 0 ? <State status="empty" empty="–" /> : (
                  <div className="table-wrap" style={{ maxHeight: 320 }}>
                    <table>
                      <thead><tr><th>{en ? "method" : "метод"}</th><th>{en ? "instance" : "задача"}</th><th className="num">{en ? "gap" : "откл."}</th><th className="num">{en ? "time" : "время"}</th></tr></thead>
                      <tbody>{s.recent.map((r, i) => (
                        <tr key={i}><td>{r.method}</td><td>{r.instance}</td><td className="num">{pct(r.gap, lang)}</td><td className="num">{num(r.time_s, 2, lang)} s</td></tr>
                      ))}</tbody>
                    </table>
                  </div>
                )}
              </Panel>
              <Panel title={en ? "Machine" : "Машина"}>
                <div className="grid grid-2">
                  <Metric label={en ? "mean CPU load" : "средняя загрузка CPU"} value={cpu.length ? `${num(cpu.reduce((a, b) => a + b, 0) / cpu.length, 0, lang)} %` : "–"} />
                  <Metric label={en ? "free RAM" : "свободная ОЗУ"} value={s.system?.ram_free_gb !== undefined ? `${num(s.system.ram_free_gb, 1, lang)} GB` : "–"} />
                  <Metric label={en ? "free disk" : "свободный диск"} value={s.system?.disk_free_gb !== undefined ? `${num(s.system.disk_free_gb, 0, lang)} GB` : "–"} />
                  <Metric label={en ? "CPU temperature" : "температура CPU"} value={s.system?.temperature !== null && s.system?.temperature !== undefined ? `${num(s.system.temperature, 0, lang)} °C` : "–"} />
                </div>
              </Panel>
            </div>
            <Source>paper_artifacts_v2/state/monitor.json</Source>
          </div>
        ) : null}
      </State>
    </>
  );
}
