# SESSION 3: "Advanced Analysis & Persuasive Presentation"

**Saturday, Weekend 2 | 10:00 AM – 5:45 PM**
**Theme:** Advanced techniques, real-world complexity, and presenting data under adversarial questioning.

---

## Learning Targets

By the end of this session, students will be able to:

1. **Add** context to data using benchmarking, trending, and segmentation (Bloom's: Analyze)
2. **Build** a 6-month forecast using accessible methods (Bloom's: Apply → Create)
3. **Define** actionable KPIs that distinguish vanity from value (Bloom's: Evaluate)
4. **Present** data findings under adversarial stakeholder questioning (Bloom's: Evaluate)
5. **Read and write** basic SQL queries (Bloom's: Apply — stretch goal)
6. **Write** SMART indicators for EU-style reporting (Bloom's: Create)

---

## Materials & Setup

- Laptops with WiFi (Google Sheets + Looker Studio access)
- Students' mid-week assignment datasets and dashboards (brought from home)
- Pre-prepared mini-dataset for the Data Challenge (new, unfamiliar)
- Forecasting template in Google Sheets (pre-built with formulas — students change assumptions)
- Browser-based SQL playground: SQLite Online (https://sqliteonline.com) or DB Fiddle (https://www.db-fiddle.com)
- Pre-loaded SQL database with a simple 3-table dataset (customers, orders, products)
- Printed KPI worksheet (1 per student)
- Printed SMART indicator template (1 per student)
- Printed capstone planning template (1 per team)
- 4 capstone option briefs (printed, 1 set per student)
- Slides deck (Session 3)
- Timer (visible — critical for the stakeholder panels)
- Whiteboard + markers

---

## Assessment at a Glance

| Method | Description |
|--------|-------------|
| **Formative** | Observe forecasting builds, KPI definitions, SQL queries. Listen to stakeholder panel presentations for clarity under pressure. |
| **Self-Assessment** | Data confidence rating compared to Days 1 and 2. |
| **Exit Ticket** | 3 SMART indicators written for a project scenario. |
| **Evidence to look for** | Forecasts use at least 2 methods (not just one). KPIs pass the "can the team influence this?" test. Every student has presented under adversarial Q&A at least once. SQL queries return correct results for SELECT/WHERE/GROUP BY. |

---

## MORNING BLOCK (10:00–1:05)

---

### 10:00–10:15 | Data Challenge (Retrieval) (15 min)

**Format:** Individual, timed | **GRR Phase:** You Do Alone | **Bloom's:** Apply

#### TEACHER DOES

> **SAY:** "Day 3. Same drill — new dataset, 10 minutes, pivot table + chart + English insight. No notes. Let's see how much faster you are compared to Day 2."

- **Project the link** to a new mini-dataset (e.g., monthly tourism data for 3 Georgian cities — arrivals, revenue, seasonality).

> **SAY:** "Go. Timer starts now."

- Circulate silently. Note improvements in speed and confidence vs. Day 2.

> **SAY (at 10 min):** "Stop. How many finished all three?" Count hands. Compare to Day 2 count.

> **SAY:** "Day 2, [X] people finished. Today, [Y] people finished. That's growth. The skill is becoming automatic — which is exactly what we want."

#### STUDENTS DO

- Open unfamiliar dataset
- Build pivot table + chart + 1-sentence English insight in 10 minutes
- Compare own performance to Day 2

#### Pacing

| Segment | Time |
|---------|------|
| Instructions + distribute link | 2 min |
| Timed challenge | 10 min |
| Debrief (compare to Day 2) | 3 min |

#### Teacher Tip

> Track the numbers across days. On Day 4, you'll show the growth trajectory: "Day 2: 4 students finished. Day 3: 10 students. Day 4: 16 students." This is powerful evidence of learning.

---

### 10:15–10:50 | "In the Wild" Debrief (35 min)

**Format:** Full group, 2 min each | **GRR Phase:** You Do Together → We Do | **Bloom's:** Evaluate

#### TEACHER DOES

> **SAY:** "Between Day 2 and today, you went out and found real data in the wild. Now tell us what you found."

> **SAY:** "Rules: 2 minutes max. Tell us: What data did you find? What story did it tell? What was the hardest part? I have a timer and I WILL cut you off at 2 minutes."

- Start the visible timer. Call on students one by one.

- **After each presentation, give 15 seconds of feedback:**
  - "Strong finding — the number was specific."
  - "Good story arc — you had a clear conflict."
  - "Next time, lead with the insight, not the process."

- After all students have shared, highlight patterns:

> **SAY:** "I noticed three things across everyone's presentations: [1] Most of you found messy data — which means Day 1's cleaning lesson was relevant. [2] Several of you found surprises in the data — that's the conflict in your story. [3] A few of you are still leading with methodology instead of findings — we'll fix that today in the stakeholder panel."

#### STUDENTS DO

- Present their mid-week project in 2 minutes: what data, what story, what was hard
- Listen to peers and note interesting findings
- Receive brief feedback from instructor

#### Pacing

| Segment | Time |
|---------|------|
| 15–18 students × 2 min each | 30–36 min |
| Instructor commentary on patterns | 2–5 min |

#### Teacher Tip

> Keep the timer ruthless. If a student hits 2 minutes, say "Thank you — great start. We'll hear more in the stakeholder panel." Students learn to be concise when the constraint is real.

#### Check for Understanding

**Observation:** Did students find real data? Did they apply Day 1–2 skills (cleaning, pivot tables, charts, briefs)? If any student didn't do the assignment, pair them with someone who did for the rest of the day.

---

### 10:50–11:20 | Benchmarking & Context (30 min)

**Format:** Interactive lecture + hands-on | **GRR Phase:** I Do → We Do → You Do | **Bloom's:** Analyze

#### TEACHER DOES

> **SAY:** "A number by itself means nothing. Let me prove it."

- Write on whiteboard: **"Revenue: 50,000 MDL"**

> **SAY:** "Is that good or bad? You can't tell. Now watch."

- Add context lines:
```
Revenue: 50,000 MDL
Industry average: 35,000 MDL    → We're above average ✓
Last quarter: 65,000 MDL        → We're declining ✗
Top performer: 120,000 MDL      → We're far from the best ✗
```

> **SAY:** "Same number. Three different stories depending on the context. This is why we need benchmarking, trending, and segmentation."

**Technique 1: Benchmarking**

> **SAY:** "Benchmarking means comparing your number to a reference point — an industry average, a competitor, a national standard. It answers: 'How do we compare?'"

- Demo: Add an "Industry Average" row to a pivot table. Calculate the difference.

**Technique 2: Trending**

> **SAY:** "Trending means looking at how a number changes over time. It answers: 'Are we getting better or worse?'"

- Demo: Create a line chart with 6 months of data. Add a trendline. "See that downward slope? One quarter's number might look fine — but the trend tells you it's declining."

**Technique 3: Segmentation**

> **SAY:** "Segmentation means breaking an average into groups. It answers: 'Does the average hide important differences?'"

- Demo: "Average customer revenue is 500 MDL. But new customers spend 200 MDL and repeat customers spend 800 MDL. The average lies. Segmentation reveals the real story."

> **SAY:** "Now add context to your own data. Pick one key finding from your dashboard. Add at least one benchmark, one trend observation, or one segmentation insight. You have 10 minutes."

#### STUDENTS DO

- Watch the 3 techniques with examples
- Add context layers to one finding from their own data (10 min)
- **Good work:** "Our program completion rate is 37%. The sector average in Moldova is 45%. We're below benchmark and the trend is flat — we need to investigate."
- **Needs coaching:** Stating a number without comparison → "Compared to what? Is 37% good or bad? Find a benchmark."

#### Pacing

| Segment | Time |
|---------|------|
| "50,000 MDL" demonstration | 4 min |
| Benchmarking technique + demo | 5 min |
| Trending technique + demo | 5 min |
| Segmentation technique + demo | 4 min |
| Students add context to own data | 10 min |
| Transition | 2 min |

#### Teacher Tip

> The "50,000 MDL" opening is the most memorable moment of this block. Students will remember that a number alone means nothing. Reference this throughout the day: "Where's your benchmark?"

#### Check for Understanding

**Cold call:** "Diana, what context did you add to your finding? Is your number above or below the benchmark?"
**If student didn't find a benchmark:** Help them Google one: "What's the industry average for [their metric]? Try statistica.md or a World Bank report."

#### Differentiation

- **Struggling learners:** Focus on just one technique (benchmarking — it's the most intuitive). Provide example benchmarks for common datasets.
- **Advanced learners:** Add all three layers to their finding and write a 1-sentence summary that includes the benchmark, trend, and segment.
- **Language support:** "Benchmark = punct de referință. Trend = tendință. Segment = segment."

---

### 11:20–11:50 | Forecasting for Non-Statisticians (30 min)

**Format:** Hands-on | **GRR Phase:** I Do → We Do → You Do | **Bloom's:** Apply → Create

#### TEACHER DOES

> **SAY:** "You can now look backward (what happened) and sideways (how do we compare). Now let's look forward. Forecasting sounds scary — but I'm going to teach you 3 methods that anyone can use in a spreadsheet."

**Method 1: Trend Extrapolation**

> **SAY:** "The simplest forecast: assume the trend continues. If revenue grew 5% per month for the last 6 months, project that forward."

- **Demo in Google Sheets:** Show 6 months of data. Add a formula: `=previous_month * 1.05` for 6 more months.

> **SAY:** "When does this work? When the trend is stable and nothing big is changing. When does it fail? When there's a disruption — a pandemic, a new competitor, a policy change."

**Method 2: Scenario Modeling (Best / Worst / Most Likely)**

> **SAY:** "More realistic: build three scenarios."

- **Demo:** Copy the trend extrapolation. Create 3 versions:
  - Best case: 8% growth
  - Most likely: 5% growth
  - Worst case: -2% decline

> **SAY:** "Now you have a range, not a single number. Decision-makers love ranges because they show you've thought about uncertainty."

**Method 3: Unit Economics Projection**

> **SAY:** "Most granular: forecast from the bottom up. How many customers × average order value × purchase frequency = revenue."

- **Demo:** Quick example with numbers.

> **SAY:** "Now open the forecasting template I've shared. It has the formulas pre-built. Your job: change the assumptions to match your data. Build a 6-month forecast using trend extrapolation. Then add scenario modeling. You have 18 minutes."

#### STUDENTS DO

- Watch 3 methods demonstrated
- Open pre-built forecasting template
- Build a 6-month forecast using trend extrapolation (guided, 10 min)
- Add scenario modeling (independent, 8 min)
- **Good forecast:** Shows best/worst/most likely scenarios with clear assumptions stated
- **Needs help:** Using arbitrary numbers instead of data-driven assumptions → "What was your actual growth rate last quarter? Use THAT as your base."

#### Pacing

| Segment | Time |
|---------|------|
| Teach 3 methods | 10 min |
| Guided build: trend extrapolation | 10 min |
| Independent build: scenario modeling | 8 min |
| Transition | 2 min |

#### Teacher Tip

> The template is essential. Do NOT expect students to build forecast formulas from scratch. Provide a pre-built spreadsheet where they only change the assumptions (growth rate, number of customers, average order). The learning objective is forecasting THINKING, not Excel gymnastics.

#### Check for Understanding

**Show Me:** "Show me your 3 scenarios. What growth rate did you use for best case? Where did that number come from?"
**Reteach trigger:** If a student used made-up numbers → "Go back to your data. What was the ACTUAL growth rate? Use that as your base, then adjust up and down."

---

### 11:50–12:05 | Break (15 min)

> ☕ **BREAK** — "After break: KPIs, then the stakeholder panel. Start thinking about your 2-minute pitch."

---

### 12:05–12:35 | KPI Workshop (30 min)

**Format:** Interactive lecture + individual exercise | **GRR Phase:** I Do → We Do → You Do | **Bloom's:** Evaluate

#### TEACHER DOES

> **SAY:** "KPI stands for Key Performance Indicator. But most 'KPIs' people track are vanity metrics — numbers that look good but don't drive decisions."

> **SAY:** "Let me show you the difference."

**Project:**
```
VANITY METRICS (feel good, don't help):
• Website visitors: 10,000/month — so what? Are they buying?
• Social media followers: 5,000 — so what? Are they engaging?
• Total revenue: growing — so what? Is profit growing too?

ACTIONABLE KPIs (drive decisions):
• Conversion rate: 3% of visitors buy → optimize the checkout page
• Customer retention rate: 60% → invest in loyalty programs
• Revenue per employee: 15,000 MDL → benchmark against industry
```

> **SAY:** "A good KPI passes 4 tests:"

**Project the 4-test framework:**
```
1. SPECIFIC: Measures one thing, not everything
2. MEASURABLE: You can actually calculate it with data you have
3. ACTIONABLE: The team can influence it (not GDP or weather)
4. DECISION-DRIVING: If this number changes, you'd change your strategy
```

> **SAY:** "Now define 3 KPIs for your project or organization. Use the worksheet. For each KPI, write: what it measures, how you calculate it, what the target is, and what you'd do if you missed the target."

- Circulate. Watch for:
  - Students who pick metrics they can't influence → "Can your team actually change this number? If not, it's not a KPI for you."
  - Students who pick too many → "Pick the 3 most important. If everything is a priority, nothing is."

> **SAY (after 12 min):** "Share one KPI with your partner. Partners: challenge it — does it pass all 4 tests?"

#### STUDENTS DO

- Learn vanity vs. actionable distinction
- Learn the 4-test framework
- Define 3 KPIs for their project (12 min)
- Partner challenge: test each KPI against the 4 criteria (5 min)
- Refine based on partner feedback

#### Pacing

| Segment | Time |
|---------|------|
| Vanity vs. actionable + examples | 7 min |
| 4-test framework | 5 min |
| Students define 3 KPIs | 12 min |
| Partner challenge | 5 min |
| Transition | 1 min |

#### Teacher Tip

> The partner challenge is where the real learning happens. Students often define KPIs that sound good but fail the "actionable" test. A partner saying "But can YOU influence Moldova's GDP?" forces a rewrite.

#### Check for Understanding

**Cold call:** "Giorgi, give me one of your KPIs. Class, does it pass the 4 tests?"
**Expected:** KPI is specific, measurable, within the team's influence, and would trigger a decision if it changed.

---

### 12:35–1:05 | Mock Stakeholder Panel — Round 1 (30 min)

**Format:** Presentations + adversarial Q&A | **GRR Phase:** You Do Alone (presenting) + We Do (Q&A) | **Bloom's:** Evaluate

#### TEACHER DOES

> **SAY:** "This is the moment. You're going to present your data to stakeholders who don't care about your process. They care about the answer."

> **SAY:** "Rules: 2 minutes to pitch. Then 1 minute of tough questions. Format:"

**Project:**
```
YOUR 2-MINUTE PITCH:
1. One headline: what did you find? (10 seconds)
2. One chart: the most important visual (30 seconds)
3. Context: benchmark or trend (20 seconds)
4. Recommendation: what should we do? (30 seconds)
5. Confidence: how sure are you, and what's the risk? (30 seconds)
```

> **SAY:** "Panel questions will include:"

**Project:**
```
"Where did you get this data?"
"What are you NOT showing me?"
"How confident are you in this number?"
"What happens if you're wrong?"
"Why should I trust this over my own experience?"
```

> **SAY:** "I'll be one panelist. I need 2 volunteers to be panelists with me. Your job: be skeptical, interrupt, push back."

- Select 2 student panelists (rotate them for Round 2).
- Call presenters one by one. Strict timer: 2 min pitch, 1 min Q&A, 30 sec transition.

- **After each presenter, give 10-second feedback:** "Strong headline." "Lead with the chart next time." "Your recommendation was specific — good."

#### STUDENTS DO

- Present their data findings in 2 minutes (8–9 students)
- Defend under adversarial questioning (1 min each)
- Watch peers and take notes on what works
- **Strong presentation:** "Revenue in our southern region dropped 15% while the north grew 8%. If we shift 20% of marketing spend south, our model shows recovery within 2 quarters. The risk: the decline could be seasonal, so I recommend a 3-month pilot before full reallocation."
- **Needs coaching:** Reading off slides, leading with methodology, unable to answer "so what?"

#### Pacing

| Segment | Time |
|---------|------|
| Setup + explain rules | 2 min |
| 8–9 students × 3.5 min (2 min pitch + 1 min Q&A + 30 sec transition) | 28–31.5 min |

#### Teacher Tip

> The adversarial Q&A is where confidence builds. Students who survive tough questions realize they know more than they thought. Be tough but fair — challenge the data, not the student.

#### Check for Understanding

**The presentation IS the assessment.** Note which students: lead with findings (good), include context (good), have a recommendation (good), handle tough questions (great) vs. freeze or ramble (needs coaching).

---

### 1:05–2:00 | Lunch (55 min)

> 🍽 **LUNCH** — "Round 1 is done. After lunch: we'll analyze what went wrong, then Round 2. Every one of you will present today."

---

## AFTERNOON BLOCK (2:00–5:45)

---

### 2:00–2:25 | Presentation Autopsy (25 min)

**Format:** Full group discussion | **GRR Phase:** We Do | **Bloom's:** Evaluate

#### TEACHER DOES

> **SAY:** "Let's debrief Round 1. I saw some great presentations and some common mistakes. Let's name them so Round 2 is better."

**Project the common mistakes (with fixes):**

```
MISTAKE 1: Too much data
  "I analyzed 500 rows and found 12 interesting things..."
  FIX: Pick ONE insight. The most important one. Save the rest for questions.

MISTAKE 2: Not enough context
  "Revenue is 50,000 MDL."
  FIX: "Revenue is 50,000 MDL — 15% above the industry benchmark."

MISTAKE 3: Reading the chart aloud
  "As you can see, the blue bars show revenue by region..."
  FIX: The chart should speak for itself. Tell me what it MEANS, not what it shows.

MISTAKE 4: The deadly "As you can see..."
  FIX: Replace with "The key takeaway is..." or "This tells us that..."

MISTAKE 5: No recommendation
  "The data is interesting."
  FIX: "Based on this, I recommend [specific action] by [specific date]."

MISTAKE 6: Freezing under questions
  FIX: "That's a great question. Based on the data, [answer]. If I had more time,
  I'd also look at [related analysis]."
```

> **SAY:** "Which of these did YOU notice in Round 1? Let's discuss."

- Open discussion. Let students call out what they observed. Add your own observations.

> **SAY:** "Round 2 presenters: you now have an advantage. You've seen what works and what doesn't. Use it."

#### STUDENTS DO

- Review the 6 common mistakes
- Identify which mistakes they saw in Round 1
- Discuss fixes as a group
- Round 2 presenters mentally revise their pitch

#### Pacing

| Segment | Time |
|---------|------|
| Present 6 mistakes + fixes | 12 min |
| Group discussion: what they observed | 8 min |
| Round 2 prep reminder | 3 min |
| Transition | 2 min |

#### Teacher Tip

> Be specific but kind. "In Round 1, three presenters started with 'So I cleaned the data...' — in Round 2, I want every presenter to start with their headline finding. Can we agree on that?"

---

### 2:25–3:05 | Mock Stakeholder Panel — Round 2 (40 min)

**Format:** Presentations + adversarial Q&A | **GRR Phase:** You Do Alone | **Bloom's:** Evaluate

#### TEACHER DOES

> **SAY:** "Round 2. Remaining presenters — you've seen Round 1 and the autopsy. Show us what you learned."

- Same format: 2 min pitch + 1 min Q&A + 30 sec transition.
- Rotate student panelists (use students who presented in Round 1 — they're now experts at asking tough questions).
- 9–10 students present.

> **SAY (after all presentations):** "Compare Round 1 and Round 2. What improved?"

- Debrief briefly. Celebrate growth.

#### STUDENTS DO

- Present their data findings under adversarial Q&A (9–10 students)
- Round 1 presenters serve as panelists
- All students observe and compare quality across rounds

#### Pacing

| Segment | Time |
|---------|------|
| 9–10 students × 3.5 min | 31.5–35 min |
| Cross-round comparison debrief | 5 min |

#### Teacher Tip

> Round 2 is almost always better than Round 1. Name this explicitly: "The Presentation Autopsy worked. You learned from watching each other. That's peer learning in action."

#### Check for Understanding

**Observe:** Do Round 2 presenters lead with findings (not methodology)? Do they include context? Do they have recommendations? If the majority do, the Autopsy block worked.

---

### 3:05–3:20 | Break (15 min)

> ☕ **BREAK** — "After break: SQL, EU frameworks, AI + data, and capstone kickoff."

---

### 3:20–3:50 | SQL Taster (30 min)

**Format:** Hands-on, guided | **GRR Phase:** I Do → We Do → You Do | **Bloom's:** Apply

#### TEACHER DOES

> **SAY:** "SQL — Structured Query Language. Every database in the world speaks it. You don't need to become an expert — but after this block, you'll know what SQL does, why it matters, and how to read a basic query."

> **SAY:** "Open your browser. Go to sqliteonline.com. You'll see a pre-loaded database with 3 tables: Customers, Orders, and Products."

- Wait for everyone to get in.

**Query 1: SELECT (reading data)**

> **SAY:** "The most basic SQL command: SELECT. It means 'show me this data.' Watch."

- **Demo:**
```sql
SELECT name, email, city
FROM customers;
```

> **SAY:** "That says: show me the name, email, and city from the customers table. Try it — type it in and hit Run."

- Wait for everyone to see results.

**Query 2: WHERE (filtering)**

> **SAY:** "Now let's filter. Only customers from Chișinău."

- **Demo:**
```sql
SELECT name, email
FROM customers
WHERE city = 'Chișinău';
```

> **SAY:** "WHERE is like the filter in Google Sheets. Same idea, different syntax. Try it — filter for a different city."

**Query 3: GROUP BY (aggregating)**

> **SAY:** "This is the SQL version of a pivot table."

- **Demo:**
```sql
SELECT city, COUNT(*) as total_customers, SUM(total_spent) as revenue
FROM customers
GROUP BY city
ORDER BY revenue DESC;
```

> **SAY:** "That says: group customers by city, count how many are in each city, and add up their spending. Then sort by revenue, highest first. This is a pivot table — in one line of code."

> **SAY:** "Now try writing your own. Pick any question about the data and answer it with a query. You have 8 minutes."

- Circulate. Help with syntax errors (missing semicolons, wrong quotes, misspelled column names).

> **SAY (after 8 min):** "Who wrote a query that surprised them? Share it."

- Call on 2–3 students.

> **SAY:** "You now speak SQL. Basic SQL, but SQL. When someone says 'we need to pull this from the database,' you understand what that means. And if you want to go deeper, there are free courses online. But for this bootcamp, what you just learned is enough."

#### STUDENTS DO

- Open SQL playground
- Run SELECT query (follow along)
- Run WHERE query (follow along, then modify)
- Run GROUP BY query (follow along, then modify)
- Write their own query (8 min independent)
- Share interesting findings
- **Good query:** `SELECT product_category, AVG(order_value) as avg_order FROM orders GROUP BY product_category ORDER BY avg_order DESC;`
- **Stuck:** Syntax error → Check for missing semicolons, wrong quotes, misspelled column names.

#### Pacing

| Segment | Time |
|---------|------|
| Intro + open SQL playground | 3 min |
| SELECT demo + practice | 5 min |
| WHERE demo + practice | 5 min |
| GROUP BY demo + practice | 5 min |
| Independent query writing | 8 min |
| 2–3 students share | 4 min |

#### Teacher Tip

> The goal is demystification, not proficiency. If a student writes one working query, they've succeeded. Don't push for joins, subqueries, or anything advanced. This is a taster.

#### Check for Understanding

**Show Me:** "Show me one query you wrote and the results it returned." Student should be able to explain what the query does in plain English.
**If a student is completely lost:** Pair them with someone who's got it. "Just watch and ask questions. You're building familiarity, not mastery."

#### Differentiation

- **Struggling learners:** Follow along only. Don't attempt independent queries — just successfully run the 3 guided ones.
- **Advanced learners:** Try a JOIN: `SELECT customers.name, orders.total FROM customers JOIN orders ON customers.id = orders.customer_id;`
- **Language support:** SQL is English-based, which helps. "SELECT = selectează. WHERE = unde. GROUP BY = grupează după."

---

### 3:50–4:20 | EU/International Reporting Frameworks (30 min)

**Format:** Interactive lecture + exercise | **GRR Phase:** I Do → We Do → You Do | **Bloom's:** Apply → Create

#### TEACHER DOES

> **SAY:** "If you work with EU-funded projects — or if Moldova continues on its EU accession path — you need to know how international organizations measure impact. It's different from business KPIs."

> **SAY:** "The tool is called a Logical Framework Matrix — or logframe. It's how every EU project reports results."

**Project a simplified logframe:**

```
LEVEL          | INDICATOR              | TARGET    | DATA SOURCE
━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━┿━━━━━━━━━━┿━━━━━━━━━━━━
Impact         | Youth unemployment     | ↓ 5%      | National stats
(long-term)    | rate in target region  |           |
───────────────┼───────────────────────┼──────────┼────────────
Outcome        | % of participants     | 70%       | Program records
(medium-term)  | employed within 6 mo  |           |
───────────────┼───────────────────────┼──────────┼────────────
Output         | # of participants     | 200       | Attendance logs
(short-term)   | completing training   |           |
───────────────┼───────────────────────┼──────────┼────────────
Activity       | # of training sessions| 40        | Schedule
(what you do)  | delivered             |           |
```

> **SAY:** "Every indicator must be SMART:"

**Project:**
```
S = Specific:    What exactly are you measuring?
M = Measurable:  Can you put a number on it?
A = Achievable:  Is the target realistic?
R = Relevant:    Does it actually measure what matters?
T = Time-bound:  By when?
```

**Bad vs. good indicators:**

```
BAD:  "Improve youth employment" — not specific, not measurable, not time-bound
GOOD: "Increase the percentage of program graduates employed within 6 months
       from 45% to 70% by December 2026"
```

> **SAY:** "Now write 3 SMART indicators for this scenario:"

**Project scenario:** "You're running an EU-funded digital literacy program in rural Moldova. 150 participants over 12 months. Write an output indicator, an outcome indicator, and an impact indicator."

#### STUDENTS DO

- Learn the logframe structure (impact → outcome → output → activity)
- Learn SMART criteria
- Write 3 SMART indicators for the scenario (12 min)
- Share 1 indicator with the class
- **Good indicator:** "By December 2026, 120 out of 150 participants (80%) will demonstrate basic digital literacy as measured by a standardized assessment scoring ≥70%."
- **Needs work:** "Participants will be more digitally literate." → Push: "How many? By when? How will you measure 'more literate'?"

#### Pacing

| Segment | Time |
|---------|------|
| Logframe structure | 8 min |
| SMART criteria + good vs. bad examples | 5 min |
| Students write 3 indicators | 12 min |
| 2–3 students share | 3 min |
| Transition | 2 min |

#### Teacher Tip

> This block is a differentiator for students working in NGOs, government, or EU-adjacent roles — which is many students in Moldova. Frame it as: "This is the language that gets projects funded. If your indicator isn't SMART, your donor will send it back."

#### Check for Understanding

**Partner review:** "Swap indicators with your partner. Check: is each one Specific? Measurable? Achievable? Relevant? Time-bound? Circle any that fail a criterion."

---

### 4:20–4:45 | AI + Data Literacy (25 min)

**Format:** Interactive discussion + hands-on | **GRR Phase:** I Do → We Do | **Bloom's:** Evaluate

#### TEACHER DOES

> **SAY:** "On Day 1, you used AI to spot patterns in your data. Some of you found AI was helpful. Some found it was wrong. Today, let's talk about what AI changes about data literacy — and what it doesn't."

> **SAY:** "Here's the new skill stack:"

**Project:**
```
OLD DATA LITERACY: Clean → Analyze → Visualize → Communicate
NEW DATA LITERACY: Ask the right question → Prompt AI → VALIDATE the answer
                   → Communicate with context AI can't provide
```

> **SAY:** "The skills that matter MORE with AI:"
```
1. Knowing WHAT to ask (AI can analyze, but it can't ask the right question)
2. Validating answers (AI will confidently give you wrong numbers)
3. Spotting hallucinated patterns (AI finds patterns that don't exist)
4. Providing context (AI doesn't know your organization, your customers,
   your regional dynamics)
```

> **SAY:** "Quick exercise. Open your AI tool. Upload your dataset and ask:"

**Project:**
```
"What are 3 actionable recommendations based on this data?
For each, rate your confidence level 1-10 and explain what
additional data would increase your confidence."
```

> **SAY:** "Read AI's response. Then evaluate: for each recommendation, would you actually follow it? Why or why not? What context is AI missing?"

- Circulate. Push students to be critical, not accepting.

> **SAY (after 10 min):** "Who found a recommendation they'd actually follow? Who found one that's dangerously wrong? Let's hear both."

#### STUDENTS DO

- Learn the new data literacy skill stack
- Prompt AI with their data (5 min)
- Evaluate AI's recommendations critically (10 min)
- Share findings: what was useful, what was wrong, what context was missing

#### Pacing

| Segment | Time |
|---------|------|
| New skill stack + discussion | 8 min |
| AI prompt exercise | 5 min |
| Critical evaluation | 10 min |
| Share findings (2–3 students) | 5 min |

#### Teacher Tip

> The key message: AI makes data analysis faster, but it doesn't make it correct. The human's job is validation, context, and judgment. Students who internalize this will use AI effectively; students who don't will make expensive mistakes.

#### Check for Understanding

**Discussion:** "Would you send AI's recommendation directly to your boss? Why or why not?" Expected answer: "No — I'd need to verify the numbers and add context about our specific situation."

---

### 4:45–5:15 | Capstone Kickoff (30 min)

**Format:** Instructor-led + team formation | **GRR Phase:** I Do → You Do Together | **Bloom's:** Create

#### TEACHER DOES

> **SAY:** "Day 4 is capstone day. You'll present a complete data analysis to real guests — team leads, finance directors, NGO managers. Let's get you set up."

**Present 4 capstone options:**

```
OPTION A: Business Analysis
Analyze a real business dataset (provided or your own).
Deliverables: Dashboard + memo + 5-minute presentation.

OPTION B: NGO Impact Report
Analyze beneficiary data from an NGO program.
Deliverables: Impact dashboard + logframe indicators + presentation.

OPTION C: Public Data Investigation
Use publicly available data (government stats, World Bank)
to investigate a question about Moldova/Georgia/Armenia.
Deliverables: Dashboard + data story + presentation.

OPTION D: Your Own Data
Bring a dataset from your actual work and analyze it.
Deliverables: Dashboard + memo + presentation.
```

> **SAY:** "Teams of 2–3. Choose your option. You have 15 minutes to form teams and start your capstone planning template."

- Distribute capstone planning templates.
- Circulate. Help teams that can't decide. Push individuals working alone to join a team: "Collaboration is a job skill. Join a team."

> **SAY:** "Fill out the planning template: What data? What question? Who does what? What's your headline hypothesis?"

#### STUDENTS DO

- Review 4 capstone options
- Form teams of 2–3
- Choose a capstone option
- Begin filling out the planning template (data source, question, roles, hypothesis)
- **Good start:** Team chooses Option B, identifies specific NGO data they have access to, divides roles (one analyst, one dashboard builder, one writer/presenter)
- **Needs coaching:** Team can't choose → "Which option is closest to your actual work? Pick that one."

#### Pacing

| Segment | Time |
|---------|------|
| Present 4 options | 8 min |
| Team formation | 5 min |
| Planning template work | 15 min |
| Transition | 2 min |

#### Teacher Tip

> Teams of 2–3 work best. Solo students produce lower-quality capstones because they can't divide the workload. Strongly encourage teaming up.

---

### 5:15–5:30 | Revised Dashboard Sprint (15 min)

**Format:** Individual/team, hands-on | **GRR Phase:** You Do Alone | **Bloom's:** Create

#### TEACHER DOES

> **SAY:** "Quick sprint. Open your Day 2 dashboard. Apply what you learned today: add one benchmark, fix one headline, add one contextual note. 15 minutes. This is practice for the capstone dashboard."

#### STUDENTS DO

- Open Day 2 dashboard in Looker Studio
- Add context (benchmark, trend line, or segmentation)
- Improve headlines
- Save updated version

#### Pacing

| Segment | Time |
|---------|------|
| Sprint | 13 min |
| Save | 2 min |

---

### 5:30–5:45 | Day 3 Wrap (15 min)

**Format:** Full group, reflective | **GRR Phase:** We Do | **Bloom's:** Evaluate

#### TEACHER DOES

> **SAY:** "Quick self-assessment — same 4 dimensions. Compare to Days 1 and 2."

**Project:**
```
                Day 1:  Day 2:  Day 3:
Reading data:    ___     ___     ___
Cleaning data:   ___     ___     ___
Analyzing data:  ___     ___     ___
Communicating:   ___     ___     ___
```

> **SAY:** "Where did you grow the most today? For most of you, I'd guess it's communicating — after the stakeholder panel, you know what it takes to present data under pressure."

- 2–3 students share.

> **SAY:** "Tomorrow is the final day. Capstone build in the morning, showcase in the afternoon. Come ready to work — and ready to impress. Bring your data, your dashboards, and your confidence."

**Data English Playbook update:**

> **SAY:** "Add 10 new terms: benchmark, trend, segmentation, forecast, scenario modeling, KPI, vanity metric, SQL, SELECT/WHERE/GROUP BY, SMART indicator, logframe."

#### STUDENTS DO

- Complete self-assessment (compare across 3 days)
- Share growth observations
- Update Data English Playbook
- Note capstone preparation steps for tonight

#### Pacing

| Segment | Time |
|---------|------|
| Self-assessment | 3 min |
| 2–3 students share | 4 min |
| Playbook update | 3 min |
| Day 4 preview + logistics | 5 min |

---

## DIFFERENTIATION NOTES (Session-Wide)

**Struggling learners:**
- During stakeholder panel: allow 3-minute pitches instead of 2
- For forecasting: use the template exactly as provided, just change one assumption
- For SQL: success = running 3 guided queries, not writing independent ones
- For SMART indicators: provide partially completed examples to modify

**Advanced learners:**
- Challenge them to build a multi-scenario forecast with sensitivity analysis
- SQL: try JOINs and subqueries
- SMART indicators: write a complete logframe (all 4 levels)
- Stakeholder panel: serve as panelists and ask tough questions

**Language support:**
- Stakeholder pitches can be rehearsed in L1 first, then delivered in English
- SMART indicators can be drafted in L1 and translated
- SQL keywords are English-based (advantage for English practice)
- Data English Playbook now has 30+ terms — review together

---

## POST-SESSION REFLECTION (For Instructor)

- [ ] What worked well today?
- [ ] What would I adjust for next time?
- [ ] Which students need extra support before the capstone?
- [ ] Did timing work? Where did I run long/short?
- [ ] Did the stakeholder panel push students to be concise?
- [ ] Did Round 2 presentations improve after the Autopsy?
- [ ] Were forecasts data-driven or arbitrary?
- [ ] Are capstone teams formed and planning started?
- [ ] Are self-assessment scores showing consistent growth?
