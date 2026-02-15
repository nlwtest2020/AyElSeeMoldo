import type { ScheduleGrid, OffSiteInputs, MonthlyResults } from './types';
import {
  ROOMS, TIME_SLOTS, DAY_PATTERNS,
  CORP_RATES, INST_RATES, PRIVATE_RATES, OE_RATES,
  MONTHLY_RENT, SALARY_SURCHARGE, OVERHEAD,
  slotKey, slotMonthlyHours,
} from './types';

export function getSurcharge(pct: number): number {
  return 1 + (pct / 100) * SALARY_SURCHARGE;
}

export function calculate(grid: ScheduleGrid, inputs: OffSiteInputs): MonthlyResults {
  const mx = getSurcharge(inputs.salaryMixPercent);

  // ── OPEN ENROLLMENT (from scheduler) ─────────────────────────────────────
  let oeRev = 0, oeTeacher = 0, oeHours = 0, oeStudents = 0, oeClasses = 0;
  for (const room of ROOMS) {
    for (const dp of DAY_PATTERNS) {
      for (const ts of TIME_SLOTS) {
        const s = grid[slotKey(room.id, dp.pattern, ts.slot)];
        if (!s || s.classType !== 'openEnrollment') continue;
        const hrs = slotMonthlyHours(ts.slot);
        const seat = Math.max(6, Math.min(15, s.studentCount));
        const rate = OE_RATES[seat];
        oeRev     += hrs * rate.rev;
        oeTeacher += hrs * rate.teacher * mx;
        oeHours   += hrs;
        oeStudents += s.studentCount;
        oeClasses++;
      }
    }
  }
  const oeAvg = oeClasses > 0 ? oeStudents / oeClasses : 0;
  const oeSeat = Math.max(6, Math.min(15, Math.round(oeAvg)));

  // ── PRIVATE (scheduler on-site) ───────────────────────────────────────────
  let privRevSched = 0, privTeacherSched = 0, privHoursSched = 0, privStudentsSched = 0;
  for (const room of ROOMS) {
    for (const dp of DAY_PATTERNS) {
      for (const ts of TIME_SLOTS) {
        const s = grid[slotKey(room.id, dp.pattern, ts.slot)];
        if (!s || s.classType !== 'private') continue;
        const hrs = slotMonthlyHours(ts.slot);
        privRevSched     += hrs * PRIVATE_RATES.revenue;
        privTeacherSched += hrs * PRIVATE_RATES.teacherCost * mx;
        privHoursSched   += hrs;
        privStudentsSched += s.studentCount;
      }
    }
  }

  // ── PRIVATE (manual off-site / additional) ────────────────────────────────
  const privManualHours   = inputs.privateStudents * inputs.privateHoursPerMonth;
  const privManualRev     = privManualHours * PRIVATE_RATES.revenue;
  const privManualTeacher = privManualHours * PRIVATE_RATES.teacherCost * mx;

  const privRev     = privRevSched + privManualRev;
  const privTeacher = privTeacherSched + privManualTeacher;
  const privHours   = privHoursSched + privManualHours;
  const privStudents = privStudentsSched + inputs.privateStudents;

  // ── CORPORATE ─────────────────────────────────────────────────────────────
  const corpRev     = inputs.corpHoursPerMonth * CORP_RATES.effRev;
  const corpTeacher = inputs.corpHoursPerMonth * CORP_RATES.teacherCost * mx;

  // ── INSTITUTIONAL ─────────────────────────────────────────────────────────
  const instRev     = inputs.instHoursPerMonth * INST_RATES.effRev;
  const instTeacher = inputs.instHoursPerMonth * INST_RATES.teacherCost * mx;

  // ── RENT (allocated to on-site facility hours: OE + Private) ─────────────
  const facilityHours = oeHours + privHours;
  const oeRentShare   = facilityHours > 0 ? (oeHours   / facilityHours) * MONTHLY_RENT : 0;
  const privRentShare = facilityHours > 0 ? (privHours / facilityHours) * MONTHLY_RENT : 0;

  // ── OVERHEAD (applied to direct costs, from historical %) ─────────────────
  // Direct costs = teacher + rent ≈ 65% of total expenses historically
  // So overhead = direct × (overhead% / 65%)
  const directCosts = (oeTeacher + privTeacher + corpTeacher + instTeacher) + MONTHLY_RENT;
  const scale = 1 / 0.65;
  const oHead = {
    indirect: OVERHEAD.indirect * directCosts * scale,
    fringe:   OVERHEAD.fringe   * directCosts * scale,
    other:    OVERHEAD.other    * directCosts * scale,
    total:    (OVERHEAD.indirect + OVERHEAD.fringe + OVERHEAD.other) * directCosts * scale,
  };

  // ── SECTION PROFITS ───────────────────────────────────────────────────────
  const oeTotal  = oeTeacher  + oeRentShare;
  const privTotal = privTeacher + privRentShare;

  const totalRevenue = oeRev + privRev + corpRev + instRev;
  const totalCosts   = (oeTeacher + privTeacher + corpTeacher + instTeacher) + MONTHLY_RENT + oHead.total;
  const netProfit    = totalRevenue - totalCosts;
  const profitMargin = totalRevenue > 0 ? (netProfit / totalRevenue) * 100 : 0;

  return {
    oe: {
      revenue: oeRev, teacherCost: oeTeacher, rentShare: oeRentShare,
      profit: oeRev - oeTotal, margin: oeRev > 0 ? ((oeRev - oeTotal) / oeRev) * 100 : 0,
      hours: oeHours, students: oeStudents, classes: oeClasses,
      avgStudents: oeAvg, seatCount: oeSeat,
    },
    priv: {
      revenue: privRev, teacherCost: privTeacher, rentShare: privRentShare,
      profit: privRev - privTotal, margin: privRev > 0 ? ((privRev - privTotal) / privRev) * 100 : 0,
      hours: privHours, students: privStudents,
    },
    corp: {
      revenue: corpRev, teacherCost: corpTeacher, rentShare: 0,
      profit: corpRev - corpTeacher, margin: corpRev > 0 ? ((corpRev - corpTeacher) / corpRev) * 100 : 0,
      hours: inputs.corpHoursPerMonth, students: inputs.corpGroups,
    },
    inst: {
      revenue: instRev, teacherCost: instTeacher, rentShare: 0,
      profit: instRev - instTeacher, margin: instRev > 0 ? ((instRev - instTeacher) / instRev) * 100 : 0,
      hours: inputs.instHoursPerMonth, students: inputs.instGroups,
    },
    rent: MONTHLY_RENT,
    overhead: oHead,
    totalRevenue, totalCosts, netProfit, profitMargin,
    totalStudents: oeStudents + privStudents + (inputs.corpGroups * 4) + (inputs.instGroups * 6),
  };
}

export function fmt$(v: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency', currency: 'USD', minimumFractionDigits: 2,
  }).format(v);
}
