---
title:  "The Hero Can't Slay the Dragon: Why Open Source Creators Keep Losing"
date:   2026-02-13 10:00:00 +0800
tags: [Programming]
---


You know the story. A lone developer, fueled by passion and caffeine, builds something incredible in their spare time. It's free. It's open. The world adopts it. Then a trillion-dollar company swoops in, wraps it in a managed cloud service, and makes billions.

The creator? Still refreshing their GitHub Sponsors page, wondering if they can make rent.

This is not a hypothetical. This is the open source economy in 2025.

---

## The Deal That Was Never Fair

Open source was born from a beautiful idea: software should be free. Free to use, free to modify, free to share. Licenses like MIT, BSD, and Apache 2.0 made this possible, and for decades, it worked. The internet as we know it was built on open source.

But here's the thing nobody said out loud: "free to use" also means "free for a mega-corp to take your life's work, slap a price tag on it, and never give you a dime."

That's not a bug. That's literally what the license says.

## The Hall of Forgotten Heroes

Let me introduce you to some people you've never heard of, whose code you use every single day.

**Daniel Stenberg** maintained cURL — alone — for over 25 years. Every time your phone talks to a server, every API call, every IoT device pinging the cloud — cURL is probably in there somewhere. For most of that time, he did it as a side project. Billions of devices, zero billions of dollars.

**Werner Koch** built GnuPG, the encryption tool that secures email communications worldwide. In 2015, journalists discovered he was nearly broke. The mass of the internet's encrypted email infrastructure was resting on one guy who was about to run out of money.

The **core-js** maintainer Denis Pushkarev powers virtually every frontend application on the web. Billions of npm downloads. He publicly pleaded for financial help. The response? Mass of developers closed the tab and moved on.

And then there's **Log4j** — a Java logging library so fundamental that when the Log4Shell vulnerability dropped in 2021, half the internet panicked. The world suddenly realized this critical piece of infrastructure was being maintained by volunteers in their free time.

These aren't edge cases. This is the norm.

## Enter the Dragon

Now let's talk about who *is* making money.

When AWS launched ElastiCache (basically hosted Redis), they didn't need permission from Redis Labs. The license said anyone could use it however they wanted. So AWS did. They built a multi-billion-dollar service on top of someone else's open source project and kept every penny.

Same story with Elasticsearch. AWS took it, launched Amazon OpenSearch, and competed directly with the company that created Elasticsearch — using their own code.

MongoDB? Same thing. HashiCorp's Terraform? Same thing.

The pattern is always the same: a company builds something amazing and open sources it. A cloud giant takes it, packages it as a managed service with their existing infrastructure, customer base, and brand trust. The original creator can't compete. They never could. You can't out-distribute AWS.

## The Three Ways to Survive (None of Them Great)

Over the years, open source projects have found roughly three survival strategies. None of them are ideal.

**Strategy 1: Get adopted by a dragon.**

This is the "if you can't beat them, join them" path. Linux has hundreds of full-time corporate contributors because every major tech company runs on it. Kubernetes was born at Google and handed to the Cloud Native Computing Foundation, where every cloud vendor chips in because they all need it. Microsoft built VS Code and TypeScript. Meta built React and PyTorch. Google built Go, TensorFlow, and Angular.

These projects thrive — but only because they serve the strategic interests of big companies. Google didn't open source Kubernetes out of generosity. They did it to commoditize container orchestration and level the playing field against AWS's head start in cloud. Microsoft didn't make VS Code free because they love developers. They made it free to pull developers into the GitHub and Azure ecosystem.

When your project aligns with a giant's business strategy, you get funded. When it doesn't, you're on your own.

**Strategy 2: Change the license and fight back.**

Redis switched from BSD to a dual license (RSALv2 + SSPL). Elasticsearch moved to SSPL. MongoDB did the same. HashiCorp switched Terraform to BSL. Grafana went AGPLv3.

Every single time, the community screamed "betrayal." And every single time, the company said, "We were dying. What did you expect us to do?"

And every single time, someone forked it. Redis became Valkey. Elasticsearch became OpenSearch. Terraform became OpenTofu. The forks are backed by the same cloud giants who were profiting from the original projects. The irony is almost poetic.

**Strategy 3: Burn out quietly.**

This is the default. The maintainer keeps going until they can't. No dramatic license change. No corporate acquisition. Just a slow fade — unanswered issues, stale PRs, and eventually a GitHub repo that hasn't been updated in two years.

Bram Moolenaar maintained Vim for decades until he passed away in 2023. The OpenSSL team was chronically underfunded until Heartbleed made headlines. FFmpeg powers every video player and streaming service you've ever used, and its maintainers have been perpetually under-resourced.

## Why "Just Donate" Doesn't Work

Every time this topic comes up, someone says "developers should donate to the projects they use." It sounds reasonable. It doesn't work.

The math is simple: if a library has 10 million weekly downloads and 0.001% of users donate $5 a month, that's $500. That doesn't pay for a single developer in any major city on earth.

Companies are even worse. A Fortune 500 company will happily build their entire infrastructure on open source and allocate exactly $0 to supporting it. It's not malice — it's just not anyone's job to care. The engineering team uses what works. Finance doesn't have a line item for "paying for free software." And so the money never flows back.

## The Uncomfortable Truth

Here's what all of this comes down to: **the open source tools you use every day exist because of an economic arrangement that is fundamentally broken.**

The projects that survive are the ones that happen to be useful as strategic weapons for tech giants. Linux lives because every cloud company needs it. Kubernetes lives because Google needed to commoditize AWS's advantage. React lives because Meta built their entire frontend on it.

The rest? They survive on the goodwill and personal sacrifice of individuals who often get nothing in return.

We like to tell ourselves that open source is a community triumph — proof that collaboration beats corporations. And in some ways, it is. But it's also a system where the biggest beneficiaries contribute the least, and the people who create the most value capture almost none of it.

The hero keeps building. The dragon keeps eating. And the village cheers for the hero while paying the dragon.

---

*If you use open source software (you do), consider checking if the projects you depend on have a way to contribute financially. It won't fix the system, but it might keep one more hero in the fight a little longer.*