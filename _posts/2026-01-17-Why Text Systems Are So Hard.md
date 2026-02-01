---
title: "Why Text Systems Are So Hard: My Ten-Year Journey to Understanding the Essence of Text and Code"
date:  2026-01-17 10:00:00 +0800
tags: [Programming]
---

## I. The Beginning: Just Wanting the Worst Website

About ten years ago, my requirements were almost naively simple: I just needed a place to keep my notes.

Initially, I tried all the major blogging platforms. I used Google Blogger and wrote on Medium for a while. They were convenient—publish with one click—but problems quickly surfaced: I was hijacked by the platform.

When I wanted to move, I found the content was hard to migrate, the formatting was a mess, and SEO had to start from scratch. I was tired of this "renting a house" feeling; I wanted my own land, my own home. So, I decided to do everything myself.

Back then, I thought databases were unnecessary. I created a GitHub repo and mapped routing logic directly to the file system structure.
`home/README.md` was the homepage, `about/README.md` was the "About Me," and `tech/linux/README.md` was a technical article.

One file per directory—that was my website. Pure, direct, ugly, but functional. I thought I was clever: no backend, no render loop, just raw HTTP file transfer.

But soon, this "rawness" became torture. There was no shared navigation bar; every time I wrote a new article, I had to manually copy and paste the HTML header. Without style management, the whole site looked like a 1990s bulletin board.

So, I stepped into the world of Jekyll.

Jekyll gave me my first taste of the power of "templating." With a theme applied, the site instantly looked decent. But as my demands for content grew, so did the pain.

I wanted to embed interactive charts or a dynamic code demonstration area in my articles. In Jekyll's logic, this was a disaster.

I had to create `chart.html` in the `_includes/` folder, filling it with `<script>` tags and Liquid logic. Then, in my Markdown, I had to call it using some strange syntax.

My project structure became spaghetti:
*   Markdown handled content, but was littered with Liquid tags.
*   HTML handled structure, but was mixed with JavaScript logic.
*   JS handled interactivity, but depended on Liquid to inject variables.

Every time I wanted to change the color of a chart, I had to open the Markdown file, the HTML layout file, and the CSS file, toggling between three windows, my mental stack constantly overflowing.

I started to run away. I tried Hugo (too fast but harder to customize), I tried Gatsby (the React ecosystem was too heavy; just setting up Webpack and GraphQL took more effort than writing the actual content).

**Until I discovered Web Components and Svelte.**

This was the first time I truly felt the power of "separation of concerns." I no longer needed Jekyll to handle complex logic.

After trying Lit to write Web Components and finding it an extremely non-intuitive way to write, I almost gave up until I stumbled upon the fact that Svelte could also compile as a Web Component.

I wrote a clean `<my-chart>` component in Svelte and compiled it into a standard Web Component.
In Markdown, I only needed to write:
`<my-chart data="[1,2,3]"></my-chart>`

Jekyll instantly degraded into an empty shell for routing that only handled `content`, while Svelte took over all interactivity. In that moment, the world became quiet. **Markdown told the story; Components performed the magic. Neither interfered with the other.**

Chatting with AI, I realized this is the modern concept of Islands Architecture, and Astro is the ultimate realization of this idea.

---

## II. Writing Books: The Typesetting Abyss

While wrestling with my blog, I also tried to write books.

During graduate school, I was forced to use LaTeX for my thesis. It was powerful but extremely painful. Our lab had a Git repository passed down through generations containing the `thesis.tex` file from seniors, filled with mysterious macros no one dared to touch. This template itself was a towering tree, forked and improved over time between various universities.

What was more painful was that LaTeX error messages were like an alien language.
A misplaced `\noalign` or a missing `}` could cost me two hours of debugging. The compiler log had only a few useful lines, the rest was just noise.

I often stared at the screen in a daze: **Was I really writing a book? Or was I learning this damn typesetting system?**

Later, I thought, since Markdown is so good, could I write a book directly in Markdown?

I tried converting to PDF directly with Pandoc. The results were disastrous—pages broke in the wrong places, images shifted position, fonts were inconsistent, and even basic paragraph spacing was unsatisfactory.

"What about writing HTML directly?" I thought. HTML offered the most control. As long as a browser could display it, I could output it.

So, I started hand-writing my book in HTML. After a few pages, I realized I was trapped in a different kind of hell: I was constantly adjusting the `margin` and `padding` of `<div>`s, writing mountains of CSS classes just to make a heading look decent.

I was back in typesetting hell, just swapping LaTeX for CSS.

After countless failures, I finally found a shortcut that no one told me about: **HTML is the ultimate intermediate layer.**

I shouldn't be hand-writing HTML, nor should I be learning LaTeX.
The correct pipeline is:
1.  **Focus on writing Markdown** (pure data).
2.  **Render Markdown to HTML using Svelte/Templates** (automated styling).
3.  **Output PDF using the browser (Chromium)'s Print function** (the most powerful rendering engine).

