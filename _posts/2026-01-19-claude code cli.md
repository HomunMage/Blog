---
title: "From Freeloader to $100/Month: Claude Code CLI Made Me Rethink What AGI Really Is"
date:  2026-01-19 10:00:00 +0800
tags: [Programming]

---

## The Story of Getting Hooked by My Coworkers

I got hooked by my coworkers.

I used to be a happy freeloader, rotating between Claude, GPT, and Gemini for coding. Since I write a lot of code daily, even rotating between all three, I'd still hit rate limits every day. That went on for quite a while, and I thought this was just the normal life of AI-assisted development.

Then my coworker on the left started talking about how great Opus is.

At first, I didn't take it seriously. I thought, "Isn't free good enough?" But he kept talking about it for weeks, and every time he demoed the output quality, my resistance gradually crumbled. Finally, I swiped my card for a Pro subscription.

But wait, the story doesn't end there.

Then my coworker on the right started pushing me to use Claude Code CLI in VSCode.

"You run it directly in the terminal, and it can modify your entire project's code. No need to copy and paste piece by piece," he said.

I tried it.

And I got addicted.

I immediately hit the limit again. Pro wasn't enough, so I upgraded straight to Max—$100 USD per month.

It's seriously powerful. Once you use it, there's no going back. Now I have two projects running simultaneously with Claude writing code. It reads the codebase, modifies files, runs tests, and fixes bugs on its own while I sit back drinking coffee and watching it work.

---

## Claude Code CLI: A Mature and Powerful Agentic Agent

Let me explain what Claude Code CLI is.

This is a command-line tool developed by Anthropic that lets you interact with Claude directly in the terminal. But it's not just chatting—it's a true **agentic agent**:

- **It can read your entire project**: Understanding your code structure, dependencies, and config files
- **It can directly modify files**: Not giving you code snippets to copy-paste, but actually making the changes for you
- **It can execute terminal commands**: Running tests, installing packages, git commits
- **It can collaborate across multiple files**: Refactoring entire modules, cross-file modifications, handling complex refactoring

This isn't a chatbot. This is an engineer living in your terminal.

And this experience made me start rethinking a bigger question:

**What is AGI? What is true intelligence?**

---

## A Contrarian View: Intelligence Doesn't Require a World Model

Right now, almost every big name in AI is talking about **World Models**.

Yann LeCun is pushing JEPA, saying AI needs to build internal models of the world. Tesla's FSD uses vision, LiDAR, and multi-dimensional sensors to understand the physical world. Everyone's saying that true AGI needs to "understand" the world like humans do.

But I have a different perspective.

**The core of true intelligence isn't about perceiving the world—it's about verification and reasoning.**

Let me explain.

---

## LLM in TUI = Embodied AI

When I watched Claude Code working in my terminal, I suddenly realized something:

**This is a form of embodiment.**

Not physical world embodiment, but it's facing a **real world**—a world composed of file systems, code execution, and compilation results.

In this world:
- Whether code runs or not is an objective fact
- Whether tests pass or not is an objective fact
- Whether logic is correct or not is an objective fact

This is completely different from pure chatting. Pure chat is text in, text out, with no real "grounding." But in the terminal environment, every action the AI takes has **verifiable results**.

Tesla's AI has sensors, vision, LiDAR, and multi-dimensional inputs. These certainly allow it to perceive the physical world.

But perception isn't intelligence.

A fly's visual system is extremely sophisticated, with reaction speeds faster than any AI. But we wouldn't say a fly is intelligent.

---

## The Essence of Intelligence: Verifiable Reasoning

What is true intelligence?

I believe it's **verifiable reasoning ability**.

This is why AlphaZero is so important.

AlphaZero didn't learn from human game records. It learned through self-play in an environment with clear rules and verifiable outcomes. Win is win, lose is lose, no gray areas.

This process allowed it to develop "game sense" that surpasses humans—a true intelligence, not just pattern matching.

Now, apply this logic to LLMs:

**When an LLM learns mathematical derivations and writes code in a terminal environment, it's facing this kind of verifiable environment.**

- Mathematical proofs: Correct is correct, wrong is wrong, formally verifiable
- Code: It runs or it doesn't, there's a bug or there isn't
- Logical reasoning: Every step can be verified

This is the essence of **RLVR (Reinforcement Learning with Verifiable Rewards)**.

---

## Andrej Karpathy's View: AI is a Ghost, Not a Creature

