"use client";

import { useState } from "react";
import { useSettings } from "../providers";
import { apiText } from "../lib/api";
import { useApi } from "../lib/use-api";
import { useAsync } from "../lib/use-async";
import { PageHead, Panel, Segmented, Source, State } from "../components/ui";
import { Markdown } from "../components/markdown";

const COMMANDS = `python -m venv .venv
.venv\\Scripts\\activate
pip install -e ".[dev]"
python -m tpga.experiments.run --config experiments/paper.yaml
python -m tpga.experiments.report --config experiments/paper.yaml`;

function Doc({ name }) {
  const doc = useAsync(name, () => apiText(`/artifacts/docs/${name}`));
  return (
    <State status={doc.status} error={doc.error} onRetry={doc.reload}>
      {doc.data && <Markdown text={doc.data} />}
    </State>
  );
}

export default function MethodsPage() {
  const { t, lang } = useSettings();
  const index = useApi("/artifacts");
  const [doc, setDoc] = useState("METHODS");
  const docs = index.data?.docs ?? [];
  return (
    <>
      <PageHead kicker={t("navResearch")} title={lang === "en" ? "Methodology and reproducibility" : "Методика и воспроизводимость"}>
        {lang === "en" ? "Generated documents of the experiment, the recorded environment and the commands that reproduce every artifact." : "Сгенерированные документы эксперимента, записанное окружение и команды, которые воспроизводят все артефакты."}
      </PageHead>
      <div className="split" style={{ gridTemplateColumns: "minmax(0, 1fr) minmax(280px, 380px)" }}>
        <Panel title={doc === "LIMITATIONS" ? t("limitations") : doc}
          actions={docs.length > 0 && <Segmented label="docs" value={doc} onChange={setDoc} options={docs.map((d) => ({ value: d, label: d }))} />}>
          <State status={index.status} error={index.error} onRetry={index.reload} empty={t("noArtifacts")} emptyHint={t("noArtifactsHint")}>
            {docs.includes(doc) ? <Doc name={doc} /> : <State status="empty" empty={t("noArtifacts")} emptyHint={t("noArtifactsHint")} />}
            <Source>{`paper_artifacts/${doc}.md`}</Source>
          </State>
        </Panel>
        <div className="stack">
          <Panel title={t("reproduce")}>
            <pre><code>{COMMANDS}</code></pre>
          </Panel>
          <Panel title={t("environment")}>
            <State status={index.status} error={index.error} onRetry={index.reload}>
              {index.data?.environment ? (
                <pre style={{ maxHeight: 420 }}><code>{JSON.stringify(index.data.environment, null, 1)}</code></pre>
              ) : (
                <State status="empty" />
              )}
              <Source>paper_artifacts/environment.json</Source>
            </State>
          </Panel>
        </div>
      </div>
    </>
  );
}
