#!/usr/bin/env bash
# Build and serve the site locally at http://localhost:4000
#
# Uses the Homebrew Ruby + Jekyll 4 (the repo's Gemfile pins the github-pages
# gem, which needs an older Ruby, so we bypass bundler for local previews).
set -euo pipefail
cd "$(dirname "$0")/.."

export PATH="/opt/homebrew/lib/ruby/gems/4.0.0/bin:/opt/homebrew/opt/ruby/bin:$PATH"
export JEKYLL_NO_BUNDLER_REQUIRE=true

command -v jekyll >/dev/null 2>&1 || {
  echo "jekyll not found. Install with:" >&2
  echo "  brew install ruby && gem install jekyll jekyll-feed jekyll-sitemap jekyll-paginate jekyll-gist jekyll-redirect-from" >&2
  exit 1
}

# _config.dev.yml points url at localhost so assets resolve locally
exec jekyll serve --config _config.yml,_config.dev.yml --host 127.0.0.1 --port 4000 "$@"
