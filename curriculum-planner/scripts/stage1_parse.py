"""
Stage 1: PARSE — Extract structured curriculum data from a .docx roadmap.

Reads the first .docx found in ../input/ and produces parsed_curriculum.json
in ../output/ with per-session data: title, subtitle, SWBATs, schedule blocks,
and evidence statements.

Usage:
    python stage1_parse.py
"""

import json
import os
import re
import sys
from pathlib import Path

from docx import Document


INPUT_DIR = Path(__file__).resolve().parent.parent / "input"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


def find_input_docx() -> Path:
    """Return the first .docx file found in the input directory."""
    docx_files = sorted(INPUT_DIR.glob("*.docx"))
    if not docx_files:
        print(f"ERROR: No .docx files found in {INPUT_DIR}")
        sys.exit(1)
    chosen = docx_files[0]
    print(f"Using input file: {chosen.name}")
    return chosen


# ---------------------------------------------------------------------------
# Heading / style helpers
# ---------------------------------------------------------------------------

SESSION_RE = re.compile(
    r"(?:session|lesson|module)\s*(\d+)\s*[:\-–—]\s*(.+)",
    re.IGNORECASE,
)

SWBAT_RE = re.compile(
    r"(?:SWBAT|students?\s+will\s+be\s+able\s+to|learning\s+(?:target|objective)s?)\s*[:\-–—]?\s*",
    re.IGNORECASE,
)

TIME_RE = re.compile(
    r"(\d{1,2}:\d{2})\s*[-–—]\s*(\d{1,2}:\d{2})",
)

DURATION_RE = re.compile(r"\(?\s*(\d+)\s*min(?:ute)?s?\s*\)?", re.IGNORECASE)

# Pattern for schedule blocks hiding in evidence: "HH:MM–HH:MM | Name | NN min"
EVIDENCE_SCHEDULE_RE = re.compile(
    r"(\d{1,2}:\d{2})\s*[-–—]\s*(\d{1,2}:\d{2})\s*\|\s*(.+?)\s*\|\s*(\d+)\s*min",
    re.IGNORECASE,
)

# Non-SWBAT lines to filter out
SWBAT_NOISE_RE = re.compile(
    r"^(session\s+\d+\s+contribution|by the end of session\s+\d+.*should be able to:?|cumulative progression|summary of all timing adjustments)",
    re.IGNORECASE,
)


def _heading_level(paragraph) -> int:
    """Return the heading level (1-9) or 0 if not a heading."""
    style_name = (paragraph.style.name if paragraph.style else "") or ""
    style_name = style_name.lower()
    if style_name.startswith("heading"):
        try:
            return int(style_name.replace("heading", "").strip())
        except ValueError:
            return 0
    return 0


# ---------------------------------------------------------------------------
# Block extraction helpers
# ---------------------------------------------------------------------------

def _extract_time_range(text: str):
    m = TIME_RE.search(text)
    return m.group(0) if m else None


def _extract_duration(text: str):
    m = DURATION_RE.search(text)
    return int(m.group(1)) if m else None


def _classify_format(text: str) -> str:
    text_lower = text.lower()
    for keyword, label in [
        ("group", "Group Work"),
        ("pair", "Pair Work"),
        ("individual", "Independent"),
        ("lecture", "Direct Instruction"),
        ("demo", "Demonstration"),
        ("discuss", "Discussion"),
        ("hands-on", "Hands-On"),
        ("practice", "Guided Practice"),
    ]:
        if keyword in text_lower:
            return label
    return "Whole Class"


def _is_pacing_subblock(activity_name: str) -> bool:
    """Check if this block is a pacing sub-block that should merge with parent."""
    lower = activity_name.lower().strip()
    return lower.startswith("pacing:") or lower.startswith("pacing ")


def _merge_pacing_blocks(blocks: list[dict]) -> list[dict]:
    """Merge pacing sub-blocks into their parent activity blocks."""
    merged = []
    for block in blocks:
        name = block.get("activity_name", "")
        if _is_pacing_subblock(name) and merged:
            parent = merged[-1]
            # Extract pacing info from the sub-block name
            pacing_text = name
            if not parent.get("pacing"):
                parent["pacing"] = pacing_text
            else:
                parent["pacing"] += " " + pacing_text
            # Merge any delivery instructions or notes
            if block.get("delivery_instructions"):
                parent["delivery_instructions"] = (
                    parent.get("delivery_instructions", "") + " " +
                    block["delivery_instructions"]
                ).strip()
            if block.get("instructor_notes"):
                parent["instructor_notes"] = (
                    parent.get("instructor_notes", "") + " " +
                    block["instructor_notes"]
                ).strip()
        else:
            merged.append(block)
    return merged


