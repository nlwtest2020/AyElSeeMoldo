import type { ScenarioResults } from '../types';
import { compareScenarios, formatCurrency, formatDiff } from '../calculations';
import { TrendingUp, TrendingDown, Minus, ArrowRight, Users, Clock, DollarSign, Percent, PiggyBank, BarChart3 } from 'lucide-react';

interface ComparisonPanelProps {
  current: ScenarioResults;
  goal: ScenarioResults;
}

function DiffIndicator({ value }: { value: number }) {
  if (Math.abs(value) < 0.01) {
    return <Minus className="w-4 h-4 text-gray-400" />;
  }
  return value > 0 ? (
    <TrendingUp className="w-4 h-4 text-emerald-500" />
  ) : (
    <TrendingDown className="w-4 h-4 text-red-500" />
  );
}

function MetricRow({ label, icon: Icon, current, goal, format, isInverse = false }: {
  label: string;
  icon: any;
  current: number;
  goal: number;
  format: (v: number) => string;
  isInverse?: boolean;
}) {
  const diff = goal - current;
  const isPositive = isInverse ? diff < 0 : diff > 0;
  const isNeutral = Math.abs(diff) < 0.01;

  return (
    <div className="flex items-center gap-4 py-3 border-b border-gray-100 last:border-0">
      <div className="flex items-center gap-2 w-40">
        <Icon className="w-4 h-4 text-gray-400" />
        <span className="text-sm font-medium text-gray-700">{label}</span>
      </div>
      <div className="flex-1 flex items-center justify-between">
        <div className="text-sm text-gray-600 w-28 text-right">{format(current)}</div>
        <ArrowRight className="w-4 h-4 text-gray-300 mx-2" />
        <div className="text-sm font-semibold text-gray-900 w-28 text-right">{format(goal)}</div>
        <div className={`flex items-center gap-1 w-32 justify-end text-sm font-medium ${
          isNeutral ? 'text-gray-400' : isPositive ? 'text-emerald-600' : 'text-red-600'
        }`}>
          <DiffIndicator value={isInverse ? -diff : diff} />
          {isNeutral ? '—' : formatDiff(diff)}
        </div>
      </div>
    </div>
  );
}

