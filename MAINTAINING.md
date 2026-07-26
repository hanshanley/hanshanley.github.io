# Maintaining this site

Everything that changes often lives in a data file or a single markdown file.
You should not need to touch HTML or CSS for routine updates.

## Preview it locally

```bash
scripts/serve.sh          # http://localhost:4000
```

First time only:

```bash
brew install ruby
gem install jekyll jekyll-feed jekyll-sitemap jekyll-paginate jekyll-gist jekyll-redirect-from
```

(The repo's `Gemfile` pins the `github-pages` gem, which needs an old Ruby.
`scripts/serve.sh` bypasses bundler and uses Jekyll 4 directly. GitHub Pages
still builds the published site from the `Gemfile`.)

## Add a new paper

1. Drop a file in `_publications/`, e.g. `_publications/my-paper.md`:

```yaml
---
title: "Paper Title"
permalink: /publication/my-paper
date: 2026-06-01
collection: publications
venue: The Full Conference Name (ACME 2026)
venue_short: ACME              # shown in the left rail
authors: <b>Hans W. A. Hanley</b> and Co Author
paperurl: 'https://...'
code: 'https://github.com/...' # optional
recording: 'https://...'       # optional
topics: nlp networks           # any of: disinformation nlp networks ai-safety privacy
featured: true                 # optional — shows on the front page
flag: Best Paper               # optional — small red badge
excerpt: 'One or two sentences.'
---
```

2. Put the PDF in `files/`.
3. Add a line to `_data/updates.yml`.

The publications page, front page, `/llms.txt`, `/are-you-an-ai/` and the
JSON-LD all update themselves.

## Add a talk

One file in `_talks/`. Links in the body (slides, recording, paper) are rendered
automatically.

```yaml
---
title: "Talk Title"
collection: talks
permalink: /talks/short-name
venue: "Where it happened"
date: 2026-05-01
type: "Talk"
location: "City, Country"
---
Short description.

[Slides](https://...)
```

## Add an update

One entry at the top of `_data/updates.yml`.

## Change a profile link

`_data/links.yml` — single source of truth for the side dock, the "Elsewhere"
list and the `/are-you-an-ai/` page.

## Change the nav

`_data/navigation.yml`.

## Rebuild the CV / résumé PDF

```bash
brew install tectonic
scripts/build-cv.sh cv        # -> files/Hans_WA_Hanley_CV.pdf
scripts/build-cv.sh resume    # needs the SourceSansPro OTF fonts installed
```

Sources are in `cv/`.

## Check the design hasn't drifted

```bash
scripts/lint-style.sh /path/to/_site
```

Fails on gradients, glassmorphism, card shadows, Inter/Poppins, font CDNs,
emoji headers, marketing filler and fake metric counters.
