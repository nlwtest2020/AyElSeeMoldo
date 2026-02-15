import { useState, useMemo } from 'react';
import type { ScheduleGrid } from './types';
import { DEFAULT_OFFSITE } from './types';
import type { OffSiteInputs } from './types';
import { calculate } from './calculations';
import { VisualScheduler } from './components/VisualScheduler';
import { RevenueCalculator } from './components/RevenueCalculator';
import { CalcBreakdown } from './components/CalcBreakdown';
import { TrendingUp, ChevronDown, ChevronUp, BookOpen } from 'lucide-react';

export default function App() {
  const [grid, setGrid]     = useState<ScheduleGrid>({});
  const [inputs, setInputs] = useState<OffSiteInputs>(DEFAULT_OFFSITE);
  const [showBreakdown, setShowBreakdown] = useState(false);

  const results = useMemo(() => calculate(grid, inputs), [grid, inputs]);

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 sticky top-0 z-50 shadow-sm">
        <div className="max-w-screen-2xl mx-auto px-6 py-3 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-gradient-to-br from-blue-500 to-emerald-500 rounded-lg">
              <TrendingUp className="w-5 h-5 text-white" />
            </div>
            <div>
              <div className="font-bold text-gray-900">Language Training Calculator</div>
              <div className="text-xs text-gray-500">Revenue & Capacity Planning Suite</div>
            </div>
          </div>

          {/* Top-line summary */}
          <div className="flex items-center gap-6 text-sm">
            <Kpi label="Revenue" value={results.totalRevenue} />
            <Kpi label="Costs" value={results.totalCosts} />
            <Kpi label="Net Profit" value={results.netProfit} highlight />
            <div className="text-center">
              <div className="text-xs text-gray-400 uppercase tracking-wide">Margin</div>
              <div className={`font-bold text-lg ${results.profitMargin >= 0 ? 'text-emerald-600' : 'text-red-600'}`}>
                {results.profitMargin.toFixed(1)}%
              </div>
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-screen-2xl mx-auto px-6 py-6">
        {/* Visual Scheduler */}
        <section className="mb-6">
          <VisualScheduler grid={grid} onChange={setGrid} />
        </section>

        {/* Calculator (off-site inputs + OE summary + totals) */}
        <section className="mb-6">
          <RevenueCalculator inputs={inputs} results={results} onChange={setInputs} />
        </section>

        {/* Calculation Methodology (collapsible) */}
        <section>
          <button
            onClick={() => setShowBreakdown(!showBreakdown)}
            className="flex items-center gap-2 px-4 py-2.5 bg-white border border-gray-200 rounded-xl shadow-sm text-sm font-medium text-gray-600 hover:bg-gray-50 transition-colors w-full mb-3"
          >
            <BookOpen className="w-4 h-4 text-blue-500" />
            How are these numbers calculated?
            <span className="ml-auto">
              {showBreakdown ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
            </span>
          </button>
          {showBreakdown && <CalcBreakdown />}
        </section>
      </main>

      <footer className="border-t border-gray-200 bg-white mt-12">
        <div className="max-w-screen-2xl mx-auto px-6 py-4 text-xs text-gray-400 text-center">
          Language Training Revenue & Capacity Calculator • Overhead rates from MOD 5-year historical average (FY20-25)
        </div>
      </footer>
    </div>
  );
}

function Kpi({ label, value, highlight }: { label: string; value: number; highlight?: boolean }) {
  const formatted = new Intl.NumberFormat('en-US', {
    style: 'currency', currency: 'USD', minimumFractionDigits: 0,
  }).format(Math.abs(value));
  const display = value < 0 ? `-${formatted}` : formatted;
  const color = highlight
    ? value >= 0 ? 'text-emerald-600' : 'text-red-600'
    : 'text-gray-800';
  return (
    <div className="text-center">
      <div className="text-xs text-gray-400 uppercase tracking-wide">{label}</div>
      <div className={`font-bold text-lg ${color}`}>{display}</div>
    </div>
  );
}
