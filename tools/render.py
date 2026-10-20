"""Render text from real font binaries: HarfBuzz shaping + FreeType rasterisation.
Also emits SVG from the shaped outlines. MIT licensed."""
from __future__ import annotations

import freetype
import numpy as np
import uharfbuzz as hb
from PIL import Image, ImageDraw


def shape(path, text, features=None, variations=None):
    blob = hb.Blob.from_file_path(path)
    face = hb.Face(blob)
    font = hb.Font(face)
    if variations:
        font.set_variations(variations)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, features or {})
    return buf.glyph_infos, buf.glyph_positions, face.upem


def render_line(path, text, size, features=None, variations=None, fg=0, bg=255, pad=8):
    infos, pos, upem = shape(path, text, features, variations)
    ft = freetype.Face(path)
    ft.set_char_size(size * 64)
    if variations:
        axes = ft.get_variation_info().axes
        ft.set_var_design_coords([variations.get(a.tag, a.default) for a in axes])
    scale = size / upem
    asc = int(ft.size.ascender / 64) + 2
    desc = int(-ft.size.descender / 64) + 2
    width = int(sum(p.x_advance for p in pos) * scale) + 2 * pad + size
    img = np.zeros((asc + desc + 2 * pad, max(width, 10)), dtype=np.uint8)
    x = pad
    for info, p in zip(infos, pos):
        ft.load_glyph(info.codepoint, freetype.FT_LOAD_RENDER | freetype.FT_LOAD_NO_HINTING)
        bm = ft.glyph.bitmap
        if bm.width and bm.rows:
            arr = np.array(bm.buffer, dtype=np.uint8).reshape(bm.rows, bm.pitch)[:, :bm.width]
            gx = int(round(x + p.x_offset * scale)) + ft.glyph.bitmap_left
            gy = pad + asc - ft.glyph.bitmap_top
            h, w = arr.shape
            y0, x0 = max(gy, 0), max(gx, 0)
            sub = img[y0:gy + h, x0:gx + w]
            src = arr[y0 - gy:y0 - gy + sub.shape[0], x0 - gx:x0 - gx + sub.shape[1]]
            np.maximum(sub, src, out=sub)
        x += p.x_advance * scale
    alpha = img.astype(np.float32) / 255
    out = (bg * (1 - alpha) + fg * alpha).astype(np.uint8)
    return Image.fromarray(out, "L")


def stack(images, bg=255, gap=4):
    w = max(i.width for i in images)
    h = sum(i.height for i in images) + gap * len(images)
    out = Image.new("L", (w, h), bg)
    y = 0
    for i in images:
        out.paste(i, (0, y))
        y += i.height + gap
    return out


def label(text, size=14):
    img = Image.new("L", (8 * len(text) + 16, size + 8), 255)
    ImageDraw.Draw(img).text((8, 2), text, fill=110)
    return img


def svg_line(path, text, size, features=None, y=0):
    """Return SVG path data for a shaped line (outlines from the binary)."""
    from fontTools.pens.svgPathPen import SVGPathPen
    from fontTools.pens.transformPen import TransformPen
    from fontTools.ttLib import TTFont
    tt = TTFont(path)
    gs = tt.getGlyphSet()
    order = tt.getGlyphOrder()
    infos, pos, upem = shape(path, text, features)
    s = size / upem
    asc = tt["hhea"].ascent
    x = 0
    parts = []
    for info, p in zip(infos, pos):
        pen = SVGPathPen(gs)
        tp = TransformPen(pen, (s, 0, 0, -s, x * s, y + asc * s))
        gs[order[info.codepoint]].draw(tp)
        d = pen.getCommands()
        if d:
            parts.append(d)
        x += p.x_advance
    return " ".join(parts), x * s, (asc - tt["hhea"].descent) * s
