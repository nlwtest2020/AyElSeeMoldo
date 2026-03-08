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
import re
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
        "formulate", "generate", "plan", "build", "write",
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


def detect_blooms_level(text: str) -> str:
    """Detect Bloom's level from verbs in text."""
    words = text.lower().split()
    for word in words[:5]:
        word_clean = word.strip(".,;:()")
        for level, verbs in BLOOMS_KEYWORDS.items():
            if word_clean in verbs:
                return level
    return "Apply"


def _detect_blooms_from_delivery(delivery: str) -> str:
    """Extract explicit Bloom's level from delivery instructions."""
    m = re.search(r"bloom'?s?:?\s*(\w+)", delivery, re.IGNORECASE)
    if m:
        level = m.group(1).capitalize()
        if level in BLOOMS_KEYWORDS:
            return level
        # Handle combined levels like "Apply + Evaluate"
        m2 = re.search(r"bloom'?s?:?\s*(\w+)\s*\+\s*(\w+)", delivery, re.IGNORECASE)
        if m2:
            return f"{m2.group(1).capitalize()} + {m2.group(2).capitalize()}"
    return ""


def assign_grr_phases(blocks: list[dict]) -> list[dict]:
    """Assign GRR phases across schedule blocks following the release model."""
    # Filter out breaks and lunch for phase assignment
    teaching_blocks = [b for b in blocks if not _is_non_teaching(b)]
    n = len(teaching_blocks)
    if n == 0:
        return blocks

    phase_boundaries = [
        max(int(n * 0.20), 1),
        max(int(n * 0.50), 2),
        max(int(n * 0.75), 3),
    ]

    teaching_idx = 0
    for block in blocks:
        if _is_non_teaching(block):
            block["grr_phase"] = ""
            continue
        if teaching_idx < phase_boundaries[0]:
            block["grr_phase"] = "I Do"
        elif teaching_idx < phase_boundaries[1]:
            block["grr_phase"] = "We Do"
        elif teaching_idx < phase_boundaries[2]:
            block["grr_phase"] = "You Do Together"
        else:
            block["grr_phase"] = "You Do Alone"
        teaching_idx += 1

    return blocks


def _is_non_teaching(block: dict) -> bool:
    """Check if a block is a break, lunch, or buffer."""
    name = block.get("activity_name", "").lower()
    return any(k in name for k in ["break", "lunch", "buffer", "overflow"])


def _activity_blooms(grr_phase: str, delivery: str = "") -> str:
    """Determine Bloom's level from delivery instructions or GRR phase."""
    # First try to extract from delivery instructions
    explicit = _detect_blooms_from_delivery(delivery)
    if explicit:
        return explicit

    mapping = {
        "I Do": "Remember / Understand",
        "We Do": "Understand / Apply",
        "You Do Together": "Apply / Analyze",
        "You Do Alone": "Analyze / Create",
    }
    return mapping.get(grr_phase, "Apply")


def _clean_delivery_text(text: str) -> str:
    """Remove Format:, Bloom's:, and Delivery: metadata from delivery text."""
    # Handle both straight and curly apostrophes
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    # Remove "Format: description."
    text = re.sub(r"Format:\s*[^.]+\.\s*", "", text)
    # Remove "Bloom's: Word" or "Bloom's: Word + Word" (one or two Bloom's level words)
    text = re.sub(r"Bloom'?s?:\s*\w+(?:\s*\+\s*\w+)?\s*", "", text)
    # Remove "Delivery:" prefix
    text = re.sub(r"Delivery:\s*", "", text)
    return text.strip()


def _extract_teacher_actions(delivery: str, notes: str) -> list[str]:
    """Extract teacher actions from delivery instructions."""
    if not delivery:
        return []

    actions = []
    text = delivery.strip()
    # Extract format description before cleaning
    format_match = re.match(r"Format:\s*([^.]+\.)\s*", text)
    format_desc = format_match.group(1).strip() if format_match else ""
    # Clean all metadata prefixes
    text = _clean_delivery_text(text)
    # Add format description as first action if it's informative
    if format_desc:
        text = format_desc + " " + text

    if not text:
        return []

    # Split on sentence boundaries
    sentences = re.split(r'(?<=[.!?])\s+', text)
    for s in sentences:
        s = s.strip()
        if s and len(s) > 5:
            actions.append(s)

    if notes:
        notes = notes.strip()
        if notes.lower().startswith("instructor note:"):
            notes = notes[len("instructor note:"):].strip()
        if notes:
            actions.append(f"**Instructor Note:** {notes}")

    return actions


