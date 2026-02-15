import { useState } from 'react';
import type { ScheduleGrid, OnSiteType } from '../types';
import { ROOMS, TIME_SLOTS, DAY_PATTERNS, MAX_CAPACITY, slotKey } from '../types';
import { Trash2, Users } from 'lucide-react';

interface Props {
  grid: ScheduleGrid;
  onChange: (grid: ScheduleGrid) => void;
}

const TYPE_CONFIG = {
  openEnrollment: { label: 'Open', color: 'bg-amber-500', border: 'border-amber-400', text: 'text-white' },
  private:        { label: 'Private', color: 'bg-purple-500', border: 'border-purple-400', text: 'text-white' },
};

export function VisualScheduler({ grid, onChange }: Props) {
  const [draggingType, setDraggingType] = useState<OnSiteType | null>(null);
  const [dragOver, setDragOver] = useState<string | null>(null);

  const totalStudents = Object.values(grid).reduce((s, sl) => s + sl.studentCount, 0);
  const utilization   = (totalStudents / MAX_CAPACITY) * 100;

  const setSlot = (key: string, type: OnSiteType, capacity: number) => {
    onChange({ ...grid, [key]: { classType: type, studentCount: capacity } });
  };

  const removeSlot = (key: string) => {
    const next = { ...grid };
    delete next[key];
    onChange(next);
  };

  const updateCount = (key: string, delta: number, max: number) => {
    const current = grid[key];
    if (!current) return;
    const next = Math.max(1, Math.min(max, current.studentCount + delta));
    onChange({ ...grid, [key]: { ...current, studentCount: next } });
  };

  const clearAll = () => onChange({});

  return (
    <div className="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
      {/* Toolbar */}
      <div className="px-5 py-3 border-b border-gray-100 flex items-center gap-4 flex-wrap">
        <span className="text-sm font-medium text-gray-600">On-site classes:</span>

        {/* Draggable pills */}
        {(['openEnrollment', 'private'] as OnSiteType[]).map(type => (
          <div
            key={type}
            draggable
            onDragStart={() => setDraggingType(type)}
            onDragEnd={() => setDraggingType(null)}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg cursor-grab active:cursor-grabbing select-none font-medium text-sm text-white shadow-sm ${TYPE_CONFIG[type].color}`}
          >
            <span className="grid grid-cols-2 gap-0.5">
              {[...Array(4)].map((_, i) => <span key={i} className="w-1 h-1 rounded-full bg-white/70" />)}
            </span>
            {TYPE_CONFIG[type].label === 'Open' ? 'Open Enrollment' : 'Private'}
          </div>
        ))}

        {/* Capacity bar */}
        <div className="ml-auto flex items-center gap-3">
          <span className="flex items-center gap-1 text-sm text-gray-500">
            <Users className="w-4 h-4" />
            <span className="font-semibold text-gray-800">{totalStudents}</span>
            <span>/ {MAX_CAPACITY} students</span>
          </span>
          <div className="w-32 h-2 bg-gray-200 rounded-full overflow-hidden">
            <div
              className={`h-full rounded-full transition-all ${utilization > 80 ? 'bg-red-500' : utilization > 50 ? 'bg-amber-500' : 'bg-blue-500'}`}
              style={{ width: `${Math.min(100, utilization)}%` }}
            />
          </div>
          <span className="text-sm font-semibold text-gray-600">{utilization.toFixed(1)}% utilized</span>
          <button
            onClick={clearAll}
            className="flex items-center gap-1 px-3 py-1.5 text-xs font-medium text-gray-500 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors border border-gray-200"
          >
            <Trash2 className="w-3.5 h-3.5" />
            Clear All
          </button>
        </div>
      </div>

      {/* Grid */}
      <div className="overflow-x-auto">
        <table className="w-full border-collapse text-sm">
          <thead>
            <tr className="bg-gray-50">
              <th className="px-4 py-3 text-left font-semibold text-gray-600 w-28 border-r border-gray-200">Time</th>
              {ROOMS.map(room => (
                <th key={room.id} colSpan={2} className="px-2 py-3 text-center border-r border-gray-200 last:border-r-0">
                  <div className="font-bold text-gray-800">{room.name}</div>
                  <div className="text-xs text-gray-400 font-normal">Max {room.maxCapacity}</div>
                </th>
              ))}
            </tr>
            <tr className="bg-gray-50 border-b border-gray-200">
              <th className="border-r border-gray-200" />
              {ROOMS.map(room =>
                DAY_PATTERNS.map(dp => (
                  <th key={`${room.id}-${dp.pattern}`} className="px-2 py-1.5 text-center text-xs text-gray-400 font-normal border-r border-gray-100 last:border-r-0">
                    {dp.label}
                  </th>
                ))
              )}
            </tr>
          </thead>
          <tbody>
            {TIME_SLOTS.map(ts => (
              <tr key={ts.slot} className="border-b border-gray-100 last:border-b-0">
                <td className="px-4 py-2 font-medium text-gray-500 text-xs border-r border-gray-200 whitespace-nowrap">
                  {ts.label}
                </td>
                {ROOMS.map(room =>
                  DAY_PATTERNS.map(dp => {
                    const key = slotKey(room.id, dp.pattern, ts.slot);
                    const slot = grid[key];
                    const isOver = dragOver === key;

                    return (
                      <td
                        key={key}
                        className="px-1.5 py-1.5 border-r border-gray-100 last:border-r-0"
                        onDragOver={e => { e.preventDefault(); setDragOver(key); }}
                        onDragLeave={() => setDragOver(null)}
                        onDrop={e => {
                          e.preventDefault();
                          setDragOver(null);
                          if (draggingType && !slot) setSlot(key, draggingType, room.maxCapacity);
                        }}
                      >
                        {slot ? (
                          <FilledCell
                            slot={slot}
                            maxCapacity={room.maxCapacity}
                            onRemove={() => removeSlot(key)}
                            onIncrease={() => updateCount(key, 1, room.maxCapacity)}
                            onDecrease={() => updateCount(key, -1, room.maxCapacity)}
                          />
                        ) : (
                          <EmptyCell isOver={isOver} draggingType={draggingType} />
                        )}
                      </td>
                    );
                  })
                )}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function FilledCell({ slot, maxCapacity, onRemove, onIncrease, onDecrease }: {
  slot: { classType: OnSiteType; studentCount: number };
  maxCapacity: number;
  onRemove: () => void;
  onIncrease: () => void;
  onDecrease: () => void;
}) {
  const cfg = TYPE_CONFIG[slot.classType];
  const pct = (slot.studentCount / maxCapacity) * 100;

  return (
    <div className={`rounded-lg p-2 ${cfg.color} min-w-[90px]`}>
      <div className="flex items-center justify-between mb-1">
        <span className="text-xs font-bold text-white">{cfg.label}</span>
        <button onClick={onRemove} className="text-white/70 hover:text-white leading-none text-xs">✕</button>
      </div>
      <div className="flex items-center gap-1 mb-1">
        <Users className="w-3 h-3 text-white/80" />
        <span className="text-white text-xs font-semibold">{slot.studentCount}</span>
        <span className="text-white/60 text-xs">/{maxCapacity}</span>
        <div className="ml-auto flex flex-col gap-0.5">
          <button onClick={onIncrease} className="text-white/80 hover:text-white leading-none text-xs">▲</button>
          <button onClick={onDecrease} className="text-white/80 hover:text-white leading-none text-xs">▼</button>
        </div>
      </div>
      <div className="h-1.5 bg-black/20 rounded-full overflow-hidden">
        <div className="h-full bg-white/70 rounded-full" style={{ width: `${pct}%` }} />
      </div>
    </div>
  );
}

function EmptyCell({ isOver, draggingType }: { isOver: boolean; draggingType: OnSiteType | null }) {
  const borderColor = isOver && draggingType ? TYPE_CONFIG[draggingType].border : 'border-gray-200';
  const bg = isOver ? 'bg-gray-50' : 'bg-white';

  return (
    <div className={`min-h-[72px] min-w-[90px] rounded-lg border-2 border-dashed ${borderColor} ${bg} flex items-center justify-center transition-colors`}>
      <span className="text-xs text-gray-300 text-center leading-tight px-1">
        {isOver ? 'Drop here' : 'Drop class\nhere'}
      </span>
    </div>
  );
}
