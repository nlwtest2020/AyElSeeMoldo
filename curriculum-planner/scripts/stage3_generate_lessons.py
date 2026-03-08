"""
Stage 3: GENERATE LESSON PLANS — Produce detailed markdown lesson plans.

Reads parsed_curriculum.json (and optionally research_notes.md) and produces
one markdown file per session in output/lessons/.

Each lesson follows the required structure with:
- Bloom's taxonomy tagging
- Gradual Release of Responsibility (GRR) phases
- Minute-by-minute pacing
- Teacher Does / Students Do columns
- CFU every 10-15 min
- Differentiation notes
- Exit tickets tied to SWBATs

Usage:
    python stage3_generate_lessons.py
"""

import json
import sys
from pathlib import Path


OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"

# Bloom's level keywords (used to auto-tag SWBATs)
BLOOMS_KEYWORDS = {
    "Remember": [
        "list", "define", "identify", "name", "recall", "recognize",
        "state", "label", "describe",
    ],
    "Understand": [
        "explain", "summarize", "paraphrase", "classify", "compare",
        "interpret", "discuss", "distinguish", "predict",
    ],
    "Apply": [
        "use", "apply", "demonstrate", "implement", "solve", "execute",
        "operate", "practice", "illustrate",
    ],
    "Analyze": [
        "analyze", "differentiate", "examine", "contrast", "organize",
        "deconstruct", "investigate", "categorize",
    ],
    "Evaluate": [
        "evaluate", "judge", "justify", "critique", "assess", "argue",
        "defend", "prioritize", "rate",
    ],
    "Create": [
        "create", "design", "develop", "construct", "produce", "compose",
        "formulate", "generate", "plan", "build",
    ],
}

GRR_PHASES = ["I Do", "We Do", "You Do Together", "You Do Alone"]

CFU_TECHNIQUES = [
    "Cold Call", "Thumbs Up/Down", "Turn-and-Talk",
    "Whiteboard Flash", "Exit Slip", "Think-Pair-Share",
    "Fist-to-Five", "Quick Write",
]


def load_parsed_curriculum() -> list[dict]:
    path = OUTPUT_DIR / "parsed_curriculum.json"
    if not path.exists():
        print(f"ERROR: {path} not found. Run stage1_parse.py first.")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def detect_blooms_level(swbat: str) -> str:
    """Detect Bloom's level from the verb in a SWBAT statement."""
    words = swbat.lower().split()
    # Check first 3 words for a Bloom's verb
    for word in words[:3]:
        word_clean = word.strip(".,;:()")
        for level, verbs in BLOOMS_KEYWORDS.items():
            if word_clean in verbs:
                return level
    return "Apply"  # Default


def assign_grr_phases(blocks: list[dict]) -> list[dict]:
    """Assign GRR phases across schedule blocks following the release model."""
    n = len(blocks)
    if n == 0:
        return blocks

    # Distribute phases: roughly I Do first 15%, We Do next 30%,
    # You Do Together next 30%, You Do Alone last 25%
    phase_boundaries = [
        int(n * 0.15) or 1,
        int(n * 0.45) or 2,
        int(n * 0.75) or 3,
    ]

    for i, block in enumerate(blocks):
        if i < phase_boundaries[0]:
            block["grr_phase"] = "I Do"
        elif i < phase_boundaries[1]:
            block["grr_phase"] = "We Do"
        elif i < phase_boundaries[2]:
            block["grr_phase"] = "You Do Together"
        else:
            block["grr_phase"] = "You Do Alone"

    return blocks