def _derive_student_actions(block: dict, swbats: list[str]) -> list[str]:
    """Derive student actions from the activity context."""
    name = block.get("activity_name", "")
    delivery = block.get("delivery_instructions", "")
    fmt = block.get("format", "")
    duration = block.get("duration", 15)

    actions = []
    name_lower = name.lower()
    delivery_lower = delivery.lower()

    # Extract student-focused sentences from delivery
    if delivery:
        # Clean the delivery text first
        clean_delivery = _clean_delivery_text(delivery)

        sentences = re.split(r'(?<=[.!?])\s+', clean_delivery)
        for s in sentences:
            sl = s.lower().strip()
            if any(kw in sl for kw in [
                "students", "they", "each student", "groups", "pairs",
                "write", "build", "create", "upload", "compare",
                "practice", "complete", "present", "share",
                "define", "outline", "analyze", "clean",
            ]):
                cleaned = s.strip()
                if cleaned and len(cleaned) > 10:
                    actions.append(cleaned)

    # If we didn't find enough, generate from context
    if not actions:
        if "follow-along" in delivery_lower or "follow along" in delivery_lower:
            actions.append("Follow along on their own laptops, replicating each step the instructor demonstrates.")
            actions.append("Pause to troubleshoot any errors before moving to the next step.")
        elif "hands-on" in delivery_lower:
            actions.append(f"Work through the {name} exercise on their laptops.")
        elif "group" in fmt.lower() or "group" in delivery_lower:
            actions.append(f"Work in small groups (3-4 students) on the {name} activity.")
            actions.append("Designate one group member to present findings to the class.")
        elif "pair" in fmt.lower() or "pair" in delivery_lower:
            actions.append(f"Work in pairs on the {name} activity, taking turns leading.")
        elif "individual" in delivery_lower:
            actions.append(f"Work independently on the {name} task.")
        elif "interactive" in delivery_lower or "voting" in delivery_lower:
            actions.append("Participate actively: respond to polls, vote on questions, share observations.")
        elif "lecture" in delivery_lower:
            actions.append("Take notes on key concepts. Flag questions for the Q&A portion.")
        elif "present" in name_lower:
            actions.append("Deliver their presentation within the time limit. Respond to panel questions with data-backed answers.")
        else:
            actions.append(f"Engage with the {name} activity as directed.")

    # Add timed sub-steps for longer activities
    if duration and duration > 10 and len(actions) < 3:
        mid = duration // 2
        actions.append(f"0:00–{mid}:00 — Work through the first part of the activity.")
        actions.append(f"{mid}:00–{duration}:00 — Complete the activity and prepare to share/discuss.")

    return actions


def _generate_pacing(block: dict) -> str:
    """Generate pacing from block data."""
    pacing = block.get("pacing", "").strip()
    if pacing:
        # Clean up the pacing text
        pacing = re.sub(r"^Pacing:\s*", "", pacing, flags=re.IGNORECASE)
        return pacing

    duration = block.get("duration", 15)
    name = block.get("activity_name", "Activity")
    if not duration or duration <= 5:
        return f"0:00–{duration}:00 — {name}"
    mid = duration // 2
    return f"0:00–{mid}:00 — First half | {mid}:00–{duration}:00 — Second half"


def _find_relevant_swbat(block: dict, swbats: list[str]) -> str:
    """Find the SWBAT most relevant to this activity block."""
    name = block.get("activity_name", "").lower()
    delivery = block.get("delivery_instructions", "").lower()
    combined = name + " " + delivery

    best_score = 0
    best_swbat = swbats[0] if swbats else ""

    for swbat in swbats:
        score = 0
        swbat_words = set(swbat.lower().split())
        # Remove common words
        swbat_words -= {"a", "an", "the", "and", "or", "to", "in", "of", "for", "with", "that", "is", "are", "be", "can"}
        for word in swbat_words:
            if len(word) > 3 and word in combined:
                score += 1
        if score > best_score:
            best_score = score
            best_swbat = swbat

    return best_swbat


