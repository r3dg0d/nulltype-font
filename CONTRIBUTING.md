# Contributing to NullType

Thanks for helping! NullType is generated **procedurally**. Never edit the UFOs or binaries by hand. Edit the source of truth and rebuild:

* Glyph designs: `sources/skeletons.txt` (polyline skeleton on an 8×14 grid → upright rectangular pen (Minkowski hexagons) → pathops union).
* Construction rules, weights, metrics: `tools/engine.py`.
* Features: `features()` in `tools/engine.py`.

## Workflow
```sh
nix develop            # or: nix-shell
make fonts             # sources/ufo + fonts/{ttf,otf,woff2,variable}
make test              # pytest: metadata, rasterisation, shaping, VF, family rules
python3 tools/qa.py regress   # visual regression vs tests/reference
make fontbakery        # FontBakery universal profile → docs/fontbakery-*.md
make site              # site/dist
```
If a glyph change is intentional, refresh the references with `python3 tools/qa.py regress --update` and say so in the PR.

## Rules
* Original work only. Don't trace or copy outlines, bitmaps or matrices from any other font.
* By contributing you agree your font contributions are licensed under OFL-1.1 and your tooling contributions under MIT.
* Keep the build deterministic (`SOURCE_DATE_EPOCH` is honoured). Rebuilding unchanged sources must give identical checksums.
