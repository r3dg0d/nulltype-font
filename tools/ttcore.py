"""Shared font-engineering core (geometry, UFO writing, compilation, naming).

This file is deliberately self-contained so each family repository can be
maintained independently. MIT licensed (see LICENSE-TOOLS)."""
from __future__ import annotations

import math
import os
import unicodedata
from dataclasses import dataclass, field

from fontTools.agl import UV2AGL

WEIGHTS = [
    (100, "Thin"), (200, "ExtraLight"), (300, "Light"), (400, "Regular"),
    (500, "Medium"), (600, "SemiBold"), (700, "Bold"), (800, "ExtraBold"),
    (900, "Black"),
]


def style_name(weight: int, italic: bool) -> str:
    base = dict(WEIGHTS)[weight]
    if italic:
        return "Italic" if base == "Regular" else f"{base} Italic"
    return base


def ps_style(weight: int, italic: bool) -> str:
    return style_name(weight, italic).replace(" ", "")


def glyph_name(cp: int) -> str:
    if cp in UV2AGL and cp > 0x1F:
        return UV2AGL[cp]
    return f"uni{cp:04X}" if cp <= 0xFFFF else f"u{cp:05X}"


@dataclass
class Glyph:
    name: str
    unicodes: list = field(default_factory=list)
    width: int = 0
    contours: list = field(default_factory=list)  # list[list[(x, y, type)]]

    # --- primitives: every primitive always emits the same point structure, so
    # masters built from the same recipe stay interpolation-compatible even
    # when a primitive collapses to zero area at some weight.
    def rect(self, x0, y0, x1, y1):
        if x1 < x0:
            x0, x1 = x1, x0
        if y1 < y0:
            y0, y1 = y1, y0
        # counter-clockwise (PostScript / UFO outer-contour direction)
        self.contours.append([(x0, y0, "line"), (x1, y0, "line"),
                              (x1, y1, "line"), (x0, y1, "line")])

    def poly(self, pts):
        """Closed polygon; direction normalised to counter-clockwise."""
        if signed_area(pts) < 0:
            pts = list(reversed(pts))
        self.contours.append([(x, y, "line") for x, y in pts])

    def ellipse(self, cx, cy, rx, ry, k=0.5523):
        hx, hy = rx * k, ry * k
        self.contours.append([
            (cx + rx, cy, "curve"), (cx + rx, cy + hy, None), (cx + hx, cy + ry, None),
            (cx, cy + ry, "curve"), (cx - hx, cy + ry, None), (cx - rx, cy + hy, None),
            (cx - rx, cy, "curve"), (cx - rx, cy - hy, None), (cx - hx, cy - ry, None),
            (cx, cy - ry, "curve"), (cx + hx, cy - ry, None), (cx + rx, cy - hy, None),
        ])

    def transform(self, fn):
        self.contours = [[(*fn(x, y), t) for x, y, t in c] for c in self.contours]


def signed_area(pts):
    a = 0.0
    for i, (x0, y0) in enumerate(pts):
        x1, y1 = pts[(i + 1) % len(pts)]
        a += x0 * y1 - x1 * y0
    return a / 2


# ---------------------------------------------------------------- box drawing
def parse_box_name(cp):
    """Return {'up':w,'down':w,'left':w,'right':w} with w in {1 light, 2 heavy, 3 double}
    for the regular U+2500..U+257F line characters, or None for special ones."""
    name = unicodedata.name(chr(cp), "")
    if not name.startswith("BOX DRAWINGS "):
        return None
    body = name[len("BOX DRAWINGS "):]
    if any(k in body for k in ("DASH", "ARC", "DIAGONAL")):
        return None
    wmap = {"LIGHT": 1, "SINGLE": 1, "HEAVY": 2, "DOUBLE": 3}
    dmap = {"UP": ["up"], "DOWN": ["down"], "LEFT": ["left"], "RIGHT": ["right"],
            "HORIZONTAL": ["left", "right"], "VERTICAL": ["up", "down"]}
    res = {}
    current = None
    for part in body.split(" AND "):
        words = part.split()
        weight = None
        dirs = []
        for w in words:
            if w in wmap:
                weight = wmap[w]
            elif w in dmap:
                dirs += dmap[w]
        if weight is None:
            weight = current
        current = weight
        for d in dirs:
            res[d] = weight
    return res or None


def box_extra_spec(cp):
    name = unicodedata.name(chr(cp), "")
    return name


BOX_RANGE = list(range(0x2500, 0x2580))
BLOCK_RANGE = list(range(0x2580, 0x25A0))
POWERLINE = [0xE0A0, 0xE0A1, 0xE0A2, 0xE0B0, 0xE0B1, 0xE0B2, 0xE0B3]

# Latin-1 precomposed letters: cp -> (base glyph, accent)
COMPOSITES = {}
for _cp in range(0x00C0, 0x0100):
    _d = unicodedata.decomposition(chr(_cp))
    if not _d or _d.startswith("<"):
        continue
    _b, _m = (int(x, 16) for x in _d.split())
    _acc = {0x300: "grave", 0x301: "acute", 0x302: "circumflex", 0x303: "tilde",
            0x308: "dieresis", 0x30A: "ring", 0x327: "cedilla"}[_m]
    COMPOSITES[_cp] = (_b, _acc)
