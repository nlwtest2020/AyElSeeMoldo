import type { ScenarioInputs, ScenarioResults } from '../types';
import { OE_RATES, MONTHLY_RENT } from '../types';
import { formatCurrency } from '../calculations';
import { Users, Clock, Building2, GraduationCap, BookOpen, User, DollarSign } from 'lucide-react';

interface ScenarioPanelProps {
  title: string;
  color: 'blue' | 'emerald';
  inputs: ScenarioInputs;
  results: ScenarioResults;
  onInputChange: (inputs: ScenarioInputs) => void;
  isGoal?: boolean;
}

export function ScenarioPanel({ title, color, inputs, results, onInputChange, isGoal = false }: ScenarioPanelProps) {
  const colorClasses = {
    blue: {
      border: 'border-blue-500/30',
      bg: 'bg-blue-500/10',
      text: 'text-blue-600',
      accent: 'bg-blue-500',
    },
    emerald: {
      border: 'border-emerald-500/30',
      bg: 'bg-emerald-500/10',
      text: 'text-emerald-600',
      accent: 'bg-emerald-500',
    },
  }[color];

  const updateInput = <K extends keyof ScenarioInputs>(key: K, value: ScenarioInputs[K]) => {
    onInputChange({ ...inputs, [key]: value });
  };

  const oeRate = OE_RATES[Math.max(6, Math.min(15, Math.round(inputs.oeStudentsPerClass)))];

  return (
    <div className={`rounded-xl border-2 ${colorClasses.border} bg-white shadow-lg overflow-hidden`}>
      {/* Header */}
      <div className={`${colorClasses.bg} px-6 py-4 border-b ${colorClasses.border}`}>
        <div className="flex items-center gap-3">
          <div className={`w-3 h-3 rounded-full ${colorClasses.accent}`} />
          <h2 className="text-xl font-bold text-gray-900">{title}</h2>
          {isGoal && (
            <span className="ml-auto text-xs font-medium px-2 py-1 rounded-full bg-emerald-100 text-emerald-700">
              Target
            </span>
          )}
        </div>
      </div>

      {/* Input Sections */}
      <div className="p-6 space-y-6">
        {/* Global Settings */}
        <div className="bg-gray-50 rounded-lg p-4">
          <h3 className="font-semibold text-gray-700 mb-3 flex items-center gap-2">
            <DollarSign className="w-4 h-4" />
            Global Settings
          </h3>
          <div className="space-y-3">
            <div>
              <label className="block text-sm text-gray-600 mb-1">
                Salary Mix: <span className="font-semibold">{inputs.salaryMixPercent}%</span> salaried
              </label>
              <input
                type="range"
                min={0}
                max={100}
                step={5}
                value={inputs.salaryMixPercent}
                onChange={(e) => updateInput('salaryMixPercent', parseInt(e.target.value))}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-blue-500"
              />
              <div className="flex justify-between text-xs text-gray-400 mt-1">
                <span>All Consultant</span>
                <span>All Salaried (+40%)</span>
              </div>
            </div>
            <div className="text-sm text-gray-500">
              Fixed Rent: <span className="font-semibold">{formatCurrency(MONTHLY_RENT)}/mo</span>
            </div>
          </div>
        </div>

        {/* Open Enrollment */}
        <div className="border border-amber-200 rounded-lg p-4 bg-amber-50/50">
          <h3 className="font-semibold text-amber-700 mb-3 flex items-center gap-2">
            <BookOpen className="w-4 h-4" />
            Open Enrollment
            <span className="ml-auto text-xs font-normal text-gray-500">
              ${oeRate.rev}/hr @ {Math.max(6, Math.min(15, Math.round(inputs.oeStudentsPerClass)))}-seat
            </span>
          </h3>
          <div className="grid grid-cols-3 gap-3">
            <div>
              <label className="block text-xs text-gray-600 mb-1">Classes</label>
              <input
                type="number"
                min={0}
                value={inputs.oeClasses}
                onChange={(e) => updateInput('oeClasses', parseInt(e.target.value) || 0)}
                className="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-amber-500 focus:border-amber-500"
              />
            </div>
            <div>
              <label className="block text-xs text-gray-600 mb-1">Students/Class</label>
              <input
                type="number"
                min={1}
                max={15}
                value={inputs.oeStudentsPerClass}
                onChange={(e) => updateInput('oeStudentsPerClass', parseInt(e.target.value) || 1)}
                className="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-amber-500 focus:border-amber-500"
              />
            </div>
            <div>
              <label className="block text-xs text-gray-600 mb-1">Hrs/Wk Each</label>
              <input
                type="number"
                min={0}
                value={inputs.oeHoursPerWeek}
                onChange={(e) => updateInput('oeHoursPerWeek', parseInt(e.target.value) || 0)}
                className="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-amber-500 focus:border-amber-500"
              />
            </div>
          </div>
          <div className="mt-2 text-sm text-amber-700">
            {inputs.oeClasses * inputs.oeStudentsPerClass} students × {inputs.oeHoursPerWeek * inputs.oeClasses} hrs/wk = <span className="font-semibold">{formatCurrency(results.oeRevenue)}/mo</span>
          </div>
        </div>

        {/* Private Lessons */}
        <div className="border border-purple-200 rounded-lg p-4 bg-purple-50/50">
          <h3 className="font-semibold text-purple-700 mb-3 flex items-center gap-2">
            <User className="w-4 h-4" />
            Private Lessons
            <span className="ml-auto text-xs font-normal text-gray-500">
              $30/hr
            </span>
          </h3>
          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-xs text-gray-600 mb-1">Students</label>
              <input
                type="number"
                min={0}
                value={inputs.privateStudents}
                onChange={(e) => updateInput('privateStudents', parseInt(e.target.value) || 0)}
                className="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500"
              />
            </div>
            <div>
              <label className="block text-xs text-gray-600 mb-1">Hrs/Mo Each</label>
              <input
                type="number"
                min={0}
                value={inputs.privateHoursPerStudent}
                onChange={(e) => updateInput('privateHoursPerStudent', parseInt(e.target.value) || 0)}
                className="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500"
              />
            </div>
          </div>
          <div className="mt-2 text-sm text-purple-700">
            {inputs.privateStudents} students × {inputs.privateHoursPerStudent} hrs = <span className="font-semibold">{formatCurrency(results.privateRevenue)}/mo</span>
          </div>
        </div>

        {/* Corporate (Off-site) */}
        <div className="border border-blue-200 rounded-lg p-4 bg-blue-50/50">
          <h3 className="font-semibold text-blue-700 mb-3 flex items-center gap-2">
            <Building2 className="w-4 h-4" />
            Corporate
            <span className="ml-auto text-xs font-normal text-gray-500">
              Off-site • $34.92/hr
            </span>
          </h3>
          <div className="grid grid-cols-3 gap-3">
            <div>
              <label className="block text-xs text-gray-600 mb-1">Groups</label>
              <input
                type="number"
                min={0}
                value={inputs.corpGroups}
                onChange={(e) => updateInput('corpGroups', parseInt(e.target.value) || 0)}
                className="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
            <div>
              <label className="block text-xs text-gray-600 mb-1">Per Group</label>
              <input
                type="number"
                min={0}
                value={inputs.corpParticipantsPerGroup}
                onChange={(e) => updateInput('corpParticipantsPerGroup', parseInt(e.target.value) || 0)}
                className="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
            <div>
              <label className="block text-xs text-gray-600 mb-1">Hrs/Mo Total</label>
              <input
                type="number"
                min={0}
                value={inputs.corpHoursPerMonth}
                onChange={(e) => updateInput('corpHoursPerMonth', parseInt(e.target.value) || 0)}
                className="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
          </div>
          <div className="mt-2 text-sm text-blue-700">
            {inputs.corpGroups * inputs.corpParticipantsPerGroup} participants × {inputs.corpHoursPerMonth} hrs = <span className="font-semibold">{formatCurrency(results.corpRevenue)}/mo</span>
          </div>
        </div>

        {/* Institutional (Off-site) */}
        <div className="border border-emerald-200 rounded-lg p-4 bg-emerald-50/50">
          <h3 className="font-semibold text-emerald-700 mb-3 flex items-center gap-2">
            <GraduationCap className="w-4 h-4" />
            Institutional
            <span className="ml-auto text-xs font-normal text-gray-500">
              Off-site • $34.62/hr
            </span>
          </h3>
          <div className="grid grid-cols-3 gap-3">
            <div>
              <label className="block text-xs text-gray-600 mb-1">Groups</label>
              <input
                type="number"
                min={0}
                value={inputs.instGroups}
                onChange={(e) => updateInput('instGroups', parseInt(e.target.value) || 0)}
                className="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500"
              />
            </div>
            <div>
              <label className="block text-xs text-gray-600 mb-1">Per Group</label>
              <input
                type="number"
                min={0}
                value={inputs.instParticipantsPerGroup}
                onChange={(e) => updateInput('instParticipantsPerGroup', parseInt(e.target.value) || 0)}
                className="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500"
              />
            </div>
            <div>
              <label className="block text-xs text-gray-600 mb-1">Hrs/Mo Total</label>
              <input
                type="number"
                min={0}
                value={inputs.instHoursPerMonth}
                onChange={(e) => updateInput('instHoursPerMonth', parseInt(e.target.value) || 0)}
                className="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500"
              />
            </div>
          </div>
          <div className="mt-2 text-sm text-emerald-700">
            {inputs.instGroups * inputs.instParticipantsPerGroup} participants × {inputs.instHoursPerMonth} hrs = <span className="font-semibold">{formatCurrency(results.instRevenue)}/mo</span>
          </div>
        </div>
      </div>

      {/* Results Summary */}
      <div className={`${colorClasses.bg} px-6 py-4 border-t ${colorClasses.border}`}>
        <div className="grid grid-cols-3 gap-4 text-center">
          <div>
            <div className="text-xs text-gray-500 uppercase tracking-wide">Revenue</div>
            <div className="text-lg font-bold text-gray-900">{formatCurrency(results.totalRevenue)}</div>
          </div>
          <div>
            <div className="text-xs text-gray-500 uppercase tracking-wide">Costs</div>
            <div className="text-lg font-bold text-gray-900">{formatCurrency(results.totalCosts)}</div>
          </div>
          <div>
            <div className="text-xs text-gray-500 uppercase tracking-wide">Net Profit</div>
            <div className={`text-lg font-bold ${results.netProfit >= 0 ? 'text-emerald-600' : 'text-red-600'}`}>
              {formatCurrency(results.netProfit)}
            </div>
          </div>
        </div>
        <div className="mt-3 flex items-center justify-center gap-4 text-sm text-gray-600">
          <span className="flex items-center gap-1">
            <Users className="w-4 h-4" />
            {results.totalStudents} students
          </span>
          <span className="flex items-center gap-1">
            <Clock className="w-4 h-4" />
            {Math.round(results.totalInstructionHours)} hrs/mo
          </span>
          <span className={`font-semibold ${results.profitMargin >= 0 ? 'text-emerald-600' : 'text-red-600'}`}>
            {results.profitMargin.toFixed(1)}% margin
          </span>
        </div>
      </div>
    </div>
  );
}
