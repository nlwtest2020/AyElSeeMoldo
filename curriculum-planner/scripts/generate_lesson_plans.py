#!/usr/bin/env python3
"""
Generate branded DOCX lesson plans for each session using the ALC template.

Usage:
    python scripts/generate_lesson_plans.py

Reads:  output/parsed_curriculum.json
        templates/ALC_Lesson_Plan_Template.docx
Output: output/Session_1_Lesson_Plan.docx (etc.)
"""

import json
import sys
from copy import deepcopy
from pathlib import Path

from docx import Document
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn


SCRIPT_DIR = Path(__file__).parent.parent
OUTPUT_DIR = SCRIPT_DIR / "output"
TEMPLATE_PATH = SCRIPT_DIR / "templates" / "ALC_Lesson_Plan_Template.docx"
PARSED_PATH = OUTPUT_DIR / "parsed_curriculum.json"


def clone_template_styles(template_doc):
    """Extract formatting info from the template for reuse."""
    styles = {}
    # Get heading style from first heading
    for para in template_doc.paragraphs:
        if para.style.name == "Heading 1":
            styles["heading1"] = {
                "font_name": para.runs[0].font.name if para.runs else None,
                "font_size": para.runs[0].font.size if para.runs else None,
                "bold": para.runs[0].font.bold if para.runs else True,
                "color": para.runs[0].font.color.rgb if para.runs and para.runs[0].font.color.type else None,
            }
            break
    return styles


def copy_table_style(src_table, dst_table):
    """Copy table styling from source to destination."""
    # Copy table-level properties
    tbl = dst_table._tbl
    src_tbl = src_table._tbl

    # Copy table properties (borders, shading, etc.)
    src_tblPr = src_tbl.find(qn('w:tblPr'))
    dst_tblPr = tbl.find(qn('w:tblPr'))
    if src_tblPr is not None and dst_tblPr is not None:
        for child in list(dst_tblPr):
            dst_tblPr.remove(child)
        for child in src_tblPr:
            dst_tblPr.append(deepcopy(child))


def apply_cell_format(cell, text, bold=False, font_size=None, font_name=None, color=None):
    """Apply formatting to a table cell."""
    cell.text = ""
    p = cell.paragraphs[0]
    run = p.add_run(text)
    if bold:
        run.font.bold = True
    if font_size:
        run.font.size = font_size
    if font_name:
        run.font.name = font_name
    if color:
        run.font.color.rgb = color


