"""NullType procedural engine: stroke skeletons + rectangular pen -> outline masters.

Construction model:
  * glyphs are polylines on an 8 x 14 grid with 45-degree chamfered corners;
  * each segment is swept by an axis-aligned rectangular pen (Minkowski sum),
    producing a convex hexagon; segments overlap at joints and are unioned for
    the static fonts (pathops);
  * vertical stems use the pen width, horizontal bars the pen height; the bar
    is progressively thinner than the stem above Regular, so heavy weights
    keep their horizontal counters open (not a uniform outline offset);
  * the stem-centre box is inset by half a stem, so every weight keeps the
    same outer extent inside the 600-unit monospaced cell;
  * italics shear the skeleton 10 degrees around mid-x-height while the pen
    stays upright, giving true slanted strokes with constant stem widths.
Every glyph recipe yields the same contour structure at every weight, so the
masters drive a variable font directly.
"""
from __future__ import annotations

import math
import os
import unicodedata

from ttcore import (BLOCK_RANGE, BOX_RANGE, COMPOSITES, POWERLINE, Glyph,
                    glyph_name, parse_box_name)

HERE = os.path.dirname(os.path.abspath(__file__))
SKEL = os.path.join(HERE, "..", "sources", "skeletons.txt")

ADV = 600
SLANT = math.tan(math.radians(10))
STEM = {100: 18, 200: 32, 300: 50, 400: 72, 500: 88, 600: 102, 700: 116, 800: 128, 900: 140}
CAP = 700

FAMILY = {
    "name": "NullType", "ps": "NullType", "version": (1, 0), "vendor": "R3DG",
    "copyright": "Copyright 2026 Vincent Patrick Chambers (https://github.com/r3dg0d/nulltype-font), with Reserved Font Name \"NullType\".",
    "designer": "Vincent Patrick Chambers", "url": "https://github.com/r3dg0d/nulltype-font",
    "description": "NullType: an original chamfered monospace for terminals and code, with source-preserving ligatures.",
    "upm": 1000, "italic_angle": 10.0, "monospace": True,
    "metrics": {"ascender": 750, "descender": -200, "cap": 700, "x": 500,
                "line_ascent": 950, "line_descent": 250, "win_ascent": 1030, "win_descent": 330,
                "underline_pos": -150, "underline_thick": 60},
}
BOX_TOP, BOX_BOTTOM = 950, -250

ACCENTS = {
    "grave": "3,2.5 5,0.5", "acute": "3,0.5 5,2.5", "circumflex": "1,0.5 4,2.5 7,0.5",
    "tilde": "1,0.5 3,2 5,1 7,2.5", "dieresis": "2,1.5 2,1.5 ; 6,1.5 6,1.5",
    "ring": "3,0 5,0 5,2.5 3,2.5 3,0", "cedilla": "4,0 4,-1 6,-2 6,-3 3,-4",
}


def pen(weight):
    stem = STEM[weight]
    ratio = 0.92 if weight <= 400 else 0.92 - 0.12 * (weight - 400) / 500
    return stem / 2, stem * ratio / 2


def load():
    out = []
    with open(SKEL) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            head, _, body = line.partition("|")
            name, cp = head.split()[:2]
            out.append((name, None if cp == "-" else int(cp, 16), body.strip()))
    return out


def parse_strokes(body):
    strokes = []
    for part in body.split(";"):
        part = part.strip()
        if not part:
            continue
        scale = 1.0
        if "@" in part:
            part, s = part.rsplit("@", 1)
            scale = float(s)
        pts = [tuple(p.split(",")) for p in part.split()]
        strokes.append((pts, scale))
    return strokes


class Mapper:
    def __init__(self, weight, italic):
        self.a, self.b = pen(weight)
        self.italic = italic
        self.xl, self.xr = 70 + self.a, 530 - self.a

    def x(self, gx):
        if gx == "W":
            return -10.0
        if gx == "E":
            return ADV + 10.0
        return self.xl + (self.xr - self.xl) * float(gx) / 8

    def y(self, gy):
        gy = float(gy)
        return self.b + gy * (CAP - 2 * self.b) / 14

    def pt(self, p, dy=0.0):
        x, y = self.x(p[0]), self.y(float(p[1]) + dy)
        if self.italic:
            x += (y - 250) * SLANT
        return x, y


def hexagon(g, P, Q, a, b):
    (x0, y0), (x1, y1) = P, Q
    if (x1, y1) < (x0, y0):
        (x0, y0), (x1, y1) = (x1, y1), (x0, y0)
    if y1 >= y0:
        pts = [(x0 - a, y0 - b), (x0 + a, y0 - b), (x1 + a, y1 - b),
               (x1 + a, y1 + b), (x1 - a, y1 + b), (x0 - a, y0 + b)]
    else:
        pts = [(x0 - a, y0 + b), (x0 - a, y0 - b), (x1 - a, y1 - b),
               (x1 + a, y1 - b), (x1 + a, y1 + b), (x0 + a, y0 + b)]
    g.contours.append([(x, y, "line") for x, y in pts])


