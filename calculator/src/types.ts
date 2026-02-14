// ==========================================
// ROOM & SCHEDULING CONFIGURATION
// ==========================================

export type RoomId = 'small1' | 'small2' | 'large1' | 'large2' | 'conference';
export type DayPattern = 'mon-wed' | 'tue-thu';
export type TimeSlot = 0 | 1 | 2 | 3;
export type ClassType = 'corporate' | 'institutional' | 'openEnrollment' | 'private';

export interface Room {
  id: RoomId;
  name: string;
  maxCapacity: number;
}

export const ROOMS: Room[] = [
  { id: 'small1', name: 'Small 1', maxCapacity: 8 },
  { id: 'small2', name: 'Small 2', maxCapacity: 8 },
  { id: 'large1', name: 'Large 1', maxCapacity: 12 },
  { id: 'large2', name: 'Large 2', maxCapacity: 12 },
  { id: 'conference', name: 'Conference', maxCapacity: 15 },
];

export const TIME_SLOTS: { slot: TimeSlot; label: string; hours: number }[] = [
  { slot: 0, label: '9:00 – 11:00', hours: 2 },
  { slot: 1, label: '12:00 – 14:15', hours: 2.25 },
  { slot: 2, label: '16:00 – 18:15', hours: 2.25 },
  { slot: 3, label: '18:30 – 20:45', hours: 2.25 },
];

export const DAY_PATTERNS: { pattern: DayPattern; label: string; daysPerWeek: number }[] = [
  { pattern: 'mon-wed', label: 'Mon/Wed', daysPerWeek: 2 },
  { pattern: 'tue-thu', label: 'Tue/Thu', daysPerWeek: 2 },
];

// Total weekly slots: 5 rooms × 4 time slots × 2 day patterns = 40 slots
export const TOTAL_WEEKLY_SLOTS = ROOMS.length * TIME_SLOTS.length * DAY_PATTERNS.length;

// Max capacity per week: sum of all room capacities × slots per room
export const MAX_WEEKLY_CAPACITY = ROOMS.reduce((sum, room) => sum + room.maxCapacity, 0) * TIME_SLOTS.length * DAY_PATTERNS.length;

// ==========================================
// REVENUE RATES BY CLASS TYPE
// ==========================================

export const CORP_RATES = {
  instrPrice: 32.00,      // Base instruction price per hour
  matEval: 2.9194,        // Materials & evaluation per hour
  effRev: 34.92,          // Effective revenue per hour (instrPrice + matEval)
  teacherCost: 15.15,     // Teacher cost per hour (base, before surcharge)
};

export const INST_RATES = {
  instrPrice: 32.00,
  matEval: 2.6212,
  effRev: 34.62,
  teacherCost: 20.16,
};

export const PRIVATE_RATES = {
  studentPrice: 30.00,    // Price per student per hour
  teacherCost: 14.73,
};

// Open Enrollment rates vary by class size (6-15 students)
export interface OERateEntry {
  rev: number;            // Revenue per hour
  teacher: number;        // Teacher cost per hour
}

export const OE_RATES: Record<number, OERateEntry> = {
  6:  { rev: 27.78, teacher: 11.20 },
  7:  { rev: 32.41, teacher: 11.20 },
  8:  { rev: 37.04, teacher: 11.20 },
  9:  { rev: 41.67, teacher: 11.20 },
  10: { rev: 46.30, teacher: 11.20 },
  11: { rev: 50.93, teacher: 11.20 },
  12: { rev: 55.56, teacher: 11.20 },
  13: { rev: 60.19, teacher: 11.20 },
  14: { rev: 64.82, teacher: 11.20 },
  15: { rev: 69.45, teacher: 11.20 },
};

// ==========================================
// FIXED COSTS (Monthly)
// ==========================================

export const MONTHLY_RENT = 3400;

