# SESSION 2: “DASHBOARD IT & TELL IT”
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Duration:** 351 minutes
**Materials:** Laptops, projector, student handouts

## LEARNING TARGETS

1. Session 2 Contribution _(Bloom's: Apply)_
2. By the end of Session 2, students should be able to: _(Bloom's: Apply)_
3. Use VLOOKUP, INDEX-MATCH, and conditional formatting for analytical questions (LO #2) _(Bloom's: Apply)_
4. Build an interactive dashboard in Looker Studio that passes the 5-second test (LO #3) _(Bloom's: Create)_
5. Tell a data story using the Setup→Conflict→Resolution narrative arc (LO #7) _(Bloom's: Apply)_
6. Write a 1-page data-driven memo with a recommendation that an executive can act on (LO #6) _(Bloom's: Apply)_
7. Identify 5 common data fallacies and distinguish correlation from causation (LO #5) _(Bloom's: Remember)_
8. Explain basic GDPR principles relevant to data they collect and analyze (LO #9) _(Bloom's: Understand)_

## ASSESSMENT AT A GLANCE

**Look for:** Delivery: Data doesn’t speak for itself. Framework: Setup (context), Conflict (problem or surprise the data reveals), Resolution (what to do). Same structure as any story—but built from evidence. Students outline a data story from their dashboard using the framework.
**Formative:** CFU checks embedded in lesson flow (see blocks below)
**Exit Ticket:** See closing section

## LESSON FLOW

┌──────────────────────────────────────────────────────────┐
│ **10:00–10:15  Data Challenge (Retrieval)  (15 min)**
│ Whole Class | Bloom's: Remember / Understand | GRR: I Do
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Delivery: Unfamiliar mini-dataset.
│ • Build a pivot table + chart + 1-sentence English insight in 10 minutes.
│ • No notes.
│ • This is the hardest retrieval exercise in any ALC bootcamp because it tests tool mechanics, analytical reasoning, and English communication simultaneously.
│
│ **STUDENTS DO**
│ • _[Write what students type, produce, discuss, or build]_
│ • _[Include timed sub-steps if activity > 10 min]_
│
│ **PACING:** 0:00–7:00 — First half | 7:00–15:00 — Second half
│
│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_
│
│ **CHECK (Thumbs Up/Down):** _[CFU question tied to SWBAT]_
│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_
│ _use simpler example, pair struggling with proficient]_
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **10:15–10:50  Advanced Spreadsheet Functions  (35 min)**
│ Whole Class | Bloom's: Remember / Understand | GRR: I Do
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Format: Hands-on, follow-along.
│ • Bloom’s: Apply Delivery: VLOOKUP, INDEX-MATCH, conditional formatting.
│ • Each taught by answering a business question.
│ • VLOOKUP is notoriously confusing—teach it slowly with a visual diagram of how it searches.
│ • INDEX-MATCH presented as the “upgrade” for when VLOOKUP breaks.
│ • Conditional formatting: highlight cells that meet criteria (e.g., all sales below target in red).
│
│ **STUDENTS DO**
│ • _[Write what students type, produce, discuss, or build]_
│ • _[Include timed sub-steps if activity > 10 min]_
│
│ **PACING:** 0:00–17:00 — First half | 17:00–35:00 — Second half
│
│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_
│
│ **CHECK (Turn-and-Talk):** _[CFU question tied to SWBAT]_
│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_
│ _use simpler example, pair struggling with proficient]_
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **Min 0–12  Pacing: VLOOKUP (teach with diagram + follow along) =. INDEX-MATCH (teach as upgrade + practice) =. Conditional formatting =. Troubleshooting buffer =.  (12 min)**
│ Guided Practice | Bloom's: Understand / Apply | GRR: We Do
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • _[Write exact teacher actions, scripted language,_
│ _  questions in quotes, and what to demonstrate]_
│ • **Note:** Instructor note: VLOOKUP will confuse 40–50% of the room. Use a physical analogy: “It’s like looking up a word in a dictionary—you search column A and return what’s in column B.” Have the syntax projected: =VLOOKUP(what you’re looking for, where to look, which column to return, FALSE). Walk the room during practice.
│
│ **STUDENTS DO**
│ • _[Write what students type, produce, discuss, or build]_
│ • _[Include timed sub-steps if activity > 10 min]_
│
│ **PACING:** 0:00–6:00 — First half | 6:00–12:00 — Second half
│
│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_
│
│ **CHECK (Whiteboard Flash):** _[CFU question tied to SWBAT]_
│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_
│ _use simpler example, pair struggling with proficient]_
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **10:50–11:30  From Spreadsheet to Dashboard  |✆  (40 min)**
│ Whole Class | Bloom's: Understand / Apply | GRR: We Do
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Format: Instructor-led demo + guided follow-along.
│ • Bloom’s: Apply Delivery: Part 1 (12 min): Looker Studio orientation.
│ • Everyone opens Looker Studio.
│ • Tour the interface: data sources panel, chart types, filter controls, sharing settings.
│ • This is pure orientation—no building yet.
│ • Part 2 (25 min): Build a dashboard together from scratch.
│ • Connect the cleaned dataset from Session
│ • 1.
│ • Add one bar chart, one line chart, one scorecard, and one filter.
│ • Instructor does each step, students follow.
│ • Part 3 (3 min): Save and verify everyone has a working dashboard.
│
│ **STUDENTS DO**
│ • _[Write what students type, produce, discuss, or build]_
│ • _[Include timed sub-steps if activity > 10 min]_
│
│ **PACING:** 0:00–20:00 — First half | 20:00–40:00 — Second half
│
│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_
│
│ **CHECK (Exit Slip):** _[CFU question tied to SWBAT]_
│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_
│ _use simpler example, pair struggling with proficient]_
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **Min 12–24  Pacing: Interface orientation =. Guided build =. Save + verify =.  (12 min)**
│ Whole Class | Bloom's: Understand / Apply | GRR: We Do
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • _[Write exact teacher actions, scripted language,_
│ _  questions in quotes, and what to demonstrate]_
│
│ **STUDENTS DO**
│ • _[Write what students type, produce, discuss, or build]_
│ • _[Include timed sub-steps if activity > 10 min]_
│
│ **PACING:** 0:00–6:00 — First half | 6:00–12:00 — Second half
│
│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_
│
│ **CHECK (Think-Pair-Share):** _[CFU question tied to SWBAT]_
│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_
│ _use simpler example, pair struggling with proficient]_
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **11:30–11:45  Break  (15 min)**
│ Whole Class | Bloom's: Understand / Apply | GRR: We Do
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • _[Write exact teacher actions, scripted language,_
│ _  questions in quotes, and what to demonstrate]_
│
│ **STUDENTS DO**
│ • _[Write what students type, produce, discuss, or build]_
│ • _[Include timed sub-steps if activity > 10 min]_
│
│ **PACING:** 0:00–7:00 — First half | 7:00–15:00 — Second half
│
│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_
│
│ **CHECK (Fist-to-Five):** _[CFU question tied to SWBAT]_
│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_
│ _use simpler example, pair struggling with proficient]_
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **11:45–12:10  Dashboard Design Principles  (25 min)**
│ Whole Class | Bloom's: Apply / Analyze | GRR: You Do Together
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Format: Interactive lecture.
│ • Bloom’s: Understand + Evaluate Delivery: The “5-second test”: can someone understand the main message in 5 seconds?
│ • Visual hierarchy, “so what?” headlines (not “Sales by Region” but “Region X outperforms all others by 40%”), filter placement, color coding.
│ • Operational dashboards (daily monitoring) vs.
│ • strategic dashboards (quarterly insight).
│ • Insert interaction at midpoint: students look at their own dashboard and identify one headline they should rewrite.
│
│ **STUDENTS DO**
│ • _[Write what students type, produce, discuss, or build]_
│ • _[Include timed sub-steps if activity > 10 min]_
│
│ **PACING:** 0:00–12:00 — First half | 12:00–25:00 — Second half
│
│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_
│
│ **CHECK (Quick Write):** _[CFU question tied to SWBAT]_
│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_
│ _use simpler example, pair struggling with proficient]_
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **Min 24–34  Pacing: Design principles =. Examples (good vs. bad dashboards) =. Interaction: rewrite one headline on own dashboard =. Operational vs. strategic =. Transition =.  (10 min)**
│ Whole Class | Bloom's: Apply / Analyze | GRR: You Do Together
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • _[Write exact teacher actions, scripted language,_
│ _  questions in quotes, and what to demonstrate]_
│
│ **STUDENTS DO**
│ • _[Write what students type, produce, discuss, or build]_
│ • _[Include timed sub-steps if activity > 10 min]_
│
│ **PACING:** 0:00–5:00 — First half | 5:00–10:00 — Second half
│
│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_
│
│ **CHECK (Cold Call):** _[CFU question tied to SWBAT]_
│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_
│ _use simpler example, pair struggling with proficient]_
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **12:10–12:50  Build Your Dashboard  (40 min)**
│ Whole Class | Bloom's: Apply / Analyze | GRR: You Do Together
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Format: Individual, hands-on.
│ • Bloom’s: Create Delivery: Complete dashboard from your dataset.
│ • Minimum 4 visualizations, 1 filter, clear “so what?” headline per section.
│ • Focus: clarity over complexity.
│ • A simple dashboard answering a real question beats a complex one impressing nobody.
│
│ **STUDENTS DO**
│ • _[Write what students type, produce, discuss, or build]_
│ • _[Include timed sub-steps if activity > 10 min]_
│
│ **PACING:** 0:00–20:00 — First half | 20:00–40:00 — Second half
│
│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_
│
│ **CHECK (Thumbs Up/Down):** _[CFU question tied to SWBAT]_
│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_
│ _use simpler example, pair struggling with proficient]_
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **Min 34–69  Pacing: Build =. Save + prepare for gallery walk =.  (35 min)**
│ Whole Class | Bloom's: Apply / Analyze | GRR: You Do Together
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • _[Write exact teacher actions, scripted language,_
│ _  questions in quotes, and what to demonstrate]_
│
│ **STUDENTS DO**
│ • _[Write what students type, produce, discuss, or build]_
│ • _[Include timed sub-steps if activity > 10 min]_
│
│ **PACING:** 0:00–17:00 — First half | 17:00–35:00 — Second half
│
│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_
│
│ **CHECK (Turn-and-Talk):** _[CFU question tied to SWBAT]_
│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_
│ _use simpler example, pair struggling with proficient]_
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **12:50–1:10  Dashboard Gallery Walk + 5-Second Test  |✆  (20 min)**
│ Whole Class | Bloom's: Analyze / Create | GRR: You Do Alone
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • _[Write exact teacher actions, scripted language,_
│ _  questions in quotes, and what to demonstrate]_
│
│ **STUDENTS DO**
│ • _[Write what students type, produce, discuss, or build]_
│ • _[Include timed sub-steps if activity > 10 min]_
│
│ **PACING:** 0:00–10:00 — First half | 10:00–20:00 — Second half
│
│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_
│
│ **CHECK (Whiteboard Flash):** _[CFU question tied to SWBAT]_
│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_
│ _use simpler example, pair struggling with proficient]_
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **Min 69–71  Pacing: Setup + explain rotation =. 5 stations × 3.= 17.. Transition to lunch = 0..  (2 min)**
│ Whole Class | Bloom's: Analyze / Create | GRR: You Do Alone
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • _[Write exact teacher actions, scripted language,_
│ _  questions in quotes, and what to demonstrate]_
│
│ **STUDENTS DO**
│ • _[Write what students type, produce, discuss, or build]_
│ • _[Include timed sub-steps if activity > 10 min]_
│
│ **PACING:** 0:00–2:00 — Pacing: Setup + explain rotation =. 5 stations × 3.= 17.. Transition to lunch = 0..
│
│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_
│
│ **CHECK (Exit Slip):** _[CFU question tied to SWBAT]_
│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_
│ _use simpler example, pair struggling with proficient]_
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **1:10–2:10  Lunch  (60 min)**
│ Whole Class | Bloom's: Analyze / Create | GRR: You Do Alone
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • _[Write exact teacher actions, scripted language,_
│ _  questions in quotes, and what to demonstrate]_
│
│ **STUDENTS DO**
│ • _[Write what students type, produce, discuss, or build]_
│ • _[Include timed sub-steps if activity > 10 min]_
│
│ **PACING:** 0:00–30:00 — First half | 30:00–60:00 — Second half
│
│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_
│
│ **CHECK (Think-Pair-Share):** _[CFU question tied to SWBAT]_
│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_
│ _use simpler example, pair struggling with proficient]_
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **2:10–2:40  Data Storytelling: The Narrative Arc  (30 min)**
│ Whole Class | Bloom's: Analyze / Create | GRR: You Do Alone
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Format: Interactive lecture + individual outlining.
│ • Bloom’s: Analyze + Create
│
│ **STUDENTS DO**
│ • _[Write what students type, produce, discuss, or build]_
│ • _[Include timed sub-steps if activity > 10 min]_
│
│ **PACING:** 0:00–15:00 — First half | 15:00–30:00 — Second half
│
│ **TEACHER TIP:** _[Common mistake to watch for and how to address it]_
│
│ **CHECK (Fist-to-Five):** _[CFU question tied to SWBAT]_
│ If <25% pass → _[Specific reteach strategy: re-demonstrate,_
│ _use simpler example, pair struggling with proficient]_
└──────────────────────────────────────────────────────────┘