def draw_strokes(g, strokes, m, dy=0.0):
    for pts, scale in strokes:
        a, b = m.a * scale, m.b * scale
        mapped = [m.pt(p, dy) for p in pts]
        if len(mapped) == 2 and mapped[0] == mapped[1]:
            x, y = mapped[0]
            s = 1.18
            g.rect(x - a * s, y - b * s * 1.08, x + a * s, y + b * s * 1.08)
            continue
        for P, Q in zip(mapped, mapped[1:]):
            hexagon(g, P, Q, a, b)


# --------------------------------------------------------- terminal glyphs
def box_glyph(cp, weight, italic):
    stem = STEM[weight]
    lt = max(stem, 40)
    hv = min(lt * 2, 220)
    g = Glyph(glyph_name(cp), [cp], ADV)
    cx, cy = ADV / 2, (BOX_TOP + BOX_BOTTOM) / 2
    spec = parse_box_name(cp)
    name = unicodedata.name(chr(cp))
    dbl = 130

    def arm(d, w):
        th = hv if w == 2 else lt
        offs = (-dbl / 2, dbl / 2) if w == 3 else (0,)
        reach = (dbl / 2 + lt / 2) if w == 3 else th / 2
        for off in offs:
            if d == "left":
                g.rect(0, cy + off - th / 2, cx + reach, cy + off + th / 2)
            elif d == "right":
                g.rect(cx - reach, cy + off - th / 2, ADV, cy + off + th / 2)
            elif d == "up":
                g.rect(cx + off - th / 2, cy - reach, cx + off + th / 2, BOX_TOP)
            else:
                g.rect(cx + off - th / 2, BOX_BOTTOM, cx + off + th / 2, cy + reach)

    if spec:
        for d, w in spec.items():
            arm(d, w)
    elif "DASH" in name:
        n = 2 if "DOUBLE DASH" in name else 3 if "TRIPLE" in name else 4
        th = hv if "HEAVY" in name else lt
        if "HORIZONTAL" in name:
            seg = ADV / n
            for i in range(n):
                g.rect(i * seg + seg * .2, cy - th / 2, (i + 1) * seg - seg * .2, cy + th / 2)
        else:
            seg = (BOX_TOP - BOX_BOTTOM) / n
            for i in range(n):
                g.rect(cx - th / 2, BOX_BOTTOM + i * seg + seg * .2, cx + th / 2, BOX_BOTTOM + (i + 1) * seg - seg * .2)
    elif "ARC" in name:
        sx = 1 if "RIGHT" in name else -1
        sy = 1 if " UP " in f" {name} " else -1
        r = 140
        vend = BOX_TOP if sy > 0 else BOX_BOTTOM
        hend = ADV if sx > 0 else 0
        hexagon(g, (cx, vend), (cx, cy + sy * r), lt / 2, lt / 2)
        hexagon(g, (cx, cy + sy * r), (cx + sx * r, cy), lt / 2, lt / 2)
        hexagon(g, (cx + sx * r, cy), (hend, cy), lt / 2, lt / 2)
    elif "DIAGONAL" in name:
        if "UPPER RIGHT TO LOWER LEFT" in name or "CROSS" in name:
            hexagon(g, (0, BOX_BOTTOM), (ADV, BOX_TOP), lt / 2, lt / 2)
        if "UPPER LEFT TO LOWER RIGHT" in name or "CROSS" in name:
            hexagon(g, (0, BOX_TOP), (ADV, BOX_BOTTOM), lt / 2, lt / 2)
    return g


def block_glyph(cp, weight, italic):
    g = Glyph(glyph_name(cp), [cp], ADV)
    T, B, W = BOX_TOP, BOX_BOTTOM, ADV
    H = T - B
    if 0x2581 <= cp <= 0x2588:
        g.rect(0, B, W, B + H * (cp - 0x2580) / 8)
    elif cp == 0x2580:
        g.rect(0, B + H / 2, W, T)
    elif 0x2589 <= cp <= 0x258F:
        g.rect(0, B, W * (8 - (cp - 0x2588)) / 8, T)
    elif cp == 0x2590:
        g.rect(W / 2, B, W, T)
    elif cp in (0x2591, 0x2592, 0x2593):
        # shades as diagonal hatching (a NullType signature), density by code point
        n = {0x2591: 6, 0x2592: 10, 0x2593: 16}[cp]
        th = {0x2591: 24, 0x2592: 46, 0x2593: 70}[cp]
        for i in range(n):
            x0 = -W + (2 * W) * (i + 0.5) / n
            g.poly([(max(x0, 0), B + max(0, -x0) * H / W), (min(x0 + W, W), B + min(W, W - x0) * H / W),
                    (min(x0 + W + th, W), B + min(W, W - x0 - th) * H / W), (max(x0 + th, 0), B + max(0, -x0 - th) * H / W)]
                   if False else [(x0, B), (x0 + th, B), (x0 + th + W, T), (x0 + W, T)])
        g.contours = [[(min(max(x, 0), W), y, t) for x, y, t in c] for c in g.contours]
    elif cp == 0x2594:
        g.rect(0, T - H / 8, W, T)
    elif cp == 0x2595:
        g.rect(W * 7 / 8, B, W, T)
    else:
        quads = {0x2596: "3", 0x2597: "4", 0x2598: "1", 0x2599: "134", 0x259A: "14",
                 0x259B: "123", 0x259C: "124", 0x259D: "2", 0x259E: "23", 0x259F: "234"}[cp]
        boxes = {"1": (0, B + H / 2, W / 2, T), "2": (W / 2, B + H / 2, W, T),
                 "3": (0, B, W / 2, B + H / 2), "4": (W / 2, B, W, B + H / 2)}
        for q in quads:
            g.rect(*boxes[q])
    return g


