import { CORP_RATES, INST_RATES, PRIVATE_RATES, OE_RATES, SESSIONS_PER_MONTH, OVERHEAD } from '../types';

export function CalcBreakdown() {
  return (
    <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-6 space-y-6 text-sm">
      <h2 className="text-lg font-bold text-gray-900">How Numbers Are Calculated</h2>

      {/* Monthly standardization */}
      <Block title="Monthly Standardization">
        <p className="text-gray-600 mb-2">All numbers are monthly. The weekly scheduler is converted using:</p>
        <Formula>
          Monthly hours = Session hours × 2 days/week × 4.33 weeks/month = {SESSIONS_PER_MONTH.toFixed(2)} sessions/month
        </Formula>
        <p className="text-gray-500 mt-2 text-xs">
          Example: A Mon/Wed slot at 9:00–11:00 (2 hrs/session) = 2 × 2 × 4.33 = <strong>17.32 hrs/month</strong>
        </p>
      </Block>

      {/* Corporate */}
      <Block title="Corporate Training (off-site)">
        <Row k="Revenue/hr" v={`$${CORP_RATES.effRev} = $32.00 instruction + $2.92 materials/eval`} />
        <Row k="Teacher cost/hr" v={`$${CORP_RATES.teacherCost} base (×surcharge for salaried)`} />
        <Formula>Monthly Revenue = Hours/Month × $34.92</Formula>
        <Formula>Monthly Cost = Hours/Month × $15.15 × surcharge</Formula>
      </Block>

      {/* Institutional */}
      <Block title="Institutional Training (off-site)">
        <Row k="Revenue/hr" v={`$${INST_RATES.effRev} = $32.00 instruction + $2.62 materials/eval`} />
        <Row k="Teacher cost/hr" v={`$${INST_RATES.teacherCost} base (higher due to institutional requirements)`} />
        <Formula>Monthly Revenue = Hours/Month × $34.62</Formula>
        <Formula>Monthly Cost = Hours/Month × $20.16 × surcharge</Formula>
      </Block>

      {/* Private */}
      <Block title="Private Lessons (1-on-1)">
        <Row k="Student price/hr" v={`$${PRIVATE_RATES.revenue}`} />
        <Row k="Teacher cost/hr" v={`$${PRIVATE_RATES.teacherCost} base`} />
        <Formula>Monthly Revenue = Students × Hours/Month × $30.00</Formula>
        <Formula>Monthly Cost = Hours × $14.73 × surcharge + rent share</Formula>
      </Block>

      {/* Open Enrollment */}
      <Block title="Open Enrollment (on-site, from scheduler)">
        <p className="text-gray-600 mb-2">Revenue rate scales with class size (6–15 students):</p>
        <div className="grid grid-cols-5 gap-1 text-xs mb-3">
          <div className="font-semibold text-gray-500">Students</div>
          <div className="font-semibold text-gray-500">Rev/hr</div>
          <div className="font-semibold text-gray-500">Students</div>
          <div className="font-semibold text-gray-500">Rev/hr</div>
          <div />
          {[6,7,8,9,10,11,12,13,14,15].map(n => [
            <div key={`s${n}`} className="text-gray-700">{n}</div>,
            <div key={`r${n}`} className="text-gray-700">${OE_RATES[n].rev}</div>,
          ]).flat().slice(0,18)}
        </div>
        <Row k="Teacher cost/hr" v={`$${OE_RATES[8].teacher} (flat regardless of class size)`} />
        <Formula>Monthly Revenue = Slot hrs/month × rate(seat count)</Formula>
        <Formula>Slot hrs/month = session_hours × {SESSIONS_PER_MONTH.toFixed(2)}</Formula>
      </Block>

      {/* Rent */}
      <Block title="Rent Allocation ($3,400/month fixed)">
        <p className="text-gray-600 mb-2">Rent is split proportionally between OE and Private by facility hours used. Corporate and Institutional are off-site — no rent.</p>
        <Formula>OE Rent = (OE hours / total facility hours) × $3,400</Formula>
        <Formula>Private Rent = (Private hours / total facility hours) × $3,400</Formula>
      </Block>

      {/* Salary surcharge */}
      <Block title="Salary Mix Surcharge">
        <p className="text-gray-600 mb-2">Salaried teachers cost 40% more than consultants due to benefits, taxes, etc.</p>
        <Formula>Surcharge multiplier = 1 + (salary% / 100) × 0.40</Formula>
        <p className="text-xs text-gray-500 mt-1">At 100% salaried: multiplier = 1.40 (all teacher costs ×1.40)</p>
      </Block>

      {/* Overhead */}
      <Block title="Overhead (from 5-year historical data, FY20-25)">
        <p className="text-gray-600 mb-2">
          These percentages come from MOD's actual expense history. Direct costs (teacher + rent) represent ~65% of total expenses historically,
          so overhead is calculated as a fraction of direct costs:
        </p>
        <Formula>Overhead = direct costs × (overhead% / 65%)</Formula>
        <div className="mt-2 space-y-1">
          <Row k="Indirect Costs (698100)" v={`${(OVERHEAD.indirect * 100).toFixed(1)}% of total expenses`} />
          <Row k="Fringe Benefits (517550)" v={`${(OVERHEAD.fringe * 100).toFixed(1)}% of total expenses`} />
          <Row k="Other Fixed (phone, email, ads)" v={`${(OVERHEAD.other * 100).toFixed(1)}% of total expenses`} />
        </div>
      </Block>
    </div>
  );
}

function Block({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="border-l-4 border-blue-500 pl-4">
      <h3 className="font-semibold text-gray-800 mb-2">{title}</h3>
      {children}
    </div>
  );
}

function Row({ k, v }: { k: string; v: string }) {
  return (
    <div className="flex gap-2 text-xs mb-1">
      <span className="text-gray-400 w-40 shrink-0">{k}:</span>
      <span className="text-gray-700">{v}</span>
    </div>
  );
}

function Formula({ children }: { children: React.ReactNode }) {
  return (
    <div className="bg-gray-50 border border-gray-200 rounded px-3 py-1.5 font-mono text-xs text-gray-700 my-1">
      {children}
    </div>
  );
}
