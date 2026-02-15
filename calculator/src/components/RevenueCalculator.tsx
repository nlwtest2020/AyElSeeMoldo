import type { OffSiteInputs, MonthlyResults } from '../types';
import { CORP_RATES, INST_RATES, PRIVATE_RATES, OE_RATES, TEACHER_BASE_RATE } from '../types';
import { fmt$ } from '../calculations';
import { Building2, GraduationCap, User, BookOpen, DollarSign, TrendingUp, TrendingDown, ChevronDown, ChevronUp } from 'lucide-react';
import { useState } from 'react';

interface Props {
  inputs: OffSiteInputs;
  results: MonthlyResults;
  onChange: (inputs: OffSiteInputs) => void;
}

function ProfitBadge({ margin }: { margin: number }) {
  const color = margin >= 40 ? 'text-emerald-600' : margin >= 20 ? 'text-amber-600' : 'text-red-600';
  const Icon = margin >= 0 ? TrendingUp : TrendingDown;
  return (
    <span className={`flex items-center gap-1 font-bold ${color}`}>
      <Icon className="w-4 h-4" />
      {margin.toFixed(1)}%
    </span>
  );
}

function StatRow({ label, value, sub }: { label: string; value: string; sub?: boolean }) {
  return (
    <div className={`flex justify-between text-sm py-1 ${sub ? 'pl-4 text-xs' : ''}`}>
      <span className={sub ? 'text-gray-500' : 'text-gray-400'}>{label}</span>
      <span className={`font-semibold ${sub ? 'text-gray-400' : 'text-gray-200'}`}>{value}</span>
    </div>
  );
}

function NumInput({ value, onChange, min = 0 }: { value: number; onChange: (v: number) => void; min?: number }) {
  return (
    <input
      type="number"
      min={min}
      value={value}
      onChange={e => onChange(Math.max(min, parseInt(e.target.value) || 0))}
      className="w-full px-3 py-2 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
    />
  );
}