PL_SKEL = {
    0xE0A0: "1,14 1,0 ; 1,4 7,9 7,14 ; 7,14 7,14",
    0xE0A1: "0,14 0,8 3,8 ; 4,6 4,0 ; 4,6 8,0 8,6",
    0xE0A2: "1,0 7,0 7,7 1,7 1,0 ; 2,7 2,10 3,12 5,12 6,10 6,7",
}


def powerline_glyph(cp, weight, italic):
    g = Glyph(glyph_name(cp), [cp], ADV)
    if cp in PL_SKEL:
        draw_strokes(g, parse_strokes(PL_SKEL[cp]), Mapper(weight, False))
        return g
    T, B, W = BOX_TOP, BOX_BOTTOM, ADV
    mid = (T + B) / 2
    lt = max(STEM[weight], 40)
    if cp == 0xE0B0:
        g.poly([(0, B), (W, mid), (0, T)])
    elif cp == 0xE0B2:
        g.poly([(W, B), (W, T), (0, mid)])
    elif cp == 0xE0B1:
        hexagon(g, (0, B), (W - lt / 2, mid), lt / 2, lt / 2)
        hexagon(g, (W - lt / 2, mid), (0, T), lt / 2, lt / 2)
    else:
        hexagon(g, (W, B), (lt / 2, mid), lt / 2, lt / 2)
        hexagon(g, (lt / 2, mid), (W, T), lt / 2, lt / 2)
    return g


def notdef(weight):
    g = Glyph(".notdef", [], ADV)
    draw_strokes(g, parse_strokes("0,0 8,0 8,14 0,14 0,0 ; 0,0 8,14"), Mapper(weight, False))
    return g


def build(weight, italic):
    m = Mapper(weight, italic)
    glyphs = [notdef(weight)]
    src = load()
    by_cp = {}
    for name, cp, body in src:
        g = Glyph(name, [cp] if cp is not None else [], ADV)
        strokes = parse_strokes(body)
        draw_strokes(g, strokes, m)
        glyphs.append(g)
        if cp is not None:
            by_cp[cp] = strokes
    for cp, (bcp, acc) in sorted(COMPOSITES.items()):
        if bcp == 0x69:
            bcp = 0x131
        g = Glyph(glyph_name(cp), [cp], ADV)
        draw_strokes(g, by_cp[bcp], m)
        if acc == "cedilla":
            draw_strokes(g, parse_strokes(ACCENTS[acc]), m)
        else:
            dy = 15.4 if chr(bcp).isupper() else 11.6
            draw_strokes(g, parse_strokes(ACCENTS[acc]), m, dy)
        glyphs.append(g)
    for cp in BOX_RANGE:
        glyphs.append(box_glyph(cp, weight, italic))
    for cp in BLOCK_RANGE:
        glyphs.append(block_glyph(cp, weight, italic))
    for cp in POWERLINE:
        glyphs.append(powerline_glyph(cp, weight, italic))
    return glyphs


def kerning():
    return None  # monospaced: no kerning


def features():
    return """languagesystem DFLT dflt;
languagesystem latn dflt;

# Programming ligatures. Every rule is a one-to-one contextual substitution:
# the glyph count, advances and cluster mapping never change, so copy/paste,
# cursor movement and search always see the original source characters.
lookup ARROWS {
    ignore sub equal equal' equal;
    ignore sub equal' equal equal;
    ignore sub equal equal' greater;
    ignore sub exclam' equal equal;
    sub hyphen' greater by hyphen.arrow;
    sub hyphen.arrow greater' by greater.arrow;
    sub less' hyphen by less.arrow;
    sub less.arrow hyphen' by hyphen.larrow;
    sub equal' greater by equal.dblarrow;
    sub equal.dblarrow greater' by greater.dblarrow;
    sub exclam' equal by exclam.ne;
    sub exclam.ne equal' by equal.ne;
    sub equal' equal by equal.eq1;
    sub equal.eq1 equal' by equal.eq2;
} ARROWS;

feature calt {
    lookup ARROWS;
} calt;

feature zero {
    sub zero by zero.slash;
} zero;

feature ss01 {
    featureNames { name "Plain zero"; };
    sub zero by zero.plain;
} ss01;
"""
