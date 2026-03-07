# Curriculum Researcher & Lesson Planner - Workflow Instructions

This directory contains a linear pipeline for building complete day-long curriculum packages from a source document. The pipeline produces two outputs: a detailed teacher lesson plan and a branded PowerPoint presentation.

## How to Use

1. Place the input `.docx` file in `input/`
2. Place the branded `.pptx` template in `templates/`
3. Follow the pipeline stages below IN ORDER. Each stage must complete before the next begins.

---

## Pipeline Overview

```
[1. PARSE] --> [2. RESEARCH] --> [3. LESSON PLAN] --> [4. PPT GENERATION]
```

**Every stage is sequential. Do not skip ahead or run stages in parallel.**

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
3. **Verify** the JSON output is complete and accurate before proceeding.
4. If the parser misses content or the .docx has unusual formatting, manually review the .docx and supplement the JSON.

**Checkpoint:** `output/parsed_curriculum.json` exists and contains all sections from the source document.

---

## Stage 2: RESEARCH Teaching Methods

**Goal:** For each content topic and SWBAT, research best practices for teaching that specific concept.

**Steps:**
1. Read `output/parsed_curriculum.json` to identify all content topics and SWBATs.
2. Read `skills.md` to understand the pedagogical framework requirements.
3. For each major content topic, use WebSearch to research:
   - Best practices for teaching that specific concept or skill
   - Common student misconceptions and how to address them
   - Effective activities and engagement strategies for the topic
   - Real-world applications and examples that connect to student experience
4. Compile research findings into `output/research_notes.md` organized by topic/SWBAT.
5. For each finding, note:
   - The source/basis of the recommendation
   - How it maps to the pedagogical principles in skills.md (Bloom's level, GRR phase, etc.)
   - Specific activity ideas with estimated timing
   - Potential misconceptions to watch for

**Checkpoint:** `output/research_notes.md` exists with research notes for every major content topic.

**Important:** Research should be targeted and practical. Focus on "how to teach X effectively" not general theory. Prioritize actionable strategies.

---

## Stage 3: GENERATE the Lesson Plan

**Goal:** Produce a comprehensive, minute-by-minute lesson plan for teachers.

**Steps:**
1. Read all three input files:
   - `output/parsed_curriculum.json` (structure and timing)
   - `output/research_notes.md` (teaching strategies)
   - `skills.md` (pedagogical framework)
2. Generate `output/lesson_plan.md` following the structure defined in skills.md Section 10. The lesson plan MUST include:

### Required Sections:
   a. **Header** - Day title, date placeholder, total duration
   b. **Materials & Preparation** - Complete list of everything needed, prep instructions
   c. **Standards/Objectives** - All SWBATs with Bloom's taxonomy level labeled
   d. **Assessment Plan** - Map each SWBAT to its formative/summative assessment
   e. **Lesson Sequence** - The core of the plan. For each timing block:
      - Exact timestamps matching the source document
      - Section title
      - GRR phase designation (I Do / We Do / You Do Together / You Do Alone)
      - **Teacher Actions**: Specific language, questions to ask, demonstrations to give
      - **Student Actions**: What students are doing during this time
      - **Materials/Slides**: Reference specific slide numbers
      - **CFU Checkpoint**: What to check, how to check it, what to do if students don't get it
   f. **Differentiation Notes** - Supports for struggling learners, extensions for advanced
   g. **Closure & Assessment** - Exit ticket or closing assessment with specific questions
   h. **Reflection Space** - Empty section for post-lesson notes

### Quality Rules:
- Follow Gradual Release of Responsibility within each content block
- Include a CFU checkpoint every 10-15 minutes minimum
- Follow the 10/2 rule (2 min processing per 10 min input)
- Include transitions with explicit teacher language
- Align every activity to a specific SWBAT
- Incorporate research findings from Stage 2 into activity design
- Build in buffer time (5-10 min per 90-min block)

**Checkpoint:** `output/lesson_plan.md` is complete, every SWBAT has instruction and assessment, and timing adds up correctly.

---

## Stage 4: GENERATE the Branded PPT

**Goal:** Create a polished PowerPoint presentation using the branded template.

**Steps:**
1. Read the completed lesson plan from `output/lesson_plan.md`.
2. Run the PPT generator:
   ```bash
   cd /home/user/AyElSeeMoldo/curriculum-planner
   python scripts/generate_pptx.py output/lesson_plan.md templates/<template_name>.pptx
   ```
3. The script generates `output/day_slides.pptx` with slides following this sequence:

### Slide Sequence (from skills.md Section 8):
   - **Title Slide** - Day/module name, date placeholder
   - **Objectives Slide** - All SWBATs in student-friendly language
   - **Content Slides** - One concept per slide, following the lesson sequence
   - **Activity Slides** - Clear numbered instructions, time limits, deliverables
   - **Discussion Slides** - Open-ended prompts in large font
   - **CFU/Check Slides** - Assessment questions at checkpoint moments
   - **Transition Slides** - Visual markers between major sections
   - **Summary Slide** - Key takeaways tied back to objectives

4. **Verify** the output:
   - Branding is preserved (fonts, colors, logo placement from template)
   - Slide count is reasonable (roughly 1 slide per 3-5 minutes of instruction)
   - Text fits within slide boundaries (no overflow)
   - Slide order matches lesson plan sequence exactly

**Checkpoint:** `output/day_slides.pptx` exists, opens correctly, and preserves template branding.

---

## Agent Coordination Rules

When using multiple Claude Code agents to handle different stages:

1. **Linear execution only** - Agent for Stage N must complete and produce its output file before Agent for Stage N+1 begins.
2. **File-based handoffs** - All inter-stage communication happens through files in `output/`. No agent should assume knowledge from a prior stage except through reading output files.
3. **skills.md is the shared reference** - Every agent reads skills.md. It is the single source of truth for pedagogical and design standards.
4. **Verify before proceeding** - Each agent checks that the previous stage's output file exists and is well-formed before starting its work.
5. **No backwards jumps** - If a problem is found in a later stage, note it in the output but do not go back and re-run earlier stages without user approval.

---

## File Reference

| File | Purpose |
|------|---------|
| `skills.md` | Pedagogical principles and design guidelines (READ-ONLY reference) |
| `CLAUDE.md` | This file - workflow instructions |
| `scripts/parse_docx.py` | Stage 1: Parse .docx to JSON |
| `scripts/generate_pptx.py` | Stage 4: Generate branded .pptx from lesson plan |
| `templates/*.pptx` | Branded PowerPoint templates |
| `input/*.docx` | Input curriculum specification documents |
| `output/parsed_curriculum.json` | Stage 1 output |
| `output/research_notes.md` | Stage 2 output |
| `output/lesson_plan.md` | Stage 3 output |
| `output/day_slides.pptx` | Stage 4 output (final PPT) |
