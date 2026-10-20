#!/usr/bin/env python3
"""Dependency-free static site generator for the showcase site.

Why not Astro: the site is one page plus a playground; a Python generator runs
inside the same Nix shell as the font build, needs no npm dependency tree or
native esbuild/rollup binaries (which need nix-ld on NixOS), and is fully
reproducible in CI. Output: site/dist/ (deployable to GitHub Pages as-is).
MIT licensed."""
import html
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import engine  # noqa: E402
from ttcore import WEIGHTS, ps_style  # noqa: E402

FAM = engine.FAMILY
C = json.load(open(os.path.join(HERE, "site.json")))
DIST = os.path.join(HERE, "dist")


def main():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(os.path.join(DIST, "fonts"))
    for sub in ("variable", "woff2"):
        for fn in os.listdir(os.path.join(ROOT, "fonts", sub)):
            if fn.endswith(".woff2"):
                shutil.copy(os.path.join(ROOT, "fonts", sub, fn), os.path.join(DIST, "fonts", fn))
    cov = json.load(open(os.path.join(ROOT, "docs", "coverage.json")))
    shutil.copy(os.path.join(HERE, "theme.css"), os.path.join(DIST, "theme.css"))
    shutil.copy(os.path.join(HERE, "playground.js"), os.path.join(DIST, "playground.js"))
    for img in ("styles.png", "confusables.png", "terminal.png"):
        p = os.path.join(ROOT, "docs", "specimens", img)
        if os.path.exists(p):
            shutil.copy(p, os.path.join(DIST, img))
    name = FAM["name"]
    faces = []
    for w, n in WEIGHTS:
        for it in (False, True):
            faces.append(f"@font-face{{font-family:'{name} Static';font-weight:{w};font-style:{'italic' if it else 'normal'};"
                         f"src:url('fonts/{FAM['ps']}-{ps_style(w, it)}.woff2') format('woff2');font-display:swap}}")
    faces.append(f"@font-face{{font-family:'{name} VF';font-weight:100 900;font-style:normal;src:url('fonts/{FAM['ps']}[wght].woff2') format('woff2');font-display:swap}}")
    faces.append(f"@font-face{{font-family:'{name} VF';font-weight:100 900;font-style:italic;src:url('fonts/{FAM['ps']}-Italic[wght].woff2') format('woff2');font-display:swap}}")
    chars = []
    for blk in cov["blocks"].values():
        for cp in blk["codepoints"]:
            c = int(cp[2:], 16)
            if c > 0x20 and c != 0xA0 and c != 0xAD:
                chars.append(f'<button class="g" title="{cp}" data-cp="{cp}">{html.escape(chr(c))}</button>')
    weights_html = "".join(
        f'<div class="wrow"><span class="wl">{w} {n}</span><span style="font-weight:{w}">{html.escape(C["weight_sample"])}</span>'
        f'<span style="font-weight:{w};font-style:italic">{html.escape(C["weight_sample"])}</span></div>' for w, n in WEIGHTS)
    feats = "".join(f'<label><input type="checkbox" data-feat="{k}" {"checked" if on else ""}> <code>{k}</code> {html.escape(d)}</label>'
                    for k, d, on in C["features"])
    presets = "".join(f'<option>{html.escape(p)}</option>' for p in C["presets"])
    sections = "".join(f'<section class="panel"><h2>{html.escape(t)}</h2>{b}</section>' for t, b in C["sections"])
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(C['title'])}</title><meta name="description" content="{html.escape(FAM['description'])}">
<style>{''.join(faces)}</style><link rel="stylesheet" href="theme.css"></head>
<body class="{C['body_class']}">
<header class="hero"><div class="brand">{html.escape(C['brand'])}</div>
<h1>{html.escape(C['headline'])}</h1><p class="lede">{html.escape(C['lede'])}</p>
<nav><a href="#playground">Playground</a><a href="#glyphs">Glyphs</a><a href="#weights">Weights</a><a href="#install">Install</a>
<a href="{FAM['url']}/releases">Download</a><a href="{FAM['url']}">Source</a></nav></header>
<main>
<section id="playground" class="panel"><h2>Playground</h2>
<div class="controls">
<label>Preset <select id="preset">{presets}</select></label>
<label>Size <input id="size" type="range" min="8" max="200" value="64"><output id="sizeo">64px</output></label>
<label>Weight <input id="weight" type="range" min="100" max="900" step="1" value="400"><output id="weighto">400</output></label>
<label>Engine <select id="engine"><option value="VF">Variable font</option><option value="Static">Static instances</option></select></label>
<label><input id="italic" type="checkbox"> Italic</label>
<label>Tracking <input id="track" type="range" min="-0.1" max="0.5" step="0.01" value="0"><output id="tracko">0em</output></label>
<label>Line height <input id="lh" type="range" min="0.8" max="2.5" step="0.05" value="1.3"><output id="lho">1.3</output></label>
<label>Align <select id="align"><option>left</option><option>center</option><option>right</option></select></label>
<label>Text <input id="fg" type="color" value="{C['fg']}"></label><label>Paper <input id="bg" type="color" value="{C['bg']}"></label>
<label><input id="waterfall" type="checkbox"> Waterfall</label><label><input id="compare" type="checkbox"> Compare all weights</label>
<button id="reset" type="button">Reset</button>
</div>
<fieldset class="features"><legend>OpenType features</legend>{feats}</fieldset>
<div id="stage" contenteditable="true" spellcheck="false">{html.escape(C['presets'][0])}</div>
<p class="css-out">CSS: <code id="cssout"></code></p>
</section>
<section id="glyphs" class="panel"><h2>Glyphs <small>{cov['glyphs']} glyphs · {cov['codepoints']} code points</small></h2>
<div class="inspect"><div id="big">A</div><div id="meta">Click a glyph</div></div><div class="grid">{''.join(chars)}</div></section>
<section id="weights" class="panel"><h2>Nine weights, nine italics</h2>{weights_html}</section>
{sections}
<section id="install" class="panel"><h2>Install</h2>{C['install_html']}</section>
<section class="panel"><h2>License</h2><p>Fonts: SIL Open Font License 1.1, Reserved Font Name “{name}”. Build tooling: MIT.
{html.escape(FAM['copyright'])}</p></section>
</main><footer>{html.escape(C['footer'])}</footer>
<script>window.FAMILY={json.dumps(name)};</script><script src="playground.js"></script></body></html>"""
    open(os.path.join(DIST, "index.html"), "w").write(page)
    open(os.path.join(DIST, ".nojekyll"), "w").close()
    print("site ->", DIST)


if __name__ == "__main__":
    main()
