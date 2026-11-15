"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useMemo, useState } from "react";
import {
  BookOpenText, Boxes, Dna, FlaskConical, Languages, LayoutDashboard, ListOrdered, Map, Menu, Microscope,
  Search, Settings2, Truck, X,
} from "lucide-react";
import { useSettings } from "../providers";
import { SettingsDialog } from "./settings-dialog";

const NAV = [
  { section: "navResearch", items: [
    { href: "/", key: "overview", icon: LayoutDashboard, tile: "tile-blue" },
    { href: "/experiment", key: "experiment", icon: FlaskConical, tile: "tile-indigo" },
    { href: "/methods", key: "methods", icon: BookOpenText, tile: "tile-slate" },
  ] },
  { section: "navLearn", items: [
    { href: "/decoder", key: "decoder", icon: ListOrdered, tile: "tile-teal" },
    { href: "/classical", key: "classical", icon: Boxes, tile: "tile-amber" },
    { href: "/ga", key: "ga", icon: Dna, tile: "tile-rose" },
  ] },
  { section: "navTools", items: [
    { href: "/map", key: "map", icon: Map, tile: "tile-cyan" },
    { href: "/lab", key: "lab", icon: Microscope, tile: "tile-violet" },
  ] },
];

export function Shell({ children }) {
  const { t, lang, update } = useSettings();
  const path = usePathname();
  const [openAt, setOpenAt] = useState(null); // the menu closes by itself when the page changes
  const open = openAt === path;
  const setOpen = (v) => setOpenAt(v ? path : null);
  const [settings, setSettings] = useState(false);
  const [query, setQuery] = useState("");
  const flat = useMemo(() => NAV.flatMap((s) => s.items), []);
  const matches = query.trim()
    ? flat.filter((i) => t(i.key).toLowerCase().includes(query.trim().toLowerCase()))
    : [];

  return (
    <div className="app">
      <a className="skip-link" href="#content">{t("skip")}</a>
      <aside className="sidebar" data-open={open} aria-label={t("menu")}>
        <div className="row" style={{ justifyContent: "space-between" }}>
          <Link href="/" className="brand">
            <span className="brand-mark"><Truck size={19} aria-hidden="true" /></span>
            <span><b>{t("appName")}</b><small>{t("appSub")}</small></span>
          </Link>
          <button className="ghost icon menu-button" style={{ color: "#fff" }} onClick={() => setOpen(false)} aria-label={t("close")}>
            <X size={18} aria-hidden="true" />
          </button>
        </div>
        <nav className="nav">
          {NAV.map((section) => (
            <div key={section.section} className="nav">
              <div className="nav-section">{t(section.section)}</div>
              {section.items.map(({ href, key, icon: Icon, tile }) => (
                <Link key={href} href={href} aria-current={path === href ? "page" : undefined}>
                  <span className={"tile " + tile}><Icon size={16} aria-hidden="true" /></span>
                  {t(key)}
                </Link>
              ))}
            </div>
          ))}
        </nav>
        <div className="sidebar-foot">
          Astana IT University · <span className="code-value">tp-ga 0.3.0</span>
        </div>
      </aside>
      <div className="main">
        <header className="topbar">
          <button className="secondary icon menu-button" onClick={() => setOpen(true)} aria-label={t("menu")} aria-expanded={open}>
            <Menu size={18} aria-hidden="true" />
          </button>
          <div className="search" role="search">
            <Search size={17} aria-hidden="true" />
            <input
              type="search"
              aria-label={t("search")}
              placeholder={t("search")}
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={(e) => e.key === "Escape" && setQuery("")}
            />
            {matches.length > 0 && (
              <ul className="search-results">
                {matches.map((m) => (
                  <li key={m.href}><Link href={m.href} onClick={() => setQuery("")}>{t(m.key)}</Link></li>
                ))}
              </ul>
            )}
          </div>
          <div className="topbar-actions">
            <button
              className="secondary"
              onClick={() => update({ lang: lang === "ru" ? "en" : "ru" })}
              aria-label={t("language")}
              title={t("language")}
            >
              <Languages size={16} aria-hidden="true" /> {lang === "ru" ? "EN" : "RU"}
            </button>
            <button className="secondary icon" onClick={() => setSettings(true)} aria-label={t("settings")} title={t("settings")}>
              <Settings2 size={17} aria-hidden="true" />
            </button>
          </div>
        </header>
        <main id="content" className="workspace" tabIndex={-1}>
          {children}
        </main>
      </div>
      <SettingsDialog open={settings} onClose={() => setSettings(false)} />
    </div>
  );
}