Andrej Karpathy's perspective in "2025 LLM Year in Review" aligns perfectly with mine:

**AI is not a creature; it's a ghost.**

Creatures need bodies, sensors, and survival in the physical world.

But ghosts don't. Ghosts exist in another dimension, interacting with reality in a different way.

LLMs are exactly this kind of existence. They don't need eyes to "see" the world or hands to "touch" objects. They understand and manipulate the world through text, code, and logical symbols.

And the terminal—this purely text-based interface—is the perfect habitat for ghosts.

Karpathy emphasized the importance of **RLVR** in his video. This is no coincidence.

Because verifiable environments are the key to allowing ghosts to truly "learn" rather than just "imitate."

---

## Redefining Embodiment

The traditional view of embodied AI holds that: AI needs a body and needs to interact with the physical world to develop true intelligence.

But I want to propose a different framework:

**The essence of embodiment isn't a physical body, but "interaction with a verifiable environment."**

- Physical robots interact with the physical world through sensors → One form of embodiment
- LLMs interact with the code/logic world through terminals → Another form of embodiment

What they have in common is: **Actions have consequences, and consequences are verifiable.**

And the latter—embodiment in the logical world—might be better suited for developing pure reasoning intelligence.

Because in the logical world, there's no sensor noise, no chaos of the physical world. Every reasoning step is clear and verifiable.

It's like cultivating intelligence in a pure laboratory, rather than in the noisy real world.

---

## Why World Models Might Not Be the Key

Back to the World Model discussion.

Proponents of World Models believe that AI needs to build internal models of how the world works to truly "understand" and make wise decisions.

This sounds very reasonable. Humans certainly have such internal models.

But my question is: **Is this a sufficient condition for intelligence, or just one possible path?**

Consider this analogy:

- **World Model Path**: Perceive the world → Build a model → Reason based on the model
- **RLVR Path**: Act in a verifiable environment → Receive clear feedback → Learn reasoning rules

Both paths might lead to intelligence. But the latter is more "pure"—it directly learns reasoning itself, rather than indirectly learning through perceiving the world.

AlphaZero doesn't have a "Go world model"—it doesn't know what material the pieces are made of, how big the board is, or which room it's playing in. But it's better at Go than any human with a "world model."

Because what it learned is **pure strategic intelligence**.

---

## Claude Code CLI: A Living Example

Let's return to Claude Code CLI.

When I watch it work in my project, I see:

1. **It reads the codebase** (perceiving the environment)
2. **It makes modifications** (taking actions)
3. **It runs tests** (verifying results)
4. **It adjusts based on test results** (learning from feedback)

This is a complete RLVR loop, happening in my terminal.

And it keeps getting stronger.

Not just because the model is getting bigger, but because this agentic way of working allows it to continuously receive feedback in real code environments.

**This is why LLMs in TUI/CLI might be the closest form to AGI.**

Not because they have any special sensors, but because they exist in an environment with clear rules and verifiable results.

---

## Conclusion: The Essence of Intelligence is Verifiable Reasoning

After writing all this, let me summarize my views:

1. **AGI doesn't need a physical World Model**. Perception and intelligence are two different things.

2. **The core of intelligence is verifiable reasoning ability**. Being able to make correct judgments under clear rules and learn from the results.

3. **Terminal/TUI is the perfect embodiment for LLMs**. It provides a clean, verifiable environment where AI can truly learn, not just imitate.

4. **RLVR might be the key to AGI**. There's a reason Andrej Karpathy emphasizes it.

5. **Claude Code CLI is living proof of this theory**. An agent living in the terminal, demonstrating remarkable problem-solving capabilities through interaction with real code environments.

---

## Afterword: From Freeloader to True Believer

Three months ago, I was still rotating between three AI services, penny-pinching every conversation's tokens.

Now I spend $100 a month to have Claude write code for me, and I think it's totally worth it.

This isn't just because it saves me time (though it definitely does).

It's because in using Claude Code CLI, I've seen a new possibility—a possibility of demonstrating true intelligence without complex sensors, without physical embodiment.

AI is a Ghost, not a Creature.

And the terminal is the Ghost's body.

---

*If you're also a developer, I strongly recommend trying Claude Code CLI. Not just for productivity, but to witness firsthand: what AI can do when it exists in a verifiable environment.*

*That experience will change your understanding of the essence of intelligence.*
