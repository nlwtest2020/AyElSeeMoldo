import {
  TEACHER_BASE_RATE, SALARIED_SURCHARGE, IDC_RATE,
  MONTHLY_RENT, MONTHLY_ADMIN, MONTHLY_OTHER,
  CORP_RATES, INST_RATES, PRIVATE_RATES, OE_RATES,
} from '../types';

export function CalcBreakdown() {
  return (
    <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-6 space-y-5 text-sm">
      <h2 className="text-lg font-bold text-gray-900">Cost Structure</h2>

      {/* Teacher Costs */}
      <Block title="Teacher Pay">
        <Row k="Base rate" v={`$${TEACHER_BASE_RATE}/hr`} />
        <Row k="Salaried surcharge" v={`+${SALARIED_SURCHARGE * 100}% (includes benefits, taxes)`} />
      </Block>

      {/* Variable Costs */}
      <Block title="Variable Costs (scale with activity)">
        <Row k="IDC" v={`${IDC_RATE * 100}% of direct costs`} />
      </Block>

      {/* Fixed Costs */}
      <Block title="Fixed Monthly Costs">
        <Row k="Rent" v={`$${MONTHLY_RENT.toLocaleString()}`} />
        <Row k="Admin" v={`$${MONTHLY_ADMIN}`} />
        <Row k="Other (utilities, Zoom, supplies)" v={`$${MONTHLY_OTHER.toLocaleString()}`} />
      </Block>

      {/* Revenue Rates */}
      <Block title="Revenue Rates">
        <Row k="Corporate" v={`$${CORP_RATES.revenue}/hr`} />
        <Row k="Institutional" v={`$${INST_RATES.revenue}/hr`} />
        <Row k="Private" v={`$${PRIVATE_RATES.revenue}/hr`} />
        <Row k="Open Enrollment" v={`$${OE_RATES[6].rev}–$${OE_RATES[15].rev}/hr (6–15 students)`} />
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
      <span className="text-gray-500 w-36 shrink-0">{k}:</span>
      <span className="text-gray-700">{v}</span>
    </div>
  );
}