This pipeline became my golden standard. I stopped fighting typesetting; I delegated styling to CSS, rendering to the browser, and I only focused on writing the text.

---

## III. The Trial of Visual Editors (LangGraph GUI)

Having solved static content, I gave myself another challenge: I wanted to create a visual editor for AI workflows (similar to ComfyUI or n8n).

This was a highly complex GUI system. Users needed to drag and drop nodes, connect lines (edges), to build logic.

This experience was a bloodbath of "technology selection":

**1. The PyQt Swamp**
Initially, I thought this was a Desktop App, so of course, I used Python + PyQt.
But I quickly realized state management was a nightmare. When I dragged a node, I had to manually calculate coordinates, manually redraw lines, and manage the Undo/Redo stack. The UI code was tightly coupled with the business logic in memory; changing one feature slightly could crash the entire App.

**2. ReactFlow's Re-rendering Hell**
Switching to the Web, I used React. React is powerful, but the Hook mechanism gave me a hard time when dealing with such high-frequency interactive graphics.
To synchronize the state of node dragging, I had to carefully manage dependency arrays in `useEffect`.
`SetState` -> `Re-render` -> `Diff` -> `Patch DOM`.
This path was too long. When the graph had 100 nodes, React's performance started to lag. I wrote tons of `useMemo` and `useCallback` just to make it run smoothly.

**3. SvelteFlow's Salvation**
Finally, I migrated to Svelte 5.
In Svelte 5, state management became incredibly simple. `$state` is just a variable; change it, and the interface updates automatically. Without the overhead of Virtual DOM diffing, dragging became silk-smooth.

During this process, I realized a truth: **A complex GUI system is essentially an "execution engine" for a JSON data structure.**

Those fancy connections the user sees on the front end are, at the bottom layer, just a DAG (Directed Acyclic Graph). My job wasn't to "draw pictures," but to "manage data flow."
When I clearly define the data structure (Schema)—for example, using JSON to describe node relationships—the interface is just a resulting side effect.

---

## V. App Development: The Platform Myth

To run my software everywhere, I also tried developing Mobile Apps.

From native Kotlin (Android) to cross-platform Dart (Flutter), I tried them all.
When writing Kotlin, I was bewildered by the lifecycle of Fragments.
When writing Flutter, although I enjoyed hot reload, a voice in my head kept asking, "Why do I have to learn a whole new Widget language just for a simple List View?"

This made me anxious: Do I have to write one set of code for the Web in Svelte, another for mobile in Flutter, and another for desktop in Qt?

Until I looked back at my Web projects. Web technology has advanced to an almost unbelievable degree now.
With tools like Capacitor, I can use the same Svelte codebase to package iOS, Android, and Desktop Apps.

I don't need to learn three languages. **The Web is the ultimate container.** Instead of wandering between different platforms, I should perfect my Web skills.

---

## VI. Convergence: All Paths Lead to One

After ten years of struggle—from the worst README.md website, to LaTeX torture, to structured YAML scripts, to complex GUIs, to cross-platform apps—

I once thought I was doing completely different things, learning completely different technologies. “Am I learning too many random things?” I often asked myself.

But when I finally looked back calmly, I was surprised to find that all these experiences converged into the same shape.

Whether blogging, writing books, designing scripts, or building complex software systems, I was always solving the same problem:

**How to make structured information flow efficiently and be presented to humans.**

Look how similar these patterns are:

* **Blog**: Markdown (data) → Svelte/WC (logic) → HTML (presentation)
* **Book**: Markdown (data) → CSS (logic) → PDF (presentation)
* **Script / Worldbuilding**: YAML (data) → Liquid Template (logic) → HTML (presentation)
* **GUI Systems**: JSON (data) → SvelteFlow (presentation) → Python (execution logic)
* **Cross-platform Apps**: Web bundle (data & logic) → Capacitor (container) → Native app (presentation)

I took a long detour, and finally threw away all the junk in my toolbox.

I no longer obsess over which framework to use, because I know **separation** is the key. Data belongs to data (Markdown/JSON/YAML), logic belongs to logic (Svelte/Python), and presentation belongs to presentation (HTML/CSS).

Why are text systems so difficult? Because we always try to solve content, logic, and style all at once.

LaTeX fails by mixing layout logic into content. Jekyll fails by mixing JavaScript logic into HTML. React fails by mixing state logic into UI rendering.

Once you cleanly separate these three, you’ll find that writing an article and building an enterprise system are fundamentally the same thing.

What I once thought were detours—years of shoveling dirt—ultimately revealed the essence of the relationship between code and text. This Swiss Army knife, sharpened over ten years, is finally sharp.
