# SESSION 2: "Research, Write, Create"

**Sunday, Weekend 1 | 10:00 AM – 5:45 PM**
**Theme:** AI for research, writing, visual/multimedia creation, and data analysis.

---

## Learning Targets

By the end of this session, students will be able to:

1. **Detect** hallucinations in AI-generated research and fact-check claims systematically
2. **Use** research tools (NotebookLM, Perplexity) to interrogate sources and triangulate information
3. **Collaborate** with AI on writing while preserving their own voice and judgment
4. **Analyze** a dataset using AI and produce a presentable summary of insights
5. **Generate** and iterate on visual content using AI image tools
6. **Build** a simple functional tool by directing AI code generation

---

## Materials & Setup

- Laptop or tablet per student (with WiFi)
- Accounts ready: ChatGPT, Claude, Google account (for NotebookLM)
- Pre-prepared CSV datasets (1 per student — see Data Analysis block)
- Pre-prepared "hallucination cheat sheets" (1 per topic)
- Printed trust rubric template (1 per student)
- Printed comparison template for writing exercise
- Slides deck (Session 2)
- Timer (visible)

---

## Assessment at a Glance

| Method | Description |
|--------|-------------|
| **Formative** | Hallucination scorecards, trust rubrics, writing comparisons, data summaries |
| **Self-Assessment** | Confidence rating (1–5) per learning target at close |
| **Exit Ticket** | See closing section |
| **Evidence** | Scorecards show students caught real fabrications. Writing comparisons show students can articulate what AI changed. Data summaries contain specific, verified findings. |

---

## MORNING BLOCK (10:00–12:00)

---

### 10:00–10:15 | Retrieval Sprint (15 min)

**Format:** Pairs, no notes | **GRR Phase:** We Do

#### TEACHER DOES

> **SAY:** "Good morning! Before anything new, let's see what stuck from yesterday. Pair up with someone you DIDN'T sit with yesterday. I'm going to project 7 questions one at a time. Discuss each with your partner for 1 minute, then I'll reveal the answer. No notes, no phones — just your memory."

**Project questions one at a time:**

| # | Question | Answer |
|---|----------|--------|
| 1 | What does CRAFT stand for? | Context, Role, Audience, Format, Tone |
| 2 | How do LLMs generate text? | By predicting the next token based on patterns in training data |
| 3 | Name one difference between Claude and ChatGPT. | Different training data, different safety boundaries, different strengths (Claude = structured; ChatGPT = creative) |
| 4 | What is chain-of-thought prompting? | Breaking a complex task into a sequence of smaller prompts where each builds on the previous output |
| 5 | What happened when we trained Teachable Machine with biased data? | The model only worked in the conditions it was trained on (same background, same lighting) — it failed in new conditions |
| 6 | What makes a good evaluation rubric for a prompt? | Specific, measurable checkpoints (not vague like "is it good?") — e.g., word count, tone, required info included |
| 7 | Name one ethical concern about AI-generated text. | Bias (gender, racial, cultural stereotypes), hallucinations (made-up facts), privacy risks, replacing human judgment |

> After each question, give pairs 1 minute to discuss, then reveal the answer on screen.

#### STUDENTS DO

- Pair up with a new partner
- Discuss each question for 1 minute without notes
- Self-check against revealed answers

#### Pacing

| Segment | Time |
|---------|------|
| 7 questions × (1 min discuss + 30 sec reveal) | ~11 min |
| Buffer and transition | 4 min |

#### Check for Understanding

**Observe:** Which questions stumped most pairs? Note these — they need reinforcement today.
**If CRAFT is forgotten:** Quick 30-second recap before moving on.

---

### 10:15–10:55 | The Hallucination Hunt (40 min)

**Format:** Pairs, research + fact-check | **GRR Phase:** You Do Together

#### TEACHER DOES

> **SAY:** "Yesterday you learned that AI predicts the next word. But what happens when the AI confidently predicts something that's completely wrong? That's called a hallucination. Today you're going to become hallucination detectives."

> **SAY:** "Each pair will get a regional topic. You'll ask AI to write a 200-word research summary on that topic, then you'll fact-check every specific claim. Here are the topics:"