COMPOSITES[0x0178] = (0x59, "dieresis")


# ------------------------------------------------------------- UFO writing
def write_ufo(path, fam, glyphs, weight, italic, features, kerning=None, extra_info=None):
    import ufoLib2
    from ufoLib2.objects import Contour, Point

    f = ufoLib2.Font()
    info = f.info
    style = style_name(weight, italic)
    info.familyName = fam["name"]
    info.styleName = style
    ribbi = weight in (400, 700)
    info.styleMapFamilyName = fam["name"] if ribbi else f"{fam['name']} {dict(WEIGHTS)[weight]}"
    info.styleMapStyleName = ("bold " if weight == 700 else "") + ("italic" if italic else "") or "regular"
    info.styleMapStyleName = info.styleMapStyleName.strip() or "regular"
    info.openTypeNamePreferredFamilyName = fam["name"]
    info.openTypeNamePreferredSubfamilyName = style
    info.postscriptFontName = f"{fam['ps']}-{ps_style(weight, italic)}"
    info.postscriptFullName = f"{fam['name']} {style}"
    info.openTypeNameCompatibleFullName = f"{fam['name']} {style}"
    info.versionMajor, info.versionMinor = fam["version"]
    info.openTypeNameVersion = f"Version {fam['version'][0]}.{fam['version'][1]:03d}"
    info.openTypeNameUniqueID = f"{fam['version'][0]}.{fam['version'][1]:03d};{fam['vendor']};{info.postscriptFontName}"
    info.copyright = fam["copyright"]
    info.trademark = None
    info.openTypeNameDesigner = fam["designer"]
    info.openTypeNameManufacturer = fam["designer"]
    info.openTypeNameDesignerURL = fam["url"]
    info.openTypeNameManufacturerURL = fam["url"]
    info.openTypeNameLicense = ("This Font Software is licensed under the SIL Open Font License, "
                                "Version 1.1. This license is available with a FAQ at: https://openfontlicense.org")
    info.openTypeNameLicenseURL = "https://openfontlicense.org"
    info.openTypeNameDescription = fam["description"]
    info.openTypeOS2VendorID = fam["vendor"]
    info.openTypeOS2Type = []  # fsType 0: installable embedding
    info.openTypeOS2WeightClass = weight
    info.openTypeOS2WidthClass = 5
    info.openTypeOS2Selection = [7]  # USE_TYPO_METRICS
    info.unitsPerEm = fam["upm"]
    m = fam["metrics"]
    info.ascender = m["ascender"]
    info.descender = m["descender"]
    info.capHeight = m["cap"]
    info.xHeight = m["x"]
    info.italicAngle = -fam["italic_angle"] if italic else 0
    for k in ("openTypeHheaAscender", "openTypeOS2TypoAscender"):
        setattr(info, k, m["line_ascent"])
    for k in ("openTypeHheaDescender", "openTypeOS2TypoDescender"):
        setattr(info, k, -m["line_descent"])
    info.openTypeHheaLineGap = 0
    info.openTypeOS2TypoLineGap = 0
    info.openTypeOS2WinAscent = m["win_ascent"]
    info.openTypeOS2WinDescent = m["win_descent"]
    info.postscriptUnderlinePosition = m.get("underline_pos", -150)
    info.postscriptUnderlineThickness = m.get("underline_thick", 60)
    info.postscriptIsFixedPitch = bool(fam.get("monospace"))
    if fam.get("monospace"):
        info.openTypeOS2Panose = [2, 11, 5, 9, 2, 2, 3, 2, 2, 7]
    # Unicode ranges are recalculated from the cmap after compilation.
    info.openTypeOS2CodePageRanges = [0]
    info.openTypeGaspRangeRecords = [{"rangeMaxPPEM": 65535, "rangeGaspBehavior": [0, 1, 2, 3]}]
    if extra_info:
        for k, v in extra_info.items():
            setattr(info, k, v)

    order = [g.name for g in glyphs]
    for g in glyphs:
        ug = f.newGlyph(g.name)
        ug.width = round(g.width)
        ug.unicodes = list(g.unicodes)
        for c in g.contours:
            ug.contours.append(Contour(points=[Point(round(x, 2), round(y, 2), t) for x, y, t in c]))
    f.lib["public.glyphOrder"] = order
    f.lib["public.postscriptNames"] = {}
    f.features.text = features
    if kerning:
        f.kerning.update(kerning)
    if os.path.exists(path):
        import shutil
        shutil.rmtree(path)
    f.save(path)
    return f


def italic_bits_ok(tt):
    """Return list of metadata problems for a compiled static font."""
    probs = []
    os2, head, name = tt["OS/2"], tt["head"], tt["name"]
    sub = name.getDebugName(17) or name.getDebugName(2)
    italic = "Italic" in sub
    if bool(os2.fsSelection & 1) != italic:
        probs.append("fsSelection italic bit")
    if bool(head.macStyle & 2) != italic:
        probs.append("macStyle italic bit")
    if italic and tt["post"].italicAngle == 0:
        probs.append("post.italicAngle")
    return probs
