---
title:  "From Copy-Paste to Engineering Manager: My Journey Through Every Era of AI-Assisted Coding"
date:   2026-02-18 10:00:00 +0800
tags: [Programming]
---

Everyone uses AI differently when writing code. Some people swear by Cursor. Others live in the terminal with Claude Code. Some just vibe-code entire apps into existence. And plenty of developers still copy-paste from ChatGPT like it's 2023.

I've done all of it. Here's what I learned along the way — and how I accidentally built myself an AI development team.

---

## The Landscape: How People Actually Use AI to Code

Before I tell my story, let's map out the major "schools" of AI-assisted coding that exist today. Knowing the landscape helps you understand where you are — and where you might want to go.

### 1. Chat + Copy-Paste

**Tools:** ChatGPT, Claude.ai, Gemini

The OG approach. You describe your problem in a chat window, get code back, paste it into your editor, and hope it works. When it doesn't, you paste the error message back and try again.

**Who it's for:** Everyone, honestly. Beginners use it to learn. Senior devs use it to explore unfamiliar territory. It's free, simple, and requires zero setup.

**The catch:** You're the middleware. You spend half your time switching windows and manually shuttling context between AI and your project.

### 2. IDE-Integrated AI

**Tools:** Cursor, Windsurf, GitHub Copilot, Continue

AI lives inside your editor. It autocompletes as you type, and you can chat with it in a sidebar that sees your entire codebase. You never have to leave your development environment.

**Who it's for:** Working developers who want acceleration, not hand-holding. You know what you want to build; you just want to get there faster.

**The catch:** Monthly subscriptions add up, and less experienced developers sometimes accept suggestions without understanding them.

### 3. Terminal Agent

**Tools:** Claude Code, OpenAI Codex CLI, Aider

AI operates from the command line. You give it a high-level instruction like "refactor the auth middleware to use decorators," and it reads files, plans changes, edits code, and runs tests — all on its own.

**Who it's for:** Experienced developers who are comfortable in the terminal and want to delegate, not just autocomplete.

**The catch:** High token consumption, steep learning curve, and you need enough judgment to review what the agent produces.

### 4. Vibe Coding

**Tools:** Bolt.new, v0, Lovable, Replit Agent

Pure natural language to working app. You describe what you want — "make me an Airbnb clone with maps and user reviews" — and AI generates the entire thing.

**Who it's for:** Non-engineers prototyping ideas, founders building MVPs, or anyone who just wants to see something working quickly.

**The catch:** The generated code is often messy, insecure, and hard to maintain. Great for demos, dangerous for production.

### 5. Multi-Agent Teams

**Tools:** MetaGPT, ChatDev, CrewAI, custom agent workflows

Instead of one AI helper, you orchestrate a team: one agent writes requirements, another designs architecture, another codes, another reviews. They pass work between each other.

**Who it's for:** Bleeding-edge experimenters. This approach is still maturing.

**The catch:** Agent-to-agent communication breaks down often, costs multiply fast, and debugging is a nightmare when you don't know which agent introduced a bug.

### 6. Knowledge-Augmented AI

**Tools:** RAG systems, Cursor's @docs, MCP servers

Instead of writing code, you build a system where AI can search your internal docs, codebase, and institutional knowledge to answer questions accurately.

**Who it's for:** Large teams with lots of legacy code and documentation. Amazing for onboarding.

**The catch:** Requires upfront investment to build and maintain the knowledge base.

### 7. Hybrid (The Real Answer)

Most experienced developers don't pick one school — they use different tools for different situations. Cursor for daily coding, Claude.ai for architecture discussions, Claude Code for large refactors, Bolt.new for quick prototypes. The key is knowing each tool's strengths.

---

## My Evolution: Four Stages

Now here's the interesting part. I didn't choose a school — I evolved through them. And each transition happened because I hit a wall with my current approach.

### Stage 1: The Human Middleware (GPT-3 Era)

I started where most people start: chatting with GPT-3, copying code, pasting it into my editor, running it, copying the error, pasting it back. Repeat forever.

To save tokens (they were expensive back then), I got good at extracting only the relevant code snippets to share. I'd carefully select which functions, which files, which error messages to include. Without realizing it, I was developing a critical skill: **context engineering** — the art of deciding what information an AI needs to see to give you a good answer.

As context windows grew longer, I could paste multiple related files at once. Suddenly the AI could understand relationships between files, and its suggestions jumped from "snippet-level" to "system-level." That was the first big leap.

**My role:** Data courier, shuttling information between two worlds.

### Stage 2: The Commander (Claude Code in VSCode)

When a colleague introduced me to Claude Code in VSCode, everything changed. Instead of manually copying file contents, I could just tell the AI: "look at `src/auth/middleware.ts` and `src/routes/api.ts`."

The AI could read files, write files, and execute commands on its own. I stopped being the person who carries information and became the person who points and says "look there, fix that."

**My role:** Directing attention, not transporting data.

### Stage 3: The System Designer (llm.*.md Files)

I quickly got tired of repeating myself. Every new conversation, I'd have to re-explain the project structure, the coding conventions, the architecture decisions, which files matter. Over and over.

So I started writing `llm.*.md` files — essentially onboarding documents for the AI. Before doing any work, the AI had to read these files to understand the project's context, conventions, and constraints.

