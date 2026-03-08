# Lesson Plan Builder Skill

This skill defines the workflow, output specifications, and quality standards for building lesson plans from parsed curriculum data.

---

## 7-Step Design Workflow

Follow these steps in order. Do not skip steps or reorder them.

### Step 1: Lock Objectives

Review each SWBAT from `parsed_curriculum.json`. Verify each objective is:

- **Observable** — describes something a teacher can see or hear
- **Measurable** — has a clear success/failure threshold
- **Bloom's-tagged** — uses a verb from Bloom's taxonomy (see `references/pedagogy-reference.md`)

If a SWBAT uses vague verbs ("understand," "learn about," "appreciate"), rewrite it using an observable verb at the same cognitive level. Do not build instruction against a vague objective.

### Step 2: Design Assessments Before Instruction

For every SWBAT, define:

- **Formative check**: Which technique? When in the block? What's the decision rule if >25% fail?
- **Summative evidence**: Exit ticket prompt, performance task, or product

The assessment plan must be concrete enough that a substitute teacher could administer it.

### Step 3: Sequence Instruction Using Gradual Release

For each content block, build through the GRR progression:

1. **I Do** (Direct Instruction) — Teacher models. Students observe. 10-15% of block time.
2. **We Do** (Guided Practice) — Teacher and students work together. 25-35% of block time.
3. **You Do Together** (Collaborative Practice) — Students practice in pairs/groups. 25-35% of block time.
4. **You Do Alone** (Independent Practice) — Students demonstrate mastery solo. 20-30% of block time.

Never skip from I Do to You Do Alone. Incorporate research findings from Stage 2 into activity design.

### Step 4: Build the Timeline

Generate the lesson plan following the template in `references/lesson-plan-template.md`. For each timing block specify:

- Exact timestamps matching the source document
- Section title and GRR phase
- **Teacher actions**: specific language, questions to ask, demonstrations (not "teacher explains")
- **Student actions**: what students are doing (not "students listen")
- Materials/slides referenced
- CFU checkpoint with technique, target, and reteach trigger

### Step 5: Embed CFU Checkpoints

- One every 10-15 minutes of instruction, minimum
- Each must check the SWBAT, not just participation
- Specify the technique (cold call, thumbs up/down, exit slip, turn-and-talk)
- Include a decision rule: "If >25% miss, do X before proceeding"

### Step 6: Add Differentiation

For each major activity:

- **Scaffold down** for struggling learners (simplified templates, sentence starters, pre-built examples)
- **Scaffold up** for advanced learners (extension challenges that deepen, not add volume)
- **Language support** for multilingual learners (key terms pre-taught, visual aids, L1 allowed)

### Step 7: Run Quality Checklist

Before delivering, run the checklist at the bottom of `references/lesson-plan-template.md`. Every box must pass.

---

## Output Format: Lesson Plan (Teaching Guide)

The lesson plan generator (`scripts/generate_lesson_plans.py`) produces per-session DOCX files with this structure:

1. **Header block** — session title, metadata (day/time/theme/duration/materials)
2. **Learning targets** — numbered SWBATs, cleaned of LO references
3. **Assessment at a glance** — evidence to look for, formative/summative methods
4. **Lesson flow** — activity blocks with:
   - Dark header bar (time, activity name, duration, format, GRR phase)
   - TEACHER DOES section (parsed from delivery field)
   - STUDENTS DO section (extracted student actions)
   - Pacing notes
   - Teacher tips (from instructor_note field)
   - CFU checkpoint per block
   - Break dividers between blocks
5. **Differentiation notes** — per-session strategies
6. **Closing & exit ticket** — specific questions tied to SWBATs
7. **Post-session reflection** — structured prompts for teacher self-assessment

## Output Format: Instructional Slides

The slide generator (`scripts/generate_pptx.py`) produces per-session PPTX files using the branded template. Slide design rules:

- **One idea per slide** — each slide communicates a single concept or instruction
- **6x6 ceiling** — maximum 6 bullet points, maximum 6 words per bullet
- **No paragraphs on slides** — if you need a paragraph, it belongs in the lesson plan
- **Visual > text** — use images, diagrams, and charts where possible
- **Consistent layout** — same slide layout for similar content types
- **High contrast** — dark on light or light on dark
- **Limit font variations** — 1 heading font, 1 body font from the brand template

Slide sequence per session:

| Type | Purpose |
|------|---------|
| Title | Session name, date, welcome |
| Objectives | SWBATs in student-friendly language |
| Content | Key concept — one per slide |
| Activity | Numbered instructions, time limit, deliverable |
| Discussion | 1-2 open-ended questions, large font |
| CFU/Check | Assessment question + response format |
| Summary | Key takeaways tied to objectives |

---

## Anti-Patterns to Catch Before Delivering

1. **Data dump** — Schedule tables with raw delivery text crammed into cells. The lesson plan should be a teaching guide, not a data export.
2. **Missing GRR** — Every instructional block needs a GRR phase label. "Teacher presents" is not a lesson.
3. **No CFU** — If there's no check-for-understanding in a 30-minute block, the teacher is flying blind.
4. **Vague teacher actions** — "Teacher explains the concept" tells the teacher nothing. Use specific language, questions, and demonstrations.
5. **Vague student actions** — "Students listen" is not an action. What are they writing, building, discussing, comparing?
6. **Truncated content** — If delivery text is cut at 400 characters, the teacher loses critical instructions. Use the full text, reformatted as steps.
7. **No differentiation** — Every class has diverse learners. No plan is complete without scaffold-up and scaffold-down notes.
8. **All the same visual weight** — If every section looks identical, nothing stands out. Use hierarchy: headers, labels, indentation, color.
