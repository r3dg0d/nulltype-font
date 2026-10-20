"""Binary-level QA for every compiled style. Run: pytest -q"""
import os
import sys

import freetype
import pytest
import uharfbuzz as hb
from fontTools.ttLib import TTFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import engine  # noqa: E402
from ttcore import WEIGHTS, ps_style, style_name  # noqa: E402

FAM = engine.FAMILY
STYLES = [(w, it) for w, _ in WEIGHTS for it in (False, True)]
ASCII = range(0x20, 0x7F)


def path(w, it, kind):
    return os.path.join(ROOT, "fonts", kind, f"{FAM['ps']}-{ps_style(w, it)}.{kind}")


def shape(p, text, features=None, variations=None):
    face = hb.Face(hb.Blob.from_file_path(p))
    font = hb.Font(face)
    if variations:
        font.set_variations(variations)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, features or {})
    order = TTFont(p).getGlyphOrder()
    return [order[i.codepoint] for i in buf.glyph_infos], buf.glyph_infos, buf.glyph_positions


def test_file_counts():
    for kind in ("ttf", "otf", "woff2"):
        files = [f for f in os.listdir(os.path.join(ROOT, "fonts", kind)) if f.endswith("." + kind)]
        assert len(files) == 18, (kind, len(files))


@pytest.mark.parametrize("w,it", STYLES)
def test_formats_and_metadata(w, it):
    ttf = TTFont(path(w, it, "ttf"))
    otf = TTFont(path(w, it, "otf"))
    woff = TTFont(path(w, it, "woff2"))
    assert "glyf" in ttf and "CFF " in otf and woff.flavor == "woff2"
    for f in (ttf, otf):
        name = f["name"]
        style = style_name(w, it)
        assert name.getDebugName(16) in (None, FAM["name"]) or name.getDebugName(16) == FAM["name"]
        typo_sub = name.getDebugName(17) or name.getDebugName(2)
        assert typo_sub == style
        assert name.getDebugName(6) == f"{FAM['ps']}-{ps_style(w, it)}"
        if w in (400, 700):
            assert name.getDebugName(1) == FAM["name"]
        else:
            assert name.getDebugName(1) == f"{FAM['name']} {dict(WEIGHTS)[w]}"
        os2, head = f["OS/2"], f["head"]
        assert os2.usWeightClass == w
        assert bool(os2.fsSelection & 1) == it and bool(head.macStyle & 2) == it
        assert bool(os2.fsSelection & 32) == (w == 700) and bool(head.macStyle & 1) == (w == 700)
        assert bool(os2.fsSelection & 64) == (w != 700 and not it)
        assert (f["post"].italicAngle != 0) == it
        assert os2.fsType == 0
        assert "Open Font License" in name.getDebugName(13)
        assert name.getDebugName(0).startswith("Copyright 2026")
        cmap = f.getBestCmap()
        assert all(c in cmap for c in ASCII)


@pytest.mark.parametrize("w,it", STYLES)
def test_freetype_rasterises_everything(w, it):
    p = path(w, it, "ttf")
    face = freetype.Face(p)
    face.set_char_size(24 * 64)
    cmap = TTFont(p).getBestCmap()
    blank = {0x20, 0xA0, 0xAD} if 0xAD not in cmap else {0x20, 0xA0}
    for cp in cmap:
        face.load_char(cp, freetype.FT_LOAD_RENDER | freetype.FT_LOAD_NO_HINTING)
        bm = face.glyph.bitmap
        if cp not in blank:
            assert bm.width > 0 and bm.rows > 0, f"U+{cp:04X} renders empty"


def test_zero_features():
    p = path(400, False, "ttf")
    assert shape(p, "0")[0] == ["zero"]
    assert shape(p, "0", {"zero": True})[0] == ["zero.slash"]
    assert shape(p, "0", {"ss01": True})[0][0].startswith("zero.")


def test_variable_fonts():
    for it in (False, True):
        p = os.path.join(ROOT, "fonts", "variable", f"{FAM['ps']}{'-Italic' if it else ''}[wght].ttf")
        vf = TTFont(p)
        ax = vf["fvar"].axes[0]
        assert (ax.axisTag, ax.minValue, ax.defaultValue, ax.maxValue) == ("wght", 100, 400, 900)
        assert len(vf["fvar"].instances) == 9
        assert "STAT" in vf and "gvar" in vf
        # advances interpolate monotonically between masters
        a1 = sum(p_.x_advance for p_ in shape(p, "Hamburg", variations={"wght": 300})[2])
        a2 = sum(p_.x_advance for p_ in shape(p, "Hamburg", variations={"wght": 650})[2])
        assert a2 >= a1


@pytest.mark.skipif(not FAM.get("monospace"), reason="proportional family")
@pytest.mark.parametrize("w,it", STYLES)
def test_monospace_advances(w, it):
    f = TTFont(path(w, it, "ttf"))
    widths = {f["hmtx"][g][0] for g in f.getGlyphOrder() if f["hmtx"][g][0] > 0}
    assert len(widths) == 1, widths
    assert f["post"].isFixedPitch


def test_glyph_compatibility_sources():
    """Masters share glyph sets (required for the variable font)."""
    import ufoLib2
    sets = []
    for w in (100, 900):
        u = ufoLib2.Font.open(os.path.join(ROOT, "sources", "ufo", f"{FAM['ps']}-{ps_style(w, False)}.ufo"))
        sets.append({g.name: len(g.contours) for g in u})
    assert sets[0] == sets[1]


@pytest.mark.parametrize("it", [False, True])
@pytest.mark.parametrize("wght", [100, 250, 400, 650, 900])
def test_variable_rasterises(it, wght):
    """FreeType must render every encoded glyph of the VF at arbitrary weights."""
    p = os.path.join(ROOT, "fonts", "variable", f"{FAM['ps']}{'-Italic' if it else ''}[wght].ttf")
    face = freetype.Face(p)
    face.set_char_size(24 * 64)
    face.set_var_design_coords([wght])
    for cp in TTFont(p).getBestCmap():
        face.load_char(cp, freetype.FT_LOAD_RENDER | freetype.FT_LOAD_NO_HINTING)
        if cp not in (0x20, 0xA0):
            assert face.glyph.bitmap.width > 0, f"U+{cp:04X} @ {wght}"
    # the VF must also pass fontTools' own gvar/glyf consistency by fully decompiling
    tt = TTFont(p)
    for g in tt.getGlyphOrder():
        tt["glyf"][g].getCoordinates(tt["glyf"])
    tt["gvar"].variations  # noqa: B018