def _generate_cfu_question(block: dict, swbat: str, technique: str) -> str:
    """Generate a specific CFU question based on the activity and SWBAT."""
    name = block.get("activity_name", "")
    delivery = block.get("delivery_instructions", "").lower()

    # Generate questions based on activity content
    if "chart" in name.lower() or "visualization" in name.lower() or "chart" in delivery:
        return "Show students a chart with a truncated y-axis. Ask: \"Is this chart trustworthy? What specifically makes it misleading, and how would you fix it?\""
    elif "pivot" in name.lower() or "pivot" in delivery:
        return "\"If I want to know which product category generates the most revenue by region, what fields go in Rows, Columns, and Values in my pivot table?\""
    elif "clean" in name.lower() or "clean" in delivery:
        return "\"I ran SUMIF on a column and got a number that seems too low. What are 3 data quality issues that could cause this?\""
    elif "function" in name.lower() or "vlookup" in delivery or "sort" in delivery or "filter" in delivery:
        return "\"When would you use FILTER instead of SORT to answer a business question? Give a specific example.\""
    elif "dashboard" in name.lower() or "dashboard" in delivery:
        return "\"Look at your dashboard. Can someone understand the main message in 5 seconds? What would you change to make it clearer?\""
    elif "story" in name.lower() or "narrative" in delivery or "storytelling" in delivery:
        return "\"Take your most important finding and structure it as Setup → Conflict → Resolution. Share with your partner in 30 seconds.\""
    elif "memo" in name.lower() or "memo" in delivery:
        return "\"Can your partner act on your memo from the first paragraph alone? If not, what needs to move up?\""
    elif "fallac" in name.lower() or "fallac" in delivery or "correlation" in delivery:
        return "\"Ice cream sales and drowning deaths both increase in summer. Is this correlation or causation? How would you test it?\""
    elif "gdpr" in name.lower() or "privacy" in delivery:
        return "\"A colleague wants to include individual customer names in a public dashboard. What GDPR principle applies, and what should they do instead?\""
    elif "present" in name.lower() or "stakeholder" in name.lower() or "panel" in name.lower():
        return "\"A stakeholder asks 'So what?' about your finding. Respond in one sentence with: the insight, why it matters, and what you recommend.\""
    elif "forecast" in name.lower() or "forecast" in delivery:
        return "\"What's the difference between a trend extrapolation and a scenario model? When would you use each?\""
    elif "kpi" in name.lower() or "kpi" in delivery:
        return "\"Your manager says 'website visits' is our KPI. Is this a vanity metric or an actionable metric? What would you propose instead?\""
    elif "sql" in name.lower() or "sql" in delivery:
        return "\"Write a SQL query that answers: 'How many orders came from each region?' What clause groups the results?\""
    elif "eu" in name.lower() or "smart" in delivery or "indicator" in delivery:
        return "\"Write one SMART indicator for this scenario: An NGO wants to measure the impact of their job training program.\""
    elif "ai" in name.lower() or "ai" in delivery:
        return "\"You uploaded data to an AI and it found 'a strong correlation between X and Y.' What 2 things should you verify before including this in your report?\""
    elif "portfolio" in name.lower() or "portfolio" in delivery:
        return "\"Look at your portfolio. Does it show the full pipeline from raw data → analysis → insight → recommendation? What's missing?\""
    elif "linkedin" in name.lower() or "linkedin" in delivery:
        return "\"Read your LinkedIn summary to your partner. Can they tell what data skills you have and how you've applied them?\""
    elif "capstone" in name.lower():
        return "\"In one sentence, what is the single most important insight from your capstone analysis, and what action should someone take based on it?\""
    elif "retrieval" in name.lower() or "challenge" in name.lower():
        return "\"Compare your speed and quality to the previous data challenge. What specific skill improved the most?\""
    elif "benchmark" in name.lower() or "context" in name.lower():
        return "\"Take one number from your analysis. Is it good or bad? Compared to what? Add one benchmark that gives it meaning.\""
    elif "brief" in name.lower() or "data brief" in delivery:
        return "\"Read your 3-sentence brief to your partner. Can they identify: (1) the finding, (2) why it matters, (3) the recommendation?\""
    elif "debrief" in name.lower() or "wild" in name.lower():
        return "\"What was the hardest part of finding and analyzing real-world data on your own? What would you do differently next time?\""
    elif "peer" in name.lower() or "review" in name.lower():
        return "\"Rate your partner's work on 3 dimensions (analytical quality, visualization clarity, narrative strength) from 1-5. Give one specific improvement suggestion for each.\""
    elif "autopsy" in name.lower():
        return "\"What was the #1 mistake you noticed across Round 1 presentations? How will you avoid it in your own presentation?\""
    else:
        # Fallback: use the SWBAT directly
        if swbat:
            return f"\"Based on what we just covered: Can you {swbat.lower().split('(')[0].strip()}? Demonstrate to your partner.\""
        return f"\"Summarize the key takeaway from {name} in one sentence to your partner.\""


