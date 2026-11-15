import { Google_Sans, JetBrains_Mono, Manrope } from "next/font/google";
import "leaflet/dist/leaflet.css";
import "./globals.css";
import { Providers } from "./providers";
import { Shell } from "./components/shell";

const manrope = Manrope({
  subsets: ["latin", "cyrillic", "cyrillic-ext"],
  weight: "variable",
  display: "swap",
  variable: "--manrope",
});
const googleSans = Google_Sans({
  subsets: ["latin", "cyrillic"],
  weight: ["400", "500", "600", "700"],
  display: "swap",
  adjustFontFallback: false,
  fallback: ["Manrope", "Arial", "sans-serif"],
  variable: "--google-sans",
});
const mono = JetBrains_Mono({ subsets: ["latin", "cyrillic"], weight: "variable", display: "swap", variable: "--jetbrains" });

export const metadata = {
  title: "tp-ga · транспортная задача и генетический алгоритм",
  description: "Исследование: генетический алгоритм с перестановочным кодированием и жадным декодером против точных и классических методов.",
};

export const viewport = { width: "device-width", initialScale: 1 };

export default function RootLayout({ children }) {
  return (
    <html lang="ru" data-theme="aspan" data-density="normal" className={[manrope.variable, googleSans.variable, mono.variable].join(" ")}>
      <body>
        <Providers>
          <Shell>{children}</Shell>
        </Providers>
      </body>
    </html>
  );
}
