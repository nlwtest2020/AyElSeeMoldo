import type { ScenarioResults } from '../types';
import { FIXED_OVERHEAD, MONTHLY_RENT } from '../types';
import { formatCurrency } from '../calculations';
import { PieChart, AlertCircle } from 'lucide-react';

interface CostBreakdownProps {
  results: ScenarioResults;
  title?: string;
}

export function CostBreakdown({ results, title = "Cost Structure" }: CostBreakdownProps) {
  const costCategories = [
    {
      name: 'Teacher Costs',
      amount: results.totalTeacherCost,
      color: 'bg-blue-500',
      description: 'Direct instruction costs (consultants/salaried)',
      subcategories: [
        { name: 'Open Enrollment', amount: results.oeTeacherCost },
        { name: 'Private', amount: results.privateTeacherCost },
        { name: 'Corporate', amount: results.corpTeacherCost },
        { name: 'Institutional', amount: results.instTeacherCost },
      ]
    },
    {
      name: 'Rent',
      amount: results.totalRent,
      color: 'bg-amber-500',
      description: `Fixed at ${formatCurrency(MONTHLY_RENT)}/month`,
      subcategories: [
        { name: 'OE Share', amount: results.oeRentShare },
        { name: 'Private Share', amount: results.privateRentShare },
      ]
    },
    {
      name: 'Indirect Costs',
      amount: results.indirectCosts,
      color: 'bg-purple-500',
      description: `${(FIXED_OVERHEAD.indirectCosts * 100).toFixed(1)}% historical average`,
      subcategories: []
    },
    {
      name: 'Fringe Benefits',
      amount: results.fringeBenefits,
      color: 'bg-pink-500',
      description: `${(FIXED_OVERHEAD.fringeBenefits * 100).toFixed(1)}% historical average`,
      subcategories: []
    },
    {
      name: 'Other Fixed',
      amount: results.otherFixed,
      color: 'bg-gray-500',
      description: 'Telephone, email, advertising',
      subcategories: []
    },
  ];

  const totalCosts = results.totalCosts;

  return (
    <div className="bg-white rounded-xl border border-gray-200 shadow-lg overflow-hidden">
      <div className="bg-gray-100 px-6 py-4 border-b border-gray-200">
        <h2 className="text-lg font-bold text-gray-800 flex items-center gap-2">
          <PieChart className="w-5 h-5" />
          {title}
        </h2>
      </div>

      <div className="p-6">
        {/* Visual breakdown */}
        <div className="flex h-6 rounded-full overflow-hidden mb-6">
          {costCategories.map((cat, i) => {
            const pct = totalCosts > 0 ? (cat.amount / totalCosts) * 100 : 0;
            if (pct < 1) return null;
            return (
              <div
                key={i}
                className={`${cat.color} relative group`}
                style={{ width: `${pct}%` }}
                title={`${cat.name}: ${formatCurrency(cat.amount)} (${pct.toFixed(1)}%)`}
              />
            );
          })}
        </div>

        {/* Legend */}
        <div className="flex flex-wrap gap-4 mb-6">
          {costCategories.map((cat, i) => (
            <div key={i} className="flex items-center gap-2">
              <div className={`w-3 h-3 rounded-full ${cat.color}`} />
              <span className="text-xs text-gray-600">{cat.name}</span>
            </div>
          ))}
        </div>

        {/* Detailed list */}
        <div className="space-y-4">
          {costCategories.map((cat, i) => {
            const pct = totalCosts > 0 ? (cat.amount / totalCosts) * 100 : 0;
            return (
              <div key={i} className="border border-gray-100 rounded-lg p-4">
                <div className="flex items-center justify-between mb-2">
                  <div className="flex items-center gap-2">
                    <div className={`w-3 h-3 rounded-full ${cat.color}`} />
                    <span className="font-medium text-gray-800">{cat.name}</span>
                  </div>
                  <div className="text-right">
                    <span className="font-bold text-gray-900">{formatCurrency(cat.amount)}</span>
                    <span className="text-sm text-gray-500 ml-2">({pct.toFixed(1)}%)</span>
                  </div>
                </div>
                <p className="text-xs text-gray-500 mb-2">{cat.description}</p>
                {cat.subcategories.length > 0 && (
                  <div className="pl-5 border-l-2 border-gray-100 space-y-1">
                    {cat.subcategories.map((sub, j) => (
                      <div key={j} className="flex justify-between text-xs text-gray-500">
                        <span>{sub.name}</span>
                        <span>{formatCurrency(sub.amount)}</span>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            );
          })}
        </div>

        {/* Total */}
        <div className="mt-6 pt-4 border-t border-gray-200 flex justify-between items-center">
          <span className="text-lg font-bold text-gray-800">Total Monthly Costs</span>
          <span className="text-2xl font-bold text-gray-900">{formatCurrency(totalCosts)}</span>
        </div>

        {/* Historical context note */}
        <div className="mt-4 bg-amber-50 border border-amber-200 rounded-lg p-3 flex items-start gap-2">
          <AlertCircle className="w-4 h-4 text-amber-500 flex-shrink-0 mt-0.5" />
          <p className="text-xs text-amber-800">
            <strong>Note:</strong> Overhead rates (indirect, fringe, other) are derived from MOD's 5-year historical average (FY20-25).
            Actual overhead may vary based on operational decisions.
          </p>
        </div>
      </div>
    </div>
  );
}
