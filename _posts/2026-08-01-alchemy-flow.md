---
title:  "Alchemy Flow: Git Flow's Shape, Trunk-Based's Mind"
date:   2026-08-01 10:00:00 +0800
tags: [Programming]
---

Git Flow and Trunk-Based Development (TBD) solve for different things, and teams often end up choosing one and living with what it doesn't cover.

**Git Flow** models the *shape* of a feature well: built somewhere, hardened somewhere, shipped somewhere, via `develop`, `release/*`, and `hotfix/*` branches.

**TBD** models the *discipline* well: one trunk, short branches, fast convergence, no long-lived side branches.

What neither one names explicitly is environment: most SaaS teams run separate dev, stage, and prod, and want to know exactly which one a commit is in. Combining the two ideas — Git Flow's staged handoff, TBD's single trunk — is what I ended up calling **Alchemy Flow**.

## The Rule

> **Branches move. Production shouldn't be bound to something that moves.**

Dev and stage can bind to branches — they're supposed to churn. Production binds to a tag instead: a name you chose on purpose, not wherever a branch happens to be right now.

<img src="{{ site.baseurl }}/blob/Programming/2026-08-01-alchemy-flow.svg" width="800" style="max-width: 100%; height: auto;" alt="Alchemy Flow: feature branches from main at 1.3.4 and merges back as 1.4.0; main keeps hardening through 1.4.1 to 1.4.3; prod fast-forwards from tag 1.3.4 to tag 1.4.3">

Three lanes, three environments, time flowing bottom to top.

## How It Works

- **`main` is stage.** Every commit deploys there. It's TBD's trunk, just relabeled.
- **Feature branches cut from a tag**, live days not weeks, and merging one back is a **minor bump**: `1.3.4` → `1.4.0`.
- **Fixes commit straight to `main`** — no `hotfix/*` — and each gets a **patch bump**: `1.4.1`, `1.4.2`, `1.4.3`.
- **Prod fast-forwards to a tag** once it's proven quiet on stage. Not a merge, not a branch move — a pointer jump. It might skip `1.4.1` and `1.4.2` entirely and land straight on `1.4.3`.

```bash
git checkout -b feature/oauth-login 1.3.4      # branch from a tag
# ...merges back...
git tag 1.4.0                                   # minor bump: a feature landed
# ...fixes land straight on main...
git tag 1.4.3                                   # patch bump: stage hardened
git checkout 1.4.3                              # prod fast-forwards here
```

Production was on `1.3.4`. Now it's on `1.4.3`. It never touched `1.4.0`, `1.4.1`, or `1.4.2` — those versions existed only to prove themselves on stage first.

## Where It Sits Between the Two

| | Git Flow | TBD | Alchemy Flow |
|---|---|---|---|
| Long-lived branches | 2+ | 1 | 1 |
| Where you stabilize | `release/*` | behind flags | on `main` (= stage) |
| What prod points at | a branch | a commit | **a tag** |
| Fixes go to | a hotfix branch | trunk | trunk |
| "What's in prod?" | check the release branch | check the deploy log | read the tag |

Alchemy Flow keeps Git Flow's separation between *merged* and *shipped*, using tags in place of `release/*` and `hotfix/*` — a tag freezes a state without needing its own branch. It keeps TBD's one-trunk discipline, and adds an explicit binding between branch and environment on top of it.

## Where It Doesn't Fit

If you maintain multiple production versions for different customers (on-prem, can't-upgrade clients), you need a real maintenance branch — this assumes one production, which is a SaaS assumption. If a human must formally sign off on a frozen release artifact, that artifact wants a branch. And past a certain team size, `main` outpaces what stage can settle, and you need merge queues instead.

For a small-to-medium SaaS team, though, this is the least ceremony I've found that still answers "what's in prod, and how did it get there?" in one word: a tag.
