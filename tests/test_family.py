"""NullType-specific tests: ligatures must never alter the source text."""
import os

import pytest
from test_fonts import ROOT, STYLES, path, shape

SAMPLE = "if (a != b && c >= d) { x => y; z -> w; q <- r; s == t; u === v; p !== q; <-> }"


@pytest.mark.parametrize("w,it", STYLES)
def test_ligatures_preserve_glyph_count_and_clusters(w, it):
    p = path(w, it, "ttf")
    names, infos, pos = shape(p, SAMPLE)
    assert len(names) == len(SAMPLE)
    assert [i.cluster for i in infos] == list(range(len(SAMPLE)))
    assert all(x.x_advance == 600 for x in pos)


def test_specific_ligatures():
    p = path(400, False, "ttf")
    assert shape(p, "->")[0] == ["hyphen.arrow", "greater.arrow"]
    assert shape(p, "<-")[0] == ["less.arrow", "hyphen.larrow"]
    assert shape(p, "=>")[0] == ["equal.dblarrow", "greater.dblarrow"]
    assert shape(p, "!=")[0] == ["exclam.ne", "equal.ne"]
    assert shape(p, "==")[0] == ["equal.eq1", "equal.eq2"]
    assert shape(p, "===")[0] == ["equal", "equal", "equal"]
    assert shape(p, "->", {"calt": False})[0] == ["hyphen", "greater"]


def test_powerline_and_box_present():
    from fontTools.ttLib import TTFont
    cmap = TTFont(path(400, False, "ttf")).getBestCmap()
    for cp in [0xE0A0, 0xE0A1, 0xE0A2, 0xE0B0, 0xE0B1, 0xE0B2, 0xE0B3] + list(range(0x2500, 0x25A0)):
        assert cp in cmap, hex(cp)
