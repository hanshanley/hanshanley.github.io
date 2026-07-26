#!/usr/bin/env bash
# Compile the LaTeX CV / résumé to PDF and publish into files/.
#
#   scripts/build-cv.sh            # build the academic CV
#   scripts/build-cv.sh resume     # build the résumé
#   scripts/build-cv.sh all
#
# Uses Tectonic, which downloads whatever LaTeX packages it needs and keeps
# everything self-contained (brew install tectonic).
set -euo pipefail

cd "$(dirname "$0")/.."
ROOT="$PWD"
OUT="$ROOT/files"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

command -v tectonic >/dev/null 2>&1 || {
  echo "tectonic not found. Install it with:  brew install tectonic" >&2
  exit 1
}

build() {
  local src="$1" dest="$2" label="$3"
  echo "==> Building $label"
  if ! tectonic -X compile "$ROOT/cv/$src" --outdir "$TMP" >"$TMP/$src.log" 2>&1; then
    echo "FAILED — last 25 lines of the log:" >&2
    tail -25 "$TMP/$src.log" >&2
    return 1
  fi
  local pdf="$TMP/${src%.tex}.pdf"
  [ -s "$pdf" ] || { echo "no PDF produced for $src" >&2; return 1; }
  # keep the previously published copy alongside, just in case
  [ -f "$OUT/$dest" ] && cp "$OUT/$dest" "$OUT/${dest%.pdf}.previous.pdf"
  cp "$pdf" "$OUT/$dest"
  echo "    wrote $OUT/$dest ($(du -h "$OUT/$dest" | cut -f1))"
}

case "${1:-cv}" in
  cv)     build Hans_WA_Hanley_CV.tex     Hans_WA_Hanley_CV.pdf   "academic CV" ;;
  resume) build Hans_WA_Hanley_Resume.tex HansWAHanley_Resume.pdf "résumé" ;;
  all)
    build Hans_WA_Hanley_CV.tex     Hans_WA_Hanley_CV.pdf   "academic CV"
    build Hans_WA_Hanley_Resume.tex HansWAHanley_Resume.pdf "résumé" || {
      echo "note: the résumé needs the SourceSansPro OTF fonts on your font path." >&2
    }
    ;;
  *) echo "usage: $0 [cv|resume|all]" >&2; exit 2 ;;
esac

echo "Done."