def _generate_teacher_tip(block: dict) -> str:
    """Generate a teacher tip based on the activity type."""
    name = block.get("activity_name", "")
    delivery = block.get("delivery_instructions", "").lower()
    name_lower = name.lower()

    if "chart" in name_lower or "visualization" in name_lower:
        return "Students often default to pie charts. Redirect: \"Pie charts are almost never the best choice. What other chart type would show this comparison more clearly?\""
    elif "pivot" in name_lower:
        return "Common mistake: dragging fields into the wrong area (putting a text field in Values). Walk the room and check each student's pivot table structure before they proceed."
    elif "clean" in name_lower:
        return "Students will skip the \"check your work\" step. Insist they verify row counts before and after cleaning. If the count changed unexpectedly, they deleted real data."
    elif "vlookup" in delivery or "function" in name_lower:
        return "VLOOKUP will confuse 40-50% of the room. Use the dictionary analogy: \"You search column A to find a word, then return what's in column B.\" Keep the syntax on screen at all times."
    elif "dashboard" in name_lower:
        return "Students will over-design. Remind them: \"A simple dashboard that answers one question clearly beats a complex one that impresses nobody.\" Check for the 5-second test."
    elif "story" in name_lower or "narrative" in delivery:
        return "Students tend to describe methodology instead of telling the story. Redirect: \"Start with the surprise—what did the data reveal that you didn't expect?\""
    elif "present" in name_lower or "stakeholder" in name_lower:
        return "Watch for students reading their slides aloud. Coach: \"Your slides are the visual. YOU tell the story. Never say 'as you can see'—just say what the data shows.\""
    elif "memo" in name_lower:
        return "Students will bury the recommendation at the end. Check: \"Can I act on this from the first paragraph?\" If not, they need to restructure."
    elif "sql" in name_lower:
        return "Students may feel intimidated by SQL. Emphasize: \"You're not learning to be a developer. You're learning enough to communicate with your data team and understand what's possible.\""
    elif "forecast" in name_lower:
        return "Students will try to build formulas from scratch. Redirect them to the template. The goal is understanding the logic, not building the spreadsheet from zero."
    elif "kpi" in name_lower:
        return "Students confuse \"things we can measure\" with \"things that matter.\" Push back on vanity metrics: \"How does knowing this number change what you'd do tomorrow?\""
    elif "ai" in name_lower:
        return "Students will over-trust AI output. Require them to document at least one discrepancy between AI analysis and their own findings."
    elif "capstone" in name_lower or "build sprint" in name_lower:
        return "Triage students who are behind. Help them scope down to something complete rather than something ambitious but unfinished."
    elif "linkedin" in name_lower:
        return "Students will be too generic (\"experienced with data\"). Push for specifics: \"What tool did you use? What question did you answer? What was the result?\""
    elif "peer" in name_lower or "review" in name_lower:
        return "Students give vague feedback (\"looks good\"). Require the rubric dimensions: analytical quality, visualization clarity, narrative strength. Each needs a specific comment."
    elif "portfolio" in name_lower:
        return "Students forget to include the 'so what.' Each portfolio piece needs: the question asked, the data used, the analysis performed, and the recommendation made."
    elif "retrieval" in name_lower or "challenge" in name_lower:
        return "This should feel slightly uncomfortable—that's the point of retrieval practice. Don't provide notes or references. The struggle is where learning happens."
    elif "debrief" in name_lower:
        return "Enforce strict time limits (2 min per student). Use a visible timer. Students who go over are cut—this teaches conciseness, which is itself a data communication skill."
    elif "break" in name_lower or "lunch" in name_lower:
        return "Use this time to check in with struggling students informally. A 1-minute conversation during break can prevent 15 minutes of confusion later."
    elif "wrap" in name_lower or "close" in name_lower:
        return "Don't rush the self-assessment. Students comparing Day 1 to today need time to reflect—this metacognition is part of the learning."
    elif "benchmark" in name_lower or "context" in name_lower:
        return "Students will present numbers without context. Challenge every standalone number: \"Compared to what? Is this good or bad? How do you know?\""
    elif "autopsy" in name_lower:
        return "Keep the tone constructive, not critical. Frame it as: \"What patterns do we notice?\" not \"What did people do wrong?\" Students learn more when they feel safe."
    elif "fallac" in name_lower or "correlation" in name_lower:
        return "Use the funny spurious correlations first to set a light tone, then transition to the real business examples where correlation-as-causation cost money."
    elif "gdpr" in name_lower or "privacy" in delivery:
        return "Students may think GDPR doesn't apply to them. Emphasize: if you work with EU-funded projects or EU citizens' data, GDPR applies regardless of where you are."
    elif "eu" in name_lower or "reporting" in name_lower or "smart" in delivery:
        return "Students will write indicators that are too vague. Test each one: \"Could two different people measure this and get the same result?\" If not, it's not specific enough."
    else:
        return "Circulate the room during this activity. Check for understanding by looking at screens, not just asking \"Any questions?\" (students rarely admit confusion publicly)."


