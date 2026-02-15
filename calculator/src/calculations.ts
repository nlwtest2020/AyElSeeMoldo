import type { ScheduleGrid, OffSiteInputs, MonthlyResults, CostBreakdown } from './types';
import {
  ROOMS, TIME_SLOTS, DAY_PATTERNS,
  CORP_RATES, INST_RATES, PRIVATE_RATES, OE_RATES,
  MONTHLY_RENT, MONTHLY_ADMIN, MONTHLY_OTHER,
  SALARIED_SURCHARGE, IDC_RATE,
  slotKey, slotMonthlyHours,
} from './types';

export function calculate(grid: ScheduleGrid, inputs: OffSiteInputs): MonthlyResults {
  const salaryMult = 1 + (inputs.salaryMixPercent / 100) * SALARIED_SURCHARGE;

  // ── OPEN ENROLLMENT (from scheduler) ─────────────────────────────────────
  let oeRev = 0, oeTeacherBase = 0, oeHours = 0, oeStudents = 0, oeClasses = 0;
  for (const room of ROOMS) {
    for (const dp of DAY_PATTERNS) {
      for (const ts of TIME_SLOTS) {
        const s = grid[slotKey(room.id, dp.pattern, ts.slot)];
        if (!s || s.classType !== 'openEnrollment') continue;
        const hrs = slotMonthlyHours(ts.slot);
        const seat = Math.max(6, Math.min(15, s.studentCount));
        const rate = OE_RATES[seat];
        oeRev += hrs * rate.rev;
        oeTeacherBase += hrs * rate.teacher;
        oeHours += hrs;
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
        privRevSched += hrs * PRIVATE_RATES.revenue;
        privTeacherSched += hrs * PRIVATE_RATES.teacherCost;
        privHoursSched += hrs;
        privStudentsSched += s.studentCount;
      }
    }
  }

  // ── PRIVATE (manual off-site / additional) ────────────────────────────────
  // Hours is total (like corp/inst), not per-student
  const privManualHours = inputs.privateHoursPerMonth;
  const privManualRev = privManualHours * PRIVATE_RATES.revenue;
  const privManualTeacher = privManualHours * PRIVATE_RATES.teacherCost;

  const privRev = privRevSched + privManualRev;
  const privTeacherBase = privTeacherSched + privManualTeacher;
  const privHours = privHoursSched + privManualHours;
  const privStudents = privStudentsSched + inputs.privateStudents;

  // ── CORPORATE ─────────────────────────────────────────────────────────────
  const corpRev = inputs.corpHoursPerMonth * CORP_RATES.revenue;
  const corpTeacherBase = inputs.corpHoursPerMonth * CORP_RATES.teacherCost;

  // ── INSTITUTIONAL ─────────────────────────────────────────────────────────
  const instRev = inputs.instHoursPerMonth * INST_RATES.revenue;
  const instTeacherBase = inputs.instHoursPerMonth * INST_RATES.teacherCost;

  // ── TOTAL HOURS ───────────────────────────────────────────────────────────
  const totalHours = oeHours + privHours + inputs.corpHoursPerMonth + inputs.instHoursPerMonth;

  // ── RENT (allocated to on-site facility hours: OE + Private on-site) ──────
  const facilityHours = oeHours + privHoursSched;
  const oeRentShare = facilityHours > 0 ? (oeHours / facilityHours) * MONTHLY_RENT : 0;
  const privRentShare = facilityHours > 0 ? (privHoursSched / facilityHours) * MONTHLY_RENT : 0;

  // ── COST BREAKDOWN ────────────────────────────────────────────────────────
  // Base teacher costs (before salaried surcharge)
  const totalTeacherBase = oeTeacherBase + privTeacherBase + corpTeacherBase + instTeacherBase;

  // Salaried surcharge (scales with teacher hours, only for salaried %)
  const salarySurchargeAmt = totalTeacherBase * (inputs.salaryMixPercent / 100) * SALARIED_SURCHARGE;

  // Total teacher cost after surcharge (surcharge includes fringe/benefits)
  const totalTeacherCost = totalTeacherBase + salarySurchargeAmt;

  // IDC: 12% of direct costs (teacher + rent) - scales with activity
  const directCosts = totalTeacherCost + MONTHLY_RENT;
  const idcCost = directCosts * IDC_RATE;

  // Fixed costs (don't scale)
  const adminCost = MONTHLY_ADMIN;
  const otherCost = MONTHLY_OTHER;

  const costs: CostBreakdown = {
    teacher: totalTeacherBase,
    salarySurcharge: salarySurchargeAmt,
    idc: idcCost,
    rent: MONTHLY_RENT,
    admin: adminCost,
    other: otherCost,
    total: totalTeacherCost + idcCost + MONTHLY_RENT + adminCost + otherCost,
  };

  // ── SECTION-LEVEL TEACHER COSTS (with salary multiplier applied) ──────────
  const oeTeacher = oeTeacherBase * salaryMult;
  const privTeacher = privTeacherBase * salaryMult;
  const corpTeacher = corpTeacherBase * salaryMult;
  const instTeacher = instTeacherBase * salaryMult;

  // ── SECTION PROFITS (direct costs only, before overhead allocation) ───────
  const oeTotal = oeTeacher + oeRentShare;
  const privTotal = privTeacher + privRentShare;

  const totalRevenue = oeRev + privRev + corpRev + instRev;
  const netProfit = totalRevenue - costs.total;
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
    costs,
    totalRevenue,
    totalCosts: costs.total,
    netProfit,
    profitMargin,
    totalStudents: oeStudents + privStudents + (inputs.corpGroups * 4) + (inputs.instGroups * 6),
    totalHours,
  };
}

export function fmt$(v: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency', currency: 'USD', minimumFractionDigits: 0, maximumFractionDigits: 0,
  }).format(v);
}