def generate_lesson_plan(session, template_doc):
    """Generate a single lesson plan DOCX from session data and template."""
    doc = Document()

    # Copy default styles from template if available
    try:
        style = doc.styles["Normal"]
        template_style = template_doc.styles["Normal"]
        if template_style.font.name:
            style.font.name = template_style.font.name
        if template_style.font.size:
            style.font.size = template_style.font.size
    except KeyError:
        pass

    num = session["session_num"]
    title = session["title"]
    subtitle = session["subtitle"]

    # --- HEADING ---
    heading = doc.add_heading(f"Session {num}: {title}", level=1)

    # Subtitle
    if subtitle:
        p = doc.add_paragraph(subtitle)
        p.style = doc.styles["Normal"]
        for run in p.runs:
            run.font.size = Pt(11)
            run.font.italic = True

    doc.add_paragraph()  # spacer

    # --- METADATA TABLE ---
    # Extract metadata from subtitle
    day_info = ""
    time_info = ""
    theme_info = ""
    if subtitle:
        parts = subtitle.split("|")
        if len(parts) >= 1:
            day_info = parts[0].strip()
        if len(parts) >= 2:
            time_info = parts[1].strip()
        if len(parts) >= 3:
            theme_info = parts[2].strip().replace("Theme:", "").strip()

    # Count non-break blocks
    instruction_blocks = [b for b in session["schedule"] if not b.get("is_break")]
    total_instruction_min = sum(int(b["duration"].replace(" min", "")) for b in instruction_blocks)

    meta_rows = [
        ("Course", "AI & Digital Workflows Bootcamp"),
        ("Session", f"Session {num}: {title}"),
        ("Day / Time", f"{day_info}  |  {time_info}" if day_info else ""),
        ("Theme", theme_info),
        ("Duration", f"{total_instruction_min} minutes instruction ({len(instruction_blocks)} blocks)"),
        ("Materials", "Slides, laptop/tablet per student, Claude & ChatGPT access, printed templates"),
    ]

    meta_table = doc.add_table(rows=len(meta_rows), cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.LEFT
    for i, (label, value) in enumerate(meta_rows):
        apply_cell_format(meta_table.cell(i, 0), label, bold=True, font_size=Pt(10))
        apply_cell_format(meta_table.cell(i, 1), value, font_size=Pt(10))
    # Set column widths
    for row in meta_table.rows:
        row.cells[0].width = Cm(4)
        row.cells[1].width = Cm(12)

    doc.add_paragraph()

    # --- LEARNING OBJECTIVES ---
    doc.add_paragraph("LEARNING OBJECTIVES", style="Heading 2")
    p = doc.add_paragraph("By the end of this session, students will be able to:")
    for swbat in session["swbats"]:
        p = doc.add_paragraph()
        run = p.add_run(f"▸  {swbat}")
        run.font.size = Pt(10)

    doc.add_paragraph()

    # --- SESSION SCHEDULE ---
    # Split into morning and afternoon blocks
    schedule = session["schedule"]
    morning_blocks = []
    afternoon_blocks = []
    lunch_seen = False

    for block in schedule:
        if "lunch" in block["activity"].lower():
            lunch_seen = True
            morning_blocks.append(block)  # include lunch as divider
            continue
        if not lunch_seen:
            morning_blocks.append(block)
        else:
            afternoon_blocks.append(block)

    # Morning block
    if morning_blocks:
        first = morning_blocks[0]
        last_morning = [b for b in morning_blocks if not b.get("is_break")]
        doc.add_paragraph(
            f"MORNING BLOCK ({first['start_time']}–{morning_blocks[-1]['end_time']})",
            style="Heading 2"
        )
        add_schedule_table(doc, morning_blocks)

    doc.add_paragraph()

    # Afternoon block
    if afternoon_blocks:
        doc.add_paragraph(
            f"AFTERNOON BLOCK ({afternoon_blocks[0]['start_time']}–{afternoon_blocks[-1]['end_time']})",
            style="Heading 2"
        )
        add_schedule_table(doc, afternoon_blocks)

    doc.add_paragraph()

    # --- TEACHER NOTES ---
    doc.add_paragraph("TEACHER NOTES", style="Heading 2")

    # Collect instructor notes from blocks
    notes_written = False
    for block in schedule:
        if block.get("is_break"):
            continue
        if block.get("instructor_note"):
            p = doc.add_paragraph()
            run = p.add_run(f"{block['activity']}: ")
            run.font.bold = True
            run.font.size = Pt(10)
            run = p.add_run(block["instructor_note"])
            run.font.size = Pt(10)
            notes_written = True

    if not notes_written:
        doc.add_paragraph("See delivery notes in schedule table above.", style="Normal")

    doc.add_paragraph()

    # --- ASSESSMENT ---
    doc.add_paragraph("ASSESSMENT", style="Heading 2")

    if session.get("evidence"):
        p = doc.add_paragraph()
        run = p.add_run("Evidence to look for: ")
        run.font.bold = True
        run.font.size = Pt(10)
        run = p.add_run(session["evidence"])
        run.font.size = Pt(10)

    # Map SWBATs to assessment methods based on Bloom's levels in schedule
    p = doc.add_paragraph()
    run = p.add_run("Formative: ")
    run.font.bold = True
    run.font.size = Pt(10)
    run = p.add_run(
        "Teacher observation during activities. Monitor student outputs at each "
        "hands-on block. Use delivery notes and pacing guidance to check quality."
    )
    run.font.size = Pt(10)

    p = doc.add_paragraph()
    run = p.add_run("Self-Assessment: ")
    run.font.bold = True
    run.font.size = Pt(10)
    run = p.add_run(
        "Students complete confidence ratings (1–5) for each learning objective "
        "at the end of the session."
    )
    run.font.size = Pt(10)

    return doc


def add_schedule_table(doc, blocks):
    """Add a schedule table for a set of time blocks."""
    table = doc.add_table(rows=1 + len(blocks), cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT

    # Header row
    headers = ["Time", "Activity", "Details & Instructions"]
    for i, header in enumerate(headers):
        apply_cell_format(table.cell(0, i), header, bold=True, font_size=Pt(9))

    for i, block in enumerate(blocks):
        row_idx = i + 1
        time_str = f"{block['start_time']}–{block['end_time']}"
        activity = block["activity"]

        # Build details
        details_parts = []
        if block.get("format"):
            details_parts.append(f"Format: {block['format']}")
        if block.get("blooms"):
            details_parts.append(f"Bloom's: {block['blooms']}")
        if block.get("delivery"):
            # Truncate very long delivery notes for the table
            delivery = block["delivery"]
            if len(delivery) > 400:
                delivery = delivery[:397] + "..."
            details_parts.append(delivery)
        if block.get("pacing"):
            pacing = block["pacing"]
            if len(pacing) > 300:
                pacing = pacing[:297] + "..."
            details_parts.append(f"Pacing: {pacing}")

        details = "\n".join(details_parts)

        if block.get("is_break"):
            details = ""

        apply_cell_format(table.cell(row_idx, 0), time_str, font_size=Pt(9))
        apply_cell_format(table.cell(row_idx, 1), activity, bold=True, font_size=Pt(9))
        apply_cell_format(table.cell(row_idx, 2), details, font_size=Pt(8))

    # Set column widths
    for row in table.rows:
        row.cells[0].width = Cm(3)
        row.cells[1].width = Cm(4)
        row.cells[2].width = Cm(10)


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    if not PARSED_PATH.exists():
        print(f"Error: {PARSED_PATH} not found. Run parse_docx.py first.")
        sys.exit(1)

    if not TEMPLATE_PATH.exists():
        print(f"Error: Template not found: {TEMPLATE_PATH}")
        sys.exit(1)

    with open(PARSED_PATH) as f:
        curriculum = json.load(f)

    template_doc = Document(TEMPLATE_PATH)

    for session in curriculum["sessions"]:
        num = session["session_num"]
        doc = generate_lesson_plan(session, template_doc)

        filename = f"Session_{num}_Lesson_Plan.docx"
        output_path = OUTPUT_DIR / filename
        doc.save(str(output_path))
        print(f"Generated: {output_path}")

    print(f"\nAll {len(curriculum['sessions'])} lesson plans generated.")


if __name__ == "__main__":
    main()