def generate_lesson_md(session: dict, session_index: int) -> str:
    """Generate a full lesson plan markdown for one session."""
    num = session["session_number"]
    title = session["title"]
    subtitle = session.get("subtitle", "")
    swbats = session.get("swbats", [])
    blocks = session.get("schedule_blocks", [])
    evidence = session.get("evidence_statements", [])

    blocks = assign_grr_phases(blocks)

    # Calculate total duration
    total_duration = sum(b.get("duration", 0) for b in blocks if b.get("duration"))

    lines = []

    # Header
    lines.append(f"# SESSION {num}: {title.upper()}")
    lines.append("━" * 60)
    lines.append("")
    if subtitle:
        lines.append(f"**Theme:** {subtitle}")
    lines.append(f"**Duration:** {total_duration} minutes" if total_duration else "**Duration:** TBD")
    lines.append(f"**Materials:** Laptops, projector, student handouts")
    lines.append("")

    # Learning Targets
    lines.append("## LEARNING TARGETS")
    lines.append("")
    if swbats:
        for i, swbat in enumerate(swbats, 1):
            level = detect_blooms_level(swbat)
            lines.append(f"{i}. {swbat} _(Bloom's: {level})_")
    else:
        lines.append("1. _[Define observable, measurable SWBATs with Bloom's verbs]_")
    lines.append("")

    # Assessment at a Glance
    lines.append("## ASSESSMENT AT A GLANCE")
    lines.append("")
    if evidence:
        lines.append(f"**Look for:** {evidence[0]}")
    else:
        lines.append("**Look for:** _[Observable evidence that students met targets]_")
    lines.append("**Formative:** CFU checks embedded in lesson flow (see blocks below)")
    lines.append("**Exit Ticket:** See closing section")
    lines.append("")

    # Lesson Flow
    lines.append("## LESSON FLOW")
    lines.append("")

    cfu_counter = 0
    running_minutes = 0

    if not blocks:
        blocks = [
            {
                "time": "",
                "activity_name": "Opening",
                "duration": 10,
                "format": "Whole Class",
                "grr_phase": "I Do",
                "delivery_instructions": "",
                "pacing": "",
                "instructor_notes": "",
            },
            {
                "time": "",
                "activity_name": "Direct Instruction",
                "duration": 15,
                "format": "Direct Instruction",
                "grr_phase": "I Do",
                "delivery_instructions": "",
                "pacing": "",
                "instructor_notes": "",
            },
            {
                "time": "",
                "activity_name": "Guided Practice",
                "duration": 20,
                "format": "Guided Practice",
                "grr_phase": "We Do",
                "delivery_instructions": "",
                "pacing": "",
                "instructor_notes": "",
            },
            {
                "time": "",
                "activity_name": "Collaborative Practice",
                "duration": 20,
                "format": "Group Work",
                "grr_phase": "You Do Together",
                "delivery_instructions": "",
                "pacing": "",
                "instructor_notes": "",
            },
            {
                "time": "",
                "activity_name": "Independent Practice",
                "duration": 15,
                "format": "Independent",
                "grr_phase": "You Do Alone",
                "delivery_instructions": "",
                "pacing": "",
                "instructor_notes": "",
            },
            {
                "time": "",
                "activity_name": "Closing",
                "duration": 10,
                "format": "Whole Class",
                "grr_phase": "You Do Alone",
                "delivery_instructions": "",
                "pacing": "",
                "instructor_notes": "",
            },
        ]
        blocks = assign_grr_phases(blocks)

    for block in blocks:
        name = block.get("activity_name", "Activity")
        duration = block.get("duration", 15)
        time_range = block.get("time", "")
        fmt = block.get("format", "Whole Class")
        grr = block.get("grr_phase", "We Do")
        delivery = block.get("delivery_instructions", "").strip()
        pacing = block.get("pacing", "").strip()
        notes = block.get("instructor_notes", "").strip()
        blooms = _activity_blooms(grr)

        # Time display
        if time_range:
            time_display = time_range
        else:
            end_min = running_minutes + (duration or 15)
            time_display = f"Min {running_minutes}–{end_min}"
            running_minutes = end_min

        # Block header
        lines.append("┌" + "─" * 58 + "┐")
        lines.append(f"│ **{time_display}  {name}  ({duration} min)**")
        lines.append(f"│ {fmt} | Bloom's: {blooms} | GRR: {grr}")
        lines.append("├" + "─" * 58 + "┤")

        # Teacher Does
        lines.append("│")
        lines.append("│ **TEACHER DOES**")
        if delivery:
            for step in _split_instructions(delivery):
                lines.append(f"│ • {step}")
        else:
            lines.append(f"│ • _[Write exact teacher actions, scripted language,_")
            lines.append(f"│ _  questions in quotes, and what to demonstrate]_")
        if notes:
            lines.append(f"│ • **Note:** {notes}")
        lines.append("│")

        # Students Do
        lines.append("│ **STUDENTS DO**")
        lines.append(f"│ • _[Write what students type, produce, discuss, or build]_")
        lines.append(f"│ • _[Include timed sub-steps if activity > 10 min]_")
        lines.append("│")

        # Pacing
        lines.append(f"│ **PACING:** {pacing if pacing else _generate_pacing(name, duration)}")
        lines.append("│")

        # Teacher Tip
        lines.append(f"│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_")
        lines.append("│")

        # CFU
        cfu_counter += 1
        technique = CFU_TECHNIQUES[cfu_counter % len(CFU_TECHNIQUES)]
        lines.append(f"│ **CHECK ({technique}):** _[CFU question tied to SWBAT]_")
        lines.append(f"│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_")
        lines.append(f"│ _use simpler example, pair struggling with proficient]_")
        lines.append("└" + "─" * 58 + "┘")
        lines.append("")

    # Differentiation
    lines.append("## DIFFERENTIATION NOTES")
    lines.append("")
    lines.append("| Level | Strategy |")
    lines.append("|-------|----------|")
    lines.append("| **Struggling** | _[Scaffolds: sentence starters, step-by-step checklist, worked example]_ |")
    lines.append("| **Advanced** | _[Extensions: open-ended challenge, teach a peer, real-world application]_ |")
    lines.append("| **Language Support** | _[Visuals, vocabulary wall, bilingual glossary, simplified instructions]_ |")
    lines.append("")

    # Closing & Exit Ticket
    lines.append("## CLOSING & EXIT TICKET")
    lines.append("")
    if swbats:
        for i, swbat in enumerate(swbats, 1):
            lines.append(f"{i}. _[Question tied to SWBAT {i}: \"{swbat}\"]_")
    else:
        lines.append("1. _[Question tied to SWBAT 1]_")
        lines.append("2. _[Question tied to SWBAT 2]_")
    lines.append("")

    # Post-Session Reflection
    lines.append("## POST-SESSION REFLECTION")
    lines.append("")
    lines.append("- [ ] What worked well?")
    lines.append("- [ ] What needs adjustment for next time?")
    lines.append("- [ ] Which students need follow-up or reteaching?")
    lines.append("- [ ] Were all SWBATs met? Evidence?")
    lines.append("")

    return "\n".join(lines)


