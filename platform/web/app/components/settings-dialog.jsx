"use client";

import { useEffect, useRef } from "react";
import { useSettings } from "../providers";
import { Field, Segmented } from "./ui";

export function SettingsDialog({ open, onClose }) {
  const { settings, update, t } = useSettings();
  const first = useRef(null);
  useEffect(() => {
    if (!open) return undefined;
    first.current?.querySelector("button")?.focus();
    const onKey = (e) => e.key === "Escape" && onClose();
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open, onClose]);
  if (!open) return null;
  return (
    <div className="dialog-backdrop" onClick={onClose}>
      <div className="dialog" role="dialog" aria-modal="true" aria-labelledby="settings-title" onClick={(e) => e.stopPropagation()}>
        <h2 id="settings-title">{t("settings")}</h2>
        <div className="stack" ref={first}>
          <Field label={t("theme")} hint={settings.lang === "ru" ? "На телефоне всегда Aspan" : "Phones always use Aspan"}>
            <Segmented label={t("theme")} value={settings.theme} onChange={(v) => update({ theme: v })}
              options={[{ value: "aspan", label: "Aspan" }, { value: "astana", label: "Astana" }]} />
          </Field>
          <Field label={t("textScale")}>
            <Segmented label={t("textScale")} value={settings.scale} onChange={(v) => update({ scale: v })}
              options={[{ value: "93", label: "93,3 %" }, { value: "100", label: "100 %" }, { value: "113", label: "113,3 %" }]} />
          </Field>
          <Field label={t("density")}>
            <Segmented label={t("density")} value={settings.density} onChange={(v) => update({ density: v })}
              options={[{ value: "compact", label: t("compact") }, { value: "normal", label: t("normal") }, { value: "spacious", label: t("spacious") }]} />
          </Field>
          <Field label={`${t("tileSaturation")}: ${settings.saturation} %`}>
            <input type="range" min={0} max={150} step={10} value={settings.saturation}
              onChange={(e) => update({ saturation: Number(e.target.value) })} />
          </Field>
          <Field label={t("language")}>
            <Segmented label={t("language")} value={settings.lang} onChange={(v) => update({ lang: v })}
              options={[{ value: "ru", label: "Русский" }, { value: "en", label: "English" }]} />
          </Field>
        </div>
        <div className="dialog-actions">
          <button onClick={onClose}>{t("close")}</button>
        </div>
      </div>
    </div>
  );
}
