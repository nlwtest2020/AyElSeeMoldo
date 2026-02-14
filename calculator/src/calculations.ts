import type { ScenarioInputs, ScenarioResults } from './types';
import {
  CORP_RATES,
  INST_RATES,
  PRIVATE_RATES,
  OE_RATES,
  MONTHLY_RENT,
  FIXED_OVERHEAD,
  ROOMS,
  TIME_SLOTS,
  getSurchargeMultiplier,
} from './types';

// ==========================================
// CORE CALCULATION FUNCTIONS
// ==========================================

/**
 * Calculate the OE rate based on students per class (clamped to 6-15)
 */
function getOERate(studentsPerClass: number) {
  const clamped = Math.max(6, Math.min(15, Math.round(studentsPerClass)));
  return OE_RATES[clamped];
}

/**
 * Calculate monthly hours from weekly hours
 */
function weeklyToMonthly(weeklyHours: number): number {
  return weeklyHours * 4.33; // Average weeks per month
}

/**
 * Main calculation function - computes all results from inputs
 */
export function calculateScenario(inputs: ScenarioInputs): ScenarioResults {
  const surcharge = getSurchargeMultiplier(inputs.salaryMixPercent);

  // ==========================================
  // OPEN ENROLLMENT CALCULATIONS
  // ==========================================
  const oeRate = getOERate(inputs.oeStudentsPerClass);
  const oeMonthlyHours = weeklyToMonthly(inputs.oeHoursPerWeek * inputs.oeClasses);
  const oeRevenue = oeMonthlyHours * oeRate.rev;
  const oeTeacherCost = oeMonthlyHours * oeRate.teacher * surcharge;
  const oeTotalStudents = inputs.oeClasses * inputs.oeStudentsPerClass;

  // ==========================================
  // PRIVATE LESSONS CALCULATIONS
  // ==========================================
  const privateMonthlyHours = inputs.privateStudents * inputs.privateHoursPerStudent;
  const privateRevenue = privateMonthlyHours * PRIVATE_RATES.studentPrice;
  const privateTeacherCost = privateMonthlyHours * PRIVATE_RATES.teacherCost * surcharge;

  // ==========================================
  // CORPORATE CALCULATIONS (off-site)
  // ==========================================
  const corpRevenue = inputs.corpHoursPerMonth * CORP_RATES.effRev;
  const corpTeacherCost = inputs.corpHoursPerMonth * CORP_RATES.teacherCost * surcharge;
  const corpTotalParticipants = inputs.corpGroups * inputs.corpParticipantsPerGroup;

  // ==========================================
  // INSTITUTIONAL CALCULATIONS (off-site)
  // ==========================================
  const instRevenue = inputs.instHoursPerMonth * INST_RATES.effRev;
  const instTeacherCost = inputs.instHoursPerMonth * INST_RATES.teacherCost * surcharge;
  const instTotalParticipants = inputs.instGroups * inputs.instParticipantsPerGroup;

  // ==========================================
  // RENT ALLOCATION (OE + Private only)
  // ==========================================
  const totalFacilityHours = oeMonthlyHours + privateMonthlyHours;
  let oeRentShare = 0;
  let privateRentShare = 0;

  if (totalFacilityHours > 0) {
    oeRentShare = (oeMonthlyHours / totalFacilityHours) * MONTHLY_RENT;
    privateRentShare = (privateMonthlyHours / totalFacilityHours) * MONTHLY_RENT;
  }
  const totalRent = MONTHLY_RENT;

  // ==========================================
  // TOTAL TEACHER COSTS
  // ==========================================
  const totalTeacherCost = oeTeacherCost + privateTeacherCost + corpTeacherCost + instTeacherCost;

  // ==========================================
  // OVERHEAD CALCULATIONS
  // Based on historical expense ratios
  // ==========================================

  // Direct costs (teacher + rent) typically represent ~65% of total expenses
  // Overhead adds the remaining ~35%
  // We calculate overhead as a percentage of direct costs

  const directCosts = totalTeacherCost + totalRent;

  // Indirect costs: 11.9% of total (which is ~18.3% of direct costs)
  // Formula: if direct = 65% and indirect = 11.9%, then indirect/direct = 11.9/65 = 0.183
  const indirectCosts = directCosts * (FIXED_OVERHEAD.indirectCosts / 0.65);

  // Fringe benefits: 5.3% of total
  const fringeBenefits = directCosts * (FIXED_OVERHEAD.fringeBenefits / 0.65);

  // Other fixed (telephone, email, advertising): 3.3% of total
  const otherFixedRate = FIXED_OVERHEAD.telephone + FIXED_OVERHEAD.emailInternet + FIXED_OVERHEAD.advertising;
  const otherFixed = directCosts * (otherFixedRate / 0.65);

  const totalOverhead = indirectCosts + fringeBenefits + otherFixed;

  // ==========================================
  // REVENUE TOTALS
  // ==========================================
  const totalRevenue = oeRevenue + privateRevenue + corpRevenue + instRevenue;

  // ==========================================
  // COST TOTALS
  // ==========================================
  const totalCosts = totalTeacherCost + totalRent + totalOverhead;

  // ==========================================
  // PROFIT CALCULATIONS
  // ==========================================
  const netProfit = totalRevenue - totalCosts;
  const profitMargin = totalRevenue > 0 ? (netProfit / totalRevenue) * 100 : 0;

  // ==========================================
  // STUDENT & CAPACITY METRICS
  // ==========================================
  const totalStudents = oeTotalStudents + inputs.privateStudents + corpTotalParticipants + instTotalParticipants;
  const totalInstructionHours = oeMonthlyHours + privateMonthlyHours + inputs.corpHoursPerMonth + inputs.instHoursPerMonth;

  // Capacity utilization: based on facility-based classes (OE only, as they use rooms)
  // Max capacity: 5 rooms × avg 11 students × 8 slots/week × 4.33 weeks
  const maxMonthlyStudentSlots = ROOMS.reduce((sum, r) => sum + r.maxCapacity, 0) * TIME_SLOTS.length * 2 * 4.33;
  const actualStudentSlots = inputs.oeClasses * inputs.oeStudentsPerClass * (inputs.oeHoursPerWeek / 2) * 4.33; // Assuming 2hr avg per slot
  const capacityUtilization = maxMonthlyStudentSlots > 0 ? (actualStudentSlots / maxMonthlyStudentSlots) * 100 : 0;

  // Per-student metrics
  const revenuePerStudent = totalStudents > 0 ? totalRevenue / totalStudents : 0;
  const costPerStudent = totalStudents > 0 ? totalCosts / totalStudents : 0;
  const profitPerStudent = totalStudents > 0 ? netProfit / totalStudents : 0;

  return {
    // Revenue breakdown
    oeRevenue,
    privateRevenue,
    corpRevenue,
    instRevenue,
    totalRevenue,

    // Cost breakdown
    oeTeacherCost,
    privateTeacherCost,
    corpTeacherCost,
    instTeacherCost,
    totalTeacherCost,

    // Rent allocation
    oeRentShare,
    privateRentShare,
    totalRent,

    // Overhead costs
    indirectCosts,
    fringeBenefits,
    otherFixed,
    totalOverhead,

    // Summary
    totalCosts,
    netProfit,
    profitMargin,

    // Capacity metrics
    totalStudents,
    totalInstructionHours,
    capacityUtilization,

    // Per-student metrics
    revenuePerStudent,
    costPerStudent,
    profitPerStudent,
  };
}

