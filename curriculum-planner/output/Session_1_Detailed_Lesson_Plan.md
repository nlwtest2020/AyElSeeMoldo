# SESSION 1: "See It & Question It"

**Saturday, Weekend 1 | 10:00 AM – 5:45 PM**
**Theme:** Learn to read data, ask the right questions, and stop being intimidated by numbers.

---

## Learning Targets

By the end of this session, students will be able to:

1. **Identify** misleading charts and explain what makes a visualization trustworthy vs. deceptive (Bloom's: Analyze)
2. **Use** 4 spreadsheet functions (SORT, FILTER, SUMIF/COUNTIF) to answer business questions (Bloom's: Apply)
3. **Clean** a messy dataset by removing duplicates, fixing formatting, and handling blanks (Bloom's: Apply)
4. **Build** 5 pivot tables answering different analytical questions (Bloom's: Apply → Create)
5. **Create** 3 appropriate chart types and evaluate which tells the story best (Bloom's: Evaluate)
6. **Write** a 3-sentence data brief in English: finding + significance + recommendation (Bloom's: Create)

---

## Materials & Setup

- Laptop per student (charged, with WiFi access)
- Google accounts pre-created with access to Google Sheets
- 3 pre-prepared datasets in Google Sheets (shared, view-only — students make copies):
  - Dataset A: Local e-commerce sales (Moldovan online retailer — orders, regions, product categories, revenue)
  - Dataset B: NGO beneficiary tracking (youth program — enrollment, completion, demographics, outcomes)
  - Dataset C: University enrollment (Georgian university — departments, years, gender, graduation rates)
- 1 deliberately messy version of each dataset (for data cleaning block)
- 8 pre-prepared chart images for "What's Wrong with This Chart?" (mix of honest and misleading)
- Slides deck (Session 1)
- Printed Data Literacy Framework handout (1 per student)
- Printed Five Questions template (1 per student)
- Whiteboard + markers
- Timer (visible to all students — phone or projected)
- AI tool access: Claude (https://claude.ai), ChatGPT (https://chat.openai.com), or Poe (https://poe.com) as fallback
- **Moldova note:** Google Sheets works everywhere. For AI tools, Claude may have limited access — use Poe.com or ChatGPT as backup.

---

## Assessment at a Glance

| Method | Description |
|--------|-------------|
| **Formative** | Observe pivot table builds (guided vs. independent). Check chart peer reviews for specific feedback (not "looks good"). Monitor data cleaning verification checks. |
| **Self-Assessment** | Students rate confidence (1–5) across 4 dimensions: reading data, cleaning data, analyzing data, communicating data. This is the Day 1 baseline. |
| **Exit Ticket** | 3-sentence data brief: finding + significance + recommendation. |
| **Evidence to look for** | Students build pivot tables without step-by-step guidance by tables 4 and 5. Chart peer reviews identify specific design issues. Data briefs lead with the finding, not the methodology. AI comparison documents identify at least one AI error or oversimplification. |

---

## MORNING BLOCK (10:00–12:45)

---

### 10:00–10:20 | Welcome + "You Already Use Data" (20 min)

**Format:** Full group, interactive | **GRR Phase:** I Do | **Bloom's:** Remember/Understand

#### TEACHER DOES

> **SAY:** "Good morning! Before I introduce myself or show a single slide, I want to prove something to you. Raise your hand if you checked the weather this morning."

- Hands go up.

> **SAY:** "Raise your hand if you've compared prices before buying something online — on 999.md, on Ozon, anywhere."

- More hands.

> **SAY:** "Raise your hand if you've ever looked at your Instagram insights — how many people saw your post, what time they were most active."

- Some hands.

> **SAY:** "Congratulations. You're already using data. Every single day. You just don't call it 'data analysis.' This bootcamp doesn't teach you something foreign — it formalizes something you already do and gives you professional tools to do it better."

- **Run the poll:** "Who's been asked to 'look at the data' at work and had no idea where to start?" Most hands go up. This is the anxiety moment — name it.

> **SAY:** "That feeling — 'I don't know where to start' — is exactly what we're going to fix over the next 4 days. By the end of today, you'll be able to open any spreadsheet and ask it smart questions."

- Quick intros: name, what you do, one thing you wish you could do with data.
- Model the intro: "I'm [name], I teach this bootcamp, and I wish I could build a dashboard that shows me my team's progress without asking 5 people for updates."
- Go around the room. 20 seconds each. Redirect anyone going long.

**Norms (project on screen):**
> **SAY:** "Three ground rules:"
> 1. "Phones on silent. If you need to take a call, step out."
> 2. "Breaks are every 90 minutes. We'll stick to the schedule."
> 3. "There are no dumb questions. Most of you have never built a pivot table — that's exactly where we want you to start."

- Quick logistics: WiFi password, bathroom location, lunch timing.

#### STUDENTS DO

- Respond to hand-raise polls (weather, prices, Instagram)
- Introduce themselves (name, role, one data wish)
- **Good example:** "I'm Ana, I work at an NGO in Chișinău, and I wish I could make sense of our beneficiary data without waiting for the M&E team."
- **Too long:** Full career history (redirect: "Great — we'll get into that. Next person!")

#### Pacing

| Segment | Time |
|---------|------|
| Data polls + reframe | 5 min |
| Student intros (15–20 students × 25 sec) | 7–8 min |
| Norms + logistics | 3 min |
| Bootcamp overview (what we'll cover in 4 days) | 4 min |
| Buffer | 1 min |

#### Teacher Tip

> Use real, local examples. "999.md price comparisons" lands better than "Amazon shopping" in Moldova. "Wildberries delivery tracking" works in Georgia. Match the examples to the room.

#### Check for Understanding

**Observe:** Are students nodding, smiling, making eye contact? Are intros flowing quickly?
**If students seem anxious:** Double down on the reframe. "By lunch today, you'll have built your first pivot table. I promise it's easier than it sounds."

---

### 10:20–10:50 | "What's Wrong with This Chart?" (30 min)

**Format:** Full group, interactive voting | **GRR Phase:** I Do → We Do | **Bloom's:** Analyze

#### TEACHER DOES

> **SAY:** "Before we touch any data ourselves, we need to learn to read data that other people show us. Because not all charts are honest. Let me show you what I mean."

- **Project Chart 1** on screen: A bar chart showing Moldova's GDP growth with a truncated Y-axis (starting at 95% instead of 0), making a 2% change look enormous.

> **SAY:** "Quick vote — thumbs up if you think this chart is trustworthy, thumbs down if something looks off. Don't overthink it — gut reaction."

- Count votes. Then deconstruct:

> **SAY:** "Look at the Y-axis. It starts at 95, not 0. That makes a tiny 2% change look like the economy doubled. This is called a truncated axis, and it's one of the most common tricks in data visualization. The data itself isn't wrong — but the chart is designed to mislead."

- **Repeat for 7 more charts** (alternate between honest and misleading):
  - **Chart 2 (honest):** Georgia tourism arrivals, line chart, properly scaled, clear labels
  - **Chart 3 (misleading):** Cherry-picked timeframe — Armenian export data showing only the best 3 months
  - **Chart 4 (misleading):** Correlation presented as causation — "ice cream sales and drowning deaths both rise in summer"
  - **Chart 5 (honest):** NGO program outcomes, bar chart with proper baselines and error context
  - **Chart 6 (misleading):** 3D pie chart making one segment look larger than it is
  - **Chart 7 (honest):** Moldovan election data, clearly sourced, appropriate chart type
  - **Chart 8 (misleading):** Missing context — revenue numbers without adjusting for inflation

- After all 8, summarize the 4 key red flags on the whiteboard:

> **SAY:** "Here are the 4 things to check every time someone shows you a chart:"
> 1. "Does the axis start at zero? If not, why?"
> 2. "What timeframe is shown? Is it cherry-picked?"
> 3. "Is the chart type appropriate? Pie charts lie. 3D charts lie more."
> 4. "What's NOT shown? Missing context is the most common form of data manipulation."

#### STUDENTS DO

- Vote on each chart: thumbs up (trustworthy) or thumbs down (misleading)
- Explain their reasoning when called on
- Take notes on the 4 red flags
- **Good response:** "The axis doesn't start at zero, so the difference looks bigger than it really is."
- **Needs coaching:** "It just looks wrong." → Push: "What specifically looks wrong? Look at the axis labels."

#### Pacing

| Segment | Time |
|---------|------|
| Setup + intro | 3 min |
| 8 charts × 3 min each (show, vote, deconstruct) | 24 min |
| Wrap-up: 4 key principles on whiteboard | 3 min |

#### Teacher Tip

> Use charts from regional news sources students would actually encounter — Moldovan news sites, Georgian economic reports, Armenian election coverage. If they recognize the source, they'll engage more deeply because it's personal.

#### Check for Understanding

**Cold call after chart 4:** "Irina, why is this chart misleading?" Student should identify the specific technique.
**If <25% can identify the trick by chart 5:** Slow down. Show charts 5–8 side-by-side with the honest versions and have students spot the difference in pairs before voting.

#### Differentiation

- **Struggling learners:** Pair them with someone who's catching on. Let them discuss before voting.
- **Advanced learners:** Ask them to name where they've seen each trick "in the wild" — news, social media, work presentations.
- **Language support:** Write the 4 red flags in both English and Romanian/Georgian on the whiteboard.

---

### 10:50–11:15 | Data Literacy Framework + Five Questions (25 min)

**Format:** Interactive lecture + exercise | **GRR Phase:** I Do → We Do | **Bloom's:** Understand → Apply

#### TEACHER DOES

> **SAY:** "Now that you can spot a bad chart, let's talk about what data literacy actually means. It's not one skill — it's four levels."

**Project the framework:**

```
Level 1: READ         → Can you read a chart or table and understand what it says?
Level 2: WORK         → Can you use tools (spreadsheets, databases) to manipulate data?
Level 3: ANALYZE      → Can you draw conclusions and spot patterns?
Level 4: COMMUNICATE  → Can you explain your findings to someone who doesn't speak data?
```

> **SAY:** "Right now, after that chart exercise, you're already at Level 1. By the end of today, you'll be at Level 2 and starting Level 3. By Day 4, you'll be at Level 4 — presenting data to real stakeholders."

> **SAY:** "Now — every good data analysis starts with 5 questions. Memorize these."

**Project the Five Questions:**

```
1. What happened?        → Describe the data
2. Why did it happen?    → Find causes
3. What will happen?     → Predict trends
4. What should we do?    → Recommend actions
5. How will we know?     → Define success metrics
```

> **SAY:** "Let's practice. Here's a scenario."

**Project scenario:** "Your NGO runs a youth employment program in Chișinău. Last quarter, 120 participants enrolled but only 45 completed the program. Your donor asks: 'What's going on?'"

> **SAY:** "In pairs, take 3 minutes. Which of the 5 questions would you start with? What data would you need to answer it?"

- Circulate. Listen for pairs that jump straight to "What should we do?" without first asking "What happened?" and "Why?"

> **SAY:** "Let's hear it. [Cold call.] Andrei, which question did your pair start with?"

- Debrief: You must answer them in order. You can't recommend actions (question 4) until you understand causes (question 2).

**Self-assessment:**

> **SAY:** "Quick self-check. On the framework handout, circle where you think you are right now — Level 1, 2, 3, or 4. No wrong answers. We'll check again at the end of the day."

#### STUDENTS DO

- Watch the framework presentation (5 min)
- Learn the Five Questions (3 min)
- **Pair exercise:** Given the NGO scenario, identify which question to start with and what data they'd need (3 min)
- Share answers when called on (4 min)
- Self-assess current data literacy level (2 min)

#### Pacing

| Segment | Time |
|---------|------|
| Teach 4-level framework | 8 min |
| Teach Five Questions | 5 min |
| Pair exercise (NGO scenario) | 3 min |
| Debrief (2–3 pairs share) | 4 min |
| Self-assessment | 3 min |
| Transition | 2 min |

#### Teacher Tip

> Students will want to skip to "What should we do?" because it feels productive. Resist. The whole point is that jumping to recommendations without understanding the data is how bad decisions get made. Make this explicit.

#### Check for Understanding

**Turn and talk:** "Which question comes BEFORE 'What should we do?' and why does it matter?"
**Expected:** Students should say "Why did it happen?" and explain that recommendations without understanding causes are guesses.
**If >25% can't sequence the questions:** Write them on the whiteboard in the wrong order and have the class fix it together.

---

### 11:15–11:30 | Break (15 min)

> ☕ **BREAK** — Remind students: "When you come back, we're opening real datasets. Make sure your laptop is charged."

---

### 11:30–12:05 | Real Data, Real Questions (35 min)

**Format:** Small groups (4–5 students) | **GRR Phase:** You Do Together | **Bloom's:** Analyze

#### TEACHER DOES

> **SAY:** "OK, time to get your hands on real data. I'm going to give each group a dataset. It's real — messy, imperfect, the kind of thing you'd actually encounter at work. Your job is NOT to analyze it yet. Just look. Explore. Ask questions."

- Distribute the 3 datasets (assign groups to A, B, or C):
  - **Dataset A:** Moldovan e-commerce — 500+ rows of orders with dates, customer IDs, regions, product categories, revenue, repeat/new customer flag
  - **Dataset B:** NGO beneficiary tracking — 300+ rows of youth program participants with demographics, enrollment dates, completion status, outcomes
  - **Dataset C:** Georgian university enrollment — 400+ rows across departments, years, gender breakdowns, graduation rates

> **SAY:** "Open the Google Sheet link. Make a copy (File → Make a Copy). Then just... look. Scroll through it. Here's what I want you to answer as a group:"

**Project on screen:**
```
1. What do you notice first?
2. What questions does this data raise?
3. What's missing — what data would you WANT that isn't here?
4. Is anything obviously wrong or suspicious?
```

> **SAY:** "You have 20 minutes. Write your observations in a shared doc or on paper. Don't try to analyze yet — just observe."

- **Circulate.** Listen for:
  - Groups that spot data quality issues (duplicates, blanks, inconsistent formatting) — praise this
  - Groups that immediately try to calculate averages — redirect: "Good instinct, but first — what are you even looking at? What do the columns mean?"
  - Groups that notice missing context (no industry benchmarks, no time comparison)

> **SAY (after 20 min):** "Time's up. Each group, give us your top 3 observations. 2 minutes max."

- Call on 3–4 groups. Write key observations on the whiteboard.
- Highlight patterns: "Notice how every group found messy data? That's normal. Real data is always messy. That's why data cleaning is a real skill — and we'll do it after lunch."

#### STUDENTS DO

- Open dataset, make a copy in Google Sheets
- Explore the data in groups (scroll, read column headers, look at value ranges)
- Discuss and record observations: what they notice, what questions arise, what's missing, what's suspicious
- Report back to the class (2 min per group)
- **Good observation:** "We noticed that the 'region' column has the same city spelled 3 different ways — 'Chisinau', 'Chișinău', and 'chisinau'. That would mess up any analysis."
- **Needs coaching:** "The data looks fine." → Push: "How many rows are there? Are there any blanks? Does every column have consistent formatting?"

#### Pacing

| Segment | Time |
|---------|------|
| Distribute datasets + orient | 5 min |
| Group exploration | 20 min |
| Report-back (3–4 groups × 2 min) | 6–8 min |
| Transition | 2 min |

#### Teacher Tip

> This block is about developing the habit of looking before doing. Students who jump straight into calculations without understanding the data will make mistakes later. Let them sit with the discomfort of not knowing what to do yet — the next blocks give them tools.

#### Check for Understanding

**Quick poll:** "How many groups found at least one data quality issue — duplicates, blanks, inconsistent spelling?" All hands should go up.
**If any group found nothing:** Open their dataset on screen and point out one issue. Say: "This is why we look first. If we'd started calculating averages with these duplicates, our numbers would be wrong."

#### Differentiation

- **Struggling learners:** Give them a printed "Data Exploration Checklist" with the 4 questions and space to write answers. Structure helps.
- **Advanced learners:** Challenge them to estimate the dataset's "trustworthiness score" on a 1–10 scale and defend it.
- **Language support:** Key terms on the whiteboard in English + Romanian: "row = rând", "column = coloană", "blank = gol", "duplicate = duplicat".

---

### 12:05–12:45 | Spreadsheet Power-Up (4 Functions) (40 min)

**Format:** Hands-on, follow-along | **GRR Phase:** I Do → We Do → You Do | **Bloom's:** Apply

#### TEACHER DOES

> **SAY:** "Now you've seen the data. Time to start asking it questions. I'm going to teach you 4 spreadsheet functions that let you interrogate any dataset. These aren't fancy — they're the ones I use every single day."

**Function 1: SORT**

> **SAY:** "First question: 'Who are our top customers?' To answer this, we need to sort by revenue. Watch me."

- **Demo live in Google Sheets:** Select the data range → Data → Sort range → Sort by Revenue column, Z→A (descending).

> **SAY:** "Now you try. Sort your dataset by revenue — highest to lowest. You have 2 minutes."

- Circulate. Help students who select the wrong range or forget to include headers.

**Function 2: FILTER**

> **SAY:** "Next question: 'How did sales look in just the Chișinău region?' We need to filter."

- **Demo:** Data → Create a filter → Click the dropdown on the Region column → Uncheck all → Check only "Chișinău".

> **SAY:** "Your turn. Filter your data to show only one region or one category. 2 minutes."

**Function 3: SUMIF**

> **SAY:** "Now — 'How much total revenue came from repeat customers?' This is where formulas start. Watch carefully."

- **Demo live.** Type in an empty cell:
```
=SUMIF(F:F, "Repeat", G:G)
```

> **SAY:** "SUMIF says: look in column F (customer type). Find every row where it says 'Repeat'. Then add up the corresponding values in column G (revenue). That's it. Three parts: where to look, what to look for, what to add up."

- **Write on whiteboard:**
```
=SUMIF(where_to_look, what_to_find, what_to_add)
```

> **SAY:** "Now you try. Write a SUMIF that answers a different question — maybe total revenue for a specific product category, or a specific region."

**Function 4: COUNTIF**

> **SAY:** "Last one. 'How many orders came from Tbilisi?' Same idea as SUMIF, but we're counting instead of adding."

- **Demo:**
```
=COUNTIF(C:C, "Tbilisi")
```

> **SAY:** "COUNTIF: where to look, what to count. Try it — count how many orders match something in your data."

**Free practice:**

> **SAY:** "You now have 4 tools: SORT, FILTER, SUMIF, COUNTIF. Take 8 minutes. Write 3 questions about your dataset and answer each one using one of these functions. Go."

#### STUDENTS DO

- Follow along with each function demo
- Practice each function on their own dataset immediately after the demo
- During free practice: write 3 questions and answer them with functions
- **Good question:** "How many NGO participants from rural areas completed the program?" → `=COUNTIF(...)` on completion column, filtered by region
- **Too basic:** "How many rows are there?" → Coach: "Good start — now ask something that compares two things."

#### Pacing

| Segment | Time |
|---------|------|
| SORT (teach + follow along) | 8 min |
| FILTER (teach + follow along) | 8 min |
| SUMIF/COUNTIF (teach + practice) | 10 min |
| Free practice (3 questions) | 8 min |
| Troubleshooting buffer | 6 min |

#### Teacher Tip

> Have the formula projected on screen AND written on the physical whiteboard. Students will look back and forth. When someone gets an error, 90% of the time it's a typo in the range reference or a missing quotation mark around the criteria. Walk the room during follow-along — don't just stand at the front.

#### Check for Understanding

**Whiteboards/Show Me (after SUMIF):** "Hold up your laptop — show me a SUMIF formula you wrote. I want to see it."
**Scan the room.** If >25% have errors or blank cells, stop and rework the example with a different question.
**Reteach trigger:** If students confuse SUMIF and COUNTIF, show them side by side: "SUMIF adds numbers. COUNTIF counts rows. That's the only difference."

#### Differentiation

- **Struggling learners:** Give them the exact formulas to type for the first 2 functions. Let them modify (not write from scratch) for functions 3–4.
- **Advanced learners:** Introduce AVERAGEIF as a bonus: "Same logic — but it calculates the average instead of the sum."
- **Language support:** Formula syntax is universal (English function names in Google Sheets), but explain the concept in simple terms: "SUMIF = add up only the ones that match."

---

### 12:45–1:45 | Lunch (60 min)

> 🍽 **LUNCH** — "Be back at 1:45. This afternoon we clean data, build pivot tables, create charts, and use AI. The fun stuff."

---

## AFTERNOON BLOCK (1:45–5:45)

---

### 1:45–2:15 | Data Cleaning — The Ugly Truth (30 min)

**Format:** Hands-on, guided | **GRR Phase:** I Do → We Do → You Do | **Bloom's:** Apply

#### TEACHER DOES

> **SAY:** "This morning, every group found messy data — duplicates, blanks, weird formatting. Now we fix it. Because here's the truth: data professionals spend 60–80% of their time cleaning data. Not analyzing. Cleaning."

> **SAY:** "I'm going to give you a deliberately messy version of your dataset. It has every common problem. Let's go through them one at a time."

**Problem 1: Duplicates**

> **SAY:** "Watch. I'll select all the data, then go to Data → Remove duplicates. But wait — before I click, how do I know which rows are duplicates? I need to decide: are two orders from the same customer on the same day duplicates, or separate orders?"

- Demo: Show how to identify duplicates first (sort by customer + date), then remove.

**Problem 2: Inconsistent formatting**

> **SAY:** "Remember the 3 spellings of Chișinău? Let's find them."

- Demo: Use Find & Replace (Ctrl+H): Find "chisinau" → Replace with "Chișinău". Then find "Chisinau" → Replace.

> **SAY:** "This is why your SUMIF returned 0 this morning — if you searched for 'Chișinău' but the data said 'chisinau', the formula found nothing. Data cleaning isn't optional. It's the difference between right answers and wrong answers."

**Problem 3: Blanks**

> **SAY:** "Blanks are dangerous. A blank in a revenue column — does that mean 0, or does it mean the data is missing? Those are very different. Let's check."

- Demo: Filter for blanks in the revenue column. Decide: fill with 0 (if it means no sale) or flag as "missing" (if we don't know).

**Problem 4: Outliers**

> **SAY:** "Sort by revenue, highest first. See that one row with 500,000 when everything else is under 10,000? Is that real or a typo? You have to investigate before you decide."

> **SAY:** "Now it's your turn. Clean your messy dataset. You have 12 minutes. At the end, I'll ask you to verify: run the same SUMIF from this morning on your cleaned data. Did the number change?"

#### STUDENTS DO

- Open the messy dataset version
- Follow along as instructor demos each cleaning technique
- Clean their own dataset independently (12 min):
  - Remove duplicates
  - Fix inconsistent formatting (Find & Replace)
  - Handle blanks (fill or flag)
  - Check for outliers
- Run a verification formula (SUMIF) on cleaned data and compare to pre-cleaning result

#### Pacing

| Segment | Time |
|---------|------|
| Intro + why cleaning matters | 3 min |
| Demo: duplicates | 3 min |
| Demo: inconsistent formatting | 3 min |
| Demo: blanks + outliers | 4 min |
| Students clean independently | 12 min |
| Verification check | 3 min |
| Transition | 2 min |

#### Teacher Tip

> The "Chișinău vs. chisinau" example is incredibly powerful because every student encountered it this morning. Use their own frustration as the hook. "Remember when your formula returned 0? This is why."

#### Check for Understanding

**Show Me:** "Hold up your screen. Show me your SUMIF result before cleaning and after cleaning. Different number? Good — that means you found and fixed something."
**If >25% get the same number:** They didn't actually clean the data. Walk them through finding a specific duplicate or formatting inconsistency.

#### Differentiation

- **Struggling learners:** Give a printed "Data Cleaning Checklist" with steps: 1) Sort and check for duplicates, 2) Find & Replace inconsistencies, 3) Filter for blanks, 4) Sort for outliers.
- **Advanced learners:** Ask them to write a summary of what they cleaned: "I found 12 duplicates, 3 spelling variants of the same city, and 8 blank revenue cells."
- **Language support:** "Duplicate = duplicat. Blank = gol. Outlier = valoare extremă."

---

### 2:15–3:00 | Pivot Table Mastery (45 min)

**Format:** Hands-on, instructor-led → independent | **GRR Phase:** I Do → We Do → You Do Together → You Do Alone | **Bloom's:** Apply → Create

#### TEACHER DOES

> **SAY:** "Pivot tables are the single most powerful non-technical analysis tool in existence. If you learn one thing today, let it be this. A pivot table lets you answer almost any question about your data in 30 seconds."

**Pivot Table 1 (Guided): Total revenue by region**

> **SAY:** "Question: 'Which region generates the most revenue?' Watch how fast we can answer this."

- Demo: Select all data → Insert → Pivot table → New sheet
- Rows: Region. Values: Revenue (SUM).

> **SAY:** "There's your answer. 10 seconds. Now follow along — build the same pivot table."

- Wait for students to catch up. Circulate.

**Pivot Table 2 (Guided): Order count by product category**

> **SAY:** "New question: 'Which product category has the most orders?' Same process, different fields."

- Demo: Rows: Product Category. Values: Order ID (COUNTA).
- Students follow along.

**Pivot Table 3 (Guided): Average revenue per customer type (new vs. repeat)**

> **SAY:** "Question: 'Do repeat customers spend more than new customers?' This time, change the value aggregation from SUM to AVERAGE."

- Demo. Students follow.

**Pivot Table 4 (Independent):**

> **SAY:** "Now you're on your own. Build a pivot table that answers: 'How does revenue break down by region AND product category?' Hint: you'll need both rows and columns."

- Circulate. Let students struggle. Only help if they're completely stuck after 3 minutes.

**Pivot Table 5 (Independent):**

> **SAY:** "Last one. Write your own question about the data. Then build a pivot table to answer it. Go."

- Circulate. This is the assessment moment — can they design a question and build the table without guidance?

> **SAY (after builds):** "Who wants to share? What question did you ask and what did the pivot table tell you?"

- Call on 2–3 students. Celebrate creative questions.

#### STUDENTS DO

- Follow along with pivot tables 1–3 (guided)
- Build pivot table 4 independently (region × category breakdown)
- Design own question and build pivot table 5 independently
- Share findings with the class
- **Good pivot table 5:** "I asked 'Which month had the highest average order value for repeat customers in Chișinău?' and found that September was highest."
- **Needs coaching:** Building the same pivot table as #1 with different labels. Push: "You already know total revenue by region. Ask something you don't know yet."

#### Pacing

| Segment | Time |
|---------|------|
| Intro + pivot table concept | 3 min |
| Guided pivot 1 (revenue by region) | 7 min |
| Guided pivot 2 (orders by category) | 7 min |
| Guided pivot 3 (avg revenue by customer type) | 6 min |
| Independent pivot 4 (region × category) | 6 min |
| Independent pivot 5 (student's own question) | 6 min |
| Share + debrief | 5 min |
| Transition | 5 min |

#### Teacher Tip

> The transition from guided (pivots 1–3) to independent (pivots 4–5) is where you'll see the real skill gap. Some students will fly through pivot 4; others will freeze. For the frozen ones, don't give the answer — ask: "What fields would you need in the rows? What goes in the columns?" Guide them to the answer.

#### Check for Understanding

**After pivot 3 (guided):** "Thumbs up if you could build that one again on your own. Thumbs sideways if you'd need the steps. Thumbs down if you're lost." Calibrate how much help to give on pivots 4–5.
**After pivot 5 (independent):** The pivot table itself IS the assessment. If a student built a meaningful pivot table from their own question, they've got it.
**Reteach trigger:** If >30% can't start pivot 4, do a quick re-demo of the drag-and-drop interface and have everyone build pivot 4 together before attempting 5.

#### Differentiation

- **Struggling learners:** For pivot 4, give them the question AND tell them which fields go where. For pivot 5, offer 3 question options to choose from.
- **Advanced learners:** Add a calculated field to their pivot table (e.g., revenue per order). Show them how to add filters to pivot tables.
- **Language support:** "Pivot table = tabel pivot. Row = rând. Column = coloană. Value = valoare. Sum = sumă. Average = medie."

---

### 3:00–3:15 | Break (15 min)

> ☕ **BREAK** — "After break: charts, AI, and your first data brief. We're in the home stretch."

---

### 3:15–3:55 | Visualization Fundamentals (40 min)

**Format:** Hands-on + peer review | **GRR Phase:** I Do → We Do → You Do Together | **Bloom's:** Apply → Evaluate

#### TEACHER DOES

> **SAY:** "You can now clean data, build formulas, and create pivot tables. But none of that matters if you can't show someone else what you found. That's where visualization comes in. And rule number one..."

> **SAY:** "Almost never use a pie chart."

- Pause for effect.

> **SAY:** "Seriously. Pie charts are hard to read when you have more than 3 slices, and humans are terrible at comparing angles. Here's what to use instead."

**Project the chart type guide:**

```
COMPARISON between categories  → Bar chart (horizontal or vertical)
CHANGE over time               → Line chart
RELATIONSHIP between variables → Scatter plot
PART of a whole (2–3 parts)    → Pie chart (only if 2–3 segments)
DISTRIBUTION                   → Histogram
```

> **SAY:** "Now — 5 design principles that separate good charts from bad ones."

**Project principles:**

```
1. Label your axes. Always. No exceptions.
2. No 3D. Ever. It distorts proportions.
3. Intentional colors — don't use rainbow. Use one color with shading,
   or highlight the key bar.
4. Put the most important number in the title.
   Not "Sales by Region" but "North Region leads all others by 40%."
5. One chart = one message. If your chart says two things, make two charts.
```

> **SAY:** "Now build 3 charts from your cleaned data. One bar chart, one line chart, and one of your choice. You have 18 minutes. Then we'll do peer review."

- Circulate. Look for: 3D charts (tell them to remove it), missing axis labels, rainbow colors, vague titles.

**Peer review:**

> **SAY:** "Swap screens with the person next to you. Rate each of their 3 charts on a scale of 1–5 for clarity. Can you understand the main message in 5 seconds? Write your rating and one specific piece of feedback on a sticky note."

#### STUDENTS DO

- Watch chart type selection guide and 5 principles (10 min)
- Build 3 charts from their data in Google Sheets (18 min):
  - 1 bar chart (comparison)
  - 1 line chart (trend over time)
  - 1 chart of their choice
- Swap screens with a partner
- Rate partner's charts 1–5 on clarity and write specific feedback
- **Good feedback:** "Your bar chart title says 'Revenue' but it should say 'Chișinău generates 3x more revenue than other regions.'"
- **Weak feedback:** "Looks good." → Coach: "Can you understand the main point in 5 seconds? What would you change?"

#### Pacing

| Segment | Time |
|---------|------|
| Chart type selection guide | 5 min |
| 5 design principles | 5 min |
| Students build 3 charts | 18 min |
| Peer review (swap + rate + feedback) | 8 min |
| Quick debrief (1–2 examples on screen) | 2 min |
| Transition | 2 min |

#### Teacher Tip

> The peer review is where learning actually happens. Students who built mediocre charts will see better ones from their partner and immediately understand the gap. Don't skip or rush this.

#### Check for Understanding

**Gallery observation:** As students build charts, check that at least 80% have labeled axes and non-3D charts. These are the minimum bar.
**After peer review:** "Raise your hand if your partner gave you feedback that changed how you'd build the chart." Most hands should go up.

#### Differentiation

- **Struggling learners:** Give them a step-by-step guide: 1) Select data, 2) Insert → Chart, 3) Change chart type, 4) Add title, 5) Label axes.
- **Advanced learners:** Challenge them to create a combo chart (bar + line on the same chart) or add a trendline.
- **Language support:** Chart vocabulary: "bar chart = diagramă cu bare, line chart = grafic liniar, axis = axă, title = titlu."

---

### 3:55–4:25 | AI-Assisted Pattern Spotting (30 min)

**Format:** Hands-on, individual | **GRR Phase:** You Do → We Do | **Bloom's:** Evaluate

#### TEACHER DOES

> **SAY:** "All afternoon, you've been analyzing data with your own eyes and spreadsheet skills. Now let's see what AI thinks. And — this is important — let's see where AI gets it right and where it gets it wrong."

> **SAY:** "Open Claude, ChatGPT, or Poe. Copy your cleaned dataset — or describe it in detail. Then ask this exact prompt:"

**Project on screen:**
```
Here is a dataset of [describe your data — e.g., 500 e-commerce orders
from a Moldovan online retailer with columns for date, region, product
category, customer type, and revenue].

What are the 3 most interesting patterns or insights in this data?
For each, explain why it matters and what action a business owner
should take.
```

> **SAY:** "You have 5 minutes to get AI's response. Then — this is the critical part — compare what AI found to what YOUR pivot tables and charts already showed you."

- After 5 minutes:

> **SAY:** "Now open a new doc or grab a piece of paper. I want you to answer 3 questions:"

**Project:**
```
1. What did AI find that you ALSO found? (Confirmation)
2. What did AI find that you MISSED? (New insight)
3. What did AI get WRONG or oversimplify? (Critical evaluation)
```

> **SAY:** "This is the most important skill in AI-assisted analysis: knowing when to trust it and when to push back. You have 12 minutes."

- Circulate. Look for students who accept everything AI says without checking. Push them: "Did you verify that number? Does it match your pivot table?"

> **SAY (after 12 min):** "Who found something AI got wrong? Tell us."

- Call on 2–3 students. This is the highlight of the block.

#### STUDENTS DO

- Upload or describe their data to an AI tool
- Read AI's 3 patterns/insights
- Compare AI findings to their own pivot table and chart findings
- Document: what AI confirmed, what was new, what was wrong
- Share discrepancies with class
- **Good finding:** "AI said Region X had the highest growth rate, but my line chart shows it's actually been declining for the last 3 months. AI only looked at the total, not the trend."
- **Needs coaching:** "AI was right about everything." → Push: "Check one specific number AI mentioned against your pivot table. Does it match exactly?"

#### Pacing

| Segment | Time |
|---------|------|
| Setup + prompt | 3 min |
| Generate AI response | 5 min |
| Compare AI vs. own findings | 12 min |
| Document discrepancies | 5 min |
| 2–3 students share | 5 min |

#### Teacher Tip

> AI will almost certainly make at least one error or oversimplification per student's data. If a student genuinely can't find one, ask them: "Did AI mention the data quality issues you found during cleaning? Did it account for the duplicates you removed?" AI rarely catches data quality problems.

#### Check for Understanding

**Cold call:** "Maria, what did AI get wrong — or what did it miss that you caught?"
**Success criterion:** Every student should identify at least one discrepancy between AI output and their own analysis.
**If a student found zero discrepancies:** They probably didn't check carefully. Pair them with someone who found a clear error.

---

### 4:25–4:45 | Day 1 Data Brief (20 min)

**Format:** Individual writing + pair delivery | **GRR Phase:** You Do Alone → You Do Together | **Bloom's:** Create

#### TEACHER DOES

> **SAY:** "Everything you've done today — cleaning data, building pivot tables, making charts, checking AI — comes down to this. Can you explain what you found to someone who wasn't in this room?"

> **SAY:** "Write a 3-sentence data brief. That's it. Three sentences. Here's the structure:"

**Project on screen:**
```
Sentence 1: "The data shows [what happened]."
Sentence 2: "This matters because [why it's significant]."
Sentence 3: "I recommend [what to do next]."
```

> **SAY:** "Example: 'The data shows that repeat customers generate 3x more revenue than new customers in the Chișinău region. This matters because our marketing budget is split equally between acquisition and retention. I recommend shifting 60% of the budget to retention programs.'"

> **SAY:** "Write yours. 7 minutes. Then you'll read it aloud to your partner."

- Circulate. Watch for:
  - Students who lead with methodology ("First I cleaned the data, then I built a pivot table...") → Redirect: "Start with the finding, not the process."
  - Students who are too vague ("The data shows some interesting patterns") → Push: "What specific finding? Give me a number."

> **SAY (after 7 min):** "Read your brief aloud to your partner. Partners: give one piece of feedback — is the finding clear? Is the recommendation actionable?"

**Data English Playbook:**

> **SAY:** "Last thing. Open a new doc and title it 'Data English Playbook.' Write down 10 terms you learned today that help you talk about data in English. Things like 'pivot table,' 'outlier,' 'data brief,' 'truncated axis.' This is your personal glossary. You'll add to it every session."

#### STUDENTS DO

- Write a 3-sentence data brief (7 min)
- Read aloud to partner (2 min each = 4 min)
- Give and receive feedback (1 min)
- Start Data English Playbook with 10 terms (5 min)

#### Pacing

| Segment | Time |
|---------|------|
| Teach structure + example | 3 min |
| Write 3-sentence brief | 7 min |
| Read aloud to partner + feedback | 5 min |
| Start Data English Playbook | 5 min |

#### Teacher Tip

> The data brief IS the exit ticket for today. It tests SWBAT #6 directly. Read a few over students' shoulders — if briefs lead with the finding (not the methodology), the lesson worked.

#### Check for Understanding

**Read 2–3 briefs aloud to the class.** Ask: "Can you act on this recommendation? Is the finding specific enough?" The class evaluates.
**Success criterion:** Brief leads with a specific finding (a number, a comparison, a trend), explains significance, and ends with a concrete recommendation.

---

### 4:45–5:15 | Day 1 Wrap (30 min)

**Format:** Full group, reflective | **GRR Phase:** We Do | **Bloom's:** Evaluate (metacognition)

#### TEACHER DOES

> **SAY:** "Let's see how far you've come in one day."

**Data Confidence Self-Assessment:**

> **SAY:** "Rate yourself 1–5 on each of these. Be honest — this is your baseline. We'll do this again on Day 4."

**Project:**
```
1. Reading data (understanding charts, tables, reports):     ___/5
2. Cleaning data (finding and fixing problems):              ___/5
3. Analyzing data (pivot tables, formulas, patterns):        ___/5
4. Communicating data (writing briefs, explaining findings): ___/5
```

> **SAY:** "Anyone want to share? Where did you start this morning vs. where are you now?"

- Call on 2–3 students. Celebrate growth.

**Mid-week assignment preview:**

> **SAY:** "Between now and Day 2, here's your assignment. 5 steps."

**Project:**
```
1. Find a real dataset relevant to your work or life
   (government data, your company's data, public datasets)
2. Clean it using what you learned today
3. Build at least 2 pivot tables and 2 charts
4. Write a 3-sentence data brief about what you found
5. Bring it to Day 2 — you'll present it to the class
```

> **SAY:** "Where to find data: Moldova's statistics bureau (statistica.md), Georgia's GeoStat (geostat.ge), World Bank Open Data, your own organization's reports. If you're stuck, message me."

- Walk through each step. Answer questions.

#### STUDENTS DO

- Complete self-assessment (4 dimensions, 1–5 each)
- Share reflections voluntarily
- Write down mid-week assignment steps
- Ask clarifying questions
- **Good question:** "Can I use data from my own company?" → "Absolutely — that's the best data to use."
- **Concerning question:** "I don't have access to any data." → "Use a public dataset. I'll share 3 links in the group chat."

#### Pacing

| Segment | Time |
|---------|------|
| Self-assessment | 5 min |
| 2–3 students share reflections | 5 min |
| Mid-week assignment walkthrough | 12 min |
| Questions + logistics | 8 min |

#### Teacher Tip

> The self-assessment is critical — it creates the baseline for the Day 4 growth comparison. Make sure every student fills it out. If someone rates themselves 5/5 on everything, gently challenge: "Could you build a dashboard right now? Could you present to a CEO?" Save these for Day 4.

---

### 5:15–5:45 | Buffer / Overflow (30 min)

**Format:** Flexible | **GRR Phase:** N/A

> This block is intentional buffer. Use it for:
> - Students who need extra help with Google Sheets setup or function practice
> - Extended Q&A
> - Individual troubleshooting (AI tool access issues, dataset problems)
> - If everything ran on time, dismiss early: "Great work today. See you next week."

---

## DIFFERENTIATION NOTES (Session-Wide)

**Struggling learners across all blocks:**
- Provide printed step-by-step guides for technical blocks (SORT, FILTER, SUMIF, pivot tables)
- Pair with a stronger partner during independent work
- Reduce the number of required outputs (3 charts → 2 charts; 5 pivot tables → 3 guided + 1 independent)

**Advanced learners across all blocks:**
- Introduce AVERAGEIF, COUNTIFS (multi-criteria) during spreadsheet blocks
- Challenge them to find patterns the instructor didn't mention
- Ask them to help struggling neighbors (peer teaching reinforces their own learning)

**Language support across all blocks:**
- Key terms on whiteboard in English + Romanian throughout the day
- Allow data briefs to be drafted in L1 first, then translated to English
- Pair bilingual students together when possible
- Provide a printed "Data English" glossary at the start of the day

---

## POST-SESSION REFLECTION (For Instructor)

- [ ] What worked well today?
- [ ] What would I adjust for next time?
- [ ] Which students need follow-up before Day 2?
- [ ] Did timing work? Where did I run long/short?
- [ ] Were the datasets appropriate? Any access issues?
- [ ] Did the AI comparison block reveal genuine discrepancies, or did students just accept AI output?
- [ ] Are self-assessment baselines captured for all students?
