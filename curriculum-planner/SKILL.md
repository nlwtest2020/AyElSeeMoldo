---
name: lesson-plan-builder
description: "Use this skill whenever the user wants to create lesson plans, teaching materials, slide decks for instruction, curriculum units, or any structured educational content. Triggers include: 'lesson plan', 'unit plan', 'teaching plan', 'curriculum', 'course outline', 'instructional materials', 'training session', 'workshop plan', SWBATs, learning objectives, or requests to build classroom-ready content. Also trigger when the user asks to design assessments tied to learning objectives, create teacher-facing slide presentations, or build scaffolded instructional sequences. Use this skill even for partial requests like 'write the activities for day 3' or 'give me a hook for this topic' — any instructional design subtask should use this skill. Do NOT use for general presentation decks, business training without pedagogical structure, or academic paper writing."
---

# Lesson Plan Builder

Build pedagogically sound, classroom-ready lesson plans with aligned slides, assessments, and materials.

## When to use this skill

Any time the user needs instructional content — full lesson plans, individual lesson components (hooks, activities, assessments), slide decks for teaching, unit sequences, or curriculum design. This includes both new creation and revision of existing materials.

## Inputs you need from the user

Before generating, gather these. If the user hasn't provided them, ask — but ask efficiently (one round, not five).

| Input | Required? | Why it matters |
|-------|-----------|----------------|
| Topic / subject area | Yes | Determines content and terminology level |
| Target learners | Yes | Drives language level, scaffolding, examples, pacing |
| Session duration | Yes | Controls block structure, number of activities, pacing |
| Learning objectives / SWBATs | Yes (or derive them) | Everything flows backward from these — they are the spine |
| Number of sessions / days | If multi-day | Determines sequencing and progression |
| Context constraints | If any | Class size, available tech, room setup, co-teaching, etc. |
| Output format | If specific | Docx, slides, markdown, or combined package |

If the user provides a topic but no objectives, draft SWBATs for their approval before building instruction. Never build a lesson plan without confirmed objectives — this is backward design, and the objectives come first.

## Core design workflow

Follow this sequence. Do not skip steps or reorder them.

### Step 1: Lock the objectives

Write or confirm SWBATs. Each must be:
- **Observable** — uses a verb you can see evidence of (not "understand" or "appreciate")
- **Measurable** — you can design an assessment that proves it
- **Bloom's-tagged** — note the cognitive level (Remember → Create)
- **Student-facing** — written as "Students will be able to..." not "Teacher will cover..."

Tag each SWBAT with its Bloom's level explicitly. This drives everything downstream.

**Anti-pattern to avoid:** Vague objectives like "Students will understand the difference between X and Y." Replace with: "Students will compare X and Y using at least three criteria and justify which is more appropriate for a given scenario (Analyze)."

### Step 2: Design assessments BEFORE instruction

For each SWBAT, specify:
- **Formative check** — how will the teacher know mid-lesson whether students are getting it? Be specific: not "teacher checks understanding" but "students write one sentence using the target structure on whiteboards; teacher scans for correct subject-verb agreement."
- **Summative evidence** — how will students prove mastery at the end? Exit ticket prompt, performance task, product, etc.

The assessment plan must be concrete enough that a substitute teacher could administer it without guessing what you meant.

### Step 3: Sequence instruction using Gradual Release

For each instructional block, follow this progression:

**I Do (Direct Instruction)** — 10-15% of block time
Teacher models explicitly. Write out what the teacher says and does, not just "teacher explains." Include the actual example, the think-aloud, the key language.

**We Do (Guided Practice)** — 25-35% of block time
Teacher and students work through examples together. Specify: what example, what questions the teacher asks, what scaffolds are in place, what correct and incorrect responses look like.

**You Do Together (Collaborative Practice)** — 25-35% of block time
Students practice in pairs or groups. Specify: the task, the grouping, the deliverable, the time limit, what the teacher monitors for, and intervention triggers.

**You Do Alone (Independent Practice)** — 20-30% of block time
Students work independently. Specify: the task, success criteria, what "done" looks like, and what early finishers do.

**Hard rule:** Never jump from I Do to You Do Alone. If time is short, compress We Do and You Do Together — don't eliminate them.

### Step 4: Build the timeline

Every lesson plan gets a minute-by-minute sequence. Use this structure:

```
[Timestamp] | [Section Name] | [GRR Phase] | [Duration]
Teacher does: [specific actions and language]
Students do: [specific actions and expected responses]  
Materials: [slides, handouts, props referenced]
CFU: [specific check-for-understanding technique and what you're checking]
```

Pacing rules:
- **Opening/Hook:** 5-8 minutes. Activate prior knowledge, create curiosity, state objectives.
- **Core blocks:** 15-25 minutes each, following GRR internally.
- **Transitions:** 2-3 minutes. Explicit signals, directions posted before calling the move.
- **Closing:** 5-10 minutes. Summary, exit ticket, preview next session.
- **Buffer:** Build 5-10 minutes of flex time per 90-minute session. Don't pack it wall-to-wall.

Attention span constraint: no single activity format runs longer than 12 minutes without a shift. After 8 minutes of teacher talk, students must process (write, discuss, move).

