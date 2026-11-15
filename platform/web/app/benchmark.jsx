import { Download } from "lucide-react";
import { format } from "./visuals";

const meanGap = (runs, method) => {
  const selected = runs.filter((row) => row.initialization === method && row.gap_percent != null);
  return selected.length ? selected.reduce((total, row) => total + row.gap_percent, 0) / selected.length : null;
};
const percent = (value) => value == null ? "—" : format(value, 2) + "%";

export default function Benchmark({ report, scenarios, choose, dataset }) {
  if (!report) return null;
  const { summary, protocol } = report;
  const scale = Math.max(summary.mean_gap_before_percent, summary.mean_gap_after_percent, 1);
  return <section className="panel benchmark">
    <div className="panel-head">
      <div><h2>Серия по всем сценариям</h2>
        <p>{summary.scenarios} задач · {protocol.seeds.length} seed на метод · {protocol.population} особи · {protocol.generations} поколений</p></div>
      <a className="secondary benchmark-download" href={"/api/scenarios/benchmark?dataset_id=" + dataset}
        download={dataset + "-benchmark.json"}><Download size={16} /> JSON</a>
    </div>
    <div className="benchmark-summary">
      <div><span>Средний разрыв до</span><strong>{percent(summary.mean_gap_before_percent)}</strong>
        <i style={{ width: 100 * summary.mean_gap_before_percent / scale + "%" }} /></div>
      <div><span>Средний разрыв после</span><strong>{percent(summary.mean_gap_after_percent)}</strong>
        <i style={{ width: 100 * summary.mean_gap_after_percent / scale + "%" }} /></div>
      <div><span>Сценарии с улучшением</span><strong>{summary.improved_scenarios} / {summary.scenarios}</strong></div>
    </div>
    <details className="benchmark-details">
      <summary>Таблица всех сценариев</summary>
      <div className="table-scroll"><table>
        <thead><tr><th>Сценарий</th><th>Точный оптимум, ₸</th><th>До</th><th>После</th></tr></thead>
        <tbody>{report.scenarios.map((row) => {
          const scenario = scenarios.find((item) => item.id === row.id);
          return <tr key={row.id}><td><button className="text-button" onClick={() => choose(row.id)}>
            {scenario?.title ?? row.id}</button></td>
            <td className="code-value">{format(row.lp_cost_kzt, 2)}</td>
            <td className="code-value">{percent(meanGap(row.runs, "random"))}</td>
            <td className="code-value">{percent(meanGap(row.runs, "cost-aware"))}</td></tr>;
        })}</tbody>
      </table></div>
      <p className="panel-note">Значения «до» и «после» — средний процентный разрыв с HiGHS по трём прогонам на сценарий.</p>
    </details>
  </section>;
}

