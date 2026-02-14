---
title:  "How a Broken Elevator Changed the History of Programming: Rust's Journey from Side Project to C++ Killer"
date:   2026-02-14 10:00:00 +0800
tags: [Programming]
---


One evening in 2006. Vancouver.

Twenty-nine-year-old Graydon Hoare dragged himself back to his apartment building and found the elevator was down again. Another software crash. He lived on the 21st floor.

As he climbed the stairs, the frustration built: "It's ridiculous that we computer people couldn't even make an elevator that works without crashing!"

He knew where the problem lay. The software inside elevators is typically written in C or C++ — languages that run blazingly fast and use minimal memory, but have an unsolved problem that's plagued the industry for decades: they make it far too easy for programmers to accidentally corrupt memory. One tiny pointer error can bring an entire system down. Like, say, your elevator.

Most people, after trudging up 21 flights of stairs, would just curse and move on. But Hoare went home, opened his laptop, and started designing a new programming language.

He named it Rust — after the rust fungi, organisms that are "over-engineered for survival."

---

## A Compiler Nomad's Arsenal

Hoare was no academic prodigy. No PhD, no paradigm-shifting papers. His identity was simple: a working compiler engineer.

But that was precisely his greatest advantage.

He'd worked on GCC, Clang, the Swift compiler, and Tracemonkey (Firefox's JavaScript engine) — he'd had his hands in nearly every major compiler project out there. He called himself a "language engineer," meaning he'd spent his career building compilers and tools for languages other people designed.

When you've spent a decade cooking in other people's kitchens, you naturally start thinking: if I opened my own restaurant, what would I put on the menu?

Hoare's menu drew from an extraordinarily deep well. The languages he cited as inspirations included CLU (1975), Mesa (1976), Erlang (1986), and Limbo (1990s) — names most working programmers have never even heard of. But Hoare hadn't just heard of them. He'd read their design documents, used their compilers, and understood exactly what problems each one solved.

He later summarized Rust's design philosophy in a single line:

> **"Technology from the past, come to save the future from itself."**

That line is the key to understanding Rust. The language invented almost nothing new. What it did was **assemble** — taking techniques that academia had validated over three decades but that had never entered the mainstream of systems programming, and packaging them into a shape that even C++ programmers could accept.

---

## Haskell Wearing a C++ Skin

If you've spent enough time in programming language circles, you'll have noticed a cruel reality: there's a massive chasm between academia and industry.

Academics knew how to make programs safer as far back as the 1980s. Haskell had a powerful type system that could catch vast categories of errors at compile time. The ML language family had Algebraic Data Types, making it impossible to forget to handle an edge case. Linear Logic, dating back to 1987, explored how type systems could track resource usage.

But all of this stayed locked in the ivory tower. Why? Because the people writing operating systems, database engines, and game engines don't read papers. They use C and C++, because those languages are fast, give you fine-grained control, and — most importantly — they've already spent a decade mastering them.

On the other side, academics didn't care about engineering practicality. Haskell is elegant, but you can't write a kernel in it. Cyclone was an attempt at a "safe C," but it was too academic, too painful to use, and never caught on.

Hoare happened to understand both worlds. He was an industry guy, dealing with C/C++ memory safety nightmares every day. But he was also a voracious language enthusiast who had devoured the designs of all those academic languages.

So here's Rust's recipe:

- **Type system**: Borrowed Haskell's typeclasses, called "traits" in Rust
- **Algebraic Data Types**: Taken from ML/Haskell, called "enums" in Rust, paired with pattern matching
- **Error handling**: Haskell's `Maybe` became `Option<T>`, `Either` became `Result<T, E>` — no more null
- **Memory management**: C++'s RAII (Resource Acquisition Is Initialization), but taken further
- **Ownership transfer**: C++11's move semantics, but redesigned from scratch as cleaner destructive moves
- **Lifetimes and borrowing**: Evolved from Cyclone's region concept, infused with ideas from linear logic
- **Performance promise**: C++'s zero-cost abstraction philosophy — you don't pay for what you don't use
- **Surface syntax**: Curly braces, semicolons, `fn` — looks like C++, so systems programmers aren't scared off

