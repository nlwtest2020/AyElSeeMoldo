#!/usr/bin/env python3
"""
Stage 4: Generate a branded PowerPoint presentation from a lesson plan.

Usage:
    python scripts/generate_pptx.py output/lesson_plan.md templates/<template>.pptx

Output:
    output/day_slides.pptx

The generator reads the lesson plan markdown, extracts slide content,
and populates the branded template while preserving its formatting.
"""

import re
import sys
from pathlib import Path
from copy import deepcopy

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR


def parse_lesson_plan(md_path):
    """Parse the lesson plan markdown into structured slide content."""
    with open(md_path, "r") as f:
        content = f.read()

    slides = []

    # Extract title
    title_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Lesson"

    slides.append({
        "type": "title",
        "title": title,
        "subtitle": "",
    })

    # Extract SWBATs / Objectives
    swbats = []
    objectives_match = re.search(
        r'(?:##\s*(?:Standards|Objectives|SWBATs|Learning Objectives).*?\n)(.*?)(?=\n##\s|\Z)',
        content, re.DOTALL | re.IGNORECASE
    )
    if objectives_match:
        obj_text = objectives_match.group(1)
        for line in obj_text.strip().split("\n"):
            cleaned = line.strip().lstrip("•-*0123456789.) ")
            if cleaned and len(cleaned) > 5:
                swbats.append(cleaned)

    if swbats:
        slides.append({
            "type": "objectives",
            "title": "Learning Objectives",
            "items": swbats,
        })

    # Extract lesson sequence sections
    sequence_match = re.search(
        r'(?:##\s*(?:Lesson Sequence|Schedule|Agenda|Timeline).*?\n)(.*?)(?=\n##\s(?!#)|\Z)',
        content, re.DOTALL | re.IGNORECASE
    )

    if sequence_match:
        sequence_text = sequence_match.group(1)
        # Split into subsections by ### headers
        sections = re.split(r'\n###\s+', sequence_text)
        for section in sections:
            if not section.strip():
                continue

            lines = section.strip().split("\n")
            section_title = lines[0].strip().rstrip("#").strip()
            section_body = "\n".join(lines[1:]).strip()

            # Determine slide type from content
            slide_type = classify_section(section_title, section_body)

            if slide_type == "activity":
                # Extract activity steps
                steps = extract_bullet_items(section_body)
                time_match = re.search(r'(\d+)\s*min', section_body, re.IGNORECASE)
                time_limit = f"{time_match.group(1)} minutes" if time_match else ""
                slides.append({
                    "type": "activity",
                    "title": section_title,
                    "items": steps if steps else [section_body],
                    "time_limit": time_limit,
                })
            elif slide_type == "discussion":
                prompts = extract_bullet_items(section_body)
                slides.append({
                    "type": "discussion",
                    "title": section_title,
                    "items": prompts if prompts else [section_body],
                })
            elif slide_type == "cfu":
                questions = extract_bullet_items(section_body)
                slides.append({
                    "type": "cfu",
                    "title": "Check for Understanding",
                    "items": questions if questions else [section_body],
                })
            else:
                # Content slide - break long content into multiple slides
                items = extract_bullet_items(section_body)
                if not items:
                    items = [p.strip() for p in section_body.split("\n\n") if p.strip()]

                # Chunk into groups of 4-6 items per slide
                for i in range(0, max(len(items), 1), 5):
                    chunk = items[i:i + 5]
                    slides.append({
                        "type": "content",
                        "title": section_title,
                        "items": chunk if chunk else [section_body[:200]],
                    })
    else:
        # Fallback: split by ## headers
        sections = re.split(r'\n##\s+', content)
        for section in sections[1:]:  # Skip content before first ##
            lines = section.strip().split("\n")
            section_title = lines[0].strip()
            section_body = "\n".join(lines[1:]).strip()

            if any(skip in section_title.lower() for skip in ["materials", "preparation", "reflection", "assessment plan"]):
                continue

            items = extract_bullet_items(section_body)
            slide_type = classify_section(section_title, section_body)

            slides.append({
                "type": slide_type,
                "title": section_title,
                "items": items if items else [section_body[:300]],
            })

    # Add summary slide
    slides.append({
        "type": "summary",
        "title": "Key Takeaways",
        "items": swbats[:6] if swbats else ["Review today's learning objectives"],
    })

    return slides