/**
 * Compare two scenarios and return the differences
 */
export function compareScenarios(current: ScenarioResults, goal: ScenarioResults) {
  return {
    revenueDiff: goal.totalRevenue - current.totalRevenue,
    costDiff: goal.totalCosts - current.totalCosts,
    profitDiff: goal.netProfit - current.netProfit,
    marginDiff: goal.profitMargin - current.profitMargin,
    studentDiff: goal.totalStudents - current.totalStudents,
    hoursDiff: goal.totalInstructionHours - current.totalInstructionHours,
    profitPerStudentDiff: goal.profitPerStudent - current.profitPerStudent,
    revenueGrowthPct: current.totalRevenue > 0
      ? ((goal.totalRevenue - current.totalRevenue) / current.totalRevenue) * 100
      : 0,
    profitGrowthPct: current.netProfit > 0
      ? ((goal.netProfit - current.netProfit) / current.netProfit) * 100
      : 0,
  };
}

/**
 * Format currency for display
 */
export function formatCurrency(value: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(value);
}

/**
 * Format currency with cents
 */
export function formatCurrencyDetailed(value: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }).format(value);
}

/**
 * Format percentage for display
 */
export function formatPercent(value: number): string {
  return `${value >= 0 ? '+' : ''}${value.toFixed(1)}%`;
}

/**
 * Format number with sign
 */
export function formatDiff(value: number): string {
  const formatted = formatCurrency(Math.abs(value));
  return value >= 0 ? `+${formatted}` : `-${formatted}`;
}
