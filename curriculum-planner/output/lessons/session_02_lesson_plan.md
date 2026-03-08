# SESSION 2: “DASHBOARD IT & TELL IT”
============================================================

**Duration:** 465 minutes
**Materials:** Laptops, projector, student handouts, whiteboard markers

## LEARNING TARGETS

1. Use VLOOKUP, INDEX-MATCH, and conditional formatting for analytical questions (LO #2) _(Bloom's: Apply)_
2. Build an interactive dashboard in Looker Studio that passes the 5-second test (LO #3) _(Bloom's: Create)_
3. Tell a data story using the Setup→Conflict→Resolution narrative arc (LO #7) _(Bloom's: Apply)_
4. Write a 1-page data-driven memo with a recommendation that an executive can act on (LO #6) _(Bloom's: Create)_
5. Identify 5 common data fallacies and distinguish correlation from causation (LO #5) _(Bloom's: Remember)_
6. Explain basic GDPR principles relevant to data they collect and analyze (LO #9) _(Bloom's: Understand)_

## ASSESSMENT AT A GLANCE

**Look for:** Delivery: Data doesn’t speak for itself. Framework: Setup (context), Conflict (problem or surprise the data reveals), Resolution (what to do). Same structure as any story—but built from evidence. Students outline a data story from their dashboard using the framework.
**Formative:** CFU checks embedded every 10-15 minutes in lesson flow (see blocks below)
**Exit Ticket:** See closing section — one question per SWBAT

## LESSON FLOW

┌──────────────────────────────────────────────────────────┐
│ **10:00–10:15  Data Challenge (Retrieval)  (15 min)**
│ Whole Class | Bloom's: Remember / Understand | GRR: I Do
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Unfamiliar mini-dataset.
│ • Build a pivot table + chart + 1-sentence English insight in 10 minutes.
│ • No notes.
│ • This is the hardest retrieval exercise in any ALC bootcamp because it tests tool mechanics, analytical reasoning, and English communication simultaneously.
│
│ **STUDENTS DO**
│ • Build a pivot table + chart + 1-sentence English insight in 10 minutes.
│ • 0:00–7:00 — Work through the first part of the activity.
│ • 7:00–15:00 — Complete the activity and prepare to share/discuss.
│
│ **PACING:** 0:00–7:00 — First half | 7:00–15:00 — Second half
│
│ **TEACHER TIP:** This should feel slightly uncomfortable—that's the point of retrieval practice. Don't provide notes or references. The struggle is where learning happens.
│
│ **CHECK (Thumbs Up/Down):** Show students a chart with a truncated y-axis. Ask: "Is this chart trustworthy? What specifically makes it misleading, and how would you fix it?"
│ If <25% pass → Re-demonstrate with a simpler example. Then pair struggling students with proficient peers for guided practice. Check back in 3 minutes.
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **10:15–10:50  Advanced Spreadsheet Functions  (35 min)**
│ Whole Class | Bloom's: Remember / Understand | GRR: I Do
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Hands-on, follow-along.
│ • VLOOKUP, INDEX-MATCH, conditional formatting.
│ • Each taught by answering a business question.
│ • VLOOKUP is notoriously confusing—teach it slowly with a visual diagram of how it searches.
│ • INDEX-MATCH presented as the “upgrade” for when VLOOKUP breaks.
│ • Conditional formatting: highlight cells that meet criteria (e.g., all sales below target in red).
│
│ **STUDENTS DO**
│ • INDEX-MATCH presented as the “upgrade” for when VLOOKUP breaks.
│ • 0:00–17:00 — Work through the first part of the activity.
│ • 17:00–35:00 — Complete the activity and prepare to share/discuss.
│
│ **PACING:** 0:00–17:00 — First half | 17:00–35:00 — Second half
│
│ **TEACHER TIP:** VLOOKUP will confuse 40-50% of the room. Use the dictionary analogy: "You search column A to find a word, then return what's in column B." Keep the syntax on screen at all times.
│
│ **CHECK (Turn-and-Talk):** "When would you use FILTER instead of SORT to answer a business question? Give a specific example."
│ If <25% pass → Project the formula syntax on screen. Walk through each argument slowly: "This part says WHERE to look. This part says WHAT to return." Have students type it character by character.
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **10:50–11:30  From Spreadsheet to Dashboard  (40 min)**
│ Whole Class | Bloom's: Understand / Apply | GRR: We Do
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Instructor-led demo + guided follow-along.
│ • Part 1 (12 min): Looker Studio orientation.
│ • Everyone opens Looker Studio.
│ • Tour the interface: data sources panel, chart types, filter controls, sharing settings.
│ • This is pure orientation—no building yet.
│ • Part 2 (25 min): Build a dashboard together from scratch.
│ • Connect the cleaned dataset from Session 1.
│ • Add one bar chart, one line chart, one scorecard, and one filter.
│ • Instructor does each step, students follow.
│ • Part 3 (3 min): Save and verify everyone has a working dashboard.
│
│ **STUDENTS DO**
│ • This is pure orientation—no building yet.
│ • Part 2 (25 min): Build a dashboard together from scratch.
│ • Connect the cleaned dataset from Session 1.
│ • Instructor does each step, students follow.
│
│ **PACING:** 0:00–20:00 — First half | 20:00–40:00 — Second half
│
│ **TEACHER TIP:** Students will over-design. Remind them: "A simple dashboard that answers one question clearly beats a complex one that impresses nobody." Check for the 5-second test.
│
│ **CHECK (Whiteboard Flash):** Show students a chart with a truncated y-axis. Ask: "Is this chart trustworthy? What specifically makes it misleading, and how would you fix it?"
│ If <25% pass → Show a good dashboard and a bad dashboard side by side. Ask: "Which one passes the 5-second test? Why?" Then have students fix ONE element of their own dashboard.
└──────────────────────────────────────────────────────────┘

### 11:30–11:45  Break  (15 min)

> Use this time to circulate and check in with struggling students. A quick 1-minute conversation during break prevents 15 minutes of confusion later.

┌──────────────────────────────────────────────────────────┐
│ **11:45–12:10  Dashboard Design Principles  (25 min)**
│ Whole Class | Bloom's: Understand / Apply | GRR: We Do
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Interactive lecture.
│ • The “5-second test”: can someone understand the main message in 5 seconds?
│ • Visual hierarchy, “so what?” headlines (not “Sales by Region” but “Region X outperforms all others by 40%”), filter placement, color coding.
│ • Operational dashboards (daily monitoring) vs.
│ • strategic dashboards (quarterly insight).
│ • Insert interaction at midpoint: students look at their own dashboard and identify one headline they should rewrite.
│
│ **STUDENTS DO**
│ • Insert interaction at midpoint: students look at their own dashboard and identify one headline they should rewrite.
│ • 0:00–12:00 — Work through the first part of the activity.
│ • 12:00–25:00 — Complete the activity and prepare to share/discuss.
│
│ **PACING:** 0:00–12:00 — First half | 12:00–25:00 — Second half
│
│ **TEACHER TIP:** Students will over-design. Remind them: "A simple dashboard that answers one question clearly beats a complex one that impresses nobody." Check for the 5-second test.
│
│ **CHECK (Exit Slip):** "When would you use FILTER instead of SORT to answer a business question? Give a specific example."
│ If <25% pass → Show a good dashboard and a bad dashboard side by side. Ask: "Which one passes the 5-second test? Why?" Then have students fix ONE element of their own dashboard.
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **12:10–12:50  Build Your Dashboard  (40 min)**
│ Whole Class | Bloom's: Understand / Apply | GRR: We Do
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Individual, hands-on.
│ • Complete dashboard from your dataset.
│ • Minimum 4 visualizations, 1 filter, clear “so what?” headline per section.
│ • Focus: clarity over complexity.
│ • A simple dashboard answering a real question beats a complex one impressing nobody.
│
│ **STUDENTS DO**
│ • Complete dashboard from your dataset.
│ • 0:00–20:00 — Work through the first part of the activity.
│ • 20:00–40:00 — Complete the activity and prepare to share/discuss.
│
│ **PACING:** 0:00–20:00 — First half | 20:00–40:00 — Second half
│
│ **TEACHER TIP:** Students will over-design. Remind them: "A simple dashboard that answers one question clearly beats a complex one that impresses nobody." Check for the 5-second test.
│
│ **CHECK (Think-Pair-Share):** "When would you use FILTER instead of SORT to answer a business question? Give a specific example."
│ If <25% pass → Show a good dashboard and a bad dashboard side by side. Ask: "Which one passes the 5-second test? Why?" Then have students fix ONE element of their own dashboard.
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **12:50–1:10  Dashboard Gallery Walk + 5-Second Test  (20 min)**
│ Whole Class | Bloom's: Understand / Apply | GRR: We Do
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Introduce the Dashboard Gallery Walk + 5-Second Test activity and explain the objective.
│ • Demonstrate the key concept or skill, narrating each step.
│ • Circulate to check understanding and provide individual support.
│
│ **STUDENTS DO**
│ • Engage with the Dashboard Gallery Walk + 5-Second Test  |✆ activity as directed.
│ • 0:00–10:00 — Work through the first part of the activity.
│ • 10:00–20:00 — Complete the activity and prepare to share/discuss.
│
│ **PACING:** 0:00–10:00 — First half | 10:00–20:00 — Second half
│
│ **TEACHER TIP:** Students will over-design. Remind them: "A simple dashboard that answers one question clearly beats a complex one that impresses nobody." Check for the 5-second test.
│
│ **CHECK (Fist-to-Five):** "Look at your dashboard. Can someone understand the main message in 5 seconds? What would you change to make it clearer?"
│ If <25% pass → Show a good dashboard and a bad dashboard side by side. Ask: "Which one passes the 5-second test? Why?" Then have students fix ONE element of their own dashboard.
└──────────────────────────────────────────────────────────┘

### 1:10–2:10  Lunch  (60 min)

> Students return refreshed. Have the next activity's materials ready on screen when they sit down.

┌──────────────────────────────────────────────────────────┐
│ **2:10–2:40  Data Storytelling: The Narrative Arc  (30 min)**
│ Whole Class | Bloom's: Apply / Analyze | GRR: You Do Together
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Interactive lecture + individual outlining.
│
│ **STUDENTS DO**
│ • Work independently on the Data Storytelling: The Narrative Arc task.
│ • 0:00–15:00 — Work through the first part of the activity.
│ • 15:00–30:00 — Complete the activity and prepare to share/discuss.
│
│ **PACING:** 0:00–15:00 — First half | 15:00–30:00 — Second half
│
│ **TEACHER TIP:** Students tend to describe methodology instead of telling the story. Redirect: "Start with the surprise—what did the data reveal that you didn't expect?"
│
│ **CHECK (Quick Write):** "Take your most important finding and structure it as Setup → Conflict → Resolution. Share with your partner in 30 seconds."
│ If <25% pass → Re-demonstrate with a simpler example. Then pair struggling students with proficient peers for guided practice. Check back in 3 minutes.
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **2:40–3:10  “Explain It Like I’m the CEO”  (30 min)**
│ Whole Class | Bloom's: Apply / Analyze | GRR: You Do Together
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Pairs, role-play.
│ • Present findings to a “busy executive” who interrupts: “So what?” / “What do you want me to do?” / “I have 2 minutes.” Adapt: cut detail, lead with insight, end with the ask.
│ • Switch roles.
│ • Debrief: What got cut?
│ • What survived?
│ • That's what matters.
│
│ **STUDENTS DO**
│ • Present findings to a “busy executive” who interrupts: “So what?” / “What do you want me to do?” / “I have 2 minutes.” Adapt: cut detail, lead with insight, end with the ask.
│ • 0:00–15:00 — Work through the first part of the activity.
│ • 15:00–30:00 — Complete the activity and prepare to share/discuss.
│
│ **PACING:** Setup + rules = 3 min. Partner A presents + CEO interruptions = 5 min. Feedback = 2 min. Switch roles = 5 min + 2 min feedback. New partner, faster round = 8 min. Debrief = 5 min.
│
│ **TEACHER TIP:** Students will over-trust AI output. Require them to document at least one discrepancy between AI analysis and their own findings.
│
│ **CHECK (Cold Call):** "You uploaded data to an AI and it found 'a strong correlation between X and Y.' What 2 things should you verify before including this in your report?"
│ If <25% pass → Re-demonstrate with a simpler example. Then pair struggling students with proficient peers for guided practice. Check back in 3 minutes.
└──────────────────────────────────────────────────────────┘

### 3:10–3:25  Break  (15 min)

> Use this time to circulate and check in with struggling students. A quick 1-minute conversation during break prevents 15 minutes of confusion later.

┌──────────────────────────────────────────────────────────┐
│ **3:25–4:05  The Data-Driven Memo  (40 min)**
│ Whole Class | Bloom's: Apply / Analyze | GRR: You Do Together
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Mini-lecture + individual writing.
│ • One-line recommendation at top.
│ • 3–4 supporting data points with charts.
│ • Risks and limitations.
│ • Next steps.
│ • Not a report—a decision document.
│ • The reader knows what to do from the first paragraph.
│ • Students write a 1-page memo in English.
│
│ **STUDENTS DO**
│ • Students write a 1-page memo in English.
│ • 0:00–20:00 — Work through the first part of the activity.
│ • 20:00–40:00 — Complete the activity and prepare to share/discuss.
│
│ **PACING:** Teach structure + before/after example = 10 min. Students write memo = 25 min (dual-skill buffer for English writing). Quick pair check (“Can you act on this from the first paragraph?”) = 5 min.
│
│ **TEACHER TIP:** Students will bury the recommendation at the end. Check: "Can I act on this from the first paragraph?" If not, they need to restructure.
│
│ **CHECK (Thumbs Up/Down):** Show students a chart with a truncated y-axis. Ask: "Is this chart trustworthy? What specifically makes it misleading, and how would you fix it?"
│ If <25% pass → Re-demonstrate with a simpler example. Then pair struggling students with proficient peers for guided practice. Check back in 3 minutes.
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **4:05–4:20  Data Fallacy Spotter  (15 min)**
│ Whole Class | Bloom's: Analyze / Create | GRR: You Do Alone
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Full group, rapid exercise.
│ • Beyond correlation/causation: survivorship bias, Simpson's paradox, base rate neglect, anchoring.
│ • 5 examples, students identify the fallacy.
│ • Fast-paced.
│ • The critical thinking that separates data literacy from data naivety.
│
│ **STUDENTS DO**
│ • 5 examples, students identify the fallacy.
│ • 0:00–7:00 — Work through the first part of the activity.
│ • 7:00–15:00 — Complete the activity and prepare to share/discuss.
│
│ **PACING:** 5 examples × 2.5 min each (present + vote + explain) = 12.5 min. Wrap-up = 2.5 min.
│
│ **TEACHER TIP:** Use the funny spurious correlations first to set a light tone, then transition to the real business examples where correlation-as-causation cost money.
│
│ **CHECK (Turn-and-Talk):** "Ice cream sales and drowning deaths both increase in summer. Is this correlation or causation? How would you test it?"
│ If <25% pass → Re-demonstrate with a simpler example. Then pair struggling students with proficient peers for guided practice. Check back in 3 minutes.
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **4:20–4:50  Correlation vs. Causation Workshop  (30 min)**
│ Whole Class | Bloom's: Analyze / Create | GRR: You Do Alone
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Group exercise.
│ • 5 spurious correlations (funny) + 5 real business examples where correlation was mistaken for causation (and it cost money).
│ • Students analyze 3 claims from their own data: correlation or causation?
│ • How would you test it?
│
│ **STUDENTS DO**
│ • Students analyze 3 claims from their own data: correlation or causation?
│ • 0:00–15:00 — Work through the first part of the activity.
│ • 15:00–30:00 — Complete the activity and prepare to share/discuss.
│
│ **PACING:** Spurious correlations (fun, fast) = 5 min. Real business examples = 8 min. Students analyze 3 own-data claims = 10 min. Discussion = 5 min. Transition = 2 min.
│
│ **TEACHER TIP:** Use the funny spurious correlations first to set a light tone, then transition to the real business examples where correlation-as-causation cost money.
│
│ **CHECK (Whiteboard Flash):** "Ice cream sales and drowning deaths both increase in summer. Is this correlation or causation? How would you test it?"
│ If <25% pass → Re-demonstrate with a simpler example. Then pair struggling students with proficient peers for guided practice. Check back in 3 minutes.
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **4:50–5:10  GDPR & Data Privacy Basics  (20 min)**
│ Whole Class | Bloom's: Analyze / Create | GRR: You Do Alone
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Interactive lecture.
│ • What GDPR means for data you collect and analyze.
│ • What can you share?
│ • What must you anonymize?
│ • When do you need consent?
│ • Essential for Moldova (EU accession) and anyone working with EU-funded projects.
│
│ **STUDENTS DO**
│ • What GDPR means for data you collect and analyze.
│ • What can you share?
│ • 0:00–10:00 — Work through the first part of the activity.
│ • 10:00–20:00 — Complete the activity and prepare to share/discuss.
│
│ **PACING:** Core GDPR principles = 10 min. Practical scenarios (“Can you put this in your dashboard?”) = 7 min. Q&A = 3 min.
│
│ **TEACHER TIP:** Students may think GDPR doesn't apply to them. Emphasize: if you work with EU-funded projects or EU citizens' data, GDPR applies regardless of where you are.
│
│ **CHECK (Exit Slip):** "A colleague wants to include individual customer names in a public dashboard. What GDPR principle applies, and what should they do instead?"
│ If <25% pass → Re-demonstrate with a simpler example. Then pair struggling students with proficient peers for guided practice. Check back in 3 minutes.
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ **5:10–5:45  Day 2 Wrap + Mid-Week Assignment  (35 min)**
│ Whole Class | Bloom's: Analyze / Create | GRR: You Do Alone
├──────────────────────────────────────────────────────────┤
│
│ **TEACHER DOES**
│ • Introduce the Day 2 Wrap + Mid-Week Assignment activity and explain the objective.
│ • Demonstrate the key concept or skill, narrating each step.
│ • Circulate to check understanding and provide individual support.
│
│ **STUDENTS DO**
│ • Engage with the Day 2 Wrap + Mid-Week Assignment activity as directed.
│ • 0:00–17:00 — Work through the first part of the activity.
│ • 17:00–35:00 — Complete the activity and prepare to share/discuss.
│
│ **PACING:** Data confidence self-assessment (compare to Day 1) = 5 min. 2–3 students share growth observations = 5 min. Mid-week assignment walkthrough (5 steps, with template on screen) = 15 min. Questions + logistics = 10 min. Pacing: VLOOKUP (teach with diagram + follow along) =. INDEX-MATCH (teach as upgrade + practice) =. Conditional formatting =. Troubleshooting buffer =. Pacing: Interface orientation =. Guided build =. Save + verify =. Pacing: Design principles =. Examples (good vs. bad dashboards) =. Interaction: rewrite one headline on own dashboard =. Operational vs. strategic =. Transition =. Pacing: Build =. Save + prepare for gallery walk =. Pacing: Setup + explain rotation =. 5 stations × 3.= 17.. Transition to lunch = 0..
│
│ **TEACHER TIP:** Don't rush the self-assessment. Students comparing Day 1 to today need time to reflect—this metacognition is part of the learning.
│
│ **CHECK (Think-Pair-Share):** "Based on what we just covered: Can you use vlookup, index-match, and conditional formatting for analytical questions? Demonstrate to your partner."
│ If <25% pass → Re-demonstrate with a simpler example. Then pair struggling students with proficient peers for guided practice. Check back in 3 minutes.
└──────────────────────────────────────────────────────────┘

## DIFFERENTIATION NOTES

| Level | Strategy |
|-------|----------|
| **Struggling** | Give a formula reference card with syntax + example for each function; Provide a dashboard template with placeholder charts already positioned |
| **Advanced** | Add calculated fields or custom metrics to the dashboard beyond the minimum requirements; Mentor a struggling peer (teaching deepens understanding) |
| **Language Support** | Vocabulary wall with key data terms in English + local language; sentence frames for data briefs and presentations; bilingual glossary handout (data literacy, pivot table, correlation, dashboard, KPI); allow draft writing in L1 before translating to English |

## CLOSING & EXIT TICKET

1. "When does INDEX-MATCH work better than VLOOKUP? Give one specific scenario."
2. "What 3 elements must every dashboard have to pass the 5-second test?"
3. "Structure this finding as Setup → Conflict → Resolution: 'Sales dropped 30% in Q3.'"
4. "Write the first sentence of a data memo that an executive can act on immediately."
5. "A report claims: 'Stores that play music sell more products, therefore music causes purchases.' Identify the fallacy and suggest how to test the claim."
6. "Name 2 types of data that must be anonymized before including in a shared dashboard under GDPR."

## POST-SESSION REFLECTION

- [ ] What worked well?
- [ ] What needs adjustment for next time?
- [ ] Which students need follow-up or reteaching?
- [ ] Were all SWBATs met? Evidence?