The result: Haskell wearing a C++ skin. On the inside, the safety and expressiveness of functional programming. On the outside, the familiar appearance and raw performance that systems programmers demand.

The brilliance? It tricked C++ programmers into absorbing academic concepts they would never have touched otherwise. You think you're learning a "better C++." In reality, you're being reshaped into a better programmer.

---

## The Borrow Checker: The Thing Everyone Loves to Hate

Rust's true killer feature — ownership and the borrow checker — deserves its own spotlight, because its lineage is more complex than most people realize.

Many assume it's just a souped-up version of C++ RAII. Not quite. It's actually a fusion of three distinct bloodlines:

**Bloodline One: C++ RAII.** A resource's lifetime is tied to the scope of its owning variable. Leave the scope, the resource is automatically freed. This concept has existed in C++ since the 1980s. Rust's `drop` function holds no surprises for anyone who's worked with RAII.

**Bloodline Two: C++11 Move Semantics.** Ownership of a value can be transferred from one variable to another. But C++, weighed down by decades of backward compatibility, had to implement this as "non-destructive moves" — the moved-from object still exists and must be in some valid "empty state." Rust, designed from scratch, went with cleaner destructive moves: a moved-from variable simply ceases to exist. Try to access it and you get a compile error.

**Bloodline Three: Linear Types and Cyclone's Regions.** This is the part C++ doesn't have at all. Cyclone (circa 2001–2006) was an academic project that tried to add safe pointers and region-based memory management to C. It was too academic, and nobody wanted to use it. But Hoare repackaged Cyclone's region concept as "lifetimes" and transformed linear logic into the rule: "every value has exactly one owner at any given time."

The borrow checker sits at the convergence of these three bloodlines: RAII manages resource lifetimes, move semantics manages ownership transfer, and lifetime-plus-borrowing rules prevent dangling pointers and data races.

The core rule is simple enough to fit in a single sentence: **At any given time, you can have either one mutable reference or any number of immutable references, but never both.**

C++ programmers are well aware of these problems — dangling pointers, use-after-free, data races — and they've tried to solve them with smart pointers and coding guidelines. But those are enforced by discipline. Rust's breakthrough was turning "suggestions" into "law," enforced by the compiler. You either comply, or your code doesn't compile. There is no third option.

---

## Then the Seed Landed in the Right Soil

From 2006 to 2009, Hoare worked on Rust alone, telling no one at Mozilla. It wasn't until 2009 that he showed the prototype to his manager.

Mozilla saw the opportunity. They were being tormented by Firefox's C++ codebase — a browser engine is one of the most kernel-like pieces of complex software in the world, demanding extreme performance, precise memory control, and heavy parallelism. And C++ kept producing memory safety vulnerabilities.

Mozilla immediately invested in Rust. The team quadrupled, then doubled again, then doubled again. They also launched Servo — a fully Rust-written experimental browser engine that served as the ultimate real-world test bed for Rust's features.

That decision changed Rust's destiny.

Interestingly, it also changed Rust's soul.

---

## The Founder Left — and the Language Got Better

In 2013, Hoare voluntarily stepped away from Rust.

His explanation was candid: "I don't like attention or stress. I was operating near my limits while I was project tech lead back in 2009–2013. Additionally, I've no reason to believe I would have set up strong or healthy formal mechanisms for decision making, conflict management, or delegation and scaling."

But the deeper reason was this: **the Rust he wanted and the Rust the world needed were not the same language.**

Hoare later wrote a blog post titled "The Rust I Wanted Had No Future." He acknowledged a fundamental divergence between his preferences and the community's direction — he would have traded performance and expressivity for simplicity, which was "broadly opposed to where a lot of people wanted it to go."

The most striking admission: "A lot of people in the Rust community think 'zero cost abstraction' is a core promise of the language. I would never have pitched this and still, personally, don't think it's good."

Zero-cost abstraction — one of the very first things anyone mentions when talking about Rust today — is something the language's own creator didn't want.

Had Hoare stayed and insisted on his vision, Rust would likely have become a simpler, slower, more niche language — something closer to Erlang. Microsoft wouldn't have looked at it. Google wouldn't have used it. The Linux kernel wouldn't have considered it.

