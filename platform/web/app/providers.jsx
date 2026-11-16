"use client";

import { createContext, useContext, useEffect, useMemo, useSyncExternalStore } from "react";
import { translate } from "./lib/i18n";

const DEFAULTS = Object.freeze({ theme: "aspan", scale: "100", density: "normal", saturation: 100, lang: "ru" });
const SCALE = { "93": 0.933, "100": 1, "113": 1.133 };
const KEY = "tpga-settings";
const Settings = createContext(null);

// Settings live in localStorage, read through useSyncExternalStore. Every access is guarded:
// with storage blocked the defaults apply and changes last for the session only.
const listeners = new Set();
let memory = null; // used when localStorage is unavailable
let cachedRaw;
let cached = DEFAULTS;

function readRaw() {
  try {
    return window.localStorage.getItem(KEY);
  } catch {
    return memory;
  }
}

function snapshot() {
  const raw = readRaw();
  if (raw !== cachedRaw) {
    cachedRaw = raw;
    try {
      const data = raw ? JSON.parse(raw) : {};
      cached = { ...DEFAULTS, ...(data && typeof data === "object" ? data : {}) };
    } catch {
      cached = DEFAULTS;
    }
  }
  return cached;
}

function subscribe(listener) {
  listeners.add(listener);
  const onStorage = (e) => e.key === KEY && listener();
  window.addEventListener("storage", onStorage);
  return () => {
    listeners.delete(listener);
    window.removeEventListener("storage", onStorage);
  };
}

function update(patch) {
  const next = JSON.stringify({ ...snapshot(), ...patch });
  try {
    window.localStorage.setItem(KEY, next);
  } catch {
    memory = next;
  }
  listeners.forEach((l) => l());
}

export function Providers({ children }) {
  const settings = useSyncExternalStore(subscribe, snapshot, () => DEFAULTS);
  useEffect(() => {
    const root = document.documentElement;
    root.dataset.theme = settings.theme;
    root.dataset.density = settings.density;
    root.style.setProperty("--text-scale", String(SCALE[settings.scale] ?? 1));
    root.style.setProperty("--tile-sat", String(Number(settings.saturation) / 100));
    root.lang = settings.lang;
  }, [settings]);
  const value = useMemo(
    () => ({ settings, update, lang: settings.lang, t: (key, vars) => translate(settings.lang, key, vars) }),
    [settings],
  );
  return <Settings.Provider value={value}>{children}</Settings.Provider>;
}

export function useSettings() {
  const ctx = useContext(Settings);
  if (!ctx) throw new Error("useSettings outside Providers");
  return ctx;
}
