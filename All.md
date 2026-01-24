---
layout: base
title: All Articles
---

<main class="post-content">
  <h2>All Articles:</h2>
  <ul>
  {% assign sorted_posts = site.posts | sort: 'date' | reverse %}
  {% for post in sorted_posts %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <span style="color: #888;">{{ post.date | date: "%Y-%m-%d" }}</span>
        {% for tag in post.tags %}
          <span style="background: #333; padding: 2px 6px; border-radius: 3px; font-size: 0.8em;">{{ tag }}</span>
        {% endfor %}
      </li>
  {% endfor %}
  </ul>
</main>