Hoare's departure wasn't just healthy. In a very real sense, it was a **prerequisite** for Rust's success.

---

## Big Tech Sits Down at the Table: Not a Matter of Taste, but Survival

After Hoare left, Rust continued to evolve under federated community governance. Then the big companies showed up.

Microsoft discovered that roughly 70% of the security vulnerabilities in Windows and Office were memory safety issues — all caused by C/C++. Google's Android team had the same nightmare. Amazon's AWS needed a language that could safely power low-level virtualization technology.

These companies weren't chasing a trend. They were paying billions of dollars a year for the consequences of C/C++ memory safety bugs. They needed an alternative — one that could match C++ in speed and low-level control but would stop producing those damn vulnerabilities.

This demand directly shaped Rust's evolution:

Zero-cost abstraction became a non-negotiable core promise — if performance was even 5% worse than C++, those companies wouldn't migrate. Foreign Function Interface (FFI) had to be first-class — no company can rewrite billions of lines of code overnight; Rust and C/C++ need to coexist. `unsafe` had to exist — in the real world, some low-level operations require bypassing safety checks. Async/await was added to the language — AWS and Cloudflare needed high-performance asynchronous networking.

In other words: Hoare planted a seed, but the soil it landed in was "every major tech company in the world is being tortured by C/C++ and desperately needs an alternative." The soil determined the shape of the tree.

Had Rust appeared in a parallel universe without security anxiety, it probably would have followed Hoare's preferences and become a simpler, more niche language — maybe occupying the position of OCaml or Erlang. It was because Big Tech arrived with real money and billions of lines of legacy C++ code saying "we need you" that Rust was forged into what it is today.

---

## Why This Isn't the React Story

At this point, you might be worried: wait — the core developer leaves, big companies take over — isn't this exactly the disaster happening to React?

It's not. Not even close.

React's problem is that Facebook/Meta's core developers were pulled away to work on Next.js or jumped ship to Vercel, leaving React's development direction deeply coupled to Next.js. What the community wants and where the framework is actually heading have been drifting apart, with every update feeling like it serves Next.js rather than everyday developers. Control was hijacked by a single company's commercial interests.

Rust took the exact opposite path. After Hoare left, governance was distributed across the community. An RFC process was introduced — any new language feature must go through a public proposal and discussion. No single company can unilaterally dictate Rust's direction. Microsoft wants to use Rust, Google wants to use Rust, Amazon wants to use Rust — fine, but they all have to go through the RFC process and discuss on equal footing with independent developers.

The biggest test came in 2020. Mozilla's mass layoffs gutted the Rust and Servo engineering teams. If Rust had depended on Mozilla the way React depends on Meta, that would have been a death sentence. But Rust survived, because governance had never been in Mozilla's hands. The independent Rust Foundation was established shortly after, supported by multiple companies.

This is the greatest legacy of Hoare's departure: because there was no "soul figure," Rust was forced to build institutionalized governance. The result is a project more resilient than anything that depends on a single person.

---

## The Linux Kernel: The Last Fortress and the Biggest Battlefield

If Rust is an army, the Linux kernel is the last fortress it had to take.

The Linux kernel has over 34 million lines of C code, over thirty years of history, and thousands of maintainers. Its success is built on a culture of extreme conservatism — every line of code is rigorously reviewed, and every change must prove its own worth. This conservatism has made Linux rock-solid, but it also means that introducing any fundamental change is agonizingly slow.

From the launch of the Rust for Linux project in 2020, the war never stopped.

Linus Torvalds himself was open to Rust — he said he was in the "wait and see" camp, willing to let Rust prove itself. But he also admitted frustration at the slow pace of adoption, acknowledging that "old-time kernel developers are used to C and don't know Rust" was the core problem.

The bigger conflicts came from the maintainers below him. Senior kernel maintainer Christoph Hellwig strongly opposed Rust in the kernel, arguing it created fragmentation and extra maintenance burden. On the other side, Asahi Linux's Hector Martin publicly called on Torvalds to intervene and resolve the deadlock, even rallying supporters on social media to apply pressure.

