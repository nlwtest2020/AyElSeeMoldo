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
