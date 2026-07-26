#!/usr/bin/env python3
"""
Rebuild the preview pages from style.css.

Injects the stylesheet inline (so it works over file:// with no external
requests), plus the sticky side dock, the theme toggle, and a clean footer.
Run from anywhere:  python3 scripts/build-preview.py
"""
import base64
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREVIEW = os.path.join(ROOT, "preview")

CSS = open(os.path.join(PREVIEW, "style.css"), encoding="utf-8").read()

# The portrait is embedded as a data URI. Some browsers refuse to load sibling
# files over file://, which leaves the page unstyled and image-less; inlining
# every subresource makes each page fully self-contained.
with open(os.path.join(PREVIEW, "portrait.jpg"), "rb") as fh:
    PORTRAIT_URI = "data:image/jpeg;base64," + base64.b64encode(fh.read()).decode("ascii")

THEME_INIT = """<script>
  (function () {
    try {
      var t = localStorage.getItem('theme');
      if (t === 'dark') document.documentElement.setAttribute('data-theme', 'dark');
    } catch (e) {}
  })();
</script>"""

HEAD_BLOCK = "<style>\n" + CSS + "\n</style>\n" + THEME_INIT

DOCK = """<aside class="dock" aria-label="Quick links">
  <span class="dock__head">Links</span>
  <ul>
    <li><a class="dock__cv" href="https://www.hanshanley.com/files/HansWAHanley_Resume.pdf"><span class="dock__ico" aria-hidden="true">📄</span>Résumé</a></li>
    <li><a class="dock__cv" href="https://www.hanshanley.com/files/Hans_WA_Hanley_CV.pdf"><span class="dock__ico" aria-hidden="true">📑</span>Academic CV</a></li>
    <li><a href="https://scholar.google.com/citations?user=ewdWfOoAAAAJ"><span class="dock__ico" aria-hidden="true">🎓</span>Scholar</a></li>
    <li><a href="https://orcid.org/0000-0002-4291-5896"><span class="dock__ico" aria-hidden="true">🆔</span>ORCID</a></li>
    <li><a href="https://github.com/hanshanley"><span class="dock__ico" aria-hidden="true">💻</span>GitHub</a></li>
    <li><a href="https://www.youtube.com/@hanshanley"><span class="dock__ico" aria-hidden="true">📺</span>YouTube</a></li>
    <li><a href="https://twitter.com/Hans_Hanley"><span class="dock__ico" aria-hidden="true">🐦</span>Twitter</a></li>
    <li><a href="https://www.linkedin.com/in/hans-hanley-0694a180"><span class="dock__ico" aria-hidden="true">💼</span>LinkedIn</a></li>
    <li><a href="https://www.themarginoferror.com/"><span class="dock__ico" aria-hidden="true">✍️</span>Blog</a></li>
    <li><a href="mailto:hhanley@cs.stanford.edu"><span class="dock__ico" aria-hidden="true">✉️</span>Email</a></li>
  </ul>
</aside>"""

FOOTER = """<footer class="site">
  <span>Hans W. A. Hanley</span>
  <span><a href="index.html">About</a> · <a href="publications.html">Publications</a> · <a href="are-you-an-ai.html">Are you an AI?</a></span>
</footer>"""

TOGGLE = ('<span class="spacer"></span>'
          '<button class="theme-toggle" id="theme-toggle" type="button" '
          'aria-label="Switch colour theme">Dark</button>')

TOGGLE_JS = """
  (function () {
    var btn = document.getElementById('theme-toggle');
    if (!btn) return;
    var root = document.documentElement;
    var sync = function () {
      btn.textContent = root.getAttribute('data-theme') === 'dark' ? 'Light' : 'Dark';
    };
    sync();
    btn.addEventListener('click', function () {
      var dark = root.getAttribute('data-theme') === 'dark';
      if (dark) { root.removeAttribute('data-theme'); }
      else { root.setAttribute('data-theme', 'dark'); }
      try { localStorage.setItem('theme', dark ? 'light' : 'dark'); } catch (e) {}
      sync();
    });
  })();"""


def build(path):
    s = open(path, encoding="utf-8").read()

    # 1. stylesheet -> inline (replace a <link> or a previously inlined <style>)
    if "<style>" in s:
        s = re.sub(r"<style>.*?</style>\s*(?:<script>\s*\(function \(\) \{\s*try \{.*?</script>)?",
                   lambda m: HEAD_BLOCK, s, count=1, flags=re.S)
    else:
        s = s.replace('<link rel="stylesheet" href="style.css">', HEAD_BLOCK, 1)

    # 2. theme toggle in the dateline (anchored on the dateline block itself)
    s = re.sub(r'(<div class="dateline">.*?)\s*(?:<span class="spacer">.*?</button>)?\s*(</div>)',
               lambda m: m.group(1) + "\n    " + TOGGLE + "\n  " + m.group(2),
               s, count=1, flags=re.S)

    # 3. footer -> clean version (no colophon, no source, no colophon strapline)
    s = re.sub(r"<footer class=\"site\">.*?</footer>", FOOTER, s, count=1, flags=re.S)

    # 4. sticky dock, once, just before the footer
    s = s.replace('<aside class="dock"', "<!--dock-->", 1)
    s = re.sub(r'<!--dock-->.*?</aside>', "", s, count=1, flags=re.S)
    s = s.replace(FOOTER, DOCK + "\n\n" + FOOTER, 1)

    # 5. theme-toggle JS: strip any previous copy, then append one before </body>
    s = re.sub(r'\s*<script>\s*\(function \(\) \{\s*var btn = document\.getElementById\(.theme-toggle.\).*?</script>',
               "", s, flags=re.S)
    s = re.sub(r"<script>\s*</script>", "", s)
    s = s.replace("</body>", "<script>" + TOGGLE_JS + "\n</script>\n</body>", 1)

    # 6. embed the portrait so no sibling file is ever requested
    s = re.sub(r'src="(?:portrait\.jpg|data:image/jpeg;base64,[^"]*)"',
               'src="' + PORTRAIT_URI + '"', s)

    open(path, "w", encoding="utf-8").write(s)
    return len(s)


def main():
    files = sorted(glob.glob(os.path.join(PREVIEW, "*.html")))
    if not files:
        sys.exit("no preview pages found")
    for f in files:
        size = build(f)
        print(f"built {os.path.basename(f):<22} {size/1024:6.1f} KB")
    print(f"\n{len(files)} pages rebuilt from style.css")


if __name__ == "__main__":
    main()