def _sort_blocks_chronologically(blocks: list[dict]) -> list[dict]:
    """Sort schedule blocks by time, handling AM schedule (10-12) before PM (1-5)."""
    def _time_sort_key(b):
        t = b.get("time", "")
        m = re.match(r"(\d{1,2}):(\d{2})", t)
        if not m:
            return 9999
        hour = int(m.group(1))
        minute = int(m.group(2))
        # Assume hours 1-9 are PM (13:00-21:00), 10-12 are AM
        if hour < 10:
            hour += 12
        return hour * 60 + minute
    blocks.sort(key=_time_sort_key)
    return blocks


def _merge_orphan_delivery_blocks(blocks: list[dict]) -> list[dict]:
    """Merge orphan blocks whose names start with 'Delivery:' or 'Format:' into the previous block."""
    merged = []
    for block in blocks:
        name = block.get("activity_name", "").strip()
        lower_name = name.lower()
        is_orphan = (
            (lower_name.startswith("delivery:") or lower_name.startswith("format:"))
            and merged
            and not block.get("time")
        )
        if is_orphan:
            parent = merged[-1]
            # The "name" is actually delivery instructions
            content = name
            if block.get("delivery_instructions"):
                content += " " + block["delivery_instructions"]
            parent["delivery_instructions"] = (
                parent.get("delivery_instructions", "") + " " + content
            ).strip()
            if block.get("pacing") and not parent.get("pacing"):
                parent["pacing"] = block["pacing"]
            if block.get("instructor_notes"):
                parent["instructor_notes"] = (
                    parent.get("instructor_notes", "") + " " + block["instructor_notes"]
                ).strip()
        else:
            merged.append(block)
    return merged


def _recover_schedule_from_evidence(session: dict):
    """Move schedule blocks hiding in evidence_statements back to schedule_blocks."""
    remaining_evidence = []
    recovered_blocks = []
    i = 0
    evidence = session["evidence_statements"]

    while i < len(evidence):
        line = evidence[i]
        m = EVIDENCE_SCHEDULE_RE.match(line)
        if m:
            time_range = f"{m.group(1)}–{m.group(2)}"
            activity_name = m.group(3).strip().rstrip("✆ ")
            duration = int(m.group(4))

            block = {
                "time": time_range,
                "activity_name": activity_name,
                "duration": duration,
                "format": _classify_format(activity_name),
                "delivery_instructions": "",
                "pacing": "",
                "instructor_notes": "",
            }

            # Collect subsequent non-schedule lines as delivery/pacing/notes
            i += 1
            while i < len(evidence):
                next_line = evidence[i]
                # Stop if we hit another schedule block
                if EVIDENCE_SCHEDULE_RE.match(next_line):
                    break
                lower = next_line.lower().strip()
                if lower.startswith("pacing:"):
                    block["pacing"] = next_line.strip()
                elif lower.startswith("instructor note"):
                    block["instructor_notes"] += next_line.strip() + " "
                elif lower.startswith("format:") or lower.startswith("bloom"):
                    block["delivery_instructions"] += next_line.strip() + " "
                elif lower.startswith("delivery:"):
                    block["delivery_instructions"] += next_line.strip() + " "
                elif _extract_time_range(next_line) or EVIDENCE_SCHEDULE_RE.match(next_line):
                    break
                else:
                    block["delivery_instructions"] += next_line.strip() + " "
                i += 1

            block["delivery_instructions"] = block["delivery_instructions"].strip()
            block["instructor_notes"] = block["instructor_notes"].strip()
            recovered_blocks.append(block)
        else:
            # Check if it's a non-schedule delivery/pacing line that belongs to the
            # last recovered block
            lower = line.lower().strip()
            if recovered_blocks and (
                lower.startswith("delivery:") or
                lower.startswith("format:") or
                lower.startswith("bloom") or
                lower.startswith("pacing:")
            ):
                last = recovered_blocks[-1]
                if lower.startswith("pacing:"):
                    last["pacing"] = line.strip()
                else:
                    last["delivery_instructions"] = (
                        last["delivery_instructions"] + " " + line.strip()
                    ).strip()
                i += 1
            else:
                remaining_evidence.append(line)
                i += 1

    if recovered_blocks:
        # Insert recovered blocks into schedule in chronological order
        all_blocks = session["schedule_blocks"] + recovered_blocks
        session["schedule_blocks"] = _sort_blocks_chronologically(all_blocks)

    session["evidence_statements"] = remaining_evidence


def _clean_swbats(session: dict):
    """Remove non-SWBAT noise lines from the SWBATs list."""
    cleaned = []
    for swbat in session["swbats"]:
        swbat = swbat.strip()
        if not swbat:
            continue
        if SWBAT_NOISE_RE.match(swbat):
            continue
        # Also skip lines that are just metadata (timing adjustments, etc.)
        if "timing adjustment" in swbat.lower() or "contact hours" in swbat.lower():
            continue
        cleaned.append(swbat)
    session["swbats"] = cleaned


