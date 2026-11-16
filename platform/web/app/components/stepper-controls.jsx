"use client";

import { ChevronLeft, ChevronRight, Pause, Play, RotateCcw } from "lucide-react";
import { useSettings } from "../providers";

export function StepperControls({ stepper, total }) {
  const { t } = useSettings();
  const { k, playing, toggle, next, prev, reset, speed, setSpeed } = stepper;
  return (
    <div className="row" role="group" aria-label={t("step")}>
      <button className="secondary icon" onClick={reset} aria-label={t("reset")} title={t("reset")}><RotateCcw size={16} aria-hidden="true" /></button>
      <button className="secondary" onClick={prev} disabled={k === 0}><ChevronLeft size={16} aria-hidden="true" />{t("back")}</button>
      <button onClick={toggle} aria-pressed={playing}>
        {playing ? <Pause size={16} aria-hidden="true" /> : <Play size={16} aria-hidden="true" />}
        {playing ? t("pause") : t("play")}
      </button>
      <button className="secondary" onClick={next} disabled={k >= total}>{t("step")}<ChevronRight size={16} aria-hidden="true" /></button>
      <label className="field" style={{ flexDirection: "row", alignItems: "center", gap: 8, marginLeft: 8 }}>
        {t("speed")}
        <input type="range" min={0.5} max={8} step={0.5} value={speed} onChange={(e) => setSpeed(Number(e.target.value))} aria-valuetext={`${speed}/s`} />
        <span className="code-value">{speed}/s</span>
      </label>
      <span className="meta" aria-live="polite">{t("stepOf", { a: k, b: total })}</span>
    </div>
  );
}
