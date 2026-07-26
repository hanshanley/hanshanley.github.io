#!/usr/bin/env bash
# Anti-"AI slop" gate. Fails if the built output drifts back toward generic template design.
# Usage: scripts/lint-style.sh [dir]   (default: preview)
set -uo pipefail

DIR="${1:-preview}"
fail=0

check() {
  local label="$1" pattern="$2" glob="$3"
  local hits
  hits=$(grep -rniE "$pattern" "$DIR" --include="$glob" 2>/dev/null || true)
  if [ -n "$hits" ]; then
    printf '\033[31mFAIL\033[0m  %s\n%s\n\n' "$label" "$hits"
    fail=1
  else
    printf '\033[32m ok \033[0m  %s\n' "$label"
  fi
}

echo "Linting $DIR for AI-template tells…"
echo

check "no CSS gradients"            'linear-gradient|radial-gradient|conic-gradient'   '*.css'
check "no glassmorphism"            'backdrop-filter'                                  '*.css'
check "no card drop-shadows"        'box-shadow'                                       '*.css'
check "no banned display fonts"     'font-family:[^;]*(Inter|Poppins|Montserrat|Nunito)' '*.css'
check "no font CDN calls"           'fonts\.googleapis|fonts\.gstatic|cdnjs|unpkg|jsdelivr' '*.html'
check "no emoji section headers"    '<h[1-6][^>]*>[^<]*[🚀✨🎯💡🔥🌟⚡🎉]'              '*.html'
check "no LLM stock phrasing"       "let'?s build something amazing|digital garden|passionate about|fast-paced world|elevate your|seamlessly|unlock the|dive into|game-?changer|cutting-edge|revolutioniz|ever-evolving" '*.html'
check "no fake metric counters"     '[0-9]+\+ *(papers|projects|years|citations|publications)' '*.html'
check "no typewriter/autotype JS"   'typewriter|typeIt|typed\.js'                      '*.html'

echo
if [ "$fail" -eq 0 ]; then
  printf '\033[32mPASS\033[0m — no AI-template tells found.\n'
else
  printf '\033[31mFAILED\033[0m — see above.\n'
fi
exit "$fail"