def _generate_reteach(swbat: str, block: dict) -> str:
    """Generate a reteach strategy for when CFU shows low understanding."""
    name = block.get("activity_name", "").lower()
    delivery = block.get("delivery_instructions", "").lower()

    if "chart" in name or "visualization" in name:
        return "Pull up the clearest misleading chart example. Walk through it step by step: \"What does the title say? What does the axis show? Do those match?\" Then show the corrected version side by side."
    elif "pivot" in name:
        return "Demo one more pivot table live with a simpler question. Have students replicate it exactly before attempting their own. Pair struggling students with proficient ones."
    elif "clean" in name:
        return "Show a before/after of one cleaning operation. Have students identify the specific problem (e.g., leading space) and the specific fix (TRIM function). Repeat with a new example."
    elif "function" in name or "vlookup" in delivery:
        return "Project the formula syntax on screen. Walk through each argument slowly: \"This part says WHERE to look. This part says WHAT to return.\" Have students type it character by character."
    elif "dashboard" in name:
        return "Show a good dashboard and a bad dashboard side by side. Ask: \"Which one passes the 5-second test? Why?\" Then have students fix ONE element of their own dashboard."
    elif "present" in name or "stakeholder" in name:
        return "Model a 30-second version: \"Here's what the data shows. Here's why it matters. Here's what I recommend.\" Have students practice just these 3 sentences before adding detail."
    elif "forecast" in name:
        return "Return to the template. Walk through changing ONE input and watching the output update. The goal is understanding input→output, not building from scratch."
    elif "sql" in name:
        return "Return to the simplest query: SELECT * FROM table. Add one clause at a time. Have students predict what each addition will do before running it."
    else:
        return "Re-demonstrate with a simpler example. Then pair struggling students with proficient peers for guided practice. Check back in 3 minutes."


