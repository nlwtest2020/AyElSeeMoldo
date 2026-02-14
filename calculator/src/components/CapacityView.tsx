import type { ScenarioInputs } from '../types';
import { ROOMS, TIME_SLOTS, DAY_PATTERNS } from '../types';
import { Users, Info } from 'lucide-react';

interface CapacityViewProps {
  currentInputs: ScenarioInputs;
  goalInputs: ScenarioInputs;
}

export function CapacityView({ currentInputs, goalInputs }: CapacityViewProps) {
  // Calculate total capacity
  const totalSlots = ROOMS.length * TIME_SLOTS.length * DAY_PATTERNS.length;
  const totalCapacity = ROOMS.reduce((sum, room) => sum + room.maxCapacity, 0) * TIME_SLOTS.length * DAY_PATTERNS.length;

  // Estimate slots used by OE classes
  const currentOESlots = Math.min(currentInputs.oeClasses, totalSlots);
  const goalOESlots = Math.min(goalInputs.oeClasses, totalSlots);

  // Calculate student capacity utilization
  const currentStudents = currentInputs.oeClasses * currentInputs.oeStudentsPerClass;
  const goalStudents = goalInputs.oeClasses * goalInputs.oeStudentsPerClass;

  return (
    <div className="bg-white rounded-xl border border-gray-200 shadow-lg overflow-hidden">
      {/* Header */}
      <div className="bg-gray-800 px-6 py-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <Users className="w-5 h-5" />
          Facility Capacity
        </h2>
        <p className="text-sm text-gray-400 mt-1">Room utilization for on-site classes (OE only)</p>
      </div>

      {/* Room Grid */}
      <div className="p-6">
        <div className="mb-6">
          <div className="flex items-center justify-between mb-2">
            <span className="text-sm font-medium text-gray-700">Total Weekly Slots</span>
            <span className="text-sm text-gray-500">{totalSlots} slots ({ROOMS.length} rooms × {TIME_SLOTS.length} times × {DAY_PATTERNS.length} day patterns)</span>
          </div>
          <div className="flex items-center justify-between mb-4">
            <span className="text-sm font-medium text-gray-700">Max Student Capacity</span>
            <span className="text-sm text-gray-500">{totalCapacity} student-slots/week</span>
          </div>
        </div>

        {/* Visual Grid */}
        <div className="grid grid-cols-5 gap-3 mb-6">
          {ROOMS.map((room) => (
            <div key={room.id} className="text-center">
              <div className="text-xs font-medium text-gray-500 mb-2">{room.name}</div>
              <div className="bg-gray-100 rounded-lg p-3">
                <div className="text-lg font-bold text-gray-700">{room.maxCapacity}</div>
                <div className="text-xs text-gray-400">max</div>
              </div>
              <div className="mt-2 text-xs text-gray-400">
                {TIME_SLOTS.length * DAY_PATTERNS.length} slots/wk
              </div>
            </div>
          ))}
        </div>

        {/* Utilization Comparison */}
        <div className="border-t border-gray-200 pt-6">
          <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-4">
            OE Class Utilization
          </h3>

          <div className="space-y-4">
            {/* Current */}
            <div>
              <div className="flex justify-between text-sm mb-1">
                <span className="text-blue-600 font-medium">Current</span>
                <span className="text-gray-500">
                  {currentOESlots} / {totalSlots} slots ({((currentOESlots / totalSlots) * 100).toFixed(0)}%)
                </span>
              </div>
              <div className="h-4 bg-gray-200 rounded-full overflow-hidden">
                <div
                  className="h-full bg-blue-500 rounded-full transition-all duration-500"
                  style={{ width: `${(currentOESlots / totalSlots) * 100}%` }}
                />
              </div>
              <div className="text-xs text-gray-400 mt-1">
                {currentStudents} students in {currentInputs.oeClasses} classes
              </div>
            </div>

            {/* Goal */}
            <div>
              <div className="flex justify-between text-sm mb-1">
                <span className="text-emerald-600 font-medium">Goal</span>
                <span className="text-gray-500">
                  {goalOESlots} / {totalSlots} slots ({((goalOESlots / totalSlots) * 100).toFixed(0)}%)
                </span>
              </div>
              <div className="h-4 bg-gray-200 rounded-full overflow-hidden">
                <div
                  className="h-full bg-emerald-500 rounded-full transition-all duration-500"
                  style={{ width: `${(goalOESlots / totalSlots) * 100}%` }}
                />
              </div>
              <div className="text-xs text-gray-400 mt-1">
                {goalStudents} students in {goalInputs.oeClasses} classes
              </div>
            </div>
          </div>
        </div>

        {/* Info Box */}
        <div className="mt-6 bg-blue-50 border border-blue-200 rounded-lg p-4 flex items-start gap-3">
          <Info className="w-5 h-5 text-blue-500 flex-shrink-0 mt-0.5" />
          <div className="text-sm text-blue-800">
            <p className="font-medium mb-1">How capacity works:</p>
            <ul className="text-blue-700 space-y-1">
              <li>• <strong>Open Enrollment</strong> uses facility rooms (counted here)</li>
              <li>• <strong>Private Lessons</strong> share facility space (implicit in OE slots)</li>
              <li>• <strong>Corporate & Institutional</strong> are off-site (not counted here)</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
