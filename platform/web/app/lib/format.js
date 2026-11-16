// Number formatting and method metadata shared by the pages.

export const METHODS = ["LP", "NWC", "LCM", "VAM", "RS", "GA-rand", "GA-cost"];
export const METHOD_COLOR = {
  LP: "var(--m-lp)",
  NWC: "var(--m-nwc)",
  LCM: "var(--m-lcm)",
  VAM: "var(--m-vam)",
  RS: "var(--m-rs)",
  "GA-rand": "var(--m-ga-rand)",
  "GA-cost": "var(--m-ga-cost)",
};
export const METHOD_NAME = {
  ru: {
    LP: "ЛП (HiGHS)",
    NWC: "Северо-западный угол",
    LCM: "Минимальный элемент",
    VAM: "Аппроксимация Фогеля",
    RS: "Случайный поиск",
    "GA-rand": "ГА, случайный старт",
    "GA-cost": "ГА, старт с учётом стоимости",
  },
  en: {
    LP: "LP (HiGHS)",
    NWC: "North-west corner",
    LCM: "Least cost",
    VAM: "Vogel's approximation",
    RS: "Random search",
    "GA-rand": "GA, random start",
    "GA-cost": "GA, cost-aware start",
  },
};

export function num(value, digits = 2, lang = "ru") {
  if (value === null || value === undefined || Number.isNaN(value)) return "–";
  const abs = Math.abs(value);
  if (abs !== 0 && (abs >= 1e15 || abs < 1e-3)) return value.toExponential(2);
  return new Intl.NumberFormat(lang === "en" ? "en-US" : "ru-RU", { maximumFractionDigits: digits }).format(value);
}

/** Short form for large values (e.g. 141,7 млрд); the exact value belongs in a title attribute. */
export function compact(value, lang = "ru") {
  if (value === null || value === undefined || Number.isNaN(value)) return "–";
  if (Math.abs(value) < 1e6) return num(value, 2, lang);
  return new Intl.NumberFormat(lang === "en" ? "en-US" : "ru-RU", { notation: "compact", maximumFractionDigits: 3 }).format(value);
}

export const pct = (v, lang) => (v === null || v === undefined ? "–" : num(v, Math.abs(v) < 10 ? 2 : 1, lang) + " %");
export const sec = (v, lang) => (v === null || v === undefined ? "–" : v < 1 ? num(v * 1000, 1, lang) + " ms" : num(v, 2, lang) + " s");