def generate_lesson_md(session: dict) -> str:
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
    lines.append("=" * 60)
    lines.append("")
    if subtitle:
        lines.append(f"**Theme:** {subtitle}")
    lines.append(f"**Duration:** {total_duration} minutes" if total_duration else "**Duration:** TBD")
    lines.append("**Materials:** Laptops, projector, student handouts, whiteboard markers")
    lines.append("")

    # Learning Targets
    lines.append("## LEARNING TARGETS")
    lines.append("")
    for i, swbat in enumerate(swbats, 1):
        level = detect_blooms_level(swbat)
        lines.append(f"{i}. {swbat} _(Bloom's: {level})_")
    lines.append("")

    # Assessment at a Glance
    lines.append("## ASSESSMENT AT A GLANCE")
    lines.append("")
    if evidence:
        lines.append(f"**Look for:** {evidence[0]}")
    else:
        # Generate from SWBATs
        evidence_items = []
        for s in swbats[:3]:
            core = s.split("(")[0].strip()
            evidence_items.append(core)
        lines.append(f"**Look for:** Students can independently {'; '.join(evidence_items).lower()}")
    lines.append("**Formative:** CFU checks embedded every 10-15 minutes in lesson flow (see blocks below)")
    lines.append("**Exit Ticket:** See closing section — one question per SWBAT")
    lines.append("")

    # Lesson Flow
    lines.append("## LESSON FLOW")
    lines.append("")

    cfu_counter = 0

    for block in blocks:
        name = block.get("activity_name", "Activity")
        duration = block.get("duration", 15)
        time_range = block.get("time", "")
        fmt = block.get("format", "Whole Class")
        grr = block.get("grr_phase", "")
        delivery = block.get("delivery_instructions", "").strip()
        pacing_raw = block.get("pacing", "").strip()
        notes = block.get("instructor_notes", "").strip()
        blooms = _activity_blooms(grr, delivery)

        # Clean activity name
        clean_name = name.strip(" |✆")

        # Skip formatting for breaks/lunch (simpler block)
        if _is_non_teaching(block):
            lines.append(f"### {time_range}  {clean_name}  ({duration} min)")
            lines.append("")
            if "break" in name.lower():
                lines.append(f"> Use this time to circulate and check in with struggling students. A quick 1-minute conversation during break prevents 15 minutes of confusion later.")
            elif "lunch" in name.lower():
                lines.append(f"> Students return refreshed. Have the next activity's materials ready on screen when they sit down.")
            elif "buffer" in name.lower() or "overflow" in name.lower():
                lines.append(f"> Use this time for: (1) reteaching any concept where CFU showed <50% understanding, (2) individual troubleshooting, (3) letting fast students explore independently.")
            lines.append("")
            continue

        # Block header
        lines.append("┌" + "─" * 58 + "┐")
        grr_label = f" | GRR: {grr}" if grr else ""
        lines.append(f"│ **{time_range}  {clean_name}  ({duration} min)**")
        lines.append(f"│ {fmt} | Bloom's: {blooms}{grr_label}")
        lines.append("├" + "─" * 58 + "┤")

        # Teacher Does
        lines.append("│")
        lines.append("│ **TEACHER DOES**")
        teacher_actions = _extract_teacher_actions(delivery, notes)
        if teacher_actions:
            for action in teacher_actions:
                lines.append(f"│ • {action}")
        else:
            # Generate based on activity type and context
            lines.append(f"│ • Introduce the {clean_name} activity and explain the objective.")
            lines.append(f"│ • Demonstrate the key concept or skill, narrating each step.")
            lines.append(f"│ • Circulate to check understanding and provide individual support.")
        lines.append("│")

        # Students Do
        lines.append("│ **STUDENTS DO**")
        student_actions = _derive_student_actions(block, swbats)
        for action in student_actions:
            lines.append(f"│ • {action}")
        lines.append("│")

        # Pacing
        pacing = _generate_pacing(block)
        lines.append(f"│ **PACING:** {pacing}")
        lines.append("│")

        # Teacher Tip
        tip = _generate_teacher_tip(block)
        lines.append(f"│ **TEACHER TIP:** {tip}")
        lines.append("│")

        # CFU
        cfu_counter += 1
        technique = CFU_TECHNIQUES[cfu_counter % len(CFU_TECHNIQUES)]
        relevant_swbat = _find_relevant_swbat(block, swbats) if swbats else ""
        cfu_question = _generate_cfu_question(block, relevant_swbat, technique)
        reteach = _generate_reteach(relevant_swbat, block)
        lines.append(f"│ **CHECK ({technique}):** {cfu_question}")
        lines.append(f"│ If <25% pass → {reteach}")
        lines.append("└" + "─" * 58 + "┘")
        lines.append("")

    # Differentiation
    lines.append("## DIFFERENTIATION NOTES")
    lines.append("")
    lines.append("| Level | Strategy |")
    lines.append("|-------|----------|")

    # Generate specific differentiation based on session content
    struggling_strategies = _gen_struggling_strategies(swbats, blocks)
    advanced_strategies = _gen_advanced_strategies(swbats, blocks)
    language_strategies = _gen_language_strategies(swbats, blocks)

    lines.append(f"| **Struggling** | {struggling_strategies} |")
    lines.append(f"| **Advanced** | {advanced_strategies} |")
    lines.append(f"| **Language Support** | {language_strategies} |")
    lines.append("")

    # Closing & Exit Ticket
    lines.append("## CLOSING & EXIT TICKET")
    lines.append("")
    for i, swbat in enumerate(swbats, 1):
        question = _generate_exit_ticket_question(swbat, i)
        lines.append(f"{i}. {question}")
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