Torvalds saw all of this and told Martin bluntly: "Maybe the problem is you." He rejected the social media pressure campaign, insisting that technical patches and discussions are the way to resolve disputes.

Torvalds also offered a razor-sharp analogy: he said the Rust vs. C debate reminded him of the vi vs. Emacs holy war from his youth — a text editor religious conflict that began in the 1970s and still hasn't ended. Technical discussion had devolved into tribal identity warfare.

Some of the resistance had legitimate engineering concerns behind it — maintainers have limited time, and not everyone has the bandwidth to maintain both C and Rust codebases. But some resistance was simply "I don't want to learn anything new" dressed up in technical-sounding language.

The turning point came at the end of 2025. At the Linux Kernel Maintainers Summit, the top maintainers reached a consensus: Rust is no longer experimental — it is now a core part of the kernel. The "experimental" tag was officially removed.

And — this decision met zero pushback.

After five years of war, the last fortress opened its gates.

---

## LLMs: Not the Catalyst, but the Cleanup Crew

Some might ask: is Rust's success tied to the rise of AI and large language models?

The timeline doesn't line up. Every critical milestone for Rust — the stable release, Big Tech adoption, entry into the Linux kernel — happened before ChatGPT's explosion in late 2022. Rust's rise was powered by thirty years of programming language theory, Hoare's integration work, Big Tech's security anxiety, and healthy community governance.

But LLMs are changing something else entirely: **the possibility of migration at scale.**

In late 2025, Microsoft Distinguished Engineer Galen Hunt announced the goal of eliminating all C/C++ code at Microsoft by 2030. The strategy: combine AI and algorithms, targeting "one engineer, one month, one million lines of code."

In a world without LLMs, this is pure fantasy. Manually rewriting hundreds of millions of lines of C/C++ into Rust would require thousands of engineers fluent in both languages — that kind of talent pool simply doesn't exist. LLMs turned large-scale language migration from a pipe dream into something that can at least be seriously attempted.

At the same time, LLMs are addressing Rust's biggest soft spot: the learning curve. Ownership, lifetimes, the borrow checker — these concepts are a wall for newcomers. But now you can throw a chunk of code that won't compile at an AI assistant and have it explain exactly why the borrow checker rejected it. The learning curve shifts from "banging your head against a wall alone" to "having a patient tutor always at your side."

There's an ironic twist, though: LLM-generated Rust code is generally much worse in quality than LLM-generated Python or JavaScript. The reason is straightforward — training data contains far less Rust code, and Rust's compiler doesn't accept "close enough." Your code must be fully correct to compile.

But flip that around, and it's actually a hidden advantage: **the compiler itself is the best AI code reviewer.** LLM-generated Python might look right but explode at runtime. LLM-generated Rust, if it passes the compiler, is at least guaranteed to be memory-safe.

The most accurate way to put it: **Rust won the war on its own. LLMs are providing the tools to clean up the battlefield.**

---

## Epilogue: The Man Who Didn't Want to Be a Hero Changed Everything

Graydon Hoare pops up on Reddit occasionally these days, writes the odd blog post. His GitHub bio reads "objecting to features" — a wry, helpless humor about watching his creation grow ever more complex.

In May 2025, Rust celebrated the tenth anniversary of its stable release. Hoare wrote a retrospective that opened with: "Rust has undergone growth and change I can barely comprehend the scale of. To say I'm surprised by its trajectory would be a vast understatement."

He reminded everyone that the bootstrap compiler he initially wrote was just a few tens of thousands of lines of code — the outer limit of what an unfunded solo hobby project can accomplish. It was Mozilla's investment, the community's participation, Big Tech's demands, and the contributions of countless engineers that transformed that side project into today's Rust.

The Rust story is not a story about genius. It's a story about a craftsman with impeccable taste who, at the right moment, assembled the right pieces, and then had the wisdom to hand them off to people better suited to carry the project forward.

Hoare isn't a genius. He's something rarer than genius — a creator who knew exactly where his limits were.

And the language he created is rewriting the foundations of our digital world, one line at a time.

Including, maybe, the software in your building's elevator.