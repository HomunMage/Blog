---
title:  "AI-native is a False Premise"
date:   2026-04-20 10:00:00 +0800
tags: [AI]
---

What is AI-native? Writing code with AI? AI-assisted development? Or designing a system from the ground up so AI can use it well?

After arguing about it for a year, I've landed on a conclusion: **AI-native is a false premise.**

Not because it's meaningless, but because it puts the focus in the wrong place. The real question isn't "what new things does AI need," but "how bad were our old designs, really?"

Humans have tolerated decades of bad design — inconsistent APIs, chaotic package management, compiler errors that read like ancient runes. We routed around the mess with "experience," "intuition," and Google.

AI doesn't route around things.

AI isn't more demanding. It just can't tolerate chaos the way humans can. A system that's "barely usable" for a human is "unusable" for AI.

**So the essence of AI-native isn't designing new things. It's finally having a reason to pay down decades of accumulated technical debt.**


## Why Do LLMs Need Such Long Prompts?

90% of the information in human communication never appears in the words. It lives in a shared world model — common sense, embodied experience, social norms, history. Two humans talking don't need to declare "I am a human," "do you have a body?", "we share the same laws of physics."

LLMs have none of that.

It isn't "a defective person." It's a different species — a statistical continuation engine that lives in a pure-text vacuum. It has read every word humans have written but doesn't know what "hunger" feels like, or the pragmatic difference between "joking" and "lying."

**Prompt / context engineering is, at root, using explicit text to simulate the vast pile of implicit, unspoken, taken-for-granted assumptions in human communication.**

This isn't a flaw in the LLM. It's the mirror image of the miracle of human communication — we don't notice those assumptions, the way fish don't notice water. The LLM is forced to freeze the water into ice cubes, one by one, written into the prompt, before it has something to walk on.

And the reason we need such long prompts is that past software design never considered "non-human agents" as users.


## Failed Attempts

### GPTs: toy-grade

Wrapping a prompt as a product. No execution structure, no version control, can't reliably execute multi-step tasks.

### LangChain: a worse abstraction

Classical OOP thinking applied to a probabilistic system, manufacturing fake determinism. Like an ORM that sacrifices SQL's expressiveness, LangChain sacrifices the visibility and debuggability of the prompt.

### MCP: the failure of specification thinking

Trying to constrain AI with enterprise-software-style specifications, instead of acknowledging that AI is fundamentally statistical continuation — what it needs is a deterministic shell, not a thicker spec document.

The shared failure of all three: **trying to "tame" AI with traditional software engineering thinking, instead of designing an environment from the ground up where AI works well.**


## The Essence of Skills — Like Docker

To understand why Skills is the right direction, look at Docker first.

What did Docker solve? "It works on my machine" — that eternal problem.

Before Docker, deploying a service meant:
- Manually writing deployment docs (usually incomplete)
- Listing dependencies (usually missing a few)
- Setting environment variables (scattered everywhere)
- Praying that prod looked like dev

What's the essence of Docker? **Taking the standardization steps everyone should have been doing — but everyone was lazy about — and turning them into a forced, executable Dockerfile.**

It didn't invent something new. It **took the "tacit knowledge" in senior engineers' heads — the SOPs that "I know how to do this because I'm experienced" — and turned it into explicit, executable, version-controllable files.**

### Skills Does the Same Thing

Before Skills, getting AI to reliably complete a task required:
- Writing a long prompt (forgetting steps every time)
- Trial and error, parameter tuning (burning tokens)
- Praying AI got lucky and didn't screw up

The essence of Skills: **taking the SOPs in senior prompt engineers' heads — the tacit knowledge of "I know how to guide AI through this because I'm experienced" — and turning them into explicit, reusable, composable SKILL.md files.**

Just as a Dockerfile means developers don't have to manually configure environments every time, Skills means AI doesn't have to relearn how to complete a task every time.

**Docker wipes engineers' butts — those environment standardization steps that should have been done but weren't, due to laziness or time pressure. Skills wipes AI's butt — those task steps that should have existed, but were missing because the prompt was incomplete.**

This isn't a put-down. **Great tools are usually the ones that take "things that should be done but no one does well" and turn them into "things you can't avoid doing."**


## The Real Turning Point — Harness + Skills

The new paradigm is simple:

| Old approach | New approach |
|-|-|
| Let the LLM execute the task directly | Let the LLM select and call deterministic tools |
| Prompt says "please calculate 1+1" | Prompt says "please call calculator(1,1,'+')" |
| Unstable output | Deterministic tool execution |
| Depend on the model "knowing how" | Depend on the tool "actually doing it" |

This is GUI vs Terminal:

GUIs let regular people operate computers, but terminal + scripts let engineers precisely control, compose, automate, and version.

GPTs / LangChain / MCP are GUI-thinking — trying to package AI as "easy to use."

Skills + Harness is terminal-thinking — providing atomic tools (bash, CLIs, scripts) so AI can compose deterministic components the way a human engineer does.

**The strongest player is neither a pure prompt engineer nor a pure software engineer, but someone who is both: knowing when prompt is enough and it's time to write a harness; knowing when the harness is too heavy and it's time to go back and fix the prompt.**


## AI-native is a False Premise — Because Good Design Helps Everyone

When I started designing my own toolchain, I noticed something:

A good environment for AI is also a good environment for humans.

| Dimension | Old design | AI-native design |
|-|-|-|
| API consistency | Inconsistent, full of exceptions | Fully consistent |
| Data model | Normalized, migration-heavy | Flexible, no migration |
| Query language | String concatenation, error-prone | Restricted, compilable, type-safe |
| Composition | Implicit, doc-dependent | Explicit, linear |
| Error messages | Stack traces for humans | Repair hints for AI |

These properties are also better for humans.

Nobody likes inconsistent APIs. Nobody likes complex migrations. Nobody likes string-concatenated SQL.

It's just that before, "no time to fix it." Now, "we have to fix it, because AI has to use it."

**So the essence of AI-native isn't that AI needs special treatment — it's that we finally have a reason to pay back decades of debt that software engineering has been carrying.**


## Rust's Biggest Beneficiary — Because It Has No Ecosystem

This is the most counterintuitive part.

Traditional view: Rust's ecosystem is too small, lacks libraries, hard to popularize.

AI-era view: **Precisely because Rust's ecosystem is small, clean, and unburdened by history, AI can rewrite the entire ecosystem in Rust from scratch.**

C/C++ has 40 years of historical debt:
- Chaotic package management (vcpkg, conan, manual builds)
- Famously incomprehensible compiler errors (hundreds of lines of template explosion)
- Undefined behavior everywhere

AI is afraid of these things. Not because AI is weak, but because AI's statistical nature can't handle "exception lists" — it needs consistent rules.

Rust's advantages:
- Unified package management (Cargo)
- Famously clear compiler errors (tells you exactly what's wrong and how to fix it)
- Memory safety, no undefined behavior

**Rust isn't favored by AI because it's "new." It's favored because it has clean design, good error messages, and a centralized ecosystem.**

And its disadvantage of "no ecosystem" becomes an advantage in the AI era — because there's no legacy, AI can write the whole ecosystem from scratch, with no migrations, no compatibility, no enduring of historical debt.