def _gen_struggling_strategies(swbats: list[str], blocks: list[dict]) -> str:
    """Generate differentiation strategies for struggling students."""
    strategies = []
    for s in swbats[:2]:
        sl = s.lower()
        if "chart" in sl or "visualization" in sl:
            strategies.append("Provide a chart evaluation checklist (title accurate? axes labeled? scale honest?)")
        elif "function" in sl or "spreadsheet" in sl or "vlookup" in sl:
            strategies.append("Give a formula reference card with syntax + example for each function")
        elif "clean" in sl:
            strategies.append("Provide a step-by-step cleaning checklist: 1) Remove duplicates, 2) TRIM spaces, 3) Fix formatting, 4) Check blanks")
        elif "pivot" in sl:
            strategies.append("Pre-label the pivot table areas (Rows/Columns/Values) with the correct fields for the first 2 tables")
        elif "dashboard" in sl:
            strategies.append("Provide a dashboard template with placeholder charts already positioned")
        elif "write" in sl or "memo" in sl or "brief" in sl:
            strategies.append("Provide sentence starters: \"The data shows...\", \"This matters because...\", \"I recommend...\"")
        elif "present" in sl or "defend" in sl:
            strategies.append("Provide a presentation script template with fill-in-the-blank sections")
        elif "forecast" in sl:
            strategies.append("Use the pre-built template; students only change input assumptions, not formulas")
        elif "kpi" in sl:
            strategies.append("Provide 5 example KPIs and have students identify which are vanity vs. actionable")
        elif "sql" in sl:
            strategies.append("Provide query templates with blanks: SELECT ___ FROM ___ WHERE ___")
        elif "portfolio" in sl:
            strategies.append("Provide a portfolio checklist: raw data, analysis, visualization, insight, recommendation")

    if not strategies:
        strategies.append("Provide step-by-step checklists and worked examples for each activity")
        strategies.append("Pair with a proficient peer for guided practice")

    return "; ".join(strategies[:3])


def _gen_advanced_strategies(swbats: list[str], blocks: list[dict]) -> str:
    """Generate differentiation strategies for advanced students."""
    strategies = []
    for s in swbats[:2]:
        sl = s.lower()
        if "chart" in sl or "visualization" in sl:
            strategies.append("Find and critique a real misleading chart from current news; present the correction")
        elif "function" in sl or "spreadsheet" in sl:
            strategies.append("Attempt nested functions (e.g., SUMIFS, INDEX-MATCH with multiple criteria)")
        elif "dashboard" in sl:
            strategies.append("Add calculated fields or custom metrics to the dashboard beyond the minimum requirements")
        elif "present" in sl:
            strategies.append("Present with a harder constraint: 60 seconds instead of 2 minutes")
        elif "forecast" in sl:
            strategies.append("Build the third forecast method independently without the template")
        elif "sql" in sl:
            strategies.append("Attempt JOIN queries and subqueries in the SQL playground")

    if not strategies:
        strategies.append("Extend the core activity with an open-ended challenge using real-world data")

    strategies.append("Mentor a struggling peer (teaching deepens understanding)")
    return "; ".join(strategies[:3])


def _gen_language_strategies(swbats: list[str], blocks: list[dict]) -> str:
    """Generate language support strategies."""
    return (
        "Vocabulary wall with key data terms in English + local language; "
        "sentence frames for data briefs and presentations; "
        "bilingual glossary handout (data literacy, pivot table, correlation, dashboard, KPI); "
        "allow draft writing in L1 before translating to English"
    )


