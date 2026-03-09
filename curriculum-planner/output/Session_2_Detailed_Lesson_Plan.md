# SESSION 2: "Dashboard It & Tell It"

**Sunday, Weekend 1 | 10:00 AM – 5:45 PM**
**Theme:** Build interactive dashboards, present data to non-technical audiences, write memos that move decisions.

---

## Learning Targets

By the end of this session, students will be able to:

1. **Use** VLOOKUP, INDEX-MATCH, and conditional formatting for analytical questions (Bloom's: Apply)
2. **Build** an interactive dashboard in Looker Studio that passes the 5-second test (Bloom's: Create)
3. **Tell** a data story using the Setup→Conflict→Resolution narrative arc (Bloom's: Apply)
4. **Write** a 1-page data-driven memo with a recommendation that an executive can act on (Bloom's: Create)
5. **Identify** 5 common data fallacies and distinguish correlation from causation (Bloom's: Analyze)
6. **Explain** basic GDPR principles relevant to data they collect and analyze (Bloom's: Understand)

---

## Materials & Setup

- Laptops with WiFi (Google Sheets + Looker Studio access required)
- Google accounts with Looker Studio enabled (https://lookerstudio.google.com)
- Students' cleaned datasets from Day 1 (or the pre-prepared datasets for those who missed Day 1)
- Pre-prepared mini-dataset for the Data Challenge (new, unfamiliar — not from Day 1)
- 5 "data fallacy" scenario cards (printed, 1 set per table)
- 5 spurious correlation examples (projected — funny ones from tylervigen.com)
- 5 real business examples of correlation ≠ causation
- Printed data-driven memo template (1 per student)
- Printed dashboard design checklist (1 per student)
- Slides deck (Session 2)
- Whiteboard + markers
- Timer (visible)

---

## Assessment at a Glance

| Method | Description |
|--------|-------------|
| **Formative** | Observe VLOOKUP formula construction. Check dashboards during gallery walk (5-second test). Listen to CEO role-play presentations for clarity. |
| **Self-Assessment** | Data confidence rating (1–5) across 4 dimensions — compare to Day 1 baseline. |
| **Exit Ticket** | 1-page data-driven memo with actionable recommendation. |
| **Evidence to look for** | Dashboards have "so what?" headlines (not generic labels). Memos lead with the recommendation, not the methodology. Students can name at least 3 data fallacies. CEO role-play presentations get to the point in under 2 minutes. |

---

## MORNING BLOCK (10:00–1:10)

---

### 10:00–10:15 | Data Challenge (Retrieval) (15 min)

**Format:** Individual, timed | **GRR Phase:** You Do Alone | **Bloom's:** Apply

#### TEACHER DOES

> **SAY:** "Good morning. No warm-up today — we're starting with a challenge. You have 10 minutes. Here's a dataset you've never seen before."

- **Project the link** to a new mini-dataset (30–50 rows — e.g., a small café's monthly sales across 4 products and 3 locations).

> **SAY:** "Build a pivot table, create one chart, and write a 1-sentence insight in English. 10 minutes. No notes, no asking your neighbor. Go."

- Start the timer. Circulate silently. Note who remembers pivot table mechanics vs. who's stuck.

> **SAY (at 10 min):** "Stop. Hands off keyboards."

> **SAY:** "Raise your hand if you finished all three — pivot table, chart, and insight." Count hands.

> **SAY:** "Raise your hand if you got the pivot table but ran out of time on the chart or insight." Count.

> **SAY:** "This is retrieval practice. It's supposed to be hard. The fact that some of you froze on the pivot table after building 5 yesterday? That's normal — it means the skill isn't automatic yet. It will be by Day 4."

#### STUDENTS DO

- Open unfamiliar dataset
- Build a pivot table answering a business question
- Create one chart from the pivot table
- Write a 1-sentence English insight
- All within 10 minutes, no notes

#### Pacing

| Segment | Time |
|---------|------|
| Instructions + distribute link | 2 min |
| Timed challenge | 10 min |
| Debrief (count hands, normalize struggle) | 3 min |

#### Teacher Tip

> This is intentionally stressful. The point is spaced retrieval — forcing recall strengthens long-term retention. Don't help during the 10 minutes. The struggle IS the learning.

#### Check for Understanding

**Observation:** Count how many students complete all 3 tasks. Compare to Day 3's challenge for growth data.
**If <30% finish:** The Day 1 content didn't stick. Consider a 5-minute pivot table refresher before moving on.

---

### 10:15–10:50 | Advanced Spreadsheet Functions (35 min)

**Format:** Hands-on, follow-along | **GRR Phase:** I Do → We Do → You Do | **Bloom's:** Apply

#### TEACHER DOES

**Function 1: VLOOKUP (12 min)**

> **SAY:** "Yesterday you learned SUMIF and COUNTIF. Today we level up. VLOOKUP is the function that lets you connect two different tables — like looking up a customer's name in one table and pulling their email from another."

> **SAY:** "Here's the analogy: VLOOKUP works like a dictionary. You look up a word in column A, and it returns what's in column D of the same row. You're searching the first column and retrieving from another."

- **Draw on whiteboard:**
```
Table 1: Orders          Table 2: Customers
Order ID | Customer ID   Customer ID | Name | Email | Region
1001     | C-045         C-045       | Ana  | ana@  | Chișinău
1002     | C-112         C-112       | Giorgi| g@   | Tbilisi
```

> **SAY:** "I want to add the customer name to my orders table. Watch."

- **Demo live:**
```
=VLOOKUP(B2, Customers!A:D, 2, FALSE)
```

> **SAY:** "Four parts: what to look up (B2 — the customer ID), where to look (the Customers table), which column to return (2 — the name column), and FALSE means exact match only. Always use FALSE."

- **Write on whiteboard:**
```
=VLOOKUP(what_to_find, where_to_look, which_column, FALSE)
```

> **SAY:** "Your turn. Add customer names to your orders using VLOOKUP. 3 minutes."

- Circulate. Common errors: wrong table range, wrong column number, forgetting FALSE.

**Function 2: INDEX-MATCH (10 min)**

> **SAY:** "VLOOKUP has a weakness: it can only search the first column and look right. INDEX-MATCH is the upgrade — it can search any column and return from any other column."

- **Demo:**
```
=INDEX(Customers!B:B, MATCH(B2, Customers!A:A, 0))
```

> **SAY:** "MATCH finds which row the customer ID is in. INDEX returns the value from that row in the name column. Think of MATCH as the detective (finds the row) and INDEX as the retriever (grabs the answer)."

> **SAY:** "Try it. Replace one of your VLOOKUPs with INDEX-MATCH. Same result, more flexible."

**Function 3: Conditional Formatting (7 min)**

> **SAY:** "Last one — visual. Conditional formatting colors your cells automatically based on rules. Want to see all orders over 1,000 in green? All negative values in red?"

- **Demo:** Select revenue column → Format → Conditional formatting → "Greater than 1000" → Green fill.

> **SAY:** "Add 2 conditional formatting rules to your data. One for high values, one for low values. Make your spreadsheet tell the story visually."

**Troubleshooting (6 min):**

> **SAY:** "Who's stuck? Let's fix it together."

- Address common VLOOKUP errors on screen. Show the #N/A error: "This means your lookup value doesn't exist in the other table. Check for spelling or formatting differences — remember data cleaning from yesterday?"

#### STUDENTS DO

- Follow along with VLOOKUP demo, then practice on their own data
- Follow along with INDEX-MATCH, replace one VLOOKUP
- Add 2 conditional formatting rules
- Troubleshoot errors with instructor support
- **Good work:** Student uses VLOOKUP to connect two related datasets and adds conditional formatting to highlight outliers
- **Needs help:** #N/A errors everywhere → check that lookup values match exactly (case, spacing, special characters)

#### Pacing

| Segment | Time |
|---------|------|
| VLOOKUP (teach with diagram + follow along) | 12 min |
| INDEX-MATCH (teach as upgrade + practice) | 10 min |
| Conditional formatting | 7 min |
| Troubleshooting buffer | 6 min |

#### Teacher Tip

> VLOOKUP will confuse 40–50% of the room. Use the dictionary analogy relentlessly. Draw the arrow on the whiteboard: "You search HERE and retrieve from THERE." When students get #N/A, walk them to the data and say: "Find this value with your eyes first. Is it actually there?"

#### Check for Understanding

**Show Me (after VLOOKUP):** "Show me your VLOOKUP formula. Point to which part is the lookup value, which is the table, and which is the column number."
**If >30% can't identify the parts:** Re-demo with a different example. Don't move to INDEX-MATCH until VLOOKUP is solid.

#### Differentiation

- **Struggling learners:** Skip INDEX-MATCH. Master VLOOKUP only — it covers 90% of use cases.
- **Advanced learners:** Show XLOOKUP (the modern replacement in newer Google Sheets): `=XLOOKUP(B2, Customers!A:A, Customers!B:B)` — simpler syntax.
- **Language support:** "Look up = a căuta. Column = coloană. Match = potrivire. Return = a returna."

---

### 10:50–11:30 | From Spreadsheet to Dashboard (40 min)

**Format:** Instructor-led demo + guided follow-along | **GRR Phase:** I Do → We Do | **Bloom's:** Apply

#### TEACHER DOES

**Part 1: Looker Studio Orientation (12 min)**

> **SAY:** "Everything you've done so far lives in a spreadsheet. That's great for analysis — but when your boss asks 'how are we doing?', you don't send them a spreadsheet. You send them a dashboard. Today you're building one."

> **SAY:** "Open Looker Studio — lookerstudio.google.com. Sign in with your Google account."

- Wait for everyone to get in. Troubleshoot access issues.

> **SAY:** "Let me give you the tour."

- **Demo on screen:** Walk through the interface:
  - Left panel: data sources
  - Top bar: add charts, add filters, add text
  - Canvas: where you drag and arrange elements
  - Share button: how to make dashboards public or share with specific people

> **SAY:** "First, connect your data. Click 'Add data' → Google Sheets → select your cleaned dataset from yesterday."

- Walk everyone through the connection. Wait for all students to see their data in Looker Studio.

**Part 2: Guided Build (25 min)**

> **SAY:** "Now we build together. Step by step."

**Step 1: Add a chart**
- Demo: Click "Add a chart" → Bar chart → drag the dimension (Region) and metric (Revenue, SUM)

> **SAY:** "Your turn. Add a bar chart showing revenue by region. Or by product category — your choice."

**Step 2: Add a filter**
- Demo: Click "Add a control" → Drop-down → set to Region

> **SAY:** "Now anyone viewing your dashboard can filter by region. Try it — click the dropdown and select one region."

**Step 3: Add a headline**
- Demo: Add a text box. Type: "Chișinău generates 45% of total revenue — 3x more than any other region."

> **SAY:** "This is NOT a label. This is a 'so what?' headline. It tells the viewer the insight, not just the category. Not 'Revenue by Region' — but 'Chișinău dominates with 45% of revenue.'"

**Step 4: Add a second chart**
- Demo: Add a time series (line chart) showing revenue over time.

> **SAY:** "Add one more chart. Any type. Then save your dashboard."

#### STUDENTS DO

- Open Looker Studio and connect their dataset
- Follow along: add bar chart, add filter, add headline, add time series
- Save their dashboard
- **Good dashboard:** Has at least 2 charts, 1 filter, and a "so what?" headline that states an insight
- **Needs work:** Charts are there but the text box just says "Revenue" → Coach: "What does this chart TELL us? Put that in the headline."

#### Pacing

| Segment | Time |
|---------|------|
| Interface orientation | 12 min |
| Guided build: first chart | 7 min |
| Guided build: filter + headline | 8 min |
| Guided build: second chart | 7 min |
| Save + verify | 3 min |
| Buffer | 3 min |

#### Teacher Tip

> Looker Studio can be slow on weak WiFi. Have students work in pairs on one laptop if connectivity is an issue. The learning objective is dashboard thinking, not tool proficiency — if Looker Studio crashes, they can sketch their dashboard on paper and discuss the design.

#### Check for Understanding

**Quick scan:** "Everyone hold up your laptops. I want to see a dashboard with at least 2 charts and a headline." Walk the room.
**If >25% are stuck on data connection:** Stop and do a group troubleshooting session. The most common issue is selecting the wrong Google Sheet or the wrong tab.

---

### 11:30–11:45 | Break (15 min)

> ☕ **BREAK** — "After break: dashboard design principles, then you build your real dashboard."

---

### 11:45–12:10 | Dashboard Design Principles (25 min)

**Format:** Interactive lecture | **GRR Phase:** I Do → We Do | **Bloom's:** Understand → Apply

#### TEACHER DOES

> **SAY:** "You've got a working dashboard. Now let's make it good. The test is simple: can someone understand the main message in 5 seconds?"

> **SAY:** "This is called the 5-second test. I'm going to show you some dashboards. You get 5 seconds to look. Then I'll ask: what was the main message?"

- **Show Dashboard A** (bad): Cluttered, 8 charts, no headlines, rainbow colors, no hierarchy. Show for 5 seconds.

> **SAY:** "What was the main message?" Students will struggle. "Exactly. There IS no main message. That's the problem."

- **Show Dashboard B** (good): Clean, 3 charts, one bold headline at top, consistent colors, clear visual hierarchy. Show for 5 seconds.

> **SAY:** "What was the main message?" Students will answer quickly. "See the difference? That's design."

**Project the 5 principles:**

```
1. THE 5-SECOND TEST: Main message obvious in 5 seconds
2. "SO WHAT?" HEADLINES: Not "Sales by Region" but
   "Region X outperforms all others by 40%"
3. VISUAL HIERARCHY: Most important chart is biggest and top-left
4. FILTER PLACEMENT: Filters at top, not buried
5. LESS IS MORE: 3–4 charts max. If you need more, make a second page.
```

> **SAY:** "Two types of dashboards:"

```
OPERATIONAL: Updated frequently, used daily, answers "how are we doing right now?"
STRATEGIC:   Updated monthly/quarterly, used by leadership, answers "where should we invest?"
```

> **SAY:** "Quick exercise: look at your dashboard from the guided build. Rewrite your headline to pass the 'so what?' test. You have 5 minutes."

#### STUDENTS DO

- Watch the 5-second test comparison (bad vs. good dashboard)
- Learn the 5 design principles
- Rewrite their dashboard headline to be a "so what?" headline
- Identify whether their dashboard is operational or strategic
- **Good headline rewrite:** From "Monthly Revenue" to "Revenue dropped 15% in October — the first decline in 6 months"
- **Still generic:** "Revenue Overview" → Push: "What does the data SAY? Put the number in the headline."

#### Pacing

| Segment | Time |
|---------|------|
| 5-second test examples | 5 min |
| 5 design principles | 5 min |
| Operational vs. strategic distinction | 3 min |
| Students rewrite headline | 5 min |
| 2–3 students share rewrites | 5 min |
| Transition | 2 min |

#### Teacher Tip

> The headline rewrite is the single highest-leverage exercise in this block. A dashboard with a strong headline communicates even if the charts are mediocre. Push hard here.

#### Check for Understanding

**Turn and talk:** "Read your new headline to your partner. Can they tell you the main insight without looking at the dashboard?" If yes, it passes.

---

### 12:10–12:50 | Build Your Dashboard (40 min)

**Format:** Individual, hands-on | **GRR Phase:** You Do Alone | **Bloom's:** Create

#### TEACHER DOES

> **SAY:** "Now build your real dashboard. Use your cleaned dataset from Day 1 — or the data from your mid-week assignment if you brought it. Requirements:"

**Project:**
```
MINIMUM:
✓ 4 visualizations (mix of chart types)
✓ 1 interactive filter
✓ "So what?" headline for each section
✓ Passes the 5-second test

BONUS:
✓ Consistent color scheme
✓ Logical layout (most important top-left)
✓ Second page for detail view
```

> **SAY:** "You have 35 minutes. I'll come around to check on each of you."

- **Circulate.** For each student, check:
  - Do headlines state insights (not labels)?
  - Is the layout clean or cluttered?
  - Do chart types match the data? (Bar for comparison, line for trends)
  - Is there at least one filter?

> **SAY (at 30 min):** "5 minutes left. Save your work and prepare for the gallery walk."

#### STUDENTS DO

- Build a complete dashboard in Looker Studio (35 min)
- Apply design principles from the previous block
- Save and prepare to share

#### Pacing

| Segment | Time |
|---------|------|
| Build dashboard | 35 min |
| Save + prepare for gallery walk | 5 min |

#### Teacher Tip

> Resist the urge to build it for them. If a student is stuck on chart selection, ask: "What are you trying to show — a comparison, a trend, or a relationship?" Let them choose the chart type from that.

#### Check for Understanding

**Individual check-ins:** Visit every student at least once during the 35 minutes. Give one specific piece of feedback: "This chart is great — now add a headline that tells me the insight."

#### Differentiation

- **Struggling learners:** Reduce to 2 charts + 1 filter + 1 headline. Quality over quantity.
- **Advanced learners:** Add a calculated field (e.g., revenue per order) or a blended data source.
- **Language support:** Headlines can be drafted in L1 first, then translated to English.

---

### 12:50–1:10 | Dashboard Gallery Walk + 5-Second Test (20 min)

**Format:** Rotating stations | **GRR Phase:** You Do Together | **Bloom's:** Evaluate

#### TEACHER DOES

> **SAY:** "Leave your dashboard open on your laptop. Stand up. You're going to walk around the room and visit 5 other dashboards. At each one, you have 5 seconds to look — then write on a sticky note: 'The main message is ___.' Leave the sticky note on their desk."

> **SAY:** "After you've visited 5, go back to your own desk and read what people wrote. Did they get your main message? If not, your dashboard needs work."

- Set a timer: 3.5 minutes per station. Ring a bell to rotate.

> **SAY (after all rotations):** "Raise your hand if every person got your main message right." (Some hands.) "Raise your hand if at least one person got it wrong." (More hands.) "That's the 5-second test in action. If one person misread it, imagine what happens when your CEO looks at it between meetings."

#### STUDENTS DO

- Walk to 5 different dashboards
- At each: look for 5 seconds, then write the main message on a sticky note
- Return to own desk and read feedback
- Identify whether their message was clear

#### Pacing

| Segment | Time |
|---------|------|
| Setup + explain rotation | 2 min |
| 5 stations × 3.5 min | 17.5 min |
| Transition to lunch | 0.5 min |

#### Teacher Tip

> This is one of the most powerful exercises in the entire bootcamp. The feedback is peer-generated and honest. Students who thought their dashboard was clear will discover it wasn't — and that's the lesson.

---

### 1:10–2:10 | Lunch (60 min)

> 🍽 **LUNCH** — "This afternoon: data storytelling, the CEO role-play, memo writing, and critical thinking. The communication half of data literacy."

---

## AFTERNOON BLOCK (2:10–5:45)

---

### 2:10–2:40 | Data Storytelling: The Narrative Arc (30 min)

**Format:** Interactive lecture + individual outlining | **GRR Phase:** I Do → We Do → You Do | **Bloom's:** Apply

#### TEACHER DOES

> **SAY:** "Data doesn't speak for itself. You have to tell its story. And every good story — whether it's a movie, a book, or a data presentation — has the same structure."

**Project the narrative arc:**

```
1. SETUP      → What's the context? What were we expecting?
2. CONFLICT   → What did the data reveal? What's the surprise or problem?
3. RESOLUTION → What should we do about it? What's the recommendation?
```

> **SAY:** "Let me show you."

**Worked example:**

> "SETUP: Our NGO runs youth employment programs in 3 regions. We expected similar completion rates across all of them."

> "CONFLICT: But the data shows that Region C has a 25% completion rate — half the rate of Regions A and B. And Region C is where we spend the most money."

> "RESOLUTION: We need to investigate why Region C is underperforming. I recommend site visits, exit interviews with dropouts, and a comparison of program delivery methods across regions."

> **SAY:** "See how that's a story, not a data dump? The setup creates expectations. The conflict breaks them. The resolution gives the audience something to do."

> **SAY:** "Now outline YOUR data story. Use the data from your dashboard. Setup → Conflict → Resolution. You have 12 minutes."

- Circulate. Watch for:
  - Students who skip the setup and jump to data → "Set the scene first. What was expected?"
  - Students whose conflict is weak ("the data was interesting") → "What was the SURPRISE? What broke expectations?"
  - Students whose resolution is vague ("we should look into it") → "Look into WHAT, specifically? What's the first action?"

> **SAY (after 12 min):** "Two volunteers — read your story arc to the class."

#### STUDENTS DO

- Learn the Setup → Conflict → Resolution framework
- Outline their own data story using their dashboard data (12 min)
- 2 students share outlines with the class (4 min)
- Give feedback on whether the conflict was surprising and the resolution was actionable

#### Pacing

| Segment | Time |
|---------|------|
| Teach framework + worked example | 12 min |
| Students outline data story | 12 min |
| 2 students share outlines | 4 min |
| Transition | 2 min |

#### Teacher Tip

> The narrative arc is the bridge between data analysis and data communication. Students who can do Setup → Conflict → Resolution will nail the CEO role-play, the memo, and the Day 4 capstone. Spend time here.

#### Check for Understanding

**Cold call:** "Levan, what's your conflict — what surprised you in the data?" The answer should be specific and data-backed.
**If the answer is vague:** "Give me a number. What did you expect vs. what did you find?"

---

### 2:40–3:10 | "Explain It Like I'm the CEO" (30 min)

**Format:** Pairs, role-play | **GRR Phase:** You Do Together | **Bloom's:** Apply → Evaluate

#### TEACHER DOES

> **SAY:** "You have a data story. Now you need to present it to someone who doesn't care about your process — they care about the answer. Let's role-play."

> **SAY:** "Partner A: you're the analyst. Present your findings in 2 minutes. Partner B: you're the CEO. Your job is to interrupt with these questions:"

**Project the CEO interruptions:**
```
"So what?"
"What do you want me to do?"
"I have 2 minutes. Get to the point."
"How confident are you in this number?"
"What are you NOT telling me?"
```

> **SAY:** "CEO — be tough. Don't let them ramble. If they start with 'First I cleaned the data, then I built a pivot table...' — interrupt immediately with 'I don't care about your process. What did you find?'"

> **SAY:** "Partner A presents. Partner B interrupts. 5 minutes. Then switch. Go."

- Circulate. Listen for:
  - Analysts who lead with findings (good)
  - Analysts who lead with methodology (redirect)
  - CEOs who are too polite (push them to be tougher)

> **SAY (after first round):** "Switch roles. Partner B presents, Partner A is the CEO."

- After second round, switch to a NEW partner for a faster round (3 min each).

> **SAY:** "Debrief. What changed between Round 1 and the faster round? What did you cut? That's what you should cut in every presentation."

#### STUDENTS DO

- Round 1: Present to "CEO" partner (5 min) + feedback (2 min)
- Round 2: Switch roles (5 min) + feedback (2 min)
- Round 3: New partner, faster (3 min each + 2 min feedback)
- Debrief: what they learned to cut (5 min)
- **Good presentation:** "Revenue in Region C dropped 15% last quarter. This is unusual because the other regions grew. I recommend reallocating 20% of Region C's marketing budget to digital channels, which are performing better in A and B."
- **Needs coaching:** "So I opened the spreadsheet and sorted by region, then I built a pivot table..." → CEO interrupts: "So what?"

#### Pacing

| Segment | Time |
|---------|------|
| Setup + rules | 3 min |
| Round 1: Partner A presents + interruptions | 5 min |
| Feedback | 2 min |
| Round 2: Switch roles | 5 min |
| Feedback | 2 min |
| Round 3: New partner, faster | 6 min |
| Debrief | 5 min |
| Transition | 2 min |

#### Teacher Tip

> The CEO role-play is terrifying for most students — and that's the point. In real life, executives will interrupt. Getting practice now, in a safe environment, builds confidence for Day 3's stakeholder panel and Day 4's capstone showcase.

#### Check for Understanding

**Debrief question:** "What's the one thing you'll never do again when presenting data?" Expected answers: "Start with the process," "Use too many numbers," "Not have a recommendation ready."

---

### 3:10–3:25 | Break (15 min)

> ☕ **BREAK** — "After break: memo writing, data fallacies, correlation vs. causation, and GDPR. The critical thinking block."

---

### 3:25–4:05 | The Data-Driven Memo (40 min)

**Format:** Mini-lecture + individual writing | **GRR Phase:** I Do → You Do Alone | **Bloom's:** Create

#### TEACHER DOES

> **SAY:** "The data story you just told verbally — now write it down. A data-driven memo is a 1-page decision document. Not a report. Not an analysis. A document that tells the reader what to DO."

**Project the memo structure:**

```
RECOMMENDATION (1 sentence — the reader knows what to do immediately)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTEXT (2–3 sentences: what was the question? what data did you analyze?)

KEY FINDINGS (3–4 bullet points, each with a number)
• Finding 1: [specific data point]
• Finding 2: [specific data point]
• Finding 3: [specific data point]

SUPPORTING VISUALIZATION (1 chart — the most important one)

RISKS & LIMITATIONS (what could be wrong? what don't you know?)

NEXT STEPS (2–3 concrete actions with owners and timelines)
```

**Before/after example:**

> **SAY:** "Here's a bad memo."

**Project BAD memo:**
```
Data Analysis Report
We analyzed the Q3 sales data using pivot tables and VLOOKUP
to examine regional performance. The data was cleaned and
28 duplicates were removed. We found several interesting patterns
in the data that suggest further investigation may be warranted...
```

> **SAY:** "What's wrong with this? It takes 4 sentences to say nothing. Now here's the same information as a good memo."

**Project GOOD memo:**
```
RECOMMENDATION: Shift 60% of Q4 marketing budget from Region C
to Regions A and B.

CONTEXT: Analyzed Q3 sales across 3 regions (500 transactions, Jul–Sep).

KEY FINDINGS:
• Region C revenue dropped 15% QoQ while A (+8%) and B (+12%) grew
• Region C's customer acquisition cost is 3x higher than other regions
• Digital campaigns in A and B convert at 2x the rate of C's print campaigns

[Bar chart: Revenue by Region, Q2 vs Q3]

RISKS: Region C drop may be seasonal (need Q3 from prior year to confirm).

NEXT STEPS:
1. Marketing team to draft Q4 budget reallocation by Oct 15
2. Region C manager to investigate local market conditions by Oct 10
3. Review results at November quarterly review
```

> **SAY:** "See the difference? The reader knows what to do from the first line. Everything else supports that one recommendation."

> **SAY:** "Write yours. Use your data, your dashboard, your story. 25 minutes."

#### STUDENTS DO

- Watch the structure breakdown and before/after comparison (10 min)
- Write their own 1-page data-driven memo (25 min)
- Quick pair check at the end: "Can your partner act on this memo?" (5 min)

#### Pacing

| Segment | Time |
|---------|------|
| Teach structure + before/after example | 10 min |
| Students write memo | 25 min |
| Pair check ("Can you act on this?") | 5 min |

#### Teacher Tip

> The 25 minutes for writing includes a dual-skill buffer — students are writing analytical content in English, which takes longer for L2 speakers. Don't rush this. Quality of thinking matters more than speed.

#### Check for Understanding

**Partner check:** "Read the first sentence of your partner's memo. Can you tell exactly what they're recommending? Yes or no?" If no, the memo needs revision.
**Circulate and read opening lines.** The #1 fix: students who bury the recommendation in paragraph 3 → move it to sentence 1.

#### Differentiation

- **Struggling learners:** Provide the memo template with fill-in-the-blank sections: "RECOMMENDATION: I recommend _____ because _____."
- **Advanced learners:** Add a "counter-argument" section: "Someone might argue _____, but the data shows _____."
- **Language support:** Allow first draft in L1, then translate the key sentences (recommendation, findings) to English.

---

### 4:05–4:20 | Data Fallacy Spotter (15 min)

**Format:** Full group, rapid exercise | **GRR Phase:** We Do | **Bloom's:** Analyze

#### TEACHER DOES

> **SAY:** "Before we go further, you need to know the 5 most common ways data lies — even when the numbers are technically correct."

**Project each fallacy with an example. Students vote on what's wrong.**

**Fallacy 1: Survivorship Bias**
> "We studied successful startups and found they all had X in common. Therefore, X causes success."
> **SAY:** "What's wrong? We only looked at the winners. What about the hundreds of startups that ALSO had X but failed?"

**Fallacy 2: Simpson's Paradox**
> "University A admits 40% of women vs. 50% of men — gender bias? But department by department, women are admitted at higher rates. The overall number is misleading because women apply more to competitive departments."

**Fallacy 3: Base Rate Neglect**
> "A medical test is 99% accurate. You test positive. Are you probably sick?"
> **SAY:** "Not necessarily. If only 1 in 10,000 people have the disease, most positives are false positives."

**Fallacy 4: Anchoring**
> "This product was $200, now $99!" — "Is that a good deal? You have no idea. The $200 anchor makes $99 feel cheap regardless of actual value."

**Fallacy 5: Cherry-Picking**
> Revenue is down this quarter. But zoom out to the full year — it's up 20%. The quarterly dip is normal seasonal variation.

> **SAY:** "Remember these. They'll protect you from being fooled — and from accidentally fooling others with your own data."

#### STUDENTS DO

- Vote on each fallacy example: what's wrong?
- Discuss as a group
- Take notes on the 5 fallacies

#### Pacing

| Segment | Time |
|---------|------|
| 5 fallacies × 2.5 min each | 12.5 min |
| Wrap-up | 2.5 min |

#### Check for Understanding

**Quick quiz:** "I tell you that ice cream sales and drowning deaths both increase in summer. Therefore, ice cream causes drowning. What fallacy is this?" (Correlation ≠ causation — sets up next block.)

---

### 4:20–4:50 | Correlation vs. Causation Workshop (30 min)

**Format:** Group exercise | **GRR Phase:** I Do → We Do → You Do Together | **Bloom's:** Analyze

#### TEACHER DOES

> **SAY:** "The biggest fallacy of all deserves its own block. Correlation vs. causation. Just because two things happen together doesn't mean one causes the other."

**Part 1: Spurious Correlations (5 min — fun)**

- Project 5 hilarious correlations from tylervigen.com:
  - "Nicholas Cage movies correlate with pool drownings"
  - "Per capita cheese consumption correlates with deaths by bedsheet tangling"

> **SAY:** "Obviously cheese doesn't kill people. But in business data, the correlations are subtler — and people fall for them."

**Part 2: Real Business Examples (8 min)**

- Project 5 real cases where correlation was mistaken for causation:
  1. "Stores that play classical music have higher sales" — (wealthier neighborhoods, not the music)
  2. "Employees who take training courses get promoted more" — (ambitious employees seek training AND promotions)
  3. "Countries with more internet access have lower birth rates" — (economic development drives both)
  4. "Students who eat breakfast score higher on tests" — (family stability, not breakfast)
  5. "Companies that advertise more have higher revenue" — (they advertise more BECAUSE they have more revenue)

> **SAY:** "Now look at YOUR data. Find 3 things that correlate. Then ask: is this causation, or is something else driving both?"

**Part 3: Student Analysis (10 min)**

- Students work in pairs to identify 3 correlations in their data and evaluate each.

> **SAY:** "For each correlation, answer: Could there be a third variable causing both? Could the direction be reversed? Would an experiment prove it?"

- Debrief: 2–3 pairs share their most interesting finding.

#### STUDENTS DO

- Laugh at spurious correlations (engagement hook)
- Analyze 5 real business examples
- Find 3 correlations in their own data (pairs)
- Evaluate: correlation or causation?
- Share findings

#### Pacing

| Segment | Time |
|---------|------|
| Spurious correlations (fun) | 5 min |
| Real business examples | 8 min |
| Students analyze 3 own-data correlations | 10 min |
| Discussion (2–3 pairs share) | 5 min |
| Transition | 2 min |

#### Teacher Tip

> Start with the funny examples to lower the stakes. By the time students analyze their own data, they'll be primed to be skeptical — which is exactly the mindset you want.

#### Check for Understanding

**Cold call:** "Nara, you found a correlation. Tell us — is it causation? How do you know?"
**Expected:** Student should be able to propose a third variable or explain why the direction might be reversed.

---

### 4:50–5:10 | GDPR & Data Privacy Basics (20 min)

**Format:** Interactive lecture | **GRR Phase:** I Do → We Do | **Bloom's:** Understand

#### TEACHER DOES

> **SAY:** "One more critical topic. If you work with data — especially in Moldova, which is aligning with EU standards — you need to know GDPR."

> **SAY:** "GDPR stands for General Data Protection Regulation. Here's what it means for you in 5 rules:"

**Project:**
```
1. CONSENT: You need permission to collect personal data
2. PURPOSE: You can only use data for the purpose you stated
3. MINIMIZATION: Only collect what you actually need
4. ACCESS: People have the right to see their data and ask you to delete it
5. SECURITY: You must protect data from breaches
```

> **SAY:** "Let's make this practical."

**Scenario-based exercise:**

> "Scenario 1: You built a dashboard showing individual employee performance scores. Can you share this dashboard with the whole company?"
> (No — personal performance data requires consent and purpose limitation.)

> "Scenario 2: Your NGO collects beneficiary names, ages, and health conditions. A donor asks to see the raw data. Can you share it?"
> (No — you must anonymize personal data before sharing externally.)

> "Scenario 3: You scraped publicly available data from social media for your analysis. Is this GDPR-compliant?"
> (It depends — public data still has privacy implications under GDPR.)

- Discuss each scenario. Let students debate.

> **SAY:** "The key principle: when in doubt, anonymize. Remove names, IDs, and anything that could identify a person. Your analysis doesn't need to know WHO — it needs to know WHAT and HOW MANY."

#### STUDENTS DO

- Learn the 5 GDPR principles
- Discuss 3 practical scenarios: can you share this data?
- Apply to their own dashboards: "Is there anything in your dashboard that should be anonymized?"

#### Pacing

| Segment | Time |
|---------|------|
| Core GDPR principles | 8 min |
| 3 practical scenarios | 7 min |
| Apply to own dashboard + Q&A | 5 min |

#### Teacher Tip

> GDPR is especially relevant for Moldova (EU accession process) and for anyone working on EU-funded projects. Frame it as a professional advantage: "Knowing GDPR sets you apart from everyone who just throws data around without thinking about privacy."

#### Check for Understanding

**Quick poll:** "Raise your hand if your current dashboard contains any personal data that should be anonymized." Discuss what should be changed.

---

### 5:10–5:45 | Day 2 Wrap + Mid-Week Assignment (35 min)

**Format:** Full group, reflective | **GRR Phase:** We Do | **Bloom's:** Evaluate (metacognition)

#### TEACHER DOES

**Data Confidence Self-Assessment:**

> **SAY:** "Same 4 questions as yesterday. Rate yourself 1–5. Then compare to your Day 1 scores."

**Project:**
```
1. Reading data:        Day 1: ___  Day 2: ___
2. Cleaning data:       Day 1: ___  Day 2: ___
3. Analyzing data:      Day 1: ___  Day 2: ___
4. Communicating data:  Day 1: ___  Day 2: ___
```

> **SAY:** "Who went up? By how much? What specifically made the difference?"

- Call on 2–3 students. Celebrate growth.

**Mid-week assignment:**

> **SAY:** "Between now and Day 3, here's what I want you to do:"

**Project:**
```
1. Find a NEW dataset from your actual work or community
   (not the bootcamp datasets)
2. Apply the full pipeline: clean → analyze → visualize → write a brief
3. Build a simple dashboard in Looker Studio
4. Write a 1-paragraph "data story" using Setup → Conflict → Resolution
5. Bring everything to Day 3 — you'll present to the class AND
   to a mock stakeholder panel
```

> **SAY:** "Day 3 is presentation day. You'll present your findings under adversarial questioning — just like the CEO role-play, but harder. Start preparing now."

- Walk through the assignment. Answer questions.

**Data English Playbook update:**

> **SAY:** "Add 10 new terms to your Data English Playbook. Today's terms: VLOOKUP, dashboard, 5-second test, narrative arc, data-driven memo, correlation, causation, GDPR, fallacy, conditional formatting."

#### STUDENTS DO

- Complete self-assessment and compare to Day 1
- Share growth observations
- Write down mid-week assignment steps
- Update Data English Playbook with 10 new terms
- Ask clarifying questions

#### Pacing

| Segment | Time |
|---------|------|
| Self-assessment + Day 1 comparison | 5 min |
| 2–3 students share growth | 5 min |
| Mid-week assignment walkthrough | 15 min |
| Data English Playbook update | 5 min |
| Questions + logistics | 5 min |

#### Teacher Tip

> The Day 1 → Day 2 comparison is motivating. Most students will see gains of 1–2 points on each dimension. Point this out explicitly: "You went from a 2 to a 4 on analyzing data in TWO DAYS. Imagine where you'll be in two more."

---

## DIFFERENTIATION NOTES (Session-Wide)

**Struggling learners:**
- Skip INDEX-MATCH — VLOOKUP is sufficient for all bootcamp tasks
- Reduce dashboard to 2 charts + 1 headline instead of 4 charts
- Provide memo template with fill-in-the-blank structure
- Pair with stronger partner during role-play and correlation analysis

**Advanced learners:**
- Introduce XLOOKUP and array formulas
- Challenge them to build a multi-page dashboard with drill-down
- Add counter-arguments to their memo
- Ask them to find a real-world example of each data fallacy from their industry

**Language support:**
- Memo can be drafted in L1 first, key sections translated to English
- Data English Playbook is the running glossary — reinforce it every session
- Dashboard headlines in English (practice professional communication)
- Pair bilingual students during role-play for peer translation support

---

## POST-SESSION REFLECTION (For Instructor)

- [ ] What worked well today?
- [ ] What would I adjust for next time?
- [ ] Which students need follow-up before Day 3?
- [ ] Did timing work? Where did I run long/short?
- [ ] Did the VLOOKUP block take too long? Should I simplify for next cohort?
- [ ] Were dashboards functional by the gallery walk, or did technical issues eat into build time?
- [ ] Did the CEO role-play push students to be concise, or did they still ramble?
- [ ] Are memos leading with recommendations or burying them?
- [ ] Are self-assessment scores showing growth from Day 1?
