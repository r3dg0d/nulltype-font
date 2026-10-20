#!/usr/bin/env bash
# FontBakery (universal profile), one run per format so TTF and OTF copies of the
# same style are not mistaken for duplicate family members. Markdown reports go to docs/.
# On NixOS the pip wheel's bundled ots-sanitize must be replaced by nixpkgs'
# opentype-sanitizer and libstdc++ must be on LD_LIBRARY_PATH (see docs/QA.md).
set -euo pipefail
FB=${FONTBAKERY:-fontbakery}
mkdir -p docs
run() { $FB check-universal --loglevel WARN --ghmarkdown "docs/fontbakery-$1.md" "${@:2}" >/dev/null 2>&1 || true
        printf '%-10s ' "$1"; grep -A2 -m1 "ERROR | ☠" "docs/fontbakery-$1.md" | tail -n1; }
run ttf fonts/ttf/*.ttf
run otf fonts/otf/*.otf
run variable fonts/variable/*.ttf
