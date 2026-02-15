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

// Each day pattern = 2 days/week × 4.33 weeks/month = 8.66 sessions/month
export const WEEKS_PER_MONTH = 4.33;
export const DAYS_PER_PATTERN = 2;
export const SESSIONS_PER_MONTH = DAYS_PER_PATTERN * WEEKS_PER_MONTH; // 8.66

// Total max capacity: 55 students/slot × 8 slots = 440
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

// ── RATES ─────────────────────────────────────────────────────────────────────
export const MONTHLY_RENT = 3400;
export const SALARY_SURCHARGE = 0.40;

export const CORP_RATES  = { effRev: 34.92, teacherCost: 15.15 };
export const INST_RATES  = { effRev: 34.62, teacherCost: 20.16 };
export const PRIVATE_RATES = { revenue: 30.00, teacherCost: 14.73 };

export const OE_RATES: Record<number, { rev: number; teacher: number }> = {
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

// Historical overhead as % of total expenses (MOD 5yr avg FY20-25)
export const OVERHEAD = {
  indirect:  0.119,   // Indirect costs (698100)
  fringe:    0.053,   // Fringe benefits (517550)
  other:     0.033,   // Telephone + email + advertising
};

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

export interface MonthlyResults {
  oe:      SectionResult & { classes: number; avgStudents: number; seatCount: number };
  priv:    SectionResult;
  corp:    SectionResult;
  inst:    SectionResult;
  rent:    number;
  overhead: { indirect: number; fringe: number; other: number; total: number };
  totalRevenue: number;
  totalCosts:   number;
  netProfit:    number;
  profitMargin: number;
  totalStudents: number;
}
