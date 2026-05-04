---
title:  "From Prompt to Harness: The Real Paradigm Shift in AI Engineering"
date:   2026-04-10 10:00:00 +0800
tags: [AI]
---

*An independent developer's notes on co-evolving with LLMs.*

---

## Part 1: We Started by Thinking AI Was a "Chat Tool"

The earliest way most people used LLMs was intuitive:

1. Write a prompt.
2. Read the result.
3. Edit the prompt.

It looked like talking to a very clever tool. From this came two disciplines:

- **prompt engineering**
- **context engineering**

But the deeper we went, the more a fundamental question kept surfacing:

> Why is AI behavior so dependent on context?
> Why does it take such fragile prompt-craft to keep it stable?

The honest answer turns out to be uncomfortable:

**An LLM is not a tool. It is a context-driven cognition system.**

---

## Part 2: What an LLM Actually Is

Strip away the marketing and an LLM is doing exactly one thing:

> Predicting the next token, conditioned on context.
>
> `P(next token | context)`

Which means:

- **Prompt** = changing the conditioning.
- **Context** = reshaping the probability distribution.
- **Output** = a behavior space that has been narrowed for you.

The implication is sharp: *intelligence here is not a fixed capability. It is a transient state, triggered by context.*

---

## Part 3: Why LLMs Need Such Long Prompts

Roughly 90% of the information in human communication never appears in the words. It lives in a shared world model — common sense, embodied experience, social norms, history. Two humans don't need to declare "I am a human", "you have a body", "we share the same physics."

An LLM has none of that.

It isn't a defective person. It's a different species — a statistical continuation engine that lives in a pure-text vacuum. It has read everything humans have written but does not know what hunger feels like, or how "joking" and "lying" differ pragmatically.

**Prompt and context engineering, at root, is using explicit text to simulate the vast pile of implicit assumptions humans take for granted.**

This isn't a flaw in the LLM. It's the mirror image of the miracle of human communication. We don't notice those assumptions, the way fish don't notice water. The LLM forces us to freeze the water into ice cubes, one by one, so it has something to walk on.

---

## Part 4: Why Prompt Engineering Works At All

The real problem with LLMs was never "not smart enough." It was **entropy** — too many plausible continuations.

Prompt engineering, properly understood, is just:

> Reducing entropy. Collapsing the behavior space.

That's what role setting, constraints, examples, and format specifications all do. They aren't "controlling the AI." They're building a temporary world model the AI can stand on.

This reframes the field. We took so long to figure it out because we kept assuming the bottleneck was *understanding*. It wasn't. It was *certainty*.

| Old framing | New framing |
|---|---|
| Understanding is weak → bigger models, more data, stronger prompts | Certainty is weak → narrow the decision space, surround the model with deterministic tools |

---

## Part 5: Sci-Fi AI vs. Real AI

Most science fiction quietly assumes an AI has stable goals, persistent memory, and autonomous agency. HAL, Skynet, Samantha — all agent-shaped.

LLMs are none of those things. They are *stateless, context-dependent systems* re-instantiated on every call.

| Sci-Fi AI | Real LLM |
|---|---|
| Stable agent | Context-dependent behavior |
| Long-term goals | Per-token prediction |
| Continuous self | Re-instantiated each call |

A lot of bad design decisions in early AI tooling come from quietly importing the sci-fi assumption.

---

## Part 6: The Failed Attempts

### GPTs — toy-grade first try

GPTs were prompt engineering, productized and democratized. They wrapped "a big context" into something shareable and composable. Useful, but only surface-level engineering: no version control, no debuggability, no reliable multi-step execution.

### LangChain — a worse abstraction

Classical OOP thinking applied to a probabilistic system. It manufactured *fake determinism* — over-abstracted, callback-hell-prone, version-churned.

It's the LLM equivalent of an ORM that wraps a relational database into objects and loses the expressive power of SQL. LangChain wrapped LLMs into composable chains and lost the visibility and debuggability of the prompt.

### MCP — protocol thinking, misapplied

The protocol itself is fine. The framing around it leaned heavily on enterprise-software instincts: governing the AI through specification rather than acknowledging that the engine underneath is statistical continuation.

The common failure mode of all three:

> Trying to replace the human + AI loop with pure traditional software thinking, instead of strengthening it.

---

## Part 7: The Turning Point — Skills + Harness

The shift isn't about constraining the *output*. It's about constraining the *behavior space*.

| Old approach | New approach |
|---|---|
| Make the LLM execute the task directly | Let the LLM select and call deterministic tools |
| "Please calculate 1+1" | "Please call `calculator(1, 1, '+')`" |
| Unstable output | Deterministic execution |
| Depend on the model "knowing how" | Depend on the tool "actually doing it" |

### GUI vs. Terminal

GPTs / LangChain / MCP are GUI-thinking — packaging AI to be "easy to use."

Skills + Harness are terminal-thinking — exposing atomic primitives (bash, CLIs, scripts) so the AI can compose deterministic components the way a human engineer would.

### The Go (weiqi) analogy

When AlphaGo first arrived, professional players said they couldn't read its moves. Today, learning Go with AI is normal. That didn't happen because AI imitated human intuition. It happened because humans gave up on "understanding why the AI played that move" and re-grounded the game on a *global win-rate calculator*.

LLM engineering is going through the same transition: from *make the AI behave like a person* to *wrap a probabilistic core in a deterministic shell.*

---

## Part 8: Two Philosophies — OpenClaw vs. Hermes

Two camps are crystallizing.

**OpenClaw — extrinsic systems**
- Skills / tools ecosystem
- Multi-agent orchestration
- External SaaS integration
- *Intelligence lives outside the model.*

**Hermes — intrinsic systems**
- Self-improving loops
- Memory-driven learning
- Autonomous behavior
- *Intelligence lives inside the model.*

| Type | Essence |
|---|---|
| OpenClaw | Orchestration system |
| Hermes | Learning system |

These are not the same product with different branding. They're different bets on where the next decade of capability comes from.

---

## Part 9: The Strongest Player

The dominant practitioner is neither a pure prompt engineer nor a pure traditional software engineer.

| Layer | Top Go player | Top LLM engineer |
|---|---|---|
| Base | Human shape-reading, board feel | Prompt engineering, model-behavior intuition |
| Middle | Reading AI win-rate distributions | Harness design, tool calling |
| Integration | When to trust AI, when to trust the human | When to let the LLM roam, when to force the deterministic path |

**Pure prompt engineer:** Writes beautiful context, but can't write a bash script to verify output. When the LLM wobbles, the only move is "add more prompt."

**Pure traditional engineer:** Determinism-pilled. Over-abstracts. First reaction to non-deterministic output is "filter it with more code."

The strongest practitioner is the one who knows *when prompt is enough and harness should take over*, and *when harness is too heavy and you should go back to prompt*.

---

## Closing

The story we keep telling ourselves about AI engineering is "make the model smarter." The story that actually matches the work is "shape the world the model lives in."

Prompts shape it. Context shapes it. Tools shape it. Harnesses shape it. Skills shape it.

The model is a probability cloud. Engineering is the act of bending it into something a human can stand on.