## DIFFERENTIATION NOTES

| Level | Strategy |
|-------|----------|
| **Struggling** | _[Scaffolds: sentence starters, step-by-step checklist, worked example]_ |
| **Advanced** | _[Extensions: open-ended challenge, teach a peer, real-world application]_ |
| **Language Support** | _[Visuals, vocabulary wall, bilingual glossary, simplified instructions]_ |

## CLOSING & EXIT TICKET

1. _[Question tied to SWBAT 1: "Session 2 Contribution"]_
2. _[Question tied to SWBAT 2: "By the end of Session 2, students should be able to:"]_
3. _[Question tied to SWBAT 3: "Use VLOOKUP, INDEX-MATCH, and conditional formatting for analytical questions (LO #2)"]_
4. _[Question tied to SWBAT 4: "Build an interactive dashboard in Looker Studio that passes the 5-second test (LO #3)"]_
5. _[Question tied to SWBAT 5: "Tell a data story using the Setup→Conflict→Resolution narrative arc (LO #7)"]_
6. _[Question tied to SWBAT 6: "Write a 1-page data-driven memo with a recommendation that an executive can act on (LO #6)"]_
7. _[Question tied to SWBAT 7: "Identify 5 common data fallacies and distinguish correlation from causation (LO #5)"]_
8. _[Question tied to SWBAT 8: "Explain basic GDPR principles relevant to data they collect and analyze (LO #9)"]_

## POST-SESSION REFLECTION

- [ ] What worked well?
- [ ] What needs adjustment for next time?
- [ ] Which students need follow-up or reteaching?
- [ ] Were all SWBATs met? Evidence?
