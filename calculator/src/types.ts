// ── ROOM & SCHEDULE ──────────────────────────────────────────────────────────
export type RoomId = 'small1' | 'small2' | 'large1' | 'large2' | 'conference';
export type DayPattern = 'mon-wed' | 'tue-thu';
export type TimeSlot = 0 | 1 | 2 | 3;
export type OnSiteType = 'openEnrollment' | 'private';

export interface Room {
  id: RoomId;
  name: string;
  maxCapacity: number;
}

export const ROOMS: Room[] = [
  { id: 'small1',    name: 'Small 1',    maxCapacity: 8  },
  { id: 'small2',    name: 'Small 2',    maxCapacity: 8  },
  { id: 'large1',    name: 'Large 1',    maxCapacity: 12 },
  { id: 'large2',    name: 'Large 2',    maxCapacity: 12 },
  { id: 'conference',name: 'Conference', maxCapacity: 15 },
];

export const TIME_SLOTS: { slot: TimeSlot; label: string; hours: number }[] = [
  { slot: 0, label: '9:00 – 11:00',   hours: 2.00 },
  { slot: 1, label: '12:00 – 14:15',  hours: 2.25 },
  { slot: 2, label: '16:00 – 18:15',  hours: 2.25 },
  { slot: 3, label: '18:30 – 20:45',  hours: 2.25 },
];

export const DAY_PATTERNS: { pattern: DayPattern; label: string }[] = [
  { pattern: 'mon-wed', label: 'Mon/Wed' },
  { pattern: 'tue-thu', label: 'Tue/Thu' },
];

// Simplified: 4 weeks/month (6 hrs/week = 24 hrs/month standard)
export const WEEKS_PER_MONTH = 4;
export const DAYS_PER_PATTERN = 2;
export const SESSIONS_PER_MONTH = DAYS_PER_PATTERN * WEEKS_PER_MONTH; // 8

export const MAX_CAPACITY = ROOMS.reduce((s, r) => s + r.maxCapacity, 0) *
  TIME_SLOTS.length * DAY_PATTERNS.length;

export function slotKey(roomId: RoomId, day: DayPattern, ts: TimeSlot): string {
  return `${roomId}|${day}|${ts}`;
}

export function slotMonthlyHours(ts: TimeSlot): number {
  return TIME_SLOTS[ts].hours * SESSIONS_PER_MONTH;
}

// ── SCHEDULED SLOT ───────────────────────────────────────────────────────────
export interface ScheduledSlot {
  classType: OnSiteType;
  studentCount: number;
}

export type ScheduleGrid = Record<string, ScheduledSlot>;

// ── COST RATES ───────────────────────────────────────────────────────────────
// Base teacher rate: $17/hr
export const TEACHER_BASE_RATE = 17;
export const SALARIED_SURCHARGE = 0.40; // +40% for salaried teachers

// Revenue per student per hour for Open Enrollment
export const OE_STUDENT_RATE = 4.63; // ~$27.78/hr at 6 students, scales up

// Revenue/teacher rates by program type (hourly)
export const CORP_RATES  = { revenue: 34.92, teacherCost: TEACHER_BASE_RATE };
export const INST_RATES  = { revenue: 34.62, teacherCost: TEACHER_BASE_RATE * 1.18 }; // higher for institutional
export const PRIVATE_RATES = { revenue: 30.00, teacherCost: TEACHER_BASE_RATE };

// Open Enrollment: revenue scales with students, teacher cost is flat $17/hr
export const OE_RATES: Record<number, { rev: number; teacher: number }> = {
  6:  { rev: 27.78, teacher: TEACHER_BASE_RATE },
  7:  { rev: 32.41, teacher: TEACHER_BASE_RATE },
  8:  { rev: 37.04, teacher: TEACHER_BASE_RATE },
  9:  { rev: 41.67, teacher: TEACHER_BASE_RATE },
  10: { rev: 46.30, teacher: TEACHER_BASE_RATE },
  11: { rev: 50.93, teacher: TEACHER_BASE_RATE },
  12: { rev: 55.56, teacher: TEACHER_BASE_RATE },
  13: { rev: 60.19, teacher: TEACHER_BASE_RATE },
  14: { rev: 64.82, teacher: TEACHER_BASE_RATE },
  15: { rev: 69.45, teacher: TEACHER_BASE_RATE },
};

// ── FIXED COSTS (monthly, don't scale with activity) ─────────────────────────
export const MONTHLY_RENT = 3400;
export const MONTHLY_ADMIN = 650;    // ~13% historical, fixed overhead
export const MONTHLY_OTHER = 165;    // Phone, email, ads (~3.3% historical)

// ── VARIABLE COST RATES (scale with activity) ────────────────────────────────
export const IDC_RATE = 0.12;        // 12% of direct costs (indirect costs)

// ── OFF-SITE INPUTS ──────────────────────────────────────────────────────────
export interface OffSiteInputs {
  corpGroups: number;
  corpHoursPerMonth: number;
  instGroups: number;
  instHoursPerMonth: number;
  privateStudents: number;
  privateHoursPerMonth: number;
  salaryMixPercent: number;
}

export const DEFAULT_OFFSITE: OffSiteInputs = {
  corpGroups: 4,
  corpHoursPerMonth: 8,
  instGroups: 2,
  instHoursPerMonth: 6,
  privateStudents: 9,
  privateHoursPerMonth: 6,
  salaryMixPercent: 0,
};

// ── MONTHLY RESULTS ──────────────────────────────────────────────────────────
export interface SectionResult {
  revenue: number;
  teacherCost: number;
  rentShare: number;
  profit: number;
  margin: number;
  hours: number;
  students: number;
}

export interface CostBreakdown {
  teacher: number;      // Base teacher pay
  salarySurcharge: number; // +40% for salaried (includes fringe/benefits)
  idc: number;          // 12% of direct costs (scales)
  rent: number;         // $3400 fixed
  admin: number;        // $650 fixed
  other: number;        // $165 fixed
  total: number;
}

export interface MonthlyResults {
  oe:      SectionResult & { classes: number; avgStudents: number; seatCount: number };
  priv:    SectionResult;
  corp:    SectionResult;
  inst:    SectionResult;
  costs:   CostBreakdown;
  totalRevenue: number;
  totalCosts:   number;
  netProfit:    number;
  profitMargin: number;
  totalStudents: number;
  totalHours: number;
}