def classify_section(title, body):
    """Classify a section into a slide type based on keywords."""
    text = (title + " " + body).lower()

    if any(w in text for w in ["activity", "practice", "exercise", "task", "you do", "group work", "pair work", "hands-on"]):
        return "activity"
    if any(w in text for w in ["discussion", "discuss", "turn and talk", "think-pair-share", "debrief"]):
        return "discussion"
    if any(w in text for w in ["check for understanding", "cfu", "exit ticket", "assessment", "quiz", "poll"]):
        return "cfu"
    if any(w in text for w in ["transition", "break", "movement"]):
        return "transition"
    return "content"


def extract_bullet_items(text):
    """Extract bulleted or numbered list items from text."""
    items = []
    for line in text.split("\n"):
        cleaned = line.strip()
        if not cleaned:
            continue
        # Match bullet or numbered items
        match = re.match(r'^(?:[-*+]|\d+[.)]\s)', cleaned)
        if match:
            item = cleaned[match.end():].strip()
            if item:
                items.append(item)
        elif cleaned.startswith("**") and cleaned.endswith("**"):
            items.append(cleaned.strip("* "))
    return items


def get_template_layouts(prs):
    """Analyze the template to find available slide layouts."""
    layouts = {}
    for i, layout in enumerate(prs.slide_layouts):
        name = layout.name.lower()
        layouts[i] = {
            "name": layout.name,
            "placeholders": [(ph.placeholder_format.idx, ph.name, ph.width, ph.height)
                             for ph in layout.placeholders],
        }
    return layouts


def find_best_layout(prs, slide_type):
    """Find the best matching slide layout for a given slide type."""
    layouts = prs.slide_layouts

    # Map slide types to preferred layout keywords
    preferences = {
        "title": ["title slide", "title", "cover"],
        "objectives": ["title and content", "content", "body", "text"],
        "content": ["title and content", "content", "body", "text", "two content"],
        "activity": ["title and content", "content", "body", "text"],
        "discussion": ["section header", "title only", "title and content"],
        "cfu": ["title and content", "content", "body", "text"],
        "transition": ["section header", "title only", "blank"],
        "summary": ["title and content", "content", "body", "text"],
    }

    preferred = preferences.get(slide_type, ["title and content", "content"])

    # Try to find a matching layout
    for keyword in preferred:
        for layout in layouts:
            if keyword in layout.name.lower():
                return layout

    # Fallback: use layout 0 for title, layout 1 for everything else
    if slide_type == "title" and len(layouts) > 0:
        return layouts[0]
    if len(layouts) > 1:
        return layouts[1]
    return layouts[0]


