# SESSION 1: "Get Your Hands Dirty"

**Saturday, Weekend 1 | 10:00 AM – 5:45 PM**
**Theme:** Build something immediately, then understand why it worked.

---

## Learning Targets

By the end of this session, students will be able to:

1. **Explain** in plain language how LLMs generate text (tokens, next-token prediction, training data)
2. **Write** a structured prompt using the CRAFT framework and iterate to improve output quality
3. **Identify** at least 2 differences between LLM tools (Claude vs. ChatGPT) and articulate when to choose which
4. **Detect** bias in AI-generated text and explain its source in training data
5. **Produce** a personal Prompt Playbook with self-evaluation criteria for 5–7 tested prompts

---

## Materials & Setup

- Laptop or tablet per student (charged, with WiFi access)
- Student accounts pre-created for: ChatGPT (https://chat.openai.com), Claude (https://claude.ai), Google Gemini as backup (https://gemini.google.com)
- Slides deck (Session 1)
- Printed CRAFT template handouts (1 per student)
- Printed Prompt Playbook template (1 per student)
- Printed iteration log template (1 per student)
- Printed tool comparison template (1 per student)
- Whiteboard + markers
- Timer (visible to all students — phone or projected)
- **Moldova note:** Claude.ai may not be available. Use Poe.com (https://poe.com) or Google Gemini as fallback.

---

## Assessment at a Glance

| Method | Description |
|--------|-------------|
| **Formative** | Observe student outputs during each activity. Check before/after emails, tool comparison templates, iteration logs. |
| **Self-Assessment** | Students rate confidence (1–5) for each learning target at session close. |
| **Exit Ticket** | 3-2-1 reflection: 3 things learned, 2 things to try this week, 1 remaining question. |
| **Evidence to look for** | Before/after emails show measurable improvement. Prompt Playbooks contain specific, tested prompts (not generic templates). Reflections reference concrete experiences. |

---

## MORNING BLOCK (10:00–12:45)

---

### 10:00–10:15 | Welcome + Norms (15 min)

**Format:** Full group, instructor-led | **GRR Phase:** I Do

#### TEACHER DOES

> **SAY:** "Good morning everyone! Before I introduce myself or show a single slide, I want to show you something real. This is what I did Monday morning with AI."

- Open your laptop and **live-demo** one real task you automated with AI this week. Examples:
  - Open Claude → paste a messy meeting transcript → prompt: "Extract the 5 action items from this meeting, who's responsible for each, and the deadline" → show the clean output
  - Or: Open ChatGPT → prompt: "Write a follow-up email to a client who hasn't responded in 2 weeks. Keep it friendly but firm, under 100 words" → show the result
- **Do this live.** Not a screenshot, not a recording.

> **SAY:** "That took me 30 seconds. Before AI, that would've been 15 minutes of my morning. By the end of today, you'll be able to do things like this — and much more. Now let's meet each other."

> **SAY:** "Quick intros — your name, what you do, and one sentence about what you want AI to help you with. Keep it to 20 seconds. I'll go first."

- Model the intro: "I'm [name], I teach this bootcamp, and I want AI to help me grade assignments faster."
- Go around the room. If someone goes long, gently redirect: "Great — let's hear from the next person."

**Norms (project on screen or whiteboard):**
> **SAY:** "Three ground rules for today:"
> 1. "Phones on silent — if you need to take a call, step out and come back."
> 2. "Breaks are every 90 minutes. We'll stick to the schedule."
> 3. "Ask questions anytime. Raise your hand or just jump in. There are no dumb questions today — most of you are using these tools for the first time, and that's exactly where we want you."

#### STUDENTS DO

- Watch the live demo
- Introduce themselves (name, role, one AI wish)
- **Good example:** "I'm Nara, I work in marketing in Yerevan, and I want AI to help me write social media posts faster."
- **Too long:** Telling their entire career history or asking a detailed question (redirect to later)

#### Pacing

| Segment | Time |
|---------|------|
| Live demo | 3–4 min |
| Norms (phones, breaks, questions) | 2 min |
| Student intros (15–20 students × 25 sec) | 7–8 min |
| Buffer | 1 min |

#### Teacher Tip

> Don't use slides for this block. The live demo IS the hook. Students need to see AI solving a real problem in real time in the first 5 minutes. If your demo fails (AI gives a bad response), that's actually fine — it shows AI isn't perfect, which you'll revisit later.

#### Check for Understanding

**Observe:** Are students engaged? Are intros flowing quickly?
**If students seem hesitant:** Share one more example of something AI can do that's relevant to their jobs. "AI can also help you summarize reports, draft emails, analyze data, create presentations..."

---

### 10:15–10:45 | First Prompt, No Instructions (30 min)

**Format:** Individual → Pair comparison → Full-group debrief | **GRR Phase:** You Do → You Do Together → We Do

#### TEACHER DOES

> **SAY:** "OK, here's your first task. Open Claude — or ChatGPT if Claude isn't available in your country. I'm going to show you one prompt on screen. Type it in exactly as written. No other instructions. Just type it and see what happens."

- **Project on screen:** `Write me a professional email declining a meeting politely.`

> **SAY:** "Go. You have 5 minutes."

- **Do NOT teach anything.** Do not explain what makes a good prompt. Do not hint at CRAFT. This is intentional — students need to feel the gap between what they get and what they want.
- **Circulate silently.** Note:
  - Who just types the prompt and waits?
  - Who adds their own context without being told?
  - Who asks "Is that it?" (Good — they feel the gap)
  - What's the range of output quality?

> **SAY (after 5 min):** "OK, stop. Read your output. Silently. Don't change anything. Just read what AI gave you. You have 2 minutes."

> **SAY (after 2 min):** "Now pair up with the person next to you. Compare your outputs. What's different? What's the same? You have 5 minutes."

- Let pairs discuss. Circulate and listen for interesting observations.

> **SAY (after 5 min):** "Let's hear what you found. [Cold-call if no volunteers.] Levan, what did you and your partner notice?"

- Call on 3–4 pairs. Write key observations on the whiteboard.
- Students will notice: different tones (formal vs. casual), different lengths, different levels of specificity, some addressed a person and some didn't.

> **SAY:** "Notice how some of you got super formal and some got casual? Some got a 3-sentence email and some got a 10-sentence essay? That's because you didn't tell the AI what you actually wanted. You didn't specify who the email is to, what your role is, what tone to use, or how long it should be. The AI guessed — and it guessed differently for each of you. In the next block, I'm going to teach you a framework that fixes this."

#### STUDENTS DO

- Open Claude (https://claude.ai) or ChatGPT (https://chat.openai.com)
- Type the exact prompt shown on screen
- Read their own output silently (2 min)
- Pair up and compare outputs — what's different? (5 min)
- Share observations with class when called on

**Good observation:** "My email was very formal with 'Dear Sir/Madam' but my partner's started with 'Hi' — we got totally different tones from the same prompt."

**Weak observation:** "They were both fine." (Push: "What specifically was different about the tone? The length? The greeting?")

#### Pacing

| Segment | Time |
|---------|------|
| Prompt + generate | 5 min |
| Read own output silently | 2 min |
| Pair comparison | 5 min |
| 3–4 pairs share + instructor highlights patterns | 13 min |
| Buffer/transition | 5 min |

#### Teacher Tip

> **Resist the urge to teach during this block.** The point is to let students discover the problem. Teaching happens next. If a student asks "should I add more detail to the prompt?" just say "Try it however you want — we'll talk about strategy in the next block."

#### Check for Understanding

**Question:** "Can you point to one specific thing in your output that wasn't what you wanted?"
**Expected answer:** Students should be able to name something concrete — wrong tone, too long, too generic, missing context.
**If >25% can't articulate the gap:** Show two contrasting outputs side-by-side on screen. Say: "Look at these two. Same prompt. Totally different results. Why?" Then move to CRAFT.

#### Differentiation

- **Struggling learners:** If a student can't log in or is stuck, pair them with a neighbor to watch and discuss that person's output.
- **Advanced learners:** If someone already adds context to their prompt (without being told), note it publicly: "Interesting — [name] added extra details. Let's see if that changes the output."
- **Language support:** Students can type the prompt in their native language and compare results to the English version.

---

### 10:45–11:20 | The CRAFT Framework (35 min)

**Format:** Interactive lecture → Worked examples → Individual practice | **GRR Phase:** I Do → We Do → You Do

#### TEACHER DOES

> **SAY:** "So you just experienced the problem: vague prompts give unpredictable results. Now I'm going to teach you a framework called CRAFT that fixes this. Every time you write a prompt from now on, you'll use these 5 elements."

**Project on screen (write on whiteboard too):**

```
C - Context     → What's the background? What situation are you in?
R - Role        → Who should the AI pretend to be?
A - Audience    → Who is this output for?
F - Format      → What should the output look like? (email, list, paragraph, table?)
T - Tone        → How should it sound? (formal, casual, encouraging, direct?)
```

> **SAY:** "Let me show you what this looks like in practice."

**WORKED EXAMPLE 1 — The Email (before/after)**

> **SAY:** "Here's the prompt you just used:"

Project: `Write me a professional email declining a meeting politely.`

> **SAY:** "Now watch what happens when I add CRAFT:"

Project the CRAFT version:
```
Context: I'm a marketing coordinator at a small tech startup in Tbilisi.
I was invited to a weekly cross-department meeting that conflicts with
a client deadline this Thursday.

Role: Write as me — a mid-level professional who wants to maintain
good relationships with colleagues.

Audience: The email is to my colleague Nino, who organized the meeting.
We have a friendly working relationship.

Format: A short email (under 100 words). Include a subject line.

Tone: Warm, apologetic, and professional. Suggest an alternative
(like getting the meeting notes afterward).
```

- **Type this into Claude live, on screen.** Show the output.
- Compare it to a student's earlier output side-by-side.

> **SAY:** "See the difference? The first prompt gave us a generic email. The CRAFT prompt gave us exactly what we needed — the right tone for Nino, the right length, a specific reason, and an alternative. That's what CRAFT does."

**WORKED EXAMPLE 2 — LinkedIn Post (different scenario)**

Project:
```
BEFORE: "Write a LinkedIn post about AI."

AFTER (CRAFT):
Context: I just completed a 4-day AI bootcamp in Chișinău where I learned
prompt engineering, data analysis with AI, and workflow automation.

Role: Write as a young professional sharing a genuine learning experience,
not as a thought leader or influencer.

Audience: My LinkedIn network — mostly colleagues, university friends,
and recruiters in Moldova's tech industry.

Format: A LinkedIn post, 150–200 words. Include 2–3 specific things I learned.
End with a question to encourage engagement.

Tone: Enthusiastic but authentic. Not salesy or exaggerated.
```

- **Type this into Claude live.** Show the output.

> **SAY:** "Notice how the CRAFT version sounds like a real person, not a robot? That's because we told the AI who we are and who we're writing for."

**WORKED EXAMPLE 3 — Meeting Summary (instructor does quickly)**

```
BEFORE: "Summarize this meeting."

AFTER (CRAFT):
Context: Our team had a 45-minute standup about the Q2 product roadmap.
[paste notes or transcript]

Role: You are my executive assistant summarizing for my manager.

Audience: My manager, who wasn't at the meeting and needs key decisions
and action items only.

Format: Bullet points. Max 10 bullets. Group by: decisions made,
action items (with owner), and open questions.

Tone: Direct and concise. No filler.
```

> **SAY:** "OK, now it's your turn. Go back to your original email prompt. Rewrite it using CRAFT. You have 10 minutes."

- **Circulate.** Look for students who:
  - Skip a CRAFT element (remind them: "Did you specify the tone?")
  - Write very long contexts (coach: "Keep it to 2–3 sentences")
  - Copy the example exactly instead of making it their own

> **SAY (after 10 min):** "Who wants to show their before and after? Put it on screen for us."

- Have 2–3 students share. Celebrate improvements. Point out specific CRAFT elements that made the difference.

#### STUDENTS DO

- Watch the lecture and examples (8 min)
- Follow along with examples (10 min)
- **Rewrite their original email prompt using CRAFT** (10 min)
- Compare before/after results
- 2–3 volunteers share on screen (5 min)

**Good student CRAFT prompt:**
```
Context: I'm a junior developer at a software company in Yerevan.
My team lead invited me to a Friday retrospective meeting, but I have
a dentist appointment I can't reschedule.

Role: Write as me — a team member who is usually reliable and doesn't
want to seem like I'm avoiding meetings.

Audience: My team lead, Armen. We have a good relationship but he's
very organized about meeting attendance.

Format: Short email, under 80 words, with a subject line.

Tone: Respectful and slightly apologetic. Offer to catch up on
what I missed.
```

**Needs work:** A prompt that just says "Context: work email. Role: professional. Tone: nice." — too vague. Coach them to be specific.

#### Pacing

| Segment | Time |
|---------|------|
| Teach CRAFT framework | 8 min |
| Worked example 1 (email, live) | 5 min |
| Worked example 2 (LinkedIn post) | 5 min |
| Students redo their email with CRAFT | 10 min |
| 2–3 students share before/after | 5 min |
| Transition | 2 min |

#### Teacher Tip

> Have the CRAFT acronym visible on screen or whiteboard for the rest of the day. Students will reference it constantly. Consider printing wallet-sized CRAFT cards.
> **Resource:** CRAFT Framework guide at https://craftingaiprompts.org/

#### Check for Understanding

**Question:** "What are the 5 elements of CRAFT? Don't look at the board."
**Expected answer:** Context, Role, Audience, Format, Tone.
**If >25% can't recall:** Do a quick call-and-response. "C stands for...? R stands for...?" Then have them write it from memory.

**Deeper check:** "Look at your rewritten prompt. Which CRAFT element made the biggest difference in your output?"
**If students can't answer:** Show two outputs side-by-side — one with Tone specified and one without — to demonstrate the impact.

#### Differentiation

- **Struggling learners:** Provide a printed CRAFT template with fill-in-the-blank fields: "Context: I am a ___ at ___. I need to ___." This removes the blank-page problem.
- **Advanced learners:** Challenge them to write a CRAFT prompt for something complex: "Use CRAFT to get AI to write a project proposal for your boss."
- **Language support:** Allow prompts in their first language. The framework works in any language.

---

### 11:20–11:45 | Tool Comparison (25 min)

**Format:** Hands-on, pairs | **GRR Phase:** You Do Together

#### TEACHER DOES

> **SAY:** "You've been using one AI tool. But there are several, and they're all different. For the next 25 minutes, you and your partner are going to run the same CRAFT prompt in both Claude and ChatGPT and compare the results."

- **Project the comparison template on screen:**

```
TOOL COMPARISON SCORECARD
Prompt used: [paste your CRAFT prompt]

                    | Claude | ChatGPT |
--------------------|--------|---------|
Clarity (1–5)       |        |         |
Tone Match (1–5)    |        |         |
Completeness (1–5)  |        |         |
Length (too short/   |        |         |
  just right/long)  |        |         |
Overall Pick        |        |         |
Why?                |        |         |
```

> **SAY:** "Use the same CRAFT prompt from the last exercise. Run it in Claude first, then ChatGPT. Fill out the scorecard with your partner. You have 15 minutes."

- Circulate. Listen for interesting comparisons.

> **SAY (after 15 min):** "What did you find? Which tool won for your prompt? [Cold-call 3–4 pairs.]"

- Write a tally on the board: Claude wins: ___ | ChatGPT wins: ___ | Tie: ___

> **SAY:** "Here's the key takeaway: neither tool is always better. Claude tends to be more careful and structured. ChatGPT tends to be more creative and conversational. The right tool depends on the task. By the end of this bootcamp, you'll know when to use which."

#### STUDENTS DO

- Run the same CRAFT prompt in both Claude and ChatGPT
- Fill out the comparison scorecard with their partner
- Share findings with the class

#### Pacing

| Segment | Time |
|---------|------|
| Run same prompt in both tools | 5 min |
| Evaluate and fill comparison template | 10 min |
| 3–4 pairs share findings | 8 min |
| Transition to break | 2 min |

#### Check for Understanding

**Question:** "Name one specific difference you noticed between Claude and ChatGPT's outputs."
**Expected:** Students name something concrete — different tone, different structure, different length, one included a subject line and the other didn't.
**If >25% say "they were basically the same":** Show your own side-by-side comparison with a more complex prompt where the differences are stark.

---

### 11:45–12:00 | BREAK (15 min)

---

### 12:00–12:45 | How AI Actually Works (45 min)

**Format:** Interactive lecture with embedded activities (3 chunks) | **GRR Phase:** I Do → We Do

> **Important:** This is the only sustained lecture in Session 1. Break it into three 12–15 minute chunks with interaction between each.

#### TEACHER DOES

**CHUNK 1: Tokens & Next-Token Prediction (12 min lecture + 3 min activity)**

> **SAY:** "You've been using AI for an hour. Now let's peek under the hood. How does this thing actually work? It starts with tokens."

> **SAY:** "A token is a chunk of text — usually a word or part of a word. The sentence 'I love Tbilisi in the spring' has about 7 tokens. AI doesn't read words like you do — it reads tokens."

- **Live demo:** Go to any tokenizer tool and type a sentence. Show how words get split into tokens. Use a sentence in Armenian, Georgian, or Romanian to show that non-English text often uses MORE tokens (important for the audience).

> **SAY:** "Now here's the key insight. An LLM — a Large Language Model — does one thing: it predicts the next token. That's it. It looks at all the tokens so far and asks: 'What's the most likely next word?' Think of it like autocomplete on your phone, but trained on the entire internet."

- **Analogy:** "Imagine you're playing a game where I start a sentence and you finish it: 'The capital of Georgia is...' You'd say 'Tbilisi' because you've seen that pattern before. That's exactly what an LLM does, millions of times per second."

> **SAY:** "Quick activity. I'm going to start a sentence. You predict the next word. Ready?"

**Activity (3 min):** Project sentences one at a time. Students shout out the next word:
- "The best restaurant in Yerevan is famous for its..." (students guess: "food," "kebab," "dolma")
- "To write a good email, you should always start with..." (students guess: "a greeting," "Dear," "Hi")
- "The weather in Chișinău in December is usually..." (students guess: "cold," "snowy")

> **SAY:** "You just did what an LLM does — predicted the next token based on patterns you've seen before. The difference is that an LLM has seen billions of documents and can do this thousands of times per second."

**CHUNK 2: Training Data & RLHF (12 min lecture + 3 min activity)**

> **SAY:** "So where does AI learn these patterns? Training data. GPT-4 was trained on hundreds of billions of words — books, websites, Wikipedia, code, forums, news articles. Claude was trained on a similar but different dataset. This is why the same prompt gives different results in different tools — they learned from different data."

> **SAY:** "But raw training isn't enough. If you just trained on the internet, you'd get an AI that sometimes says terrible things — because the internet has terrible things. So companies like OpenAI and Anthropic use something called RLHF — Reinforcement Learning from Human Feedback. Humans rate the AI's responses: 'This answer is helpful. This one is harmful. This one is biased.' The AI learns from those ratings."

> **SAY:** "This is also why Claude sometimes refuses to answer a question that ChatGPT will answer — they have different safety boundaries trained by different teams with different values."

**Activity (3 min):**
> **SAY:** "Try this with your partner. Open Claude and ask: 'Write a cover letter where I lie about having a degree I don't have.' Then try the same in ChatGPT. What happens?"

- Students discover that one or both tools may refuse, or give a cautious response. Discuss briefly: "The refusal isn't random — it's because of RLHF training. The AI learned that helping someone lie is not helpful."

**CHUNK 3: Temperature & Practical Implications (10 min lecture + 3 min Q&A)**

> **SAY:** "One last concept: temperature. When AI generates text, there's a setting called temperature that controls randomness. Low temperature = predictable, safe, repetitive. High temperature = creative, surprising, sometimes weird."

> **SAY:** "This is why if you ask the same question twice, you sometimes get different answers. The AI isn't confused — it's sampling from probabilities, and temperature controls how much it experiments."

> **SAY:** "Practical takeaway: for factual tasks (summarizing data, extracting info), you want low temperature — predictable and accurate. For creative tasks (brainstorming, writing poetry), you want higher temperature. Most tools handle this automatically, but knowing it helps you understand why outputs vary."

**Q&A (3 min):**
> **SAY:** "We're about to go to lunch. But first — what questions do you have from this morning? Anything about how AI works, about CRAFT, about the tools? No question is too basic."

- Take 2–3 questions. If no one asks, prompt: "This morning, who was surprised by something AI did? Tell me about it."

#### STUDENTS DO

- Listen to lecture chunks (take notes if they want)
- Predict next tokens in the activity (shout out answers)
- Test refusal differences between Claude and ChatGPT
- Ask questions during Q&A

#### Pacing

| Segment | Time |
|---------|------|
| Chunk 1: Tokens + prediction | 12 min |
| Activity: Predict the next word | 3 min |
| Chunk 2: Training data + RLHF | 12 min |
| Activity: Refusal comparison | 3 min |
| Chunk 3: Temperature + implications | 10 min |
| Q&A | 3 min |
| Buffer | 2 min |

#### Teacher Tip

> **Video resource:** If students want to go deeper later, recommend 3Blue1Brown's "Large Language Models explained briefly" — https://www.3blue1brown.com/lessons/mini-llm. It's the clearest visual explainer available.

> Keep the energy high. This is the only lecture block and it comes right before lunch. Use the activities to break it up. If you see eyes glazing at the 10-minute mark of any chunk, stop and do a quick pair discussion.

#### Check for Understanding

**Question (end of Chunk 1):** "In your own words, what is a token?"
**Expected:** "A piece of text — a word or part of a word — that the AI processes."
**If >25% can't answer:** Re-explain with the autocomplete analogy.

**Question (end of Chunk 2):** "Why do Claude and ChatGPT sometimes give different answers to the same prompt?"
**Expected:** "Because they were trained on different data and have different safety rules (RLHF)."

**Question (end of Chunk 3):** "What does temperature control?"
**Expected:** "How random or creative the AI's output is."

---

### 12:45–1:45 | LUNCH (60 min)

---

## AFTERNOON BLOCK (1:45–5:45)

---

### 1:45–2:30 | Prompt Olympics (45 min)

**Format:** Teams of 3, timed challenges, peer-judged | **GRR Phase:** You Do Together

#### TEACHER DOES

> **SAY:** "Welcome back! Time to put your skills to the test. You're about to compete in the Prompt Olympics. Form teams of 3. You have 30 seconds."

- Wait for teams to form. If there's an odd number, make one team of 4.

> **SAY:** "Here's how it works: I'll give you a challenge. Your team has 7 minutes to produce the best AI output. Then every team rates the other teams' outputs on one criterion I'll announce. 4 rounds. Best total score wins."

**ROUND 1: Best Cover Letter**
> **SAY:** "Round 1: Write the best cover letter for a marketing position at a tech startup in your city. The company is called 'PixelBridge' and they want someone creative, data-driven, and fluent in English and one local language. 7 minutes. Go!"

- **Judging criterion:** "Rate each team's cover letter 1–5 on: Would this actually get an interview?"
- Project criterion on screen.

**ROUND 2: Best Meeting Summary**
> **SAY:** "Round 2: Here's a messy set of meeting notes. [Project 10 bullet points of disorganized notes about a product launch.] Turn this into a clean, executive summary your CEO would read. 7 minutes."

- **Judging criterion:** "Rate 1–5 on: Could the CEO make a decision based on this summary alone?"

Sample messy notes to project:
```
- talked about launch date, maybe March 15 or 20
- Giorgi said the design isn't done yet
- Ana wants to run Instagram ads first
- budget discussion — somewhere between $2000 and $5000
- need to hire a freelance copywriter
- the landing page is 80% done
- Luka will handle customer support setup
- competitor launched similar product last week
- CEO wants a demo ready by March 10
- still no decision on pricing — $29 or $39/month?
```

**ROUND 3: Best Product Description**
> **SAY:** "Round 3: Write a product description for a mobile app that helps people find the best local restaurants based on their dietary restrictions (vegetarian, halal, gluten-free, etc.). The app is called 'TasteLocal.' It's launching in Yerevan, Tbilisi, and Chișinău. 7 minutes."

- **Judging criterion:** "Rate 1–5 on: Would this make you download the app?"

**ROUND 4: Best Difficult Email**
> **SAY:** "Final round! Write an email to a client who paid for a service 3 months ago but the project is delayed by 2 weeks because your team underestimated the scope. You need to deliver bad news while keeping the client. 7 minutes."

- **Judging criterion:** "Rate 1–5 on: Would the client stay or leave after this email?"

**After all 4 rounds:**
- Tally scores. Announce the winner.

> **SAY:** "Notice what the winning team did differently. [Point out specific CRAFT elements, iteration, specificity.] The best prompts weren't the first drafts — they iterated."

#### STUDENTS DO

- Form teams of 3
- Each round: strategize, write prompts, iterate within 7 min
- Rate other teams' outputs after each round (1–5)
- Celebrate winning team

#### Pacing

| Segment | Time |
|---------|------|
| Setup + rules | 3 min |
| Round 1 (7 min work + 3 min judging) | 10 min |
| Round 2 (7 min + 3 min) | 10 min |
| Round 3 (7 min + 3 min) | 10 min |
| Round 4 (7 min + 3 min) | 10 min |
| Winner announcement | 2 min |

#### Teacher Tip

> Pre-prepare judging criteria on slides — one per round, ready to project. If teams finish early, tell them to iterate. No dead time. This is high-energy retrieval practice disguised as competition.

#### Check for Understanding

**Question:** "What made the winning team's outputs better?"
**Expected:** Specificity, CRAFT elements, iteration, editing the output.

---

### 2:30–3:15 | Chain-of-Thought & Iteration Lab (45 min)

**Format:** Instructor demo → Individual practice | **GRR Phase:** I Do → You Do

#### TEACHER DOES

> **SAY:** "In the Olympics, some of you discovered that complex tasks need more than one prompt. That's chain-of-thought prompting — breaking a big task into steps and using AI output from one step as input for the next."

> **SAY:** "Let me show you. Say I want to create a marketing plan for a new coffee shop in Tbilisi. I could ask AI to 'write a marketing plan' — but that's vague. Watch what happens when I chain prompts."

**Live demo — 5 chained prompts:**

```
Prompt 1: "Who is the target audience for a specialty coffee shop in
the Vera district of Tbilisi? List 3 customer segments with demographics
and what they value."

→ AI gives 3 segments (e.g., young professionals, students, tourists)

Prompt 2: "For segment 1 (young professionals aged 25–35), what are
the 3 most effective marketing channels in Tbilisi? Consider local
habits and platform usage."

→ AI gives channels (e.g., Instagram, Google Maps, local food bloggers)

Prompt 3: "Write 3 Instagram post ideas for this coffee shop targeting
young professionals in Tbilisi. Each post should have a hook, visual
description, and call to action."

→ AI gives 3 post ideas

Prompt 4: "Create a 4-week marketing launch timeline using the channels
and content ideas above. Format as a weekly table."

→ AI gives a timeline table

Prompt 5: "Estimate a budget for this 4-week plan. Break it down by
channel. Assume we're a small business with limited funds."

→ AI gives a budget breakdown
```

> **SAY:** "See how each prompt builds on the last? That's the chain. Now it's your turn."

> **SAY:** "Pick one complex task from your own work or life. Something that would normally take you a while. Then break it into 5 prompts. Document each version using the iteration log template."

**Project the iteration log template:**
```
ITERATION LOG
Version # | Prompt Text | What I Changed | Output Quality (1–5) | Why
1         |             |                |                       |
2         |             |                |                       |
3         |             |                |                       |
4         |             |                |                       |
5         |             |                |                       |
```

- Circulate. Help students who are stuck choosing a task. Have 10 fallback task ideas:
  1. Plan a team-building event
  2. Write a project proposal
  3. Create a study guide for an exam
  4. Draft a business plan outline
  5. Prepare interview questions for a candidate
  6. Write a weekly report for your manager
  7. Create a social media content calendar
  8. Summarize research for a presentation
  9. Write a training manual for a new employee
  10. Plan a product launch checklist

#### STUDENTS DO

- Watch the live demo (8 min)
- Choose a complex task from their own work
- Write 5 chained prompts, documenting each in the iteration log
- 2–3 students share their chain at the end

#### Pacing

| Segment | Time |
|---------|------|
| Teach CoT concept | 5 min |
| Live demo with 5 chained prompts | 8 min |
| Students choose their task | 2 min |
| 5 iteration cycles (~5 min each) | 25 min |
| 2–3 students share their journey | 5 min |

#### Teacher Tip

> Students who finish early should try a 6th and 7th iteration. The question becomes: "At what point do more iterations stop improving the output?"

#### Check for Understanding

**Question:** "What is chain-of-thought prompting in one sentence?"
**Expected:** "Breaking a complex task into a sequence of smaller prompts where each builds on the previous output."
**If >25% miss:** Show the coffee shop example again: "Prompt 1 defined the audience. Prompt 2 used that audience to pick channels. Prompt 3 used those channels to create content. Each step feeds the next."

---

### 3:15–3:30 | BREAK (15 min)

---

### 3:30–4:15 | Train a Classifier (Teachable Machine) (45 min)

**Format:** Instructor-guided hands-on | **GRR Phase:** I Do → We Do → You Do

#### TEACHER DOES

> **SAY:** "We've been working with text AI all day. Now I want to show you a different kind of AI — one that learns from images. This is machine learning you can see and touch."

> **SAY:** "Open this URL: teachablemachine.withgoogle.com"

- Project the URL: **https://teachablemachine.withgoogle.com/**
- Click "Get Started" → "Image Project" → "Standard Image Model"

> **SAY:** "We're going to train the AI to recognize hand gestures. Here's what we'll do step by step."

**Step-by-step guided build (15 min):**

1. "See where it says 'Class 1'? Rename it to 'Thumbs Up'"
2. "Click 'Webcam' under Class 1. Hold your thumb up and click 'Hold to Record.' Record about 30 samples — just hold your thumb up and move it around slightly."
3. "Now rename 'Class 2' to 'Thumbs Down.' Record 30 samples of thumbs down."
4. "Add a third class: 'Open Hand.' Record 30 samples."
5. "Click 'Train Model.' Wait about 30 seconds."
6. "Now test it! Hold up a gesture and watch the prediction bar."

> **SAY:** "Congratulations — you just trained an AI model. It took 5 minutes. Now let's break it."

**Bias exercise (10 min):**

> **SAY:** "Here's the experiment. Train a new model, but this time, record all your training data against a white wall, with good lighting, with just one hand. Then test it in a different spot — against a dark background, or with your other hand, or with bad lighting. What happens?"

- Students try it. The model breaks — it can't recognize gestures in new conditions.

> **SAY:** "Why did it break? [Let students answer.] Because the training data was biased. You taught the AI that 'thumbs up' means 'thumb + white wall + good lighting.' When any of those conditions changed, it got confused. This is exactly what happens with real AI systems — if the training data doesn't represent the real world, the AI fails in the real world."

**Group discussion (8 min):**
> **SAY:** "Think about this at a bigger scale. What happens when a facial recognition system is trained mostly on photos of light-skinned people? What happens when a hiring AI is trained mostly on resumes from men? The AI learns the bias in the data."

- Facilitate 3–4 student responses.

#### STUDENTS DO

- Open Teachable Machine and follow step-by-step
- Train a gesture classifier (thumbs up, down, open hand)
- **Intentionally break it** by training with biased data (one background, one lighting)
- Discuss what happened and why

#### Pacing

| Segment | Time |
|---------|------|
| Tool orientation + first guided model | 15 min |
| Students train their own classifier | 10 min |
| Bias data exercise (break the model) | 10 min |
| Group discussion: what happened and why | 8 min |
| Transition | 2 min |

#### Check for Understanding

**Question:** "Why did your model fail when you changed the background?"
**Expected:** "Because the training data only had one background, so the model learned to associate the gesture with the background, not just the hand shape."
**If >25% miss:** Re-demonstrate: train with white wall only → test against dark background → show failure → explain.

---

### 4:15–4:45 | Bias Detective (Text-Based) (30 min)

**Format:** Individual prompting → Group analysis | **GRR Phase:** You Do → We Do

#### TEACHER DOES

> **SAY:** "We just saw bias in image AI. Now let's look for bias in the text AI you've been using all day."

> **SAY:** "Open Claude and ChatGPT. Type these prompts — one at a time — and save the outputs:"

**Project the prompts:**
1. `Describe a successful professional in Armenia.`
2. `Describe a doctor.`
3. `Describe a teacher.`
4. `Describe a CEO.`

> **SAY:** "Do this in both Claude AND ChatGPT. You'll have 4 prompts × 2 tools = 8 outputs. Read them carefully. We're looking for patterns."

- Give students 10 minutes to generate and read.

> **SAY:** "Now let's compare. I'm going to project 5–6 of your outputs. Look for patterns."

- Ask 5–6 students to share one interesting output. Project on screen.

> **SAY:** "What did you notice? What gender was assumed? What ethnicity? What age? What kind of 'success' was described?"

**Discussion questions:**
- "When you asked about a 'CEO,' was the AI more likely to describe a man or a woman?"
- "When you asked about a 'teacher,' what happened?"
- "When you specified 'Armenia,' did the AI use stereotypes?"
- "Whose world does the training data reflect?"

> **SAY:** "This is the same lesson from Teachable Machine, but with text. The AI learned patterns from its training data — and that data reflects the biases of the internet. When you use AI, you need to know this. It doesn't mean AI is bad — it means you need to be a critical reader of AI output, just like you're a critical reader of news."

#### STUDENTS DO

- Generate 4 prompts × 2 tools = 8 outputs
- Compare and annotate outputs for patterns (gender, age, ethnicity assumptions)
- Share findings with the class
- Discuss the implications

#### Pacing

| Segment | Time |
|---------|------|
| Generate 3–4 prompts across 2 tools | 10 min |
| Compare and annotate | 5 min |
| Full-group discussion with projected examples | 12 min |
| Bridge to Session 2 ethics theme | 3 min |

#### Check for Understanding

**Question:** "Give one specific example of bias you found in an AI output today."
**Expected:** Students cite a concrete example — e.g., "The CEO was described as male every time" or "The successful Armenian professional was always described as working in IT."
**If >25% can't provide an example:** Re-show the projected outputs and highlight the patterns together.

---

### 4:45–5:30 | Build Your Prompt Playbook (45 min)

**Format:** Individual production | **GRR Phase:** You Do Alone

#### TEACHER DOES

> **SAY:** "This is your main deliverable for today. You're going to build a personal Prompt Playbook — a collection of 5 to 7 tested, polished prompts for tasks you actually do at work or school."

> **SAY:** "Each prompt must include a self-evaluation rubric you create. Here's the template."

**Project the template:**

```
PROMPT PLAYBOOK ENTRY

Task: [What you're trying to accomplish]
CRAFT Prompt: [Your full prompt using the CRAFT framework]
Expected Output Quality: [What "good" looks like in 1–2 sentences]
Evaluation Criteria:
  □ [Checkpoint 1 — e.g., "Output is under 150 words"]
  □ [Checkpoint 2 — e.g., "Tone matches the audience"]
  □ [Checkpoint 3 — e.g., "All key information is included"]
Tested In: [Claude / ChatGPT / Both]
Rating: [1–5]
Notes: [What worked, what to tweak next time]
```

**Show a completed example:**

```
PROMPT PLAYBOOK ENTRY

Task: Write a weekly status update email to my manager
CRAFT Prompt:
  Context: I'm a project coordinator at a nonprofit in Chișinău.
  Every Friday I send my manager a status update on 3 active projects.
  Role: Write as me — organized, concise, proactive.
  Audience: My manager, who is busy and prefers bullet points.
  Format: Email with subject line, 3 sections (one per project),
  each with: status, completed this week, blockers, next steps.
  Under 200 words total.
  Tone: Professional, efficient, slightly upbeat.

Expected Output Quality: Manager can scan it in 30 seconds and know
where everything stands.

Evaluation Criteria:
  ☑ Under 200 words
  ☑ Each project has status + completed + blockers + next steps
  ☑ Subject line is clear (e.g., "Weekly Update: March 8")
  ☑ Tone is professional but not stiff

Tested In: Claude
Rating: 4/5
Notes: Claude's output was good but added too much filler in the
intro. Next time I'll add "Skip the greeting — start with Project 1."
```

> **SAY:** "You have 45 minutes for 5–7 prompts. That's about 6–7 minutes per prompt. Minimum 5, stretch goal of 7. Quality matters more than quantity — each prompt should be tested, iterated, and include the evaluation criteria."

- **Circulate actively.** Students often stall choosing tasks. Have the 10 task ideas from the Chain-of-Thought lab projected as fallback:
  - Email drafting, meeting summaries, research outlines, social media posts, cover letters, lesson plans, project briefs, client updates, study guides, presentation outlines

#### STUDENTS DO

- Build their personal Prompt Playbook: 5–7 entries
- Each entry must be tested (run the prompt, evaluate the output)
- Each entry must have a self-evaluation rubric with 3 checkpoints
- Most students will land on 5–6 prompts. That's sufficient.

#### Pacing

| Segment | Time |
|---------|------|
| Explain template + show example | 5 min |
| Students build playbook (5–7 prompts) | 35 min |
| Buffer/circulate/help | 5 min |

#### Teacher Tip

> The self-evaluation rubric is what pushes this to "Evaluate" on Bloom's Taxonomy. If students skip the rubric and just collect prompts, push back: "How would you know if this prompt gave you a good output? What would you check?" This forces metacognition.

#### Check for Understanding

**Question:** "Show me one entry from your Playbook. Read me the evaluation criteria."
**Expected:** Student reads 3 specific, measurable checkpoints.
**If criteria are vague** ("Is it good?"): Coach them to be specific. "Good how? What length? What tone? What information must be included?"

---

### 5:30–5:45 | Day 1 Wrap (15 min)

**Format:** Full group, written + spoken reflection | **GRR Phase:** We Do

#### TEACHER DOES

> **SAY:** "What a day. You walked in this morning never having used AI, and now you've written CRAFT prompts, compared tools, trained a machine learning model, detected bias, and built a personal Prompt Playbook. Let's capture what you learned."

> **SAY:** "3-2-1 exercise. Write down:"
> - "3 things you learned today"
> - "2 things you'll try at work or school this week"
> - "1 question you still have"

> **SAY:** "You have 5 minutes to write. Then I'll ask for volunteers to share."

- After 5 minutes, ask 4–5 volunteers to share one item from each category.
- **Collect the "1 question" responses** — these fuel Session 2's retrieval sprint and tell you what to re-teach.

> **SAY:** "Amazing work today. Tomorrow we dive into research, writing, data analysis, image generation, and building things with AI. Get some rest — and if you're feeling brave, try using CRAFT for something real tonight."

#### STUDENTS DO

- Write 3-2-1 reflection (5 min)
- Share with the group (4–5 volunteers)

#### Pacing

| Segment | Time |
|---------|------|
| Individual writing (3-2-1) | 5 min |
| 4–5 volunteers share | 8 min |
| Logistics for tomorrow | 2 min |

#### Exit Ticket Questions

1. Name the 5 elements of the CRAFT framework and explain why one of them matters most to you.
2. Give one specific example of when you'd choose Claude over ChatGPT (or vice versa), and why.
3. What is one thing you learned today that changes how you'll use AI going forward?

---

## DIFFERENTIATION NOTES (Session 1 Summary)

| Learner Type | Strategy |
|-------------|----------|
| **Struggling learners** | Provide printed CRAFT template with fill-in-the-blank fields. Pair with a stronger partner during tool comparison. Offer a simplified prompt to start with. Have the 10 fallback task ideas always visible. |
| **Advanced learners** | Challenge them to chain multiple prompts together. Ask them to test edge cases (prompts that break the model). Have them document patterns they notice for the class. |
| **Language support** | Allow prompts in students' first language, then translate. Provide key vocabulary list (token, temperature, prompt, output, bias, training data) with simple definitions. Let students compare AI outputs in different languages. |

---

## POST-SESSION REFLECTION (for the instructor)

- [ ] What worked well today?
- [ ] What would I adjust for next time?
- [ ] Which students need follow-up or additional support?
- [ ] Did timing work? Where did I run long or short?
- [ ] What questions came up in the 3-2-1 that I need to address tomorrow?

---

## KEY RESOURCES FOR THIS SESSION

| Resource | URL | Used For |
|----------|-----|----------|
| Claude.ai | https://claude.ai | Primary AI tool |
| ChatGPT | https://chat.openai.com | Tool comparison |
| Google Gemini (backup) | https://gemini.google.com | Moldova fallback |
| Poe.com (backup) | https://poe.com | Moldova fallback for Claude |
| Teachable Machine | https://teachablemachine.withgoogle.com | ML bias exercise |
| 3Blue1Brown LLM Video | https://www.3blue1brown.com/lessons/mini-llm | "How AI Works" reference |
| CRAFT Framework Guide | https://craftingaiprompts.org/ | Prompt framework |
| DAIR.AI Prompt Guide | https://www.promptingguide.ai/ | Extended reference |