export function RevenueCalculator({ inputs, results, onChange }: Props) {
  const [showBreakdown, setShowBreakdown] = useState(false);
  const set = <K extends keyof OffSiteInputs>(k: K, v: OffSiteInputs[K]) => onChange({ ...inputs, [k]: v });
  const oeRate = OE_RATES[results.oe.seatCount] || OE_RATES[8];

  return (
    <div className="space-y-4">
      {/* Salary Mix */}
      <div className="bg-white rounded-xl border border-gray-200 p-4 shadow-sm">
        <div className="flex items-center justify-between mb-2">
          <span className="font-semibold text-gray-700">Salary Mix</span>
          <span className="text-sm font-bold text-blue-600">{inputs.salaryMixPercent}% salaried</span>
        </div>
        <input
          type="range" min={0} max={100} step={5}
          value={inputs.salaryMixPercent}
          onChange={e => set('salaryMixPercent', parseInt(e.target.value))}
          className="w-full accent-blue-500"
        />
        <div className="flex justify-between text-xs text-gray-400 mt-1">
          <span>All Consultant</span>
          <span>All Salaried (+40% cost)</span>
        </div>
      </div>

      {/* Corporate */}
      <Section icon={<Building2 className="w-5 h-5 text-blue-500" />} title="Corporate Training" subtitle="Off-site" borderColor="border-blue-200" bg="bg-blue-50/40">
        <div className="grid grid-cols-2 gap-3 mb-3">
          <Field label="Groups">
            <NumInput value={inputs.corpGroups} onChange={v => set('corpGroups', v)} />
          </Field>
          <Field label="Hours/Month">
            <NumInput value={inputs.corpHoursPerMonth} onChange={v => set('corpHoursPerMonth', v)} />
          </Field>
        </div>
        <ResultBlock r={results.corp} rateNote={`$${CORP_RATES.revenue}/hr revenue | $${TEACHER_BASE_RATE}/hr base teacher`} />
      </Section>

      {/* Institutional */}
      <Section icon={<GraduationCap className="w-5 h-5 text-emerald-500" />} title="Institutional Training" subtitle="Off-site" borderColor="border-emerald-200" bg="bg-emerald-50/40">
        <div className="grid grid-cols-2 gap-3 mb-3">
          <Field label="Groups">
            <NumInput value={inputs.instGroups} onChange={v => set('instGroups', v)} />
          </Field>
          <Field label="Hours/Month">
            <NumInput value={inputs.instHoursPerMonth} onChange={v => set('instHoursPerMonth', v)} />
          </Field>
        </div>
        <ResultBlock r={results.inst} rateNote={`$${INST_RATES.revenue}/hr revenue | $${INST_RATES.teacherCost.toFixed(0)}/hr teacher`} />
      </Section>

      {/* Private */}
      <Section icon={<User className="w-5 h-5 text-purple-500" />} title="Private Lessons" subtitle="1-on-1" borderColor="border-purple-200" bg="bg-purple-50/40">
        <div className="grid grid-cols-2 gap-3 mb-3">
          <Field label="Students">
            <NumInput value={inputs.privateStudents} onChange={v => set('privateStudents', v)} />
          </Field>
          <Field label="Hours/Month (each)">
            <NumInput value={inputs.privateHoursPerMonth} onChange={v => set('privateHoursPerMonth', v)} />
          </Field>
        </div>
        <ResultBlock
          r={results.priv}
          rateNote={`$${PRIVATE_RATES.revenue}/hr revenue | $${TEACHER_BASE_RATE}/hr teacher | Rent: ${fmt$(results.priv.rentShare)}/mo`}
        />
      </Section>

      {/* Open Enrollment (read-only — driven by scheduler) */}
      <Section icon={<BookOpen className="w-5 h-5 text-amber-500" />} title="Open Enrollment" subtitle="From visual scheduler" borderColor="border-amber-200" bg="bg-amber-50/40">
        {results.oe.classes === 0 ? (
          <p className="text-sm text-gray-400 italic">No OE classes scheduled — drag Open Enrollment onto the grid above.</p>
        ) : (
          <>
            <div className="flex flex-wrap gap-4 text-sm text-gray-600 mb-3">
              <span>{results.oe.classes} classes</span>
              <span>Avg {results.oe.avgStudents.toFixed(1)} students/class</span>
              <span>{Math.round(results.oe.hours)} hrs/mo</span>
            </div>
            <ResultBlock
              r={results.oe}
              rateNote={`$${oeRate.rev}/hr rev | $${TEACHER_BASE_RATE}/hr teacher | Rent: ${fmt$(results.oe.rentShare)}/mo`}
            />
          </>
        )}
      </Section>

      {/* Monthly Summary */}
      <div className="bg-gray-900 rounded-xl p-5 text-white shadow-lg">
        <h3 className="font-bold text-lg mb-4 flex items-center gap-2">
          <DollarSign className="w-5 h-5 text-emerald-400" />
          Monthly Summary
        </h3>
        <div className="grid grid-cols-3 gap-4 mb-4">
          <div className="bg-white/10 rounded-lg p-3 text-center">
            <div className="text-xs text-gray-400 uppercase tracking-wide mb-1">Revenue</div>
            <div className="text-xl font-bold text-white">{fmt$(results.totalRevenue)}</div>
          </div>
          <div className="bg-white/10 rounded-lg p-3 text-center">
            <div className="text-xs text-gray-400 uppercase tracking-wide mb-1">Total Costs</div>
            <div className="text-xl font-bold text-white">{fmt$(results.totalCosts)}</div>
          </div>
          <div className={`rounded-lg p-3 text-center ${results.netProfit >= 0 ? 'bg-emerald-500/30' : 'bg-red-500/30'}`}>
            <div className="text-xs text-gray-300 uppercase tracking-wide mb-1">Net Profit</div>
            <div className={`text-xl font-bold ${results.netProfit >= 0 ? 'text-emerald-300' : 'text-red-300'}`}>
              {fmt$(results.netProfit)}
            </div>
          </div>
        </div>

        {/* Cost breakdown toggle */}
        <button
          onClick={() => setShowBreakdown(!showBreakdown)}
          className="w-full flex items-center justify-center gap-2 text-xs text-gray-400 hover:text-gray-200 transition-colors py-2"
        >
          {showBreakdown ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
          {showBreakdown ? 'Hide' : 'Show'} cost breakdown
        </button>

        {showBreakdown && (
          <div className="mt-3 space-y-2 text-sm border-t border-white/10 pt-3">
            {/* Variable Costs */}
            <div className="text-xs text-emerald-400 font-semibold uppercase tracking-wide">Variable (scales with activity)</div>
            <StatRow label="Teacher Pay (base)" value={fmt$(results.costs.teacher)} />
            {results.costs.salarySurcharge > 0 && (
              <StatRow label="Salaried Surcharge (+40%)" value={fmt$(results.costs.salarySurcharge)} sub />
            )}
            <StatRow label="Fringe (5% of payroll)" value={fmt$(results.costs.fringe)} sub />
            <StatRow label="IDC (12% of direct)" value={fmt$(results.costs.idc)} sub />

            {/* Fixed Costs */}
            <div className="text-xs text-amber-400 font-semibold uppercase tracking-wide mt-3">Fixed (monthly)</div>
            <StatRow label="Rent" value={fmt$(results.costs.rent)} />
            <StatRow label="Admin" value={fmt$(results.costs.admin)} />
            <StatRow label="Other (phone, email, ads)" value={fmt$(results.costs.other)} />

            {/* Total */}
            <div className="flex justify-between text-sm pt-3 border-t border-white/10">
              <span className="font-semibold text-gray-300">Total Costs</span>
              <span className="font-bold text-white">{fmt$(results.costs.total)}</span>
            </div>
            <div className="flex justify-between text-sm pt-1">
              <span className="font-semibold text-gray-300">Margin</span>
              <span className={`font-bold text-lg ${results.profitMargin >= 0 ? 'text-emerald-400' : 'text-red-400'}`}>
                {results.profitMargin.toFixed(1)}%
              </span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

function Section({ icon, title, subtitle, borderColor, bg, children }: {
  icon: React.ReactNode;
  title: string;
  subtitle: string;
  borderColor: string;
  bg: string;
  children: React.ReactNode;
}) {
  return (
    <div className={`bg-white rounded-xl border ${borderColor} ${bg} p-4 shadow-sm`}>
      <div className="flex items-center gap-2 mb-3">
        {icon}
        <div>
          <div className="font-semibold text-gray-800">{title}</div>
          <div className="text-xs text-gray-400">{subtitle}</div>
        </div>
      </div>
      {children}
    </div>
  );
}

function Field({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div>
      <label className="block text-xs text-gray-500 mb-1">{label}</label>
      {children}
    </div>
  );
}

function ResultBlock({ r, rateNote }: { r: { revenue: number; teacherCost: number; profit: number; margin: number }; rateNote: string }) {
  return (
    <>
      <div className="grid grid-cols-4 gap-2 text-sm">
        <div><span className="text-gray-400 text-xs block">Revenue</span><span className="font-semibold">{fmt$(r.revenue)}</span></div>
        <div><span className="text-gray-400 text-xs block">Cost</span><span className="font-semibold">{fmt$(r.teacherCost)}</span></div>
        <div><span className="text-gray-400 text-xs block">Profit</span><span className={`font-semibold ${r.profit >= 0 ? 'text-emerald-600' : 'text-red-600'}`}>{fmt$(r.profit)}</span></div>
        <div><span className="text-gray-400 text-xs block">Margin</span><ProfitBadge margin={r.margin} /></div>
      </div>
      <div className="text-xs text-gray-400 mt-2">{rateNote}</div>
    </>
  );
}
