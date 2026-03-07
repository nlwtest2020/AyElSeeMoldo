#!/usr/bin/env python3
"""
Stage 1: Parse the AI & Digital Workflows Bootcamp roadmap into structured
session data for lesson plan and slide generation.

Usage:
    python scripts/parse_docx.py input/<filename>.docx

Output:
    output/parsed_curriculum.json
"""

import json
import re
import sys
from pathlib import Path

from docx import Document


def parse_roadmap(file_path):
    """Parse the bootcamp roadmap into 4 structured sessions."""
    doc = Document(file_path)
    full_text = "\n".join(p.text for p in doc.paragraphs)

    # Split into sessions
    session_splits = re.split(
        r'\n(Session \d: .+)\n',
        full_text
    )

    sessions = []
    # session_splits: [preamble, "Session 1: ...", content1, "Session 2: ...", content2, ...]
    for i in range(1, len(session_splits), 2):
        header = session_splits[i].strip()
        content = session_splits[i + 1] if i + 1 < len(session_splits) else ""

        session_num = int(re.search(r'Session (\d)', header).group(1))
        title_match = re.search(r'"([^"]+)"', header)
        title = title_match.group(1) if title_match else header.split(":", 1)[-1].strip()

        # Extract subtitle (day/date/theme line)
        subtitle_match = re.search(r'((?:Saturday|Sunday).+?Theme:.+?)(?:\n|$)', content)
        subtitle = subtitle_match.group(1).strip() if subtitle_match else ""

        # Extract schedule blocks
        schedule = extract_schedule(content)

        # Extract SWBATs
        swbats = extract_swbats(content)

        # Extract evidence
        evidence_match = re.search(
            r'Evidence the instructor looks for:\s*(.+?)(?:\n\n|\Z)',
            content, re.DOTALL
        )
        evidence = evidence_match.group(1).strip() if evidence_match else ""

        sessions.append({
            "session_num": session_num,
            "title": title,
            "header": header,
            "subtitle": subtitle,
            "schedule": schedule,
            "swbats": swbats,
            "evidence": evidence,
        })

    # Extract global pacing principles from preamble
    preamble = session_splits[0] if session_splits else full_text

    # Extract LO progression table from tables
    tables = []
    for table in doc.tables:
        rows = []
        for row in table.rows:
            cells = [cell.text.strip() for cell in row.cells]
            rows.append(cells)
        tables.append(rows)

    return {
        "bootcamp_title": "AI & Digital Workflows Bootcamp",
        "total_sessions": 4,
        "total_hours": 28,
        "sessions": sessions,
        "tables": tables,
    }


def extract_schedule(content):
    """Extract time blocks from session content."""
    blocks = []
    # Match patterns like: 10:00–10:15  |  Welcome + Norms  |  15 min
    pattern = r'(\d{1,2}:\d{2})\s*[–-]\s*(\d{1,2}:\d{2})\s*\|\s*(.+?)\s*\|\s*(\d+\s*min)'
    matches = re.finditer(pattern, content)

    for match in matches:
        start_time = match.group(1)
        end_time = match.group(2)
        activity_name = match.group(3).strip()
        duration = match.group(4).strip()

        # Get the content after this match until the next time block or section
        pos = match.end()
        next_match = re.search(pattern, content[pos:])
        if next_match:
            block_content = content[pos:pos + next_match.start()].strip()
        else:
            # Until next major section or end
            remaining = content[pos:]
            end_marker = re.search(r'\nSession \d SWBAT', remaining)
            block_content = remaining[:end_marker.start()].strip() if end_marker else remaining.strip()

        # Extract sub-fields from block content
        format_match = re.search(r'Format:\s*(.+?)(?:\n|$)', block_content)
        blooms_match = re.search(r"Bloom'?s:\s*(.+?)(?:\n|$)", block_content)
        delivery_match = re.search(r'Delivery:\s*(.+?)(?=\nPacing:|\nInstructor note:|\n\d{1,2}:\d{2}|\Z)', block_content, re.DOTALL)
        pacing_match = re.search(r'Pacing:\s*(.+?)(?=\nInstructor note:|\nDelivery:|\n\d{1,2}:\d{2}|\Z)', block_content, re.DOTALL)
        instructor_note_match = re.search(r'Instructor note:\s*(.+?)(?=\n\d{1,2}:\d{2}|\Z)', block_content, re.DOTALL)

        block = {
            "start_time": start_time,
            "end_time": end_time,
            "activity": activity_name,
            "duration": duration,
            "format": format_match.group(1).strip() if format_match else "",
            "blooms": blooms_match.group(1).strip() if blooms_match else "",
            "delivery": delivery_match.group(1).strip() if delivery_match else "",
            "pacing": pacing_match.group(1).strip() if pacing_match else "",
            "instructor_note": instructor_note_match.group(1).strip() if instructor_note_match else "",
        }

        # Detect breaks/lunch
        if any(w in activity_name.lower() for w in ["break", "lunch"]):
            block["is_break"] = True

        blocks.append(block)

    return blocks


def extract_swbats(content):
    """Extract SWBAT statements from session content."""
    swbats = []
    swbat_match = re.search(
        r'students should be able to:\s*\n(.+?)(?=\nEvidence|\Z)',
        content, re.DOTALL
    )
    if swbat_match:
        lines = swbat_match.group(1).strip().split("\n")
        for line in lines:
            line = line.strip()
            if line and len(line) > 10:
                # Clean up LO references
                swbats.append(line)
    return swbats


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/parse_docx.py input/<filename>.docx")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    if not input_file.exists():
        print(f"Error: File not found: {input_file}")
        sys.exit(1)

    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "output"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "parsed_curriculum.json"

    print(f"Parsing: {input_file}")
    curriculum = parse_roadmap(input_file)

    with open(output_file, "w") as f:
        json.dump(curriculum, f, indent=2)

    print(f"Output: {output_file}")
    for session in curriculum["sessions"]:
        n = session["session_num"]
        print(f"  Session {n}: \"{session['title']}\"")
        print(f"    Schedule blocks: {len(session['schedule'])}")
        print(f"    SWBATs: {len(session['swbats'])}")


if __name__ == "__main__":
    main()