This was a turning point. I was no longer giving instructions per task; I was **building a system** that made every future task go better. My implicit knowledge — all the stuff in my head about how this project works — became explicit documentation that any AI session could absorb instantly.

A nice side effect: these docs helped human teammates too.

**My role:** Designing the rules of engagement, not fighting individual battles.

### Stage 4: The Engineering Manager (Agent Teams)

This is where I am now, and it's a fundamentally different way of working.

I use Claude Code's agent team capabilities. Multiple agents run in tmux sessions, working in parallel or in sequence. But here's the key innovation: **I require the agents to maintain two status files.**

- **`plan.status`** — The strategic layer. What's the overall plan? What's been completed? What's next? Think of it as a living project roadmap.
- **`working.status`** — The tactical layer. What is this specific agent working on right now? What step are they on? What problems have they encountered? Think of it as a real-time standup update.

Every agent reads these files before starting work, and updates them continuously as it progresses. When one agent finishes its task, it updates the plan, and a new tmux session spins up to pick up the next task. This loops until everything is done.

Why does this matter? Because AI agents have no memory between sessions. Each new session is a blank slate. But by reading `plan.status` and `working.status`, a fresh agent can immediately understand what happened before and what needs to happen next. **I'm using the file system as shared memory between agents** — essentially a shift-change handoff log, just like nurses or factory workers use.

**My role:** Setting strategy, defining process, reviewing outcomes. Not writing code.

---

## The Secret Sauce: A Built-In Quality Pipeline

But here's what really makes this setup work. It's not just that AI writes the code — it's that AI **tests its own code** at every step.

I require my agents to run a full quality pipeline during development, all inside Docker Compose:

**Static analysis first.** `docker compose exec fe npm lint` and `docker compose exec be uv ruff` enforce coding standards automatically. The AI's code has to pass lint before moving on. No exceptions. No "I'll clean it up later."

**Architecture check-ins.** Midway through implementation, the agent pauses to re-evaluate the architecture. Is the current structure still making sense? Does anything need refactoring before we go further? This prevents the "code snowball" problem where bad early decisions compound into an unmaintainable mess.

**Automated tests.** The agent writes its own test cases and runs them. If tests fail, the agent debugs and fixes until they pass. It's TDD, but the AI does both sides — writing the tests and writing the implementation.

**Backend verification.** The agent uses `curl` to hit API endpoints and verify correct behavior. Not just "does the function return the right value" but "does the full HTTP request-response cycle work correctly?" Routes, middleware, response formats, status codes — all checked.

**Frontend visual verification.** This is my favorite part. The agent runs Playwright to take screenshots of the rendered UI, then examines those screenshots to judge if the frontend looks correct. It's visual regression testing, powered by the LLM's ability to "see" images. An AI looking at another AI's work and deciding if it looks right.

### Why This Pipeline Matters

Most AI coding setups are **open-loop** — the AI generates code and hopes it works, like a chef who never tastes their own food. My setup is **closed-loop** — every piece of output gets fed back through multiple verification layers. Lint catches style issues. Tests catch logic bugs. Curl catches integration problems. Screenshots catch visual regressions.

Each layer provides feedback that drives the AI to self-correct. Write, verify, fix, verify again. The agent doesn't move forward until every check passes.

The result: by the time code reaches me for review, it's already been linted, tested, integration-tested, and visually verified. The AI has "testing consciousness" baked into its workflow — not as an afterthought, but as a fundamental part of how it works.

---

## The Bigger Picture: What Changed At Each Stage

Looking back at my journey, there's a clear pattern:

| Stage | My Role | What I Manage |
|-------|---------|---------------|
| Copy-Paste | Data courier | Every line of code |
| Claude Code in VSC | Task commander | Each task |
| llm.*.md files | System designer | Processes and standards |
| Agent Teams | Engineering manager | Strategy and quality |

At each stage, I moved up one level of abstraction. I went from managing code to managing tasks to managing processes to managing a team. The "code" I write now is mostly markdown files — plans, conventions, architectural decisions — that tell AI agents how to do the actual coding.

This isn't about being lazy. It's about leverage. An engineering manager who insists on writing every line of code themselves is a bottleneck. An engineering manager who builds great systems and hires great people (or agents) multiplies their impact.

---

## Finding Your Own Path

Here's the thing: there's no "right" school of AI-assisted coding. The best approach depends on your experience level, your project's needs, and honestly, what you enjoy.

If you love the craft of coding and want AI to handle the tedious parts, IDE-integrated tools are probably your sweet spot. If you're a non-technical founder who needs to validate an idea fast, vibe coding will get you there. If you're a senior engineer managing complex systems, the agent-based approach might transform your productivity.

The one piece of advice I'd give: **don't get stuck in Stage 1 forever.** Copy-paste works, but it leaves an enormous amount of potential on the table. Push yourself to the next stage — whatever that looks like for you — and you'll be surprised how much your relationship with code (and with AI) changes.

The future of software development isn't "AI writes all the code." It's humans and AI finding the right division of labor — and that division is different for everyone.

---

*This post grew out of a conversation about different approaches to AI-assisted development. The evolution described is real. The tmux sessions are still running.*