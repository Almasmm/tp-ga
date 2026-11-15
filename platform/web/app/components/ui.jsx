"use client";

import { useEffect, useRef } from "react";
import { AlertTriangle, Inbox, LoaderCircle, RotateCw } from "lucide-react";
import { useSettings } from "../providers";
import { METHOD_COLOR, METHOD_NAME } from "../lib/format";

export function PageHead({ kicker, title, children, actions }) {
  return (
    <header className="page-head">
      <div>
        {kicker && <div className="kicker">{kicker}</div>}
        <h1 className="page-title">{title}</h1>
        {children && <p>{children}</p>}
      </div>
      {actions && <div className="row">{actions}</div>}
    </header>
  );
}

export function Panel({ title, subtitle, actions, children, className = "", as: Tag = "section", ...rest }) {
  return (
    <Tag className={"panel " + className} {...rest}>
      {(title || actions) && (
        <div className="panel-head">
          <div>
            {title && <h2>{title}</h2>}
            {subtitle && <p>{subtitle}</p>}
          </div>
          {actions && <div className="row">{actions}</div>}
        </div>
      )}
      {children}
    </Tag>
  );
}

/** Loading, error and empty states with a clear message and an action. */
export function State({ status, error, onRetry, empty, emptyHint, children }) {
  const { t } = useSettings();
  if (status === "loading")
    return (
      <div className="state" role="status" aria-live="polite">
        <LoaderCircle className="spin" size={28} aria-hidden="true" />
        <span>{t("loading")}</span>
      </div>
    );
  if (status === "error") {
    const offline = error?.status === 0 || error?.message === "offline";
    return (
      <div className="state error" role="alert">
        <AlertTriangle size={28} aria-hidden="true" />
        <h3>{offline ? t("apiDown") : error?.status === 404 && empty ? empty : error?.message}</h3>
        {error?.status === 404 && emptyHint && <p className="code-value">{emptyHint}</p>}
        {onRetry && (
          <button className="secondary" onClick={onRetry}>
            <RotateCw size={16} aria-hidden="true" /> {t("retry")}
          </button>
        )}
      </div>
    );
  }
  if (status === "empty")
    return (
      <div className="state">
        <Inbox size={28} aria-hidden="true" />
        <h3>{empty ?? t("empty")}</h3>
        {emptyHint && <p className="code-value">{emptyHint}</p>}
      </div>
    );
  return children;
}

export function Segmented({ label, value, options, onChange }) {
  return (
    <div className="segmented" role="group" aria-label={label}>
      {options.map((o) => (
        <button key={o.value} type="button" aria-pressed={value === o.value} onClick={() => onChange(o.value)}>
          {o.icon}
          {o.label}
        </button>
      ))}
    </div>
  );
}

export function Field({ label, hint, children }) {
  return (
    <label className="field">
      {label}
      {children}
      {hint && <span className="hint">{hint}</span>}
    </label>
  );
}

export function Metric({ label, value, source }) {
  return (
    <div className="metric">
      <span className="value">{value}</span>
      <span className="label">{label}</span>
      {source && <span className="source">{source}</span>}
    </div>
  );
}

export function MethodLabel({ code, short = false }) {
  const { lang } = useSettings();
  return (
    <span>
      <i className="method-dot" style={{ background: METHOD_COLOR[code] }} aria-hidden="true" />
      {short ? code : METHOD_NAME[lang]?.[code] ?? code}
    </span>
  );
}

/** Modal confirmation with focus on the safe action and Escape to dismiss. */
export function ConfirmDialog({ open, title, text, confirm, cancel, onConfirm, onCancel }) {
  const safe = useRef(null);
  useEffect(() => {
    if (!open) return undefined;
    safe.current?.focus();
    const onKey = (e) => e.key === "Escape" && onCancel();
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open, onCancel]);
  if (!open) return null;
  return (
    <div className="dialog-backdrop" onClick={onCancel}>
      <div className="dialog" role="alertdialog" aria-modal="true" aria-labelledby="confirm-title" onClick={(e) => e.stopPropagation()}>
        <h2 id="confirm-title">{title}</h2>
        <p>{text}</p>
        <div className="dialog-actions">
          <button ref={safe} className="secondary" onClick={onCancel}>
            {cancel}
          </button>
          <button className="danger" onClick={onConfirm}>
            {confirm}
          </button>
        </div>
      </div>
    </div>
  );
}

export function Progress({ value, label }) {
  const v = Math.max(0, Math.min(1, value || 0));
  return (
    <div className="progress" role="progressbar" aria-label={label} aria-valuemin={0} aria-valuemax={100} aria-valuenow={Math.round(v * 100)}>
      <span style={{ width: `${v * 100}%` }} />
    </div>
  );
}

export function Source({ children }) {
  const { t } = useSettings();
  return (
    <span className="source">
      {t("source")}: <code>{children}</code>
    </span>
  );
}