// Historical overhead percentages (from MOD 5-year average FY20-25)
// These are percentages of total expenses that represent fixed overhead
export const FIXED_OVERHEAD = {
  indirectCosts: 0.119,      // 11.9% - Indirect costs (698100)
  fringeBenefits: 0.053,     // 5.3% - Fringe benefits (517550)
  telephone: 0.015,          // 1.5% - Telephone (673000)
  emailInternet: 0.006,      // 0.6% - Email & Internet (673600)
  advertising: 0.012,        // 1.2% - Advertising (694000)
};

// Total fixed overhead as % of variable costs
// If direct costs (teacher + rent) are X, total overhead adds ~25% on top
export const FIXED_OVERHEAD_RATE = Object.values(FIXED_OVERHEAD).reduce((a, b) => a + b, 0);

// ==========================================
// VARIABLE COSTS (Scale with students/hours)
// ==========================================

// These are included in the per-hour teacher rates above, but here for reference
export const VARIABLE_COST_CATEGORIES = {
  consultantsAndTuition: 0.309,  // 30.9% - Teacher payments (697000 + 667000)
  honoraria: 0.170,              // 17.0% - Non-salaried payments (518000)
  salariesNonUS: 0.167,          // 16.7% - Staff salaries (510100)
  supplies: 0.031,               // 3.1% - Supplies (680000)
};

// ==========================================
// SALARY MIX SURCHARGE
// ==========================================

// Salaried teachers cost 40% more than consultants
export const SALARY_SURCHARGE_RATE = 0.40;

export function getSurchargeMultiplier(salaryMixPercent: number): number {
  return 1 + (salaryMixPercent / 100) * SALARY_SURCHARGE_RATE;
}

// ==========================================
// SCENARIO SNAPSHOT TYPES
// ==========================================

export interface ClassAllocation {
  classType: ClassType;
  roomId: RoomId;
  dayPattern: DayPattern;
  timeSlot: TimeSlot;
  studentCount: number;
}

export interface ScenarioInputs {
  // Open Enrollment
  oeClasses: number;
  oeStudentsPerClass: number;
  oeHoursPerWeek: number;

  // Private Lessons
  privateStudents: number;
  privateHoursPerStudent: number;

  // Corporate (off-site, no rent allocation)
  corpGroups: number;
  corpParticipantsPerGroup: number;
  corpHoursPerMonth: number;

  // Institutional (off-site, no rent allocation)
  instGroups: number;
  instParticipantsPerGroup: number;
  instHoursPerMonth: number;

  // Global settings
  salaryMixPercent: number;
}

export interface ScenarioResults {
  // Revenue breakdown
  oeRevenue: number;
  privateRevenue: number;
  corpRevenue: number;
  instRevenue: number;
  totalRevenue: number;

  // Cost breakdown
  oeTeacherCost: number;
  privateTeacherCost: number;
  corpTeacherCost: number;
  instTeacherCost: number;
  totalTeacherCost: number;

  // Rent allocation (OE + Private only)
  oeRentShare: number;
  privateRentShare: number;
  totalRent: number;

  // Overhead costs
  indirectCosts: number;
  fringeBenefits: number;
  otherFixed: number;
  totalOverhead: number;

  // Summary
  totalCosts: number;
  netProfit: number;
  profitMargin: number;

  // Capacity metrics
  totalStudents: number;
  totalInstructionHours: number;
  capacityUtilization: number;

  // Per-student metrics
  revenuePerStudent: number;
  costPerStudent: number;
  profitPerStudent: number;
}

export interface Snapshot {
  name: string;
  inputs: ScenarioInputs;
  results: ScenarioResults;
}

// ==========================================
// DEFAULT VALUES
// ==========================================

export const DEFAULT_INPUTS: ScenarioInputs = {
  oeClasses: 10,
  oeStudentsPerClass: 8,
  oeHoursPerWeek: 6,

  privateStudents: 9,
  privateHoursPerStudent: 6,

  corpGroups: 4,
  corpParticipantsPerGroup: 4,
  corpHoursPerMonth: 8,

  instGroups: 2,
  instParticipantsPerGroup: 6,
  instHoursPerMonth: 6,

  salaryMixPercent: 0,
};
