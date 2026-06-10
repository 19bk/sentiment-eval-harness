#!/usr/bin/env bash
# Rasterize each assets/img-*.svg to a high-res PNG, programmatically.
# No extra installs: uses the Google Chrome already on the machine, headless,
# at 3x device scale so the text stays crisp.
#
#   ./assets/render.sh
#
# Auto-discovers the SVGs and reads each one's width/height, so it renders
# whatever is present (a fresh clone of the repo has only img-result.svg).
# Edit an .svg, re-run this, commit the new .png. That's the whole loop.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
SCALE="${SCALE:-3}"

[ -x "$CHROME" ] || { echo "Chrome not found at: $CHROME (set \$CHROME)"; exit 1; }

render() {
  local svg="$1" out="${1%.svg}.png" w h td
  w="$(sed -n 's/.*<svg[^>]* width="\([0-9]*\)".*/\1/p' "$svg" | head -1)"
  h="$(sed -n 's/.*<svg[^>]* height="\([0-9]*\)".*/\1/p' "$svg" | head -1)"
  td="$(mktemp -d)"
  # Wrap the SVG in a zero-margin HTML page so the screenshot has no padding.
  { printf '<!doctype html><meta charset="utf-8"><style>*{margin:0;padding:0;border:0}svg{display:block}</style>'
    cat "$svg"; } > "$td/page.html"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --no-sandbox \
    --force-device-scale-factor="$SCALE" --window-size="$w,$h" \
    --default-background-color=FFFFFFFF \
    --screenshot="$out" "file://$td/page.html" >/dev/null 2>&1
  rm -rf "$td"
  echo "rendered $(basename "$out")  (${w}x${h} @ ${SCALE}x)"
}

for svg in "$DIR"/img-*.svg; do render "$svg"; done
