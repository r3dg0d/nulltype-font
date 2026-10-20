# Run inside `nix develop` (flake) or `nix-shell`.
PY ?= python3
FONTBAKERY ?= fontbakery

.PHONY: all sources fonts test qa fontbakery site clean
all: fonts test qa site

sources:
	$(PY) tools/build.py --sources-only

fonts:
	$(PY) tools/build.py

test:
	$(PY) -m pytest -q tests

qa:
	$(PY) tools/qa.py all

fontbakery:
	FONTBAKERY=$(FONTBAKERY) tools/fontbakery.sh

site:
	$(PY) site/build.py

clean:
	rm -rf fonts build site/dist