# ---------------------------------------------------------------------------
# Main parser
# ---------------------------------------------------------------------------

def parse_docx(path: Path) -> list[dict]:
    """Parse a curriculum .docx and return a list of session dicts."""
    doc = Document(str(path))
    sessions: list[dict] = []
    current_session: dict | None = None
    current_section: str | None = None
    buffer: list[str] = []

    def _flush_section():
        """Flush accumulated buffer lines into the current session."""
        nonlocal buffer, current_section
        if not current_session or not current_section:
            buffer = []
            return
        text_block = "\n".join(buffer).strip()
        if not text_block:
            buffer = []
            return

        if current_section == "swbats":
            for line in buffer:
                line = line.strip().lstrip("•-–—*0123456789.) ")
                line = SWBAT_RE.sub("", line).strip()
                if line:
                    current_session["swbats"].append(line)

        elif current_section == "schedule":
            _parse_schedule_lines(buffer, current_session)

        elif current_section == "evidence":
            for line in buffer:
                line = line.strip().lstrip("•-–—* ")
                if line:
                    current_session["evidence_statements"].append(line)

        buffer = []

    def _parse_schedule_lines(lines: list[str], session: dict):
        block: dict | None = None
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            time_range = _extract_time_range(stripped)
            duration = _extract_duration(stripped)
            if time_range or (duration and len(stripped) < 200):
                if block:
                    session["schedule_blocks"].append(block)
                activity_name = stripped
                activity_name = TIME_RE.sub("", activity_name)
                activity_name = DURATION_RE.sub("", activity_name)
                activity_name = activity_name.strip(" \t-–—:•|")
                block = {
                    "time": time_range or "",
                    "activity_name": activity_name or "Activity",
                    "duration": duration,
                    "format": _classify_format(stripped),
                    "delivery_instructions": "",
                    "pacing": "",
                    "instructor_notes": "",
                }
            elif block:
                lower = stripped.lower()
                if lower.startswith("pacing"):
                    block["pacing"] = stripped
                elif lower.startswith("note") or lower.startswith("instructor"):
                    block["instructor_notes"] += stripped + " "
                else:
                    block["delivery_instructions"] += stripped + " "
        if block:
            session["schedule_blocks"].append(block)

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        hlevel = _heading_level(para)

        # Detect session heading
        m = SESSION_RE.search(text)
        if m and hlevel > 0:
            _flush_section()
            if current_session:
                sessions.append(current_session)
            current_session = {
                "session_number": int(m.group(1)),
                "title": m.group(2).strip(),
                "subtitle": "",
                "swbats": [],
                "schedule_blocks": [],
                "evidence_statements": [],
            }
            current_section = None
            continue

        # Detect section headers within a session
        lower = text.lower()
        if any(k in lower for k in ["swbat", "learning target", "learning objective", "objective"]):
            _flush_section()
            current_section = "swbats"
            remainder = SWBAT_RE.sub("", text).strip()
            if remainder:
                buffer.append(remainder)
            continue
        if any(k in lower for k in ["schedule", "agenda", "lesson flow", "activity", "timeline"]):
            _flush_section()
            current_section = "schedule"
            continue
        if any(k in lower for k in ["evidence", "assessment", "success criteria"]):
            _flush_section()
            current_section = "evidence"
            remainder = text
            for prefix in ["evidence:", "assessment:", "success criteria:"]:
                if lower.startswith(prefix):
                    remainder = text[len(prefix):].strip()
            if remainder:
                buffer.append(remainder)
            continue

        # Subtitle detection (heading right after session heading)
        if hlevel > 0 and current_session and not current_section:
            current_session["subtitle"] = text
            continue

        buffer.append(text)

    _flush_section()
    if current_session:
        sessions.append(current_session)

    # Post-processing: recover lost blocks, merge pacing/orphans, sort, clean SWBATs
    for session in sessions:
        _recover_schedule_from_evidence(session)
        session["schedule_blocks"] = _merge_pacing_blocks(session["schedule_blocks"])
        session["schedule_blocks"] = _merge_orphan_delivery_blocks(session["schedule_blocks"])
        session["schedule_blocks"] = _sort_blocks_chronologically(session["schedule_blocks"])
        _clean_swbats(session)

    return sessions


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    docx_path = find_input_docx()
    sessions = parse_docx(docx_path)

    out_path = OUTPUT_DIR / "parsed_curriculum.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(sessions, f, indent=2, ensure_ascii=False)

    print(f"\nParsed {len(sessions)} session(s).")
    for s in sessions:
        print(f"  Session {s['session_number']}: {s['title']}")
        print(f"    SWBATs: {len(s['swbats'])}")
        print(f"    Schedule blocks: {len(s['schedule_blocks'])}")
        print(f"    Evidence statements: {len(s['evidence_statements'])}")
    print(f"\nOutput written to {out_path}")


if __name__ == "__main__":
    main()
