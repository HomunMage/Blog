---
title:  "AI workflow"
date:   2024-04-30 10:00:00 +0800
tags: [Fairy]
---

# AI workflow on local PC 

When we want to run local LLM workflow.

we need:

* domain knowledge to spilt workflow into nodes
* LLM agent
* task management


## domain knowledge

take SEO as example, there are stages such as prepare data, TA setting, keyword setting, article SEO-lize, community ver.


## LLM agent

agent frameworke such crewAI maybe good option because it use langchain and ollama.

and if we want to run crewAI with llama3, seems need run dolphin-llama3

(current, it is broken, cannot work well)

in other way, if use gemma, it can write right article but cannot use crewAI.tool.


## Task management

we need cli ver to do task management.

Maybe Joplin be the better choise. ( Taskwarrior and Taiga might be substutude solution)
