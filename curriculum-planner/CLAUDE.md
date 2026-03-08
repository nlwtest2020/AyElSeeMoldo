Curriculum Researcher & Lesson Planner - Workflow Instructions

This directory contains a linear pipeline for building complete day-long curriculum packages from a source document. The pipeline produces two outputs: a detailed teacher lesson plan and a branded PowerPoint presentation.

## How to Use

1. Place the input .docx file in `input/`
2. Place the branded .pptx template in `templates/`
3. Follow the pipeline stages below IN ORDER. Each stage must complete before the next begins.

## Pipeline Overview

```
[1. PARSE] --> [2. RESEARCH] --> [3. LESSON PLAN] --> [4. PPT GENERATION]
```

Every stage is sequential. Do not skip ahead or run stages in parallel.

## Quality Authority

The `skills/` directory contains the lesson plan builder skill, which is the single source of truth for all instructional design decisions:

```
skills/
├── SKILL.md                          # Design workflow, output specs, anti-patterns
└── references/
    ├── lesson-plan-template.md       # Output template + worked example + quality checklist
    └── pedagogy-reference.md         # Bloom's, GRR, scaffolding, assessment, pacing rules
```

**When to read which file:**

- `SKILL.md` — Read at the start of Stage 3. Defines the 7-step design workflow, output structure, slide design rules, and anti-patterns to catch before delivering. This is the operational playbook.
- `references/lesson-plan-template.md` — Read during Stage 3 generation. Contains the exact output template to follow and a worked example showing the quality bar. Also contains the pre-delivery quality checklist — run this before marking Stage 3 complete.
- `references/pedagogy-reference.md` — Consult as needed during Stages 2 and 3 when making specific decisions about Bloom's alignment, GRR phase structure, formative assessment technique selection, scaffolding strategy, or pacing. This is a lookup reference, not a sequential read.

---

## Stage 1: PARSE the Input Document

**Goal:** Extract structured curriculum data from the .docx file.

**Steps:**

1. Run the parser script:
```bash
cd /home/user/AyElSeeMoldo/curriculum-planner
python scripts/parse_docx.py input/<filename>.docx
```

2. This produces `output/parsed_curriculum.json` with structured data:
   - Day/module title and duration
   - Timing blocks (start time, end time, section name)
   - Content topics per block
   - SWBATs (Students Will Be Able To)
   - Deliverables and assessments
   - Any notes or special instructions from the source document

3. Verify the JSON output is complete and accurate before proceeding. If the parser misses content or the .docx has unusual formatting, manually review the .docx and supplement the JSON.

**Checkpoint:** `output/parsed_curriculum.json` exists and contains all sections from the source document.

---

## Stage 2: RESEARCH Teaching Methods

**Goal:** For each content topic and SWBAT, research best practices for teaching that specific concept.

**Steps:**

1. Read `output/parsed_curriculum.json` to identify all content topics and SWBATs.
2. Read `skills/references/pedagogy-reference.md` — specifically the Bloom's Taxonomy section — to tag each SWBAT with its cognitive level. This tagging drives the research: an "Apply"-level SWBAT needs practice activities and worked examples; an "Analyze"-level SWBAT needs case studies and comparison tasks. Research accordingly.
3. For each major content topic, use WebSearch to research:
   - Best practices for teaching that specific concept or skill
   - Common student misconceptions and how to address them
   - Effective activities and engagement strategies for the topic
   - Real-world applications and examples that connect to student experience
4. Compile research findings into `output/research_notes.md` organized by topic/SWBAT. For each finding, note:
   - The source/basis of the recommendation
   - The Bloom's level of the SWBAT it serves
   - The GRR phase where this strategy fits (I Do / We Do / You Do Together / You Do Alone)
   - Specific activity ideas with estimated timing
   - Potential misconceptions to watch for

**Checkpoint:** `output/research_notes.md` exists with research notes for every major content topic, tagged by Bloom's level and GRR phase.

**Important:** Research should be targeted and practical. Focus on "how to teach X effectively" not general theory. Prioritize actionable strategies over literature reviews.

---

## Stage 3: GENERATE the Lesson Plan

**Goal:** Produce a comprehensive, minute-by-minute lesson plan for teachers.

**Before starting this stage, read these files in order:**
1. `skills/SKILL.md` — the design workflow you will follow
2. `skills/references/lesson-plan-template.md` — the output template and worked example

Then read the three input files:
- `output/parsed_curriculum.json` (structure and timing from Stage 1)
- `output/research_notes.md` (teaching strategies from Stage 2)

**Steps:**

1. **Lock objectives (SKILL.md Step 1).** Review the SWBATs from parsed_curriculum.json. Verify each one is observable, measurable, and Bloom's-tagged. If any SWBAT uses vague verbs ("understand," "learn about," "appreciate"), rewrite it before proceeding. Do not build instruction against a vague objective.

2. **Design assessments before instruction (SKILL.md Step 2).** For every SWBAT, define the formative check (technique, timing, decision rule for failure) and summative evidence (exit ticket prompt, performance task, product). The assessment plan must be concrete enough that a substitute teacher could administer it.

3. **Sequence instruction using Gradual Release (SKILL.md Step 3).** For each content block, build through I Do → We Do → You Do Together → You Do Alone. Never skip from I Do to You Do Alone. Incorporate research findings from Stage 2 into activity design — this is where the research becomes instruction.

4. **Build the timeline (SKILL.md Step 4).** Generate `output/lesson_plan.md` following the template in `skills/references/lesson-plan-template.md`. Use the exact section structure. For each timing block, specify:
   - Exact timestamps matching the source document
   - Section title and GRR phase
   - Teacher actions (specific language, questions, demonstrations — not "teacher explains")
   - Student actions (what students are doing, not "students listen")
   - Materials/slides referenced (specific slide numbers)
   - CFU checkpoint with technique, target, and reteach trigger

5. **Embed CFU checkpoints (SKILL.md Step 5).** One every 10-15 minutes minimum. Each must check the SWBAT, specify the technique, and include a decision rule.

6. **Add differentiation (SKILL.md Step 6).** For each major activity: scaffold-down for struggling learners, scaffold-up for advanced learners. Extensions must deepen, not add volume.

7. **Run the quality checklist.** Before marking this stage complete, run the checklist at the bottom of `skills/references/lesson-plan-template.md`. Every box must pass.

**Checkpoint:** `output/lesson_plan.md` is complete, every SWBAT has aligned instruction and assessment, timing adds up correctly, and the quality checklist passes.

---

## Stage 4: GENERATE the Branded PPT

**Goal:** Create a polished PowerPoint presentation using the branded template.

**Before starting, read:** `skills/SKILL.md` — the "Output format: Instructional slides" section for slide design rules.

**Steps:**

1. Read the completed lesson plan from `output/lesson_plan.md`.
2. Run the PPT generator:
```bash
cd /home/user/AyElSeeMoldo/curriculum-planner
python scripts/generate_pptx.py output/lesson_plan.md templates/<template_name>.pptx
```

3. The script generates `output/day_slides.pptx` with slides following this sequence:

| Slide Type | Purpose | Design Rule |
|------------|---------|-------------|
| Title | Day/module name, date | Clean, minimal, branded |
| Objectives | SWBATs in student-friendly language | Numbered list |
| Content | Key concept or definition | One concept per slide, visual + brief text |
| Example | Worked demonstration | Step-by-step with annotations |
| Activity | Instructions for student work | Numbered steps, time limit, deliverable stated |
| Discussion | Prompts for conversation | 1-2 open-ended questions, large font |
| CFU/Check | Assessment question | Question + response format |
| Transition | Signal shift between sections | Brief, visual marker |
| Summary | Key takeaways | Tied back to objectives |

4. Verify the output:
   - Branding is preserved (fonts, colors, logo placement from template)
   - Slide count is reasonable (roughly 1 slide per 3-5 minutes of instruction)
   - Text fits within slide boundaries (no overflow)
   - One idea per slide — if a slide has two concepts, split it
   - 6x6 ceiling: maximum 6 bullet points, maximum 6 words per point
   - No paragraphs on slides
   - Slide order matches lesson plan sequence exactly

**Checkpoint:** `output/day_slides.pptx` exists, opens correctly, preserves template branding, and follows the slide design rules.

---

## Agent Coordination Rules

When using multiple Claude Code agents to handle different stages:

1. **Linear execution only** — Agent for Stage N must complete and produce its output file before Agent for Stage N+1 begins.
2. **File-based handoffs** — All inter-stage communication happens through files in `output/`. No agent should assume knowledge from a prior stage except through reading output files.
3. **Skills directory is the shared quality authority** — Every agent reads the relevant files from `skills/` for their stage. It is the single source of truth for pedagogical and design standards.
4. **Verify before proceeding** — Each agent checks that the previous stage's output file exists and is well-formed before starting its work.
5. **No backwards jumps** — If a problem is found in a later stage, note it in the output but do not go back and re-run earlier stages without user approval.

---

## File Reference

| File | Purpose |
|------|---------|
| `CLAUDE.md` | This file — workflow instructions |
| `skills/SKILL.md` | Design workflow, output specs, anti-patterns (quality authority) |
| `skills/references/lesson-plan-template.md` | Output template, worked example, quality checklist |
| `skills/references/pedagogy-reference.md` | Bloom's, GRR, scaffolding, assessment, pacing (lookup reference) |
| `scripts/parse_docx.py` | Stage 1: Parse .docx to JSON |
| `scripts/generate_pptx.py` | Stage 4: Generate branded .pptx from lesson plan |
| `templates/*.pptx` | Branded PowerPoint templates |
| `input/*.docx` | Input curriculum specification documents |
| `output/parsed_curriculum.json` | Stage 1 output |
| `output/research_notes.md` | Stage 2 output |
| `output/lesson_plan.md` | Stage 3 output |
| `output/day_slides.pptx` | Stage 4 output (final PPT) |
