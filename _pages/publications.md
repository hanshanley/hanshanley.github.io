---
layout: default
title: "Publications"
permalink: /publications/
---
{% include base_path %}

<h2 class="section">Filter</h2>
<div class="filters" id="filters">
  <button type="button" data-topic="all" aria-pressed="true">All</button>
  <button type="button" data-topic="disinformation" aria-pressed="false">Disinformation</button>
  <button type="button" data-topic="nlp" aria-pressed="false">NLP</button>
  <button type="button" data-topic="networks" aria-pressed="false">Networks</button>
  <button type="button" data-topic="ai-safety" aria-pressed="false">AI safety</button>
  <button type="button" data-topic="privacy" aria-pressed="false">Privacy</button>
</div>

<div class="index" id="index">
  {% assign pubs = site.publications | sort: "date" | reverse %}
  {% for post in pubs %}
    {% include record-publication.html %}
  {% endfor %}
</div>

<script>
  (function () {
    var filters = document.getElementById('filters');
    if (!filters) return;
    var records = document.querySelectorAll('#index .record');
    filters.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-topic]');
      if (!b) return;
      Array.prototype.forEach.call(filters.querySelectorAll('button'), function (x) {
        x.setAttribute('aria-pressed', String(x === b));
      });
      var t = b.dataset.topic;
      Array.prototype.forEach.call(records, function (r) {
        var topics = (r.getAttribute('data-topics') || '').split(/\s+/);
        r.hidden = !(t === 'all' || topics.indexOf(t) !== -1);
      });
    });
  })();
</script>
