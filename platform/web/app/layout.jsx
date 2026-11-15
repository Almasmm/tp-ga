import { Google_Sans, JetBrains_Mono, Manrope } from "next/font/google";
import "leaflet/dist/leaflet.css";
import "./globals.css";

const manrope = Manrope({
  subsets: ["latin", "cyrillic", "cyrillic-ext"], display: "swap", variable: "--manrope",
});
const googleSans = Google_Sans({
  subsets: ["latin", "cyrillic"], weight: ["400", "500", "600", "700"], display: "swap", adjustFontFallback: false, variable: "--google-sans",
});
const mono = JetBrains_Mono({
  subsets: ["latin", "cyrillic"], display: "swap", variable: "--jetbrains",
});

export const metadata = {
  title: "tp-ga · Планирование поставок",
  description: "Сценарии поставок по Астане и сравнение алгоритмов оптимизации.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="ru" className={[manrope.variable, googleSans.variable, mono.variable].join(" ")}>
      <body>{children}</body>
    </html>
  );
}