def _generate_exit_ticket_question(swbat: str, num: int) -> str:
    """Generate a specific exit ticket question from a SWBAT."""
    sl = swbat.lower()

    if "misleading" in sl or "trustworthy" in sl or "deceptive" in sl:
        return "Show a chart with a truncated y-axis. \"Identify what makes this chart misleading and rewrite the title to make it honest.\""
    elif "spreadsheet function" in sl or "sort" in sl or "filter" in sl or "sumif" in sl:
        return "\"Using this mini-dataset, write a SUMIF formula that answers: 'What is the total revenue from Region A?'\""
    elif "clean" in sl:
        return "\"List 3 data quality problems you should check for before analyzing any dataset.\""
    elif "pivot table" in sl:
        return "\"Given this business question: 'Which product category had the highest sales last quarter?' — describe which fields go in Rows, Columns, and Values.\""
    elif "chart type" in sl or "appropriate chart" in sl:
        return "\"You need to show sales trends over 12 months. Which chart type do you choose and why? Name one chart type that would be a poor choice.\""
    elif "data brief" in sl or "3-sentence" in sl:
        return "\"Write a 3-sentence data brief about one finding from today's work: [What happened] + [Why it matters] + [What to do next].\""
    elif "vlookup" in sl or "index-match" in sl:
        return "\"When does INDEX-MATCH work better than VLOOKUP? Give one specific scenario.\""
    elif "dashboard" in sl or "5-second" in sl:
        return "\"What 3 elements must every dashboard have to pass the 5-second test?\""
    elif "data story" in sl or "narrative arc" in sl:
        return "\"Structure this finding as Setup → Conflict → Resolution: 'Sales dropped 30% in Q3.'\""
    elif "memo" in sl or "recommendation" in sl:
        return "\"Write the first sentence of a data memo that an executive can act on immediately.\""
    elif "fallac" in sl or "correlation" in sl or "causation" in sl:
        return "\"A report claims: 'Stores that play music sell more products, therefore music causes purchases.' Identify the fallacy and suggest how to test the claim.\""
    elif "gdpr" in sl or "privacy" in sl:
        return "\"Name 2 types of data that must be anonymized before including in a shared dashboard under GDPR.\""
    elif "benchmark" in sl or "context" in sl or "segmentation" in sl:
        return "\"Take the number 15% growth. Is that good or bad? What benchmark would you compare it to, and why?\""
    elif "forecast" in sl:
        return "\"Name the 3 forecasting methods we learned. Which would you choose for predicting next quarter's sales, and why?\""
    elif "kpi" in sl:
        return "\"Write one actionable KPI for a customer support team. Explain why it's better than tracking 'total tickets received.'\""
    elif "present" in sl or "confidence" in sl or "audience" in sl:
        return "\"In one sentence, what is the #1 rule for presenting data to a non-technical audience?\""
    elif "defend" in sl or "methodology" in sl or "questioning" in sl:
        return "\"A stakeholder challenges: 'Your sample size is too small.' How do you respond? (Acknowledge, explain, offer next steps.)\""
    elif "portfolio" in sl:
        return "\"List the 4 components every data portfolio piece should include.\""
    elif "growth" in sl or "metacognition" in sl or "articulate" in sl:
        return "\"Compare your data confidence on Day 1 vs. today across: reading data, cleaning data, analyzing data, communicating data. Which grew the most?\""
    elif "linkedin" in sl or "career" in sl or "position" in sl:
        return "\"Write one bullet point for your LinkedIn that describes a data skill you demonstrated this week, with a specific example.\""
    elif "sql" in sl:
        return "\"Write a SELECT query with a WHERE clause that filters for orders above $100.\""
    elif "smart" in sl or "eu" in sl or "indicator" in sl:
        return "\"Write one SMART indicator for measuring the success of a youth employment program.\""
    else:
        return f"\"Demonstrate: {swbat}\""


def main():
    sessions = load_parsed_curriculum()
    LESSONS_DIR.mkdir(parents=True, exist_ok=True)

    for session in sessions:
        md = generate_lesson_md(session)
        num = session["session_number"]
        filename = f"session_{num:02d}_lesson_plan.md"
        out_path = LESSONS_DIR / filename
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Generated: {filename}")

    print(f"\n{len(sessions)} lesson plan(s) written to {LESSONS_DIR}")


if __name__ == "__main__":
    main()
