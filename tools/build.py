#!/usr/bin/env python3
"""Deterministic build: engine -> UFO/designspace sources -> TTF, CFF OTF, WOFF2, variable TTF.

Usage: python3 tools/build.py [--sources-only] [--no-vf] [--weights 400,700]"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import engine  # noqa: E402
from ttcore import WEIGHTS, ps_style, style_name, write_ufo  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FAM = engine.FAMILY


def ufo_path(w, it):
    return os.path.join(ROOT, "sources", "ufo", f"{FAM['ps']}-{ps_style(w, it)}.ufo")


def make_sources(weights):
    os.makedirs(os.path.join(ROOT, "sources", "ufo"), exist_ok=True)
    kern = engine.kerning() if hasattr(engine, "kerning") else None
    fea = engine.features()
    for w in weights:
        for it in (False, True):
            glyphs = engine.build(w, it)
            write_ufo(ufo_path(w, it), FAM, glyphs, w, it, fea, kern)
    write_designspaces(weights)


def write_designspaces(weights):
    from fontTools.designspaceLib import (AxisDescriptor, DesignSpaceDocument,
                                          InstanceDescriptor, SourceDescriptor)
    for it in (False, True):
        doc = DesignSpaceDocument()
        ax = AxisDescriptor()
        ax.tag, ax.name, ax.minimum, ax.default, ax.maximum = "wght", "Weight", min(weights), 400 if 400 in weights else weights[0], max(weights)
        doc.addAxis(ax)
        for w in weights:
            s = SourceDescriptor()
            s.path = ufo_path(w, it)
            s.filename = os.path.relpath(s.path, os.path.join(ROOT, "sources"))
            s.location = {"Weight": w}
            s.familyName, s.styleName = FAM["name"], style_name(w, it)
            doc.addSource(s)
            ins = InstanceDescriptor()
            ins.familyName, ins.styleName = FAM["name"], style_name(w, it)
            ins.postScriptFontName = f"{FAM['ps']}-{ps_style(w, it)}"
            ins.location = {"Weight": w}
            doc.addInstance(ins)
        doc.write(os.path.join(ROOT, "sources", f"{FAM['ps']}{'-Italic' if it else ''}.designspace"))


def stat_axes(weights, italic):
    return [
        {"tag": "wght", "name": "Weight", "values": [
            {"value": w, "name": n, **({"flags": 2, "linkedValue": 700} if w == 400 else {})}
            for w, n in WEIGHTS if w in weights]},
        {"tag": "ital", "name": "Italic", "values": [
            {"value": 1 if italic else 0, "name": "Italic" if italic else "Roman",
             **({} if italic else {"flags": 2, "linkedValue": 1})}]},
    ]


def drop_zero_length_segments(tt):
    """Remove consecutive duplicate on-curve points left by overlap removal."""
    glyf = tt["glyf"]
    for name in tt.getGlyphOrder():
        g = glyf[name]
        if g.numberOfContours <= 0:
            continue
        coords, ends, flags = g.coordinates, g.endPtsOfContours, g.flags
        keep, start = [], 0
        for end in ends:
            idx = list(range(start, end + 1))
            kept = []
            for k, i in enumerate(idx):
                j = idx[k - 1]  # cyclic predecessor
                if len(idx) > 3 and coords[i] == coords[j] and flags[i] & 1 and flags[j] & 1:
                    continue
                kept.append(i)
            keep.append(kept)
            start = end + 1
        if sum(len(k) for k in keep) == len(coords):
            continue
        from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates
        new_c, new_f, new_e = [], [], []
        for kept in keep:
            for i in kept:
                new_c.append(coords[i])
                new_f.append(flags[i])
            new_e.append(len(new_c) - 1)
        g.coordinates = GlyphCoordinates(new_c)
        g.flags = __import__("array").array("B", new_f)
        g.endPtsOfContours = new_e
        g.recalcBounds(glyf)


def postprocess(tt, monospace=False, stat=None):
    from fontTools.ttLib import newTable
    from fontTools.ttLib.tables import ttProgram
    if stat is not None and "STAT" not in tt:
        from fontTools.otlLib.builder import buildStatTable
        buildStatTable(tt, stat, elidedFallbackName="Regular")
    if "glyf" in tt:
        # unhinted outlines: enable smart dropout control so thin pixel/dot
        # features never vanish at small sizes
        prep = newTable("prep")
        prep.program = ttProgram.Program()
        prep.program.fromAssembly(["PUSHW[ ]", "511", "SCANCTRL[ ]", "PUSHB[ ]", "4", "SCANTYPE[ ]"])
        tt["prep"] = prep
    tt["name"].removeNames(platformID=1)  # Windows/Unicode names only
    if "glyf" in tt and "gvar" not in tt:  # never alter point counts under gvar
        drop_zero_length_segments(tt)
    # Windows clips outside usWin*: cover the real bounding box (USE_TYPO_METRICS keeps line spacing)
    head, os2 = tt["head"], tt["OS/2"]
    if "glyf" in tt:
        ys = [(g.yMin, g.yMax) for g in (tt["glyf"][n] for n in tt.getGlyphOrder()) if g.numberOfContours]
        ymin, ymax = min(y[0] for y in ys), max(y[1] for y in ys)
    else:
        bb = [tt["CFF "].cff[0].CharStrings[n].calcBounds(tt["CFF "].cff[0].CharStrings) for n in tt.getGlyphOrder()]
        bb = [b for b in bb if b]
        ymin, ymax = min(b[1] for b in bb), max(b[3] for b in bb)
    os2.usWinAscent = max(os2.usWinAscent, int(round(ymax)))
    os2.usWinDescent = max(os2.usWinDescent, int(round(-ymin)))
    tt["OS/2"].recalcUnicodeRanges(tt)
    tt["OS/2"].recalcCodePageRanges(tt) if hasattr(tt["OS/2"], "recalcCodePageRanges") else None
    tt["head"].flags |= 1 << 3
    if monospace:
        tt["post"].isFixedPitch = 1
    return tt


def compile_statics(weights):
    import ufoLib2
    from ufo2ft import compileOTF, compileTTF
    out = {k: os.path.join(ROOT, "fonts", k) for k in ("ttf", "otf", "woff2")}
    for p in out.values():
        os.makedirs(p, exist_ok=True)
    for w in weights:
        for it in (False, True):
            ufo = ufoLib2.Font.open(ufo_path(w, it))
            base = f"{FAM['ps']}-{ps_style(w, it)}"
            ttf = postprocess(compileTTF(ufo, removeOverlaps=True, overlapsBackend="pathops", reverseDirection=True, useProductionNames=False), FAM.get("monospace"), stat_axes([w], it))
            ttf.save(os.path.join(out["ttf"], base + ".ttf"))
            ufo = ufoLib2.Font.open(ufo_path(w, it))
            otf = postprocess(compileOTF(ufo, removeOverlaps=True, overlapsBackend="pathops", useProductionNames=False), FAM.get("monospace"), stat_axes([w], it))
            otf.save(os.path.join(out["otf"], base + ".otf"))
            ttf.flavor = "woff2"
            ttf.save(os.path.join(out["woff2"], base + ".woff2"))
            print("built", base, flush=True)


def compile_variable(weights):
    from fontTools.designspaceLib import DesignSpaceDocument
    from fontTools.otlLib.builder import buildStatTable
    from ufo2ft import compileVariableTTF
    outdir = os.path.join(ROOT, "fonts", "variable")
    os.makedirs(outdir, exist_ok=True)
    for it in (False, True):
        ds = DesignSpaceDocument.fromfile(os.path.join(ROOT, "sources", f"{FAM['ps']}{'-Italic' if it else ''}.designspace"))
        import ufoLib2
        ds.loadSourceFonts(ufoLib2.Font.open)
        vf = compileVariableTTF(ds, optimizeGvar=True, useProductionNames=False)
        # keep overlapping primitives; flag them so rasterisers union correctly
        glyf = vf["glyf"]
        for gn in vf.getGlyphOrder():
            g = glyf[gn]
            if g.numberOfContours > 0:
                g.flags[0] |= 0x40
        axes = [
            {"tag": "wght", "name": "Weight", "values": [
                {"value": w, "name": n, **({"flags": 2, "linkedValue": 700} if w == 400 else {})}
                for w, n in WEIGHTS if w in weights]},
            {"tag": "ital", "name": "Italic", "values": [
                {"value": 1 if it else 0, "name": "Italic" if it else "Roman",
                 **({} if it else {"flags": 2, "linkedValue": 1})}]},
        ]
        buildStatTable(vf, axes, elidedFallbackName="Regular")
        postprocess(vf, FAM.get("monospace"))
        name = f"{FAM['ps']}{'-Italic' if it else ''}[wght]"
        vf.save(os.path.join(outdir, name + ".ttf"))
        vf.flavor = "woff2"
        vf.save(os.path.join(outdir, name + ".woff2"))
        print("built", name, flush=True)


def checksums():
    lines = []
    for sub in ("ttf", "otf", "woff2", "variable"):
        d = os.path.join(ROOT, "fonts", sub)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            with open(os.path.join(d, fn), "rb") as fh:
                lines.append(f"{hashlib.sha256(fh.read()).hexdigest()}  {sub}/{fn}")
    with open(os.path.join(ROOT, "fonts", "SHA256SUMS"), "w") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources-only", action="store_true")
    ap.add_argument("--no-vf", action="store_true")
    ap.add_argument("--weights", default=",".join(str(w) for w, _ in WEIGHTS))
    a = ap.parse_args()
    ws = [int(x) for x in a.weights.split(",")]
    os.environ.setdefault("SOURCE_DATE_EPOCH", "1792800000")
    make_sources(ws)
    if not a.sources_only:
        compile_statics(ws)
        if not a.no_vf and len(ws) > 1:
            compile_variable(ws)
        checksums()
