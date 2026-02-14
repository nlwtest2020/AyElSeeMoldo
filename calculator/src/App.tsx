import { useState, useMemo } from 'react';
import type { ScenarioInputs } from './types';
import { DEFAULT_INPUTS } from './types';
import { calculateScenario } from './calculations';
import { ScenarioPanel } from './components/ScenarioPanel';
import { ComparisonPanel } from './components/ComparisonPanel';
import { CapacityView } from './components/CapacityView';
import { CostBreakdown } from './components/CostBreakdown';
import { Calculator, BarChart3, RefreshCw, ChevronDown, ChevronUp } from 'lucide-react';

function App() {
  const [currentInputs, setCurrentInputs] = useState<ScenarioInputs>(DEFAULT_INPUTS);
  const [goalInputs, setGoalInputs] = useState<ScenarioInputs>({
    ...DEFAULT_INPUTS,
    oeClasses: 15,
    oeStudentsPerClass: 10,
    privateStudents: 12,
  });

  const [showAdvanced, setShowAdvanced] = useState(false);

  const currentResults = useMemo(() => calculateScenario(currentInputs), [currentInputs]);
  const goalResults = useMemo(() => calculateScenario(goalInputs), [goalInputs]);

  const resetToDefaults = () => {
    setCurrentInputs(DEFAULT_INPUTS);
    setGoalInputs({
      ...DEFAULT_INPUTS,
      oeClasses: 15,
      oeStudentsPerClass: 10,
      privateStudents: 12,
    });
  };

  const copyGoalToCurrent = () => {
    setCurrentInputs({ ...goalInputs });
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 sticky top-0 z-50">
        <div className="max-w-[1800px] mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="p-2 bg-gradient-to-br from-blue-500 to-emerald-500 rounded-lg">
                <Calculator className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-gray-900">Revenue & Capacity Calculator</h1>
                <p className="text-sm text-gray-500">Model current vs. goal scenarios with full cost accounting</p>
              </div>
            </div>
            <div className="flex items-center gap-2">
              <button
                onClick={copyGoalToCurrent}
                className="px-3 py-2 text-sm font-medium text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg transition-colors flex items-center gap-2"
              >
                <RefreshCw className="w-4 h-4" />
                Goal → Current
              </button>
              <button
                onClick={resetToDefaults}
                className="px-3 py-2 text-sm font-medium text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg transition-colors"
              >
                Reset
              </button>
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-[1800px] mx-auto px-6 py-8">
        {/* Quick Stats */}
        <div className="grid grid-cols-4 gap-4 mb-8">
          <QuickStat
            label="Current Net Profit"
            value={currentResults.netProfit}
            isCurrency
            color={currentResults.netProfit >= 0 ? 'emerald' : 'red'}
          />
          <QuickStat
            label="Goal Net Profit"
            value={goalResults.netProfit}
            isCurrency
            color={goalResults.netProfit >= 0 ? 'emerald' : 'red'}
          />
          <QuickStat
            label="Profit Difference"
            value={goalResults.netProfit - currentResults.netProfit}
            isCurrency
            showSign
            color={goalResults.netProfit >= currentResults.netProfit ? 'emerald' : 'red'}
          />
          <QuickStat
            label="Margin Improvement"
            value={goalResults.profitMargin - currentResults.profitMargin}
            suffix="pts"
            showSign
            color={goalResults.profitMargin >= currentResults.profitMargin ? 'emerald' : 'red'}
          />
        </div>

        {/* Main Content - Side by Side Scenarios */}
        <div className="grid grid-cols-2 gap-6 mb-8">
          <ScenarioPanel
            title="Current State"
            color="blue"
            inputs={currentInputs}
            results={currentResults}
            onInputChange={setCurrentInputs}
          />
          <ScenarioPanel
            title="Goal State"
            color="emerald"
            inputs={goalInputs}
            results={goalResults}
            onInputChange={setGoalInputs}
            isGoal
          />
        </div>

        {/* Comparison Panel */}
        <div className="mb-8">
          <ComparisonPanel current={currentResults} goal={goalResults} />
        </div>

        {/* Advanced Section Toggle */}
        <div className="mb-4">
          <button
            onClick={() => setShowAdvanced(!showAdvanced)}
            className="flex items-center gap-2 px-4 py-2 text-sm font-medium text-gray-600 hover:text-gray-900 bg-white border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <BarChart3 className="w-4 h-4" />
            {showAdvanced ? 'Hide' : 'Show'} Advanced Views
            {showAdvanced ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
          </button>
        </div>

        {/* Advanced Views */}
        {showAdvanced && (
          <div className="grid grid-cols-3 gap-6">
            <CapacityView currentInputs={currentInputs} goalInputs={goalInputs} />
            <CostBreakdown results={currentResults} title="Current Cost Structure" />
            <CostBreakdown results={goalResults} title="Goal Cost Structure" />
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-12">
        <div className="max-w-[1800px] mx-auto px-6 py-4">
          <p className="text-sm text-gray-500 text-center">
            Revenue & Capacity Calculator • Overhead rates based on MOD 5-year historical average (FY20-25)
          </p>
        </div>
      </footer>
    </div>
  );
}

interface QuickStatProps {
  label: string;
  value: number;
  isCurrency?: boolean;
  suffix?: string;
  showSign?: boolean;
  color: 'emerald' | 'red' | 'blue' | 'gray';
}

function QuickStat({ label, value, isCurrency, suffix, showSign, color }: QuickStatProps) {
  const colorClasses = {
    emerald: 'text-emerald-600',
    red: 'text-red-600',
    blue: 'text-blue-600',
    gray: 'text-gray-600',
  }[color];

  let formatted: string;
  if (isCurrency) {
    const absValue = Math.abs(value);
    formatted = new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(absValue);
    if (showSign && value >= 0) formatted = '+' + formatted;
    if (value < 0) formatted = '-' + formatted;
  } else {
    formatted = value.toFixed(1);
    if (showSign && value >= 0) formatted = '+' + formatted;
    if (suffix) formatted += suffix;
  }

  return (
    <div className="bg-white rounded-xl border border-gray-200 p-4 shadow-sm">
      <div className="text-xs text-gray-500 uppercase tracking-wide mb-1">{label}</div>
      <div className={`text-2xl font-bold ${colorClasses}`}>{formatted}</div>
    </div>
  );
}

export default App;