def add_slide(prs, slide_data):
    """Add a slide to the presentation based on slide data and template layout."""
    layout = find_best_layout(prs, slide_data["type"])
    slide = prs.slides.add_slide(layout)

    # Find title and body placeholders
    title_ph = None
    body_ph = None
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:  # Title
            title_ph = ph
        elif ph.placeholder_format.idx == 1:  # Body/Subtitle
            body_ph = ph
        elif ph.placeholder_format.idx >= 2 and body_ph is None:
            body_ph = ph

    # Set title
    if title_ph is not None:
        title_ph.text = slide_data.get("title", "")
        # Preserve template font but ensure readable size
        for para in title_ph.text_frame.paragraphs:
            for run in para.runs:
                if run.font.size and run.font.size < Pt(18):
                    run.font.size = Pt(24)

    # Set body content
    items = slide_data.get("items", [])
    if body_ph is not None and items:
        tf = body_ph.text_frame
        tf.clear()

        # Add time limit for activity slides
        if slide_data["type"] == "activity" and slide_data.get("time_limit"):
            p = tf.paragraphs[0] if tf.paragraphs else tf.add_paragraph()
            p.text = f"Time: {slide_data['time_limit']}"
            p.font.bold = True
            p.font.size = Pt(16)
            p.space_after = Pt(8)

        for i, item in enumerate(items):
            if i == 0 and not (slide_data["type"] == "activity" and slide_data.get("time_limit")):
                p = tf.paragraphs[0] if tf.paragraphs else tf.add_paragraph()
            else:
                p = tf.add_paragraph()
            p.text = item
            p.level = 0

            # Style based on slide type
            if slide_data["type"] == "discussion":
                p.font.size = Pt(20)
                p.alignment = PP_ALIGN.LEFT
            elif slide_data["type"] == "cfu":
                p.font.size = Pt(18)
                if i == 0:
                    p.font.bold = True
            else:
                p.font.size = Pt(16)

            p.space_after = Pt(6)

    elif not body_ph and items:
        # No body placeholder - add a text box
        left = Inches(0.75)
        top = Inches(1.75)
        width = Inches(8.5)
        height = Inches(5.0)
        txBox = slide.shapes.add_textbox(left, top, width, height)
        tf = txBox.text_frame
        tf.word_wrap = True

        for i, item in enumerate(items):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = item
            p.font.size = Pt(16)
            p.space_after = Pt(6)

    return slide


def generate_pptx(slides, template_path, output_path):
    """Generate the PowerPoint file from slide data using the branded template."""
    prs = Presentation(template_path)

    # Remove any existing slides from the template (keep only layouts)
    # We need to work around python-pptx limitations for slide removal
    # by building a new presentation using the template's slide masters
    while len(prs.slides) > 0:
        rId = prs.slides._sldIdLst[0].rId
        prs.part.drop_rel(rId)
        del prs.slides._sldIdLst[0]

    # Add slides
    for slide_data in slides:
        add_slide(prs, slide_data)

    prs.save(output_path)
    return len(prs.slides)


def main():
    if len(sys.argv) < 3:
        print("Usage: python scripts/generate_pptx.py output/lesson_plan.md templates/<template>.pptx")
        sys.exit(1)

    lesson_plan_path = Path(sys.argv[1])
    template_path = Path(sys.argv[2])

    if not lesson_plan_path.exists():
        print(f"Error: Lesson plan not found: {lesson_plan_path}")
        sys.exit(1)

    if not template_path.exists():
        print(f"Error: Template not found: {template_path}")
        sys.exit(1)

    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "output"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "day_slides.pptx"

    print(f"Lesson plan: {lesson_plan_path}")
    print(f"Template: {template_path}")

    # Parse lesson plan into slide structure
    slides = parse_lesson_plan(lesson_plan_path)
    print(f"Slides planned: {len(slides)}")

    # Print slide outline
    for i, slide in enumerate(slides, 1):
        type_label = slide["type"].upper()
        title = slide.get("title", "")
        items_count = len(slide.get("items", []))
        print(f"  [{i:2d}] {type_label:12s} | {title}")
        if items_count:
            print(f"       {items_count} items")

    # Generate the presentation
    slide_count = generate_pptx(slides, template_path, output_path)
    print(f"\nGenerated: {output_path}")
    print(f"Total slides: {slide_count}")

    # Analyze template for reference
    print("\n--- Template Analysis ---")
    prs = Presentation(template_path)
    layouts = get_template_layouts(prs)
    for idx, info in layouts.items():
        ph_names = [f"{name} (idx={pidx})" for pidx, name, w, h in info["placeholders"]]
        print(f"  Layout {idx}: {info['name']}")
        if ph_names:
            print(f"    Placeholders: {', '.join(ph_names)}")


if __name__ == "__main__":
    main()
