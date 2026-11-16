"use client";

import { useState } from "react";
import { useSettings } from "../providers";
import { useApi } from "../lib/use-api";
import { useAsync } from "../lib/use-async";
import { apiText } from "../lib/api";
import { num } from "../lib/format";
import { Field, PageHead, Panel, Source, State } from "../components/ui";
import { Markdown } from "../components/markdown";

const DOC_TITLE = {
  PREREGISTRATION: ["Предрегистрация", "Pre-registration"],
  METHODS_v2: ["Методика v0.4", "Methods v0.4"],
  HEAVY_RUN: ["Подготовка ноутбука к прогону", "Preparing the laptop"],
  PILOT: ["Пилотный прогон и оценка времени", "Pilot and time estimate"],
  GPU: ["Прототип на GPU", "GPU prototype"],
  AUDIT: ["Аудит перед v0.4", "Audit before v0.4"],
};
const STEPS = [
  "git clone … && cd tp-ga && git checkout v0.4.0",
  "python -m venv .venv && .venv\\Scripts\\activate && pip install -e .[dev]",
  "tpga-exp doctor --config experiments/paper-v2.yaml",
  "tpga-exp run --config experiments/paper-v2.yaml",
  "tpga-exp report --config experiments/paper-v2.yaml",
];

function Doc({ name }) {
  const doc = useAsync(name, () => apiText(`/artifacts/v2/docs/${name}`));
  return (
    <State status={doc.status} error={doc.error} onRetry={doc.reload}>
      {doc.data && <Markdown text={doc.data} />}
    </State>
  );
}

export default function ReproducibilityPage() {
  const { t, lang } = useSettings();
  const en = lang === "en";
  const L = en ? 1 : 0;
  const rep = useApi("/artifacts/v2/reproducibility");
  const index = useApi("/artifacts/v2");
  const docs = index.data?.docs ?? [];
  const [doc, setDoc] = useState("PREREGISTRATION");
  const r = rep.data;
  const params = Object.entries(r?.tuned?.parameters ?? {});

  return (
    <>
      <PageHead kicker={t("navResearch")} title={t("reproducibility")}>
        {en
          ? "What fixes the v0.4 results: the configuration and the frozen tuned parameters (with their SHA-256), the instance manifest, the pre-registration and the commands that rebuild everything."
          : "Что фиксирует результаты v0.4: конфигурация и замороженные настроенные параметры (с SHA-256), манифест задач, предрегистрация и команды, которые всё воспроизводят."}
      </PageHead>
      <State status={rep.status} error={rep.error} onRetry={rep.reload}>
        {r && (
          <div className="stack">
            <Panel title={en ? "Fixed files" : "Зафиксированные файлы"}>
              <div className="table-wrap">
                <table>
                  <thead><tr><th>{en ? "file" : "файл"}</th><th>SHA-256</th></tr></thead>
                  <tbody>
                    {Object.entries(r.configs).map(([k, c]) => (
                      <tr key={k}><td><code>{c.file}</code></td><td className="code-value">{c.exists ? c.sha256 : (en ? "missing" : "нет файла")}</td></tr>
                    ))}
                  </tbody>
                </table>
              </div>
              <p className="meta" style={{ marginTop: 8 }}>
                {r.instances
                  ? (en ? `Test instances: ${r.instances.count} (` : `Тестовых задач: ${r.instances.count} (`) + Object.entries(r.instances.sets).map(([s, n]) => `${s} ${n}`).join(", ") + ")"
                  : (en ? "The instance manifest is created by the first run." : "Манифест задач создаётся при первом запуске.")}
                {r.run.invocations > 0 && ` · ${en ? "run invocations" : "запусков команды"}: ${r.run.invocations}, commit ${r.run.first?.git_commit ?? "–"}`}
              </p>
            </Panel>
            <Panel title={en ? "Frozen tuned parameters" : "Замороженные настроенные параметры"}
              subtitle={r.tuned ? `${en ? "frozen" : "заморожены"} ${r.tuned.frozen ?? "–"} · ${en ? "training instances" : "обучающих задач"}: ${r.tuned.training_instances} · TPE, ${r.tuned.procedure?.trials ?? "–"} ${en ? "trials per method" : "испытаний на метод"}` : undefined}>
              {params.length === 0 ? (
                <State status="empty" empty={en ? "Tuning has not been run yet" : "Настройка ещё не выполнялась"} emptyHint="tpga-exp tune --config experiments/paper-v2.yaml" />
              ) : (
                <div className="table-wrap">
                  <table>
                    <thead><tr><th>{en ? "method" : "метод"}</th><th>{en ? "parameters" : "параметры"}</th><th className="num">{en ? "training mean gap, %" : "среднее откл. на обучении, %"}</th></tr></thead>
                    <tbody>
                      {params.map(([m, p]) => (
                        <tr key={m}>
                          <td>{m}</td>
                          <td className="code-value">{Object.entries(p).map(([k, v]) => `${k}=${typeof v === "number" ? num(v, 4, "en") : v}`).join(", ")}</td>
                          <td className="num">{num(r.tuned.best_objective?.[m], 3, lang)}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
              <Source>experiments/tuned-v2.yaml</Source>
            </Panel>
            <Panel title={en ? "Rebuild the results" : "Как воспроизвести"}>
              <ol className="stack" style={{ margin: 0, paddingLeft: 20 }}>
                {STEPS.map((s) => <li key={s}><code>{s}</code></li>)}
              </ol>
            </Panel>
            <Panel title={en ? "Documents" : "Документы"} actions={docs.length > 0 && (
              <Field label={<span className="sr-only">{en ? "Document" : "Документ"}</span>}>
                <select aria-label={en ? "Document" : "Документ"} value={docs.includes(doc) ? doc : docs[0]} onChange={(e) => setDoc(e.target.value)}>
                  {docs.map((d) => <option key={d} value={d}>{DOC_TITLE[d]?.[L] ?? d}</option>)}
                </select>
              </Field>)}>
              {docs.length === 0 ? <State status="empty" empty={en ? "No documents yet" : "Документов пока нет"} /> : <Doc key={doc} name={docs.includes(doc) ? doc : docs[0]} />}
            </Panel>
          </div>
        )}
      </State>
    </>
  );
}