### Step 5: Embed formative assessment checkpoints

Place a CFU every 10-15 minutes minimum. Each CFU must:
- Check the SWBAT, not just participation
- Specify the technique (cold call, whiteboard, turn-and-talk, exit ticket — not just "check understanding")
- Include a decision rule: "If more than 25% miss this, stop and reteach using [specific alternative explanation] before proceeding"

### Step 6: Add differentiation

For each major activity, note:
- **Scaffold down:** What support exists for struggling learners? (sentence frames, simplified prompts, strategic pairing, chunked instructions)
- **Scaffold up:** What extension exists for fast finishers that deepens, not just adds more? (analyze instead of apply, create instead of analyze)

### Step 7: Write the materials

Now — and only now — create slides, handouts, or other materials. Materials serve the lesson plan, not the other way around.

## Output format: Lesson Plan document

Use this structure for every lesson plan. Read `references/lesson-plan-template.md` for the full template with formatting specifications.

**Header block:**
- Title, date, duration, level/audience
- Materials and preparation checklist (everything needed, with prep notes)

**Objectives block:**
- Numbered SWBATs with Bloom's level tags

**Assessment plan:**
- Table mapping each SWBAT → formative check → summative evidence

**Lesson sequence:**
- Minute-by-minute timeline per Step 4 above

**Differentiation notes:**
- Per-activity scaffold-down and scaffold-up notes

**Closure and assessment:**
- Exit ticket or closing assessment with specific prompts

**Reflection space:**
- Blank section for post-lesson teacher notes (always include this)

## Output format: Instructional slides

If the user requests slides, read the pptx SKILL.md for creation mechanics, then apply these instructional design rules:

**One idea per slide.** If you're putting two concepts on one slide, split it.

**Slide type determines design:**

| Slide Type | Purpose | Design Rule |
|------------|---------|-------------|
| Title | Session name, date | Clean, minimal, branded |
| Objectives | Display SWBATs | Numbered, student-friendly language |
| Content | Key concept or definition | Visual + brief text, one concept only |
| Example | Worked demonstration | Step-by-step with annotations |
| Activity | Instructions for student work | Numbered steps, time limit, deliverable stated |
| Discussion | Prompts for conversation | 1-2 open-ended questions, large font |
| CFU | Check-for-understanding question | Question + response format (A/B/C/D, whiteboard, etc.) |
| Summary | Recap key takeaways | Tie back to objectives |
| Transition | Signal shift between topics | Brief, visual, marks the boundary |

**Progressive disclosure:** Reveal information incrementally. Don't show the full model before you've built to it.

**6x6 ceiling:** Maximum 6 bullet points, maximum 6 words per point. Aim for less. If you need more text, it belongs in a handout, not a slide.

**No paragraphs on slides.** If there's a paragraph, it's wrong.

## Anti-patterns — what bad output looks like

These are the failure modes. Catch them before they ship.

- **Vague activity descriptions.** "Students discuss in groups" is useless. Specify: the prompt, the grouping (pairs? triads?), the deliverable, the time, and what the teacher monitors for.
- **Assessment afterthought.** If the assessment section says "teacher observes" or "informal assessment" without specifying what is observed and what counts as evidence, it's not an assessment.
- **GRR violations.** Jumping from lecture to independent practice. Every new skill needs guided practice in the middle.
- **Bloated slides.** Slides with 8+ bullet points or full paragraphs. Slides are signposts, not textbooks.
- **Time math that doesn't add up.** If activities sum to 95 minutes in a 90-minute session with no buffer, the plan will fail in execution.
- **Objectives without teeth.** "Students will understand..." or "Students will learn about..." are not SWBATs. They can't be measured.
- **Undifferentiated instruction.** A plan that assumes all students arrive at the same level and proceed at the same pace. At minimum, scaffold-down and scaffold-up must be specified.
- **Missing transitions.** Activities that slam into each other with no signal, no direction, no movement. Transitions are instructional moments, not dead time.
- **Cognitive level mismatch.** Asking students to "create" something when instruction only covered "remember" and "understand." You must scaffold through the levels.

## File creation

**For lesson plans as documents:** Read the docx SKILL.md, then use the lesson plan template structure above. Produce a .docx file.

**For lesson plans as markdown:** Output to .md with clean formatting. Use the same structural sections.

**For slide decks:** Read the pptx SKILL.md for creation mechanics. Follow the instructional slide rules in this skill.

**For combined packages:** Create the lesson plan document first, then create slides that reference it. The lesson plan is the source of truth; slides are the delivery vehicle.

## Reference files

- `references/lesson-plan-template.md` — Full template with section-by-section formatting guidance and a worked example
- `references/pedagogy-reference.md` — Detailed pedagogical frameworks (Bloom's taxonomy, GRR, scaffolding strategies, formative assessment techniques, differentiation). Consult when making design decisions about cognitive level alignment, activity sequencing, or assessment design.

## Keywords

lesson plan, unit plan, teaching plan, curriculum, course outline, instructional materials, training session, workshop plan, SWBAT, learning objectives, backward design, teaching slides, instructional slides, lesson sequence, formative assessment, exit ticket, gradual release, scaffolding, differentiation, Bloom's taxonomy, hook, closure, guided practice