**Project the topic assignments:**
- **Armenian history pairs:** "Write a 200-word summary of the history of the Armenian alphabet and its cultural significance."
- **Moldovan wine pairs:** "Write a 200-word summary of Moldova's wine industry, including key wine regions and historical milestones."
- **Georgian architecture pairs:** "Write a 200-word summary of Georgian architectural traditions, focusing on churches and fortresses."

> **SAY:** "Step 1: Generate the summary in Claude or ChatGPT. Step 2: Fact-check EVERY specific claim — names, dates, places, statistics. Use Google, Wikipedia, or Perplexity (https://www.perplexity.ai). Step 3: Fill out the Hallucination Scorecard."

**Project the scorecard template:**
```
HALLUCINATION SCORECARD
Topic: _______________
AI Tool Used: _______________

Total specific claims found: ___
Claims verified as TRUE: ___
Claims FABRICATED (hallucinations): ___
Claims AMBIGUOUS (can't verify): ___

Worst hallucination found:
_________________________________

How confident was the AI when it hallucinated? (very/somewhat/not at all)
```

**Known fabrication examples to watch for (instructor cheat sheet — don't share with students):**

*Armenian alphabet:*
- AI may claim Mesrop Mashtots created the alphabet in the wrong year (correct: 405 AD)
- AI may fabricate specific scholars or monasteries that didn't exist
- AI may mix up details about which king commissioned the alphabet

*Moldovan wine:*
- AI may invent specific vineyard names or founding dates
- AI may cite incorrect production statistics
- AI may claim Moldova is the "Nth largest wine producer" with a wrong ranking
- AI may confuse Moldovan regions with Romanian ones

*Georgian architecture:*
- AI may assign wrong construction dates to real churches
- AI may invent architects' names (medieval Georgian architects are mostly unknown)
- AI may confuse Jvari Monastery details with Svetitskhoveli Cathedral

- Circulate during fact-checking. Help pairs who are stuck verifying claims.

> **SAY (after 30 min):** "Time's up! Who found the best hallucination? Share your worst one."

- Have 3–4 pairs share their most egregious hallucination. Project on screen if possible.

> **SAY:** "Key takeaway: AI doesn't know when it's lying. It doesn't have a concept of truth — it has a concept of 'what sounds right based on patterns.' This is why you must ALWAYS fact-check AI output when accuracy matters."

#### STUDENTS DO

- Generate a 200-word AI summary on their regional topic
- Fact-check every specific claim using web search
- Fill out the Hallucination Scorecard
- Share worst hallucination with the class

**Good scorecard:** Found 12 claims, verified 8, found 3 fabricated, 1 ambiguous. Worst hallucination: "AI claimed Mileștii Mici winery was founded in 1947 — the actual date is 1969."

**Weak scorecard:** "Everything looked correct." (Push: "Did you check the dates? The specific names? The statistics?")

#### Pacing

| Segment | Time |
|---------|------|
| Generate AI summary | 5 min |
| Fact-check claims using web search | 20 min |
| Compile hallucination scorecard | 5 min |
| 3–4 pairs share worst hallucination | 8 min |
| Transition | 2 min |

#### Teacher Tip

> Pre-test the prompts yourself and note which claims are fabricated. This lets you confirm student findings quickly and adds credibility: "Yes, that's a known hallucination — good catch!"

#### Check for Understanding

**Question:** "Why does AI hallucinate? Is it trying to deceive you?"
**Expected:** "No — AI doesn't have a concept of truth. It predicts what sounds right based on patterns. It can't tell the difference between a real fact and a plausible-sounding fiction."
**If >25% miss:** Re-explain: "Think of autocomplete. If your phone suggests 'See you at 3pm' it's not checking your calendar — it's guessing what you'd normally type. AI does the same thing, but at a much larger scale."

#### Differentiation

- **Struggling learners:** Provide a fact-checking checklist: (1) Google the name/date/statistic, (2) Check if the Wikipedia article exists, (3) Look for the claim in at least 2 sources.
- **Advanced learners:** Ask them to find a subtle hallucination — one that sounds plausible and would be easy to miss.
- **Language support:** Allow students to fact-check in their native language using local search engines and local Wikipedia.

---

### 10:55–11:40 | Research Tools Deep-Dive (45 min)

**Format:** Instructor demo → Guided hands-on | **GRR Phase:** I Do → We Do

#### TEACHER DOES

**Part 1: NotebookLM (20 min)**

> **SAY:** "You just saw that AI can get facts wrong. What if you could point AI at YOUR documents — sources you trust — and have it answer questions based only on those? That's what NotebookLM does."

> **SAY:** "Open https://notebooklm.google.com — you'll need your Google account."

**Step-by-step demo (project your screen):**

1. "Click 'New Notebook'"
2. "Click 'Add Source' — you can upload a PDF, paste a URL, or paste text"
3. "I'm going to upload a sample document. [Upload a 2-3 page article about AI in education — have this pre-prepared.]"
4. "Now watch — I'll ask it a question about the document."
5. Type: `What are the 3 main arguments in this article?`
6. "See how it gives me an answer WITH citations? It points to the exact paragraph where it found each point. This is how you can trust the output — it shows its sources."
7. "Now try: `What does this article NOT address? What are the gaps?`"
8. "This is powerful — it's not just summarizing, it's analyzing."

> **SAY:** "Now you try. Upload your own source — or use this one I've provided. [Share a Google Drive link to a pre-loaded document for anyone who doesn't have their own.] Ask it 3 questions about the document."

- Give students 8 minutes to explore.

**Part 2: Perplexity (15 min)**

> **SAY:** "NotebookLM works with your documents. Perplexity works with the entire internet. Open https://www.perplexity.ai"

**Demo:**

1. "Watch what happens when I ask Perplexity a research question."
2. Type: `What are the current trends in AI adoption among small businesses in Eastern Europe?`
3. "See the difference from ChatGPT? Perplexity cites its sources with numbered references. You can click each one to verify."

> **SAY:** "Now try the same research question you used in the Hallucination Hunt — ask Perplexity about your topic. Compare its output and sources to what ChatGPT gave you."

- Give students 8 minutes.

> **SAY:** "Quick mention — for audio transcription, two tools worth knowing: Otter.ai (https://otter.ai) for meeting transcription, and Whisper by OpenAI for local, private transcription. We won't demo these today, but add them to your toolkit."

**Closing comparison (5 min):**

> **SAY:** "Take 3 minutes to write down: When would you use NotebookLM vs. Perplexity vs. ChatGPT/Claude?"

**Expected student answers:**
- **NotebookLM:** When I have specific documents I want to analyze — reports, articles, research papers
- **Perplexity:** When I need up-to-date information from the web with cited sources
- **ChatGPT/Claude:** When I need to generate, write, brainstorm, or work with general knowledge

#### STUDENTS DO

- Follow along with NotebookLM demo, then explore independently (upload a source, ask 3 questions)
- Follow along with Perplexity demo, then try their own research question
- Document which tool is better for what (3 min comparison)

#### Pacing

| Segment | Time |
|---------|------|
| NotebookLM demo + follow-along | 20 min |
| Perplexity demo + student try | 15 min |
| Whisper/Otter mention | 2 min |
| Documentation + comparison | 5 min |
| Transition | 3 min |

#### Check for Understanding

**Question:** "What's the key difference between NotebookLM and Perplexity?"
**Expected:** "NotebookLM analyzes your uploaded documents; Perplexity searches the live internet."
**If >25% miss:** Draw it on the board — two circles: "Your docs → NotebookLM" and "The internet → Perplexity"

---

### 11:40–12:00 | Source Triangulation + Trust Rubric (20 min)

**Format:** Individual work | **GRR Phase:** You Do

#### TEACHER DOES

> **SAY:** "You now have 3 research tools — Claude/ChatGPT, NotebookLM, and Perplexity. How do you know when to trust AI output? You build a personal trust rubric."

**Project the starter template:**
```
MY AI TRUST RUBRIC

Score each criterion 1–5 for any AI research output:

1. Does the AI cite sources?                    [ ] / 5
2. Can I verify those sources exist?             [ ] / 5
3. Does the answer hold up across tools?         [ ] / 5
   (Same question in Claude, Perplexity, NotebookLM)
4. Does the answer change when I rephrase?       [ ] / 5
5. Are statistics specific or vague?             [ ] / 5

MY ADDITIONAL CRITERIA:
6. ________________________________              [ ] / 5
7. ________________________________              [ ] / 5
8. ________________________________              [ ] / 5
```

> **SAY:** "Customize this template — keep the first 5 criteria and add 2–3 of your own. Then test it: run one research question through Claude, Perplexity, and NotebookLM. Score each tool using your rubric."

#### STUDENTS DO

- Customize the trust rubric (add 2–3 personal criteria) — 5 min
- Run one research question through 3 tools — 10 min
- Score each tool using the rubric — 5 min

**Good custom criteria examples:**
- "Does the AI acknowledge uncertainty or say 'I'm not sure'?"
- "Does the output include dates that I can cross-reference?"
- "Does the AI give a balanced view or only one perspective?"

#### Pacing

| Segment | Time |
|---------|------|
| Customize rubric template | 5 min |
| Test one question across 3 tools | 10 min |
| Score and compare | 5 min |

#### Check for Understanding

**Question:** "Which tool scored highest on your trust rubric, and why?"
**Expected:** Students give a specific answer with reasoning — e.g., "Perplexity scored highest because it cited real sources I could verify."

---

### 12:00–12:15 | BREAK (15 min)

---

### 12:15–1:00 | Writing with AI (Combined Block) (45 min)

**Format:** Individual writing → AI interaction → Pair comparison → Group debrief | **GRR Phase:** You Do → You Do Together → We Do

#### TEACHER DOES

> **SAY:** "This next block is about writing. Not AI writing FOR you — AI writing WITH you. There's a huge difference, and by the end of this block, you'll know exactly where AI helps your writing and where it hurts it."

**Phase 1 — Write Without AI (15 min)**

> **SAY:** "Step 1: Write 150–200 words on a topic of your choice. A professional email, a blog intro, a LinkedIn post, a cover letter paragraph — anything you'd actually write at work. Write it yourself. No AI. You have 15 minutes."

- Let students write. Circulate silently.

**Phase 2 — AI Interaction (10 min)**

> **SAY:** "Step 2: Now take your writing and do two things:"
> 1. "Ask AI to 'improve' your writing. Paste your text and prompt: 'Improve this writing. Make it clearer and more professional.'"
> 2. "Then ask AI to help at only ONE stage — brainstorm, outline, OR edit. You pick which stage."

> **SAY:** "When you're done, you should have 3 versions:"
> - "Version A: Your original writing (no AI)"
> - "Version B: AI-'improved' version"
> - "Version C: Your writing with AI help at one specific stage"

**Phase 3 — Pair Comparison (10 min)**

> **SAY:** "Pair up. Read each other's 3 versions. Then answer these questions together:"
> - "Which version is 'most you' — which one sounds like the real person?"
> - "Which version is the best writing?"
> - "Are those the same version? If not, what does that tell you?"

**Phase 4 — Group Debrief (10 min)**

- Ask 3–4 students to share insights.

> **SAY:** "Here's the key takeaway: AI is most useful as a collaborator at specific stages, not as a replacement for your voice. When you ask AI to 'improve' your writing, it often strips out your personality and makes everything sound the same. But when you use AI at one specific stage — brainstorming ideas, organizing an outline, or polishing grammar — you keep your voice and get the AI's strengths."

**Worked Example (show on screen):**

```
VERSION A (Original — human only):
"I've been thinking about how our team handles client feedback.
Right now it's a mess — emails, Slack messages, sticky notes.
Nobody knows what's been addressed and what hasn't. I think we
need a simple system. Nothing fancy. Just one place where
feedback goes and someone is responsible for each item."

VERSION B (AI "improved"):
"I would like to propose an enhancement to our current client
feedback management workflow. At present, client feedback is
dispersed across multiple communication channels, leading to
potential oversight and inefficiency. I recommend implementing
a centralized feedback tracking system that would consolidate
all client communications and assign clear ownership for each
action item."

VERSION C (Human + AI for editing only):
"I've been thinking about how our team handles client feedback.
Right now, it's scattered across emails, Slack, and sticky notes,
and nobody knows what's been addressed. I think we need one simple
place where all feedback goes, with someone responsible for each
item. Nothing fancy — just clarity and accountability."
```

> **SAY:** "Version A is authentic but rough. Version B is polished but sounds like a corporate robot — it lost the person's voice. Version C is the sweet spot — the human's ideas and voice, cleaned up by AI."

#### STUDENTS DO

- Write 150–200 words on their own topic (15 min)
- Create 3 versions using AI (10 min)
- Pair up and compare versions (10 min)
- Share insights with the group (10 min)

#### Pacing

| Segment | Time |
|---------|------|
| Phase 1: Write without AI | 15 min |
| Phase 2: Create AI versions | 10 min |
| Phase 3: Pair comparison | 10 min |
| Phase 4: Group debrief | 10 min |

#### Check for Understanding

**Question:** "When does AI hurt your writing?"
**Expected:** "When you ask it to fully rewrite — it removes your voice, personality, and authentic tone."
**Better question:** "What's the most effective way to use AI for writing?"
**Expected:** "Use it at a specific stage — brainstorming, outlining, or editing — rather than asking it to do everything."

---

### 1:00–2:00 | LUNCH (60 min)

---

## AFTERNOON BLOCK (2:00–5:45)

---

### 2:00–2:40 | Data Analysis with AI (40 min)

**Format:** Individual, instructor-guided | **GRR Phase:** I Do → You Do

#### TEACHER DOES

> **SAY:** "This afternoon we start with data. You're going to upload a real dataset to AI and make it tell you something useful."

**Distribute pre-prepared CSV files** (1 per student, relevant to their country):

*Sample CSV structure for all datasets (50-100 rows):*

**Armenian dataset — "Yerevan Small Business Survey":**
```
business_name, sector, employees, monthly_revenue_usd, years_operating,
uses_social_media, customer_rating, neighborhood
```
Includes 60 fictional but realistic small businesses.

**Moldovan dataset — "Chișinău University Graduate Employment":**
```
graduate_name, degree_field, graduation_year, months_to_first_job,
current_salary_mdl, company_type, uses_ai_at_work, satisfaction_1to10
```
Includes 75 fictional but realistic graduate records.

**Georgian dataset — "Tbilisi Tourism Survey Q4 2025":**
```
visitor_id, origin_country, visit_duration_days, spending_usd,
main_attraction, accommodation_type, would_return, rating_1to5
```
Includes 80 fictional but realistic survey responses.

> **SAY:** "Upload your CSV to Claude or ChatGPT. Then try this prompt:"

**Project the prompt:**
```
Analyze this data. What are the 3 most interesting findings?
Create a summary I could present to my boss in 2 minutes.
```

> **SAY:** "After you get the first analysis, iterate. Try these follow-up prompts:"

**Project follow-up prompts:**
```
- "Create a comparison between [column A] and [column B]"
- "What trends do you see over time?"
- "Which segment is performing best and why?"
- "Summarize this in 5 bullet points for a non-technical audience"
```

> **SAY:** "Your final output: a 1-paragraph summary of your 3 key insights with supporting data points. This is a portfolio artifact."

#### STUDENTS DO

- Upload CSV to Claude or ChatGPT (5 min)
- Run initial analysis prompt (5 min)
- Iterate with 2–3 follow-up prompts (10 min)
- Write a 1-paragraph summary of insights (10 min)
- 2–3 students share findings (5 min)

#### Pacing

| Segment | Time |
|---------|------|
| Distribute CSV + explain exercise | 5 min |
| Upload and first analysis prompt | 5 min |
| Iterate with follow-up prompts | 10 min |
| Write summary paragraph | 10 min |
| 2–3 students share findings | 5 min |
| Buffer | 5 min |

#### Teacher Tip

> Pre-test all CSVs with both Claude and ChatGPT. Ensure they produce interesting results. Have a backup CSV ready in case a student's file doesn't upload correctly. Claude's Artifacts feature is particularly good for creating interactive charts.

#### Check for Understanding

**Question:** "What did AI find in your data that you wouldn't have spotted manually?"
**Expected:** Students cite a specific finding — a correlation, a trend, an outlier.

---

### 2:40–3:30 | Image Generation + Client Brief (50 min)

**Format:** Instructor demo → Guided practice → Individual production | **GRR Phase:** I Do → We Do → You Do

#### TEACHER DOES

**Part 1 — Demo (15 min)**

> **SAY:** "Now let's work with visual AI. ChatGPT can generate images using its built-in image generator. Let me show you how specificity changes everything."

**3 prompts showing progression of specificity:**

```
Prompt 1 (vague):
"A coffee shop"

Prompt 2 (better):
"A cozy specialty coffee shop with exposed brick walls,
warm lighting, and plants"

Prompt 3 (CRAFT-style, specific):
"A photograph-style interior of a modern Georgian coffee shop
in Tbilisi's Vera district. Exposed brick walls, wooden tables,
hanging Edison bulbs, lush green plants on shelves, a marble
counter with an espresso machine, morning light through tall
windows, 2-3 customers working on laptops. Style: warm,
inviting, Instagram-worthy."
```

- Generate all 3 live in ChatGPT. Show the dramatic difference.

> **SAY:** "See how Prompt 3 gives you exactly what you want? The same CRAFT thinking applies to images — the more specific you are about context, audience, format, and tone, the better the output."

> **SAY:** "Now you try. Generate your first image — anything you want. Use what you just learned about specificity."

- Give students 7 minutes to generate their first image.

**Part 2 — Client Brief (35 min)**

> **SAY:** "Now let's get professional. You're a freelance designer. Here's your client brief:"

**Project the brief:**
```
CLIENT BRIEF: Café Soare
————————————————————————
Client: A local coffee shop in Chișinău launching a delivery service
Target audience: Young professionals, 22–35, who work from home
Deliverable: 3 social media image options for the launch announcement
Requirements:
- Must include coffee imagery
- Must feel modern and warm (not corporate)
- Must work as an Instagram square post
- Text "Now Delivering! ☕" should be integrated naturally

Your deliverable:
1. Three image options (generated with AI)
2. A 1-sentence rationale for each option explaining your creative choice
3. Present your best option to a partner for feedback
```

> **SAY:** "You have 20 minutes to generate your 3 options. Iterate — your first attempt won't be your best. Write the rationale for each."

- Circulate. Help students with prompting specificity.

> **SAY (after 20 min):** "Pair up. Show your partner your 3 options. They pick the best one and tell you why."

#### STUDENTS DO

- Generate first image with specific prompt (7 min)
- Read the client brief (2 min)
- Generate 3 image options with iteration (20 min)
- Write 1-sentence rationale for each option (5 min)
- Partner feedback on best option (5 min)

#### Pacing

| Segment | Time |
|---------|------|
| Demo: 3 prompts showing specificity | 8 min |
| First student-generated image | 7 min |
| Client brief: read + plan | 5 min |
| Generate 3 options with iteration | 20 min |
| Write rationales + partner feedback | 10 min |

#### Teacher Tip

> **Free alternatives if ChatGPT image generation is limited:** Microsoft Copilot (https://copilot.microsoft.com) uses DALL-E 3 for free. Craiyon (https://www.craiyon.com) works without an account. Leonardo AI (https://leonardo.ai) has a generous free tier.

#### Check for Understanding

**Question:** "Why did your third image attempt look better than your first?"
**Expected:** "Because I added more specific details — style, lighting, composition, mood."

---

### 3:30–3:45 | BREAK (15 min)

---

### 3:45–4:15 | Presentation Builder (30 min)

**Format:** Hands-on, individual | **GRR Phase:** You Do

#### TEACHER DOES

> **SAY:** "You've written with AI, analyzed data with AI, and created images with AI. Now let's build a presentation with AI. Open https://gamma.app"

**Step-by-step Gamma orientation (5 min):**
1. "Create a free account (or sign in with Google)"
2. "Click 'Create New' → 'Presentation'"
3. "Type your topic or paste a description"

> **SAY:** "Your task: build a 10-slide presentation in 30 minutes. Topic: pitch your current employer or school on adopting one AI tool you learned about this weekend. Use CRAFT thinking for the prompt you give Gamma."

**Example Gamma prompt:**
```
Create a 10-slide presentation pitching the adoption of Perplexity AI
for the marketing department at a mid-size company in Tbilisi.
Audience: department head who is skeptical about AI but values efficiency.
Include: problem (current research is slow), solution (Perplexity),
3 use cases, cost comparison, and a recommended pilot plan.
Style: modern, professional, minimal text per slide.
```

> **SAY:** "Gamma will generate a first draft in about 30 seconds. But the first draft is never final. Spend at least 10 minutes customizing and improving the slides — edit the text, change the layout, replace images."

#### STUDENTS DO

- Open Gamma.app and create an account (2 min)
- Generate initial deck with AI (5 min)
- Customize, edit, and improve slides (15 min)
- Save and note what worked (3 min)

#### Pacing

| Segment | Time |
|---------|------|
| Gamma orientation (new users) | 5 min |
| Generate initial deck with AI | 5 min |
| Customize, edit, and improve | 15 min |
| Save and note what worked | 5 min |

#### Teacher Tip

> **Gamma free tier:** ~10 presentations with AI, exports to PPTX. Sufficient for the bootcamp. If students hit the limit, they can use Google Slides + Gemini as a backup. Resource: https://gamma.app

#### Check for Understanding

**Question:** "What did you have to change in Gamma's AI-generated slides?"
**Expected:** Specifics like "The text was too wordy," "The images didn't match my topic," "I had to reorganize the flow."

---

### 4:15–5:10 | Build Something in 50 Minutes (55 min)

**Format:** Individual, self-directed | **GRR Phase:** You Do Alone

#### TEACHER DOES

> **SAY:** "This is the most open-ended block of the bootcamp. You're going to use AI to build a working mini-tool. Not write code yourself — direct AI to write it for you."

> **SAY:** "Here are 5 project ideas if you don't know what to build:"

**Project on screen:**

```
1. TIP CALCULATOR
   Prompt: "Build me an HTML page with a tip calculator. Input: bill
   amount, number of people, tip percentage (15/18/20/custom). Output:
   tip amount and per-person total. Make it look modern with CSS."

2. QUIZ APP
   Prompt: "Build a 10-question quiz about [your topic]. Multiple choice,
   4 options each. Show the score at the end with correct answers.
   HTML + JavaScript, mobile-friendly."

3. PERSONAL WEBSITE
   Prompt: "Build a simple personal portfolio website. Include: my name,
   a short bio, 3 skills, contact info, and a professional photo
   placeholder. Modern design, responsive, single page."

4. UNIT CONVERTER
   Prompt: "Build a unit converter that handles: temperature (C/F/K),
   weight (kg/lbs), distance (km/miles), currency (USD/EUR/GEL/AMD/MDL).
   Clean UI, instant conversion as you type."

5. FLASHCARD STUDY TOOL
   Prompt: "Build a flashcard app for studying [topic]. 20 cards with
   front and back. Click to flip. Track how many you got right.
   Shuffle option."
```

> **SAY:** "Choose one — or come up with your own idea. Use Claude or ChatGPT to generate the code. Then test it. If it doesn't work, paste the error back to AI and say 'Fix this.' You have 50 minutes."

- Circulate for troubleshooting. Help students who are stuck.

> **SAY:** "Students who finish early — help a neighbor! Peer teaching is one of the best ways to solidify your own understanding."

#### STUDENTS DO

- Choose a project (or create their own)
- Use AI to generate code (HTML/CSS/JavaScript)
- Test in the browser (open the HTML file)
- Debug with AI's help (paste errors back)
- Document what they built

#### Pacing

| Segment | Time |
|---------|------|
| Choose project + initial prompt | 5 min |
| Iterative building | 40 min |
| Test and document | 10 min |

#### Teacher Tip

> The skill being practiced is DIRECTING AI to build something — not writing code. If a student says "I don't know how to code," respond: "Perfect. That's the point. You don't need to. Just describe what you want in plain English, and let AI write the code."

> This is a stretch exercise, not a required artifact. Students who are fatigued (this is hour 6 of day 2) should build something simple. A working tip calculator is better than an ambitious, broken app.

#### Differentiation

- **Struggling learners:** Start with the tip calculator — it's the simplest. Provide the exact prompt to copy-paste.
- **Advanced learners:** Challenge them to add features: "Can you add a dark mode toggle? Can you save results to local storage?"
- **Language support:** The prompts work in any language. Students can describe their project in their first language.

---

### 5:10–5:30 | Show & Tell (20 min)

**Format:** Presentations, full group | **GRR Phase:** We Do

#### TEACHER DOES

> **SAY:** "Who wants to show what they made today? This isn't just the mini-tool — it can be any artifact from today: your data analysis, your image generation, your presentation, or your tool."

- Ask for 5–6 volunteers. 2–3 minutes per person.
- **Prioritize variety** — one data analysis, one visual, one presentation, one mini-tool.
- After each presentation, ask the group: "What surprised you about this?"

#### STUDENTS DO

- 5–6 volunteers demo their work
- Group discusses what surprised them

#### Pacing

| Segment | Time |
|---------|------|
| 5–6 presentations × 3 min each | 15–18 min |
| Buffer | 2–5 min |

---

### 5:30–5:45 | Day 2 Wrap + Mid-Week Assignment Briefing (15 min)

**Format:** Full group | **GRR Phase:** I Do

#### TEACHER DOES

**Quick reflection (5 min):**
> **SAY:** "1-2-1 before we go: 1 highlight from today, 2 tools you'll actually use this week, 1 thing that confused you. Write it down. 3 minutes."

- 2–3 volunteers share.

**Mid-week assignment (8 min):**

> **SAY:** "Between now and next Saturday, you have a structured assignment. This is NOT optional — it's how you'll stay sharp across the week gap. Let me walk through it on screen."

- **Project the assignment template on screen.**
- **Show one completed example** so students know exactly what's expected.
- Walk through every section.
- Answer questions.

> **SAY:** "If this runs a few minutes over, that's fine. It's more important that you understand the assignment than that we finish exactly at 5:45."

#### Exit Ticket Questions

1. Describe your process for fact-checking an AI-generated claim. What steps do you take?
2. What is source triangulation, and why does using multiple AI tools matter?
3. Rate your confidence (1–5) in distinguishing AI-generated text that needs human editing.

---

## DIFFERENTIATION NOTES (Session 2 Summary)

| Learner Type | Strategy |
|-------------|----------|
| **Struggling learners** | Provide fact-checking checklist. Pre-select simpler research topics. Pair with a partner for source triangulation exercise. Start with the tip calculator for the build exercise. |
| **Advanced learners** | Find a subtle hallucination that's hard to detect. Create their own trust rubric criteria. Add features to their mini-tool. |
| **Language support** | Allow use of translation tools alongside AI research tools. Provide sentence frames for analysis writing. Allow fact-checking in native language. |

---

## POST-SESSION REFLECTION (for the instructor)

- [ ] What worked well today?
- [ ] What would I adjust for next time?
- [ ] Which students need follow-up or additional support?
- [ ] Did timing work? Where did I run long or short?
- [ ] Is the mid-week assignment clear? Did students ask enough questions?

---

## KEY RESOURCES FOR THIS SESSION

| Resource | URL | Used For |
|----------|-----|----------|
| Perplexity AI | https://www.perplexity.ai | Research + fact-checking |
| Google NotebookLM | https://notebooklm.google.com | Document analysis |
| Gamma.app | https://gamma.app | AI presentations |
| ChatGPT (image gen) | https://chat.openai.com | Image generation |
| Microsoft Copilot | https://copilot.microsoft.com | Free image gen backup |
| Craiyon | https://www.craiyon.com | Free image gen (no account) |
| Otter.ai | https://otter.ai | Meeting transcription |
| Grammarly | https://www.grammarly.com | Writing assistance |