export function ComparisonPanel({ current, goal }: ComparisonPanelProps) {
  const comparison = compareScenarios(current, goal);

  return (
    <div className="bg-white rounded-xl border border-gray-200 shadow-lg overflow-hidden">
      {/* Header */}
      <div className="bg-gradient-to-r from-blue-500 to-emerald-500 px-6 py-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <BarChart3 className="w-5 h-5" />
          Impact Analysis
        </h2>
        <p className="text-sm text-white/80 mt-1">See how your goal compares to current state</p>
      </div>

      {/* Summary Cards */}
      <div className="grid grid-cols-4 gap-4 p-6 bg-gray-50 border-b border-gray-200">
        <div className="bg-white rounded-lg p-4 shadow-sm text-center">
          <div className="text-xs text-gray-500 uppercase tracking-wide mb-1">Revenue Change</div>
          <div className={`text-2xl font-bold ${comparison.revenueDiff >= 0 ? 'text-emerald-600' : 'text-red-600'}`}>
            {formatDiff(comparison.revenueDiff)}
          </div>
          <div className={`text-xs ${comparison.revenueGrowthPct >= 0 ? 'text-emerald-500' : 'text-red-500'}`}>
            {comparison.revenueGrowthPct >= 0 ? '+' : ''}{comparison.revenueGrowthPct.toFixed(1)}%
          </div>
        </div>
        <div className="bg-white rounded-lg p-4 shadow-sm text-center">
          <div className="text-xs text-gray-500 uppercase tracking-wide mb-1">Cost Change</div>
          <div className={`text-2xl font-bold ${comparison.costDiff <= 0 ? 'text-emerald-600' : 'text-amber-600'}`}>
            {formatDiff(comparison.costDiff)}
          </div>
          <div className="text-xs text-gray-400">
            {comparison.costDiff > 0 ? 'Higher costs' : comparison.costDiff < 0 ? 'Lower costs' : 'Same'}
          </div>
        </div>
        <div className="bg-white rounded-lg p-4 shadow-sm text-center">
          <div className="text-xs text-gray-500 uppercase tracking-wide mb-1">Profit Change</div>
          <div className={`text-2xl font-bold ${comparison.profitDiff >= 0 ? 'text-emerald-600' : 'text-red-600'}`}>
            {formatDiff(comparison.profitDiff)}
          </div>
          <div className={`text-xs ${comparison.profitGrowthPct >= 0 ? 'text-emerald-500' : 'text-red-500'}`}>
            {comparison.profitGrowthPct >= 0 ? '+' : ''}{comparison.profitGrowthPct.toFixed(1)}%
          </div>
        </div>
        <div className="bg-white rounded-lg p-4 shadow-sm text-center">
          <div className="text-xs text-gray-500 uppercase tracking-wide mb-1">Student Change</div>
          <div className={`text-2xl font-bold ${comparison.studentDiff >= 0 ? 'text-emerald-600' : 'text-red-600'}`}>
            {comparison.studentDiff >= 0 ? '+' : ''}{comparison.studentDiff}
          </div>
          <div className="text-xs text-gray-400">
            {current.totalStudents} → {goal.totalStudents}
          </div>
        </div>
      </div>

      {/* Detailed Breakdown */}
      <div className="p-6">
        <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-4">Detailed Comparison</h3>

        <div className="space-y-1">
          <MetricRow
            label="Total Revenue"
            icon={DollarSign}
            current={current.totalRevenue}
            goal={goal.totalRevenue}
            format={formatCurrency}
          />
          <MetricRow
            label="Total Costs"
            icon={DollarSign}
            current={current.totalCosts}
            goal={goal.totalCosts}
            format={formatCurrency}
            isInverse
          />
          <MetricRow
            label="Net Profit"
            icon={PiggyBank}
            current={current.netProfit}
            goal={goal.netProfit}
            format={formatCurrency}
          />
          <MetricRow
            label="Profit Margin"
            icon={Percent}
            current={current.profitMargin}
            goal={goal.profitMargin}
            format={(v) => `${v.toFixed(1)}%`}
          />
          <MetricRow
            label="Total Students"
            icon={Users}
            current={current.totalStudents}
            goal={goal.totalStudents}
            format={(v) => v.toString()}
          />
          <MetricRow
            label="Hours/Month"
            icon={Clock}
            current={current.totalInstructionHours}
            goal={goal.totalInstructionHours}
            format={(v) => Math.round(v).toString()}
          />
          <MetricRow
            label="Profit/Student"
            icon={Users}
            current={current.profitPerStudent}
            goal={goal.profitPerStudent}
            format={formatCurrency}
          />
        </div>
      </div>

      {/* Cost Breakdown Comparison */}
      <div className="p-6 bg-gray-50 border-t border-gray-200">
        <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-4">Cost Breakdown</h3>
        <div className="grid grid-cols-2 gap-6">
          <div>
            <div className="text-xs text-gray-400 mb-2">Current</div>
            <div className="space-y-2">
              <CostBar label="Teacher" amount={current.totalTeacherCost} total={current.totalCosts} color="blue" />
              <CostBar label="Rent" amount={current.totalRent} total={current.totalCosts} color="amber" />
              <CostBar label="Overhead" amount={current.totalOverhead} total={current.totalCosts} color="purple" />
            </div>
          </div>
          <div>
            <div className="text-xs text-gray-400 mb-2">Goal</div>
            <div className="space-y-2">
              <CostBar label="Teacher" amount={goal.totalTeacherCost} total={goal.totalCosts} color="blue" />
              <CostBar label="Rent" amount={goal.totalRent} total={goal.totalCosts} color="amber" />
              <CostBar label="Overhead" amount={goal.totalOverhead} total={goal.totalCosts} color="purple" />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function CostBar({ label, amount, total, color }: { label: string; amount: number; total: number; color: string }) {
  const pct = total > 0 ? (amount / total) * 100 : 0;
  const colorClass = {
    blue: 'bg-blue-500',
    amber: 'bg-amber-500',
    purple: 'bg-purple-500',
  }[color] || 'bg-gray-500';

  return (
    <div>
      <div className="flex justify-between text-xs mb-1">
        <span className="text-gray-600">{label}</span>
        <span className="text-gray-500">{formatCurrency(amount)} ({pct.toFixed(0)}%)</span>
      </div>
      <div className="h-2 bg-gray-200 rounded-full overflow-hidden">
        <div className={`h-full ${colorClass} rounded-full`} style={{ width: `${pct}%` }} />
      </div>
    </div>
  );
}
