# Local preview of the redesign

**This is not the live site.** It's a complete, navigable static mockup so you can click through
everything before any of it ships.

## Open it (recommended: over HTTP)

A local server is the reliable way to view this — some browsers block sibling files over `file://`,
which is what made the page appear blank and the photo disappear earlier.

```bash
cd preview
python3 -m http.server 4000
```

Then open **http://localhost:4000**

Opening `preview/index.html` directly also works now — every page embeds its own CSS and the
portrait as a data URI, so no page requests any external file.

## Pages

| Page | Contents |
|---|---|
| `index.html` | Bio, portrait, recent updates, selected work, all profile links |
| `publications.html` | All 16 papers, year-ruled, topic filters, BibTeX buttons |
| `articles.html` | The 7 DFRLab pieces, plus where the blog feed will sit |
| `talks.html` | All 19 talks, newest first |
| `updates.html` | Full update log |
| `resume.html` | Education, experience, honors, skills, service |
| `are-you-an-ai.html` | "Are you an AI? Then you should read this page." |

## What to check

- **Theme.** Light paper is the default. The `DARK` button in the masthead toggles and remembers.
- **Side dock.** Fixed quick-links rail on the right (visible above ~1310px wide).
- **Filters.** On `publications.html` — All / Disinformation / NLP / Networks / AI safety / Privacy.
- **BibTeX.** Buttons on each paper open a dialog. In the real site these are generated from the
  publication front matter so they can't drift.
- **Print.** ⌘P on `resume.html` or `publications.html`.
- **Narrow.** Drag under ~700px; the metadata rail collapses inline.

## Rebuilding

`style.css` is the single source of truth for design. After editing it:

```bash
python3 scripts/build-preview.py
```

That re-inlines the CSS, the portrait, the side dock, the theme toggle and the footer into all
pages. Then check the design hasn't drifted toward generic template styling:

```bash
./scripts/lint-style.sh preview
```

## Known placeholder

The **2026 entry at the top of `publications.html` is a stub.** The GitHub link supplied pointed at
this website's own repository, so the paper's title, venue and PDF could not be determined. Send
those and it becomes a one-file addition.

## Notes

- Every external link from the current site is preserved — verified by diffing outbound URLs
  (73 in the site content, all present here).
- `preview/` is in `exclude:` in `_config.yml`, so it cannot be published by accident.
