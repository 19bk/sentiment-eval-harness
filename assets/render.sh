#!/usr/bin/env bash
# Rasterize the diagram SVGs to high-res PNGs, programmatically.
# No extra installs: uses the Google Chrome already on the machine, headless,
# at 3x device scale so the text stays crisp after LinkedIn re-compresses it.
#
#   ./assets/render.sh          # render all three
#
# Edit a .svg, re-run this, commit the new .png. That's the whole loop.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
SCALE="${SCALE:-3}"

[ -x "$CHROME" ] || { echo "Chrome not found at: $CHROME (set \$CHROME)"; exit 1; }

render() {
  local name="$1" w="$2" h="$3"
  local svg="$DIR/$name.svg" out="$DIR/$name.png"
  local td; td="$(mktemp -d)"
  # Wrap the SVG in a zero-margin HTML page sized exactly to the artwork, so the
  # screenshot has no padding and no scrollbars.
  { printf '<!doctype html><meta charset="utf-8"><style>*{margin:0;padding:0;border:0}html,body{background:#fff}svg{display:block}</style>'
    cat "$svg"; } > "$td/page.html"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --no-sandbox \
    --force-device-scale-factor="$SCALE" --window-size="$w,$h" \
    --default-background-color=FFFFFFFF \
    --screenshot="$out" "file://$td/page.html" >/dev/null 2>&1
  rm -rf "$td"
  echo "rendered $out  (${w}x${h} @ ${SCALE}x)"
}

render results        760 372
render what-is-an-eval 760 290
render how-evals-work  800 290