def _activity_blooms(grr_phase: str) -> str:
    """Map GRR phase to typical Bloom's level."""
    mapping = {
        "I Do": "Remember / Understand",
        "We Do": "Understand / Apply",
        "You Do Together": "Apply / Analyze",
        "You Do Alone": "Analyze / Create",
    }
    return mapping.get(grr_phase, "Apply")


def _split_instructions(text: str) -> list[str]:
    """Split delivery instructions into individual steps."""
    # Try splitting on sentence boundaries or numbered items
    import re
    parts = re.split(r'(?<=[.!?])\s+|\n|(?=\d+[.)]\s)', text)
    return [p.strip() for p in parts if p.strip()]


def _generate_pacing(activity_name: str, duration: int) -> str:
    """Generate a simple pacing breakdown."""
    if not duration:
        return "_[Minute-by-minute breakdown]_"
    if duration <= 5:
        return f"0:00–{duration}:00 — {activity_name}"
    mid = duration // 2
    return f"0:00–{mid}:00 — First half | {mid}:00–{duration}:00 — Second half"


def main():
    sessions = load_parsed_curriculum()
    LESSONS_DIR.mkdir(parents=True, exist_ok=True)

    for i, session in enumerate(sessions):
        md = generate_lesson_md(session, i)
        num = session["session_number"]
        filename = f"session_{num:02d}_lesson_plan.md"
        out_path = LESSONS_DIR / filename
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Generated: {filename}")

    print(f"\n{len(sessions)} lesson plan(s) written to {LESSONS_DIR}")
    print("\nNext steps:")
    print("  1. Review each lesson plan and fill in specific teacher/student actions")
    print("  2. Add worked examples with exact prompts and expected outputs")
    print("  3. Write CFU questions tied to each SWBAT")
    print("  4. Add culturally relevant examples for your audience")
    print("  5. Optionally run stage4_generate_slides.py")


if __name__ == "__main__":
    main()
