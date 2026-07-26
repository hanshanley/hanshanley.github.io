---
layout: default
permalink: /
title: "Hans W. A. Hanley"
excerpt: "Member of Technical Staff at Microsoft AI. AI safety and truthfulness, disinformation, networks, and natural language processing."
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

<div class="lede">
    <p>I am Hans Hanley (<span lang="zh-Hans">汉斯·汉隶</span>), a Member of Technical Staff at Microsoft AI. I am broadly interested in AI safety and truthfulness, disinformation, networks, and natural language processing.</p>

    <p>I was formerly a Computer Science Ph.D. candidate at Stanford University researching in the <a href="https://esrg.stanford.edu/">Empirical Security Research Group</a> and supported by the <a href="https://research.facebook.com/blog/2023/4/announcing-the-2023-meta-research-phd-fellowship-award-winners/">Meta PhD Research Fellowship</a>, the <a href="https://www.nsfgrfp.org/">National Science Foundation Graduate Research Fellowship</a> and the <a href="https://vpge.stanford.edu/fellowships-funding/current-vpge-fellows/all-2020">Stanford University EDGE Fellowship</a>. I completed two Masters' degrees in Computer Science and in Statistics with the <a href="https://sachs.princeton.edu/">Daniel M. Sachs Scholarship</a> at the University of Oxford. I completed my undergraduate degree in Electrical Engineering at Princeton University.</p>

    <p>Outside of research, I did disinformation reporting with the <a href="https://www.atlanticcouncil.org/programs/digital-forensic-research-lab/">Atlantic Council's Digital Forensic Research Lab</a>.</p>

    <p>I have a blog, <a href="https://www.themarginoferror.com/">The Margin of Error</a>, where I talk about my research, computational looks at different economic and political issues, and a ton of other topics. <a href="https://themarginoferror.substack.com/">Subscribe on Substack</a>, or <a href="https://docs.google.com/forms/d/e/1FAIpQLSeHPhVHdJ0xdCYq3wDYjkOIxgVdErP4qszNOBQYrnyzTz3xyQ/viewform">via this form</a>.</p>
</div>

<div class="affordances" style="margin-top:1.6rem">
  <a class="is-primary" href="https://www.hanshanley.com/files/HansWAHanley_Resume.pdf">Résumé (PDF)</a>
  <a href="https://www.hanshanley.com/files/Hans_WA_Hanley_CV.pdf">Academic CV (PDF)</a>
  <a href="https://scholar.google.com/citations?user=ewdWfOoAAAAJ">Google Scholar</a>
</div>

<h2 class="section">Recently</h2>
<ul class="log">
  {% for u in site.data.updates %}
  <li>
    <time{% if u.datetime %} datetime="{{ u.datetime }}"{% endif %}>{{ u.date }}</time>
    <div>
      <p>{{ u.text }}</p>
      {% if u.kind %}<span class="kind">{{ u.kind }}</span>{% endif %}
    </div>
  </li>
  {% endfor %}
</ul>

<h2 class="section">Selected work <a href="{{ base_path }}/publications/">All publications →</a></h2>
<div class="index">
  {% assign featured = site.publications | where: "featured", true | sort: "date" | reverse %}
  {% for post in featured %}
    {% include record-publication.html %}
  {% endfor %}
</div>

<h2 class="section">Elsewhere</h2>
<ul class="profiles">
  {% for l in site.data.links.elsewhere %}
  <li><span class="label">{{ l.label }}</span><a href="{{ l.url }}">{{ l.title }}</a></li>
  {% endfor %}
</ul>

<div class="aside-note">
  For fun, I enjoy stand-up comedy, listening to UK rhythm and blues music, long-distance running,
  and learning Mandarin Chinese (HSK5).
</div>
