---
title:  "The Confused Junior Developer and the Three Questions"
date:   2026-02-01 10:00:00 +0800
tags: [Programming]
---

## 🐣 A Story About Growing Up in Tech

Last week, I watched a junior developer named Amy debug a sorting algorithm for three hours. She finally fixed it. Her code was beautiful—clean, efficient, O(n log n).

Then her tech lead Sarah walked over.

"Amy, why are we sorting this data at all?"

Amy froze. The feature spec said "sort the user list." So she sorted. She never asked *why*.

Sarah smiled. "The PM wanted users to find their friends faster. Sorting alphabetically won't help—we need to sort by interaction frequency. But actually... maybe we don't need sorting. Maybe we need a search bar."

Amy had solved the wrong problem *perfectly*.

---

## 🎓 The Three Questions of Mastery

This moment reminded me of something I've been thinking about for years: **the difference between HOW, WHAT, and WHY.**

I believe these three questions map perfectly to both academic degrees and software engineering levels:

| Level | Degree | Engineer | Core Question | Example Task |
|-------|--------|----------|---------------|--------------|
| **Foundation** | Bachelor's | Junior | **HOW** do I implement this? | LeetCode, algorithms, coding patterns |
| **Applied** | Master's | Senior | **WHAT** approach should we use? | System design, choosing technologies, handling ambiguity |
| **Strategic** | Doctorate | Staff/Principal | **WHY** are we building this? | Architecture vision, defining what problems matter |

Let me break this down.

---

## 👶 The Bachelor / Junior: Masters of HOW

**The Question:** *"How do I implement this?"*

When you're starting out, the problems are *given* to you. Clear inputs. Expected outputs. Your job is execution.

- LeetCode problems have test cases
- Homework assignments have rubrics  
- Jira tickets have acceptance criteria

This isn't a criticism—it's the foundation. You *need* to know how to implement a binary search before you can decide *when* to use one. You *need* to write a hundred APIs before you develop intuition about which patterns work.

**Amy knew HOW to sort.** That's valuable. But it wasn't enough.

---

## 🧑‍💼 The Master's / Senior: Masters of WHAT

**The Question:** *"What approach should we use?"*

At this level, the problems get fuzzy. Someone says "make it faster" or "users are complaining" or "we need to scale."

No one hands you a LeetCode problem. You have to:

- Choose between SQL and NoSQL
- Decide on microservices vs monolith
- Pick the right caching strategy
- Navigate trade-offs with incomplete information

**Senior engineers translate ambiguous business needs into technical approaches.**

Sarah knew WHAT the real options were: sorting differently, or maybe not sorting at all. She could see multiple paths where Amy saw only one.

---

## 🎯 The Doctorate / Staff+: Masters of WHY

**The Question:** *"Why are we building this at all?"*

Here's where it gets interesting.

Staff and Principal engineers don't just solve problems—they *define which problems are worth solving*. They ask:

- Why does this system need to exist?
- Why will this architecture serve us for the next 5 years?
- Why should the company invest engineering resources here instead of there?

**This is the hardest skill.** Anyone can solve a well-defined problem. Fewer can figure out what to build. But identifying *why* something matters—connecting technical work to business value, user needs, and long-term vision—that's rare.

The Doctorate isn't about more knowledge. It's about asking a question no one has asked before and proving the answer matters.

---

## 🔄 Wait, Isn't This Just Simon Sinek's Golden Circle?

You might be thinking: *"This sounds like Start With Why!"*

Here's where I respectfully disagree with Sinek.

**Sinek's Golden Circle:**
```
WHY → HOW → WHAT
(Purpose → Process → Product)
```

Sinek argues leaders should *communicate* starting with Why. It's a persuasion framework. "People don't buy what you do, they buy why you do it."

**My Framework:**
```
WHY > WHAT > HOW
(Define the problem > Choose the approach > Execute)
```

This is a *cognitive complexity* hierarchy. Not about communication—about thinking.

**The difference:**

| Sinek's WHY | My WHY |
|-------------|--------|
| Inspirational purpose | Analytical reasoning |
| "We believe in challenging the status quo" | "Why does this problem exist? Why does solving it matter?" |
| Emotional motivation | Problem definition |
| Used to persuade | Used to discover |

Sinek's WHY is about *belief*. My WHY is about *understanding*.

When a Staff engineer asks "Why are we building this?", they're not crafting a marketing message. They're doing the hard analytical work of:

1. Understanding the root cause of a problem
2. Questioning assumptions
3. Ensuring effort goes to the right place
4. Connecting technical decisions to real-world impact

---

## 📈 Why This Framework Matters for Your Career

If you're a junior wondering how to grow, here's the roadmap:

**Junior → Senior Transition:**
Stop waiting for clear requirements. Start asking "What are our options here?" Develop opinions about technologies. Learn to navigate ambiguity.

**Senior → Staff Transition:**
Stop just solving the problems handed to you. Start asking "Is this the right problem?" Zoom out. Connect your work to business outcomes. Define the roadmap, don't just execute it.

---

## 🎁 The Gift Amy Received

Back to Amy. Sarah didn't just fix the feature. She gave Amy a gift: permission to question the problem itself.

Three months later, I saw Amy in a sprint planning meeting. A PM described a new feature. Before anyone could estimate it, Amy asked:

"Why do users need this? What problem are we actually solving?"

The room went quiet. Then the PM smiled.

Amy wasn't a junior anymore.

---

## TL;DR

```
BACHELOR / JUNIOR  → HOW  → "How do I implement this?"
MASTER'S / SENIOR  → WHAT → "What approach should we use?"  
DOCTORATE / STAFF  → WHY  → "Why are we building this?"
```

**Cognitive complexity:** WHY > WHAT > HOW

**This is NOT Sinek's Golden Circle.** Sinek's "Why" is inspirational purpose for communication. My "Why" is analytical problem-definition for discovery.

**The hardest skill isn't solving problems. It's knowing which problems to solve.**

---

*What level are you at? What question do you find yourself asking most? Drop a comment below.* 👇

---

**#SoftwareEngineering #CareerGrowth #TechLeadership #Engineering #StartupLife #CodingLife #ProgrammerLife**