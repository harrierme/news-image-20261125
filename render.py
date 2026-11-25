# Render the 25 November 2026 front page to entry.png (1024x1024, <= 1 MiB).
# Pure Pillow drawing: every illustration is drawn from primitives, no photos.
# Deterministic: fixed data, fixed fonts, no timestamps, no randomness.
# Run: python3 render.py  -> writes entry.png next to this file.
# Fonts ship in assets/fonts/ so the render is reproducible anywhere.

import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "assets", "fonts")

W, H = 1024, 1024
PAPER = (246, 241, 230)
PAPER_CARD = (255, 253, 246)
INK = (25, 23, 19)
MUTED = (92, 86, 74)
FAINT = (150, 142, 126)
RULE = (25, 23, 19)
CARD_LINE = (216, 208, 189)
RED = (163, 19, 19)
BLUE = (29, 78, 121)
TEAL = (14, 94, 86)
GOLD = (146, 106, 24)
SKY = (38, 68, 110)
SEA = (46, 98, 140)


def font_serif(size):
    return ImageFont.truetype(os.path.join(FONTS, "DMSerifDisplay-Regular.ttf"), size)


def font_sans(size, weight=400):
    f = ImageFont.truetype(os.path.join(FONTS, "Montserrat-Variable.ttf"), size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f


def font_cond(size):
    return ImageFont.truetype(os.path.join(FONTS, "BebasNeue-Regular.ttf"), size)


def spaced(text):
    """Fake letter-spacing for kickers: thin spaces between letters."""
    return " ".join(list(text.replace(" ", "  ")))


def wrap(draw, text, font, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, font, max_w, fill, leading=None, max_lines=None,
                 ellipsis=True):
    """Draw wrapped text; returns y just below the last line."""
    if leading is None:
        leading = int(font.size * 1.28)
    lines = wrap(draw, text, font, max_w)
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        if ellipsis:
            while lines and draw.textlength(lines[-1] + "…", font=font) > max_w:
                lines[-1] = lines[-1][:-1]
            lines[-1] = lines[-1].rstrip(" ,.;:") + "…"
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def trunc(draw, text, font, max_w):
    if draw.textlength(text, font=font) <= max_w:
        return text
    while text and draw.textlength(text + "…", font=font) > max_w:
        text = text[:-1]
    return text.rstrip(" ,.;:") + "…"


def rrect(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


# ---------------------------------------------------------------- illustrations
# Every scene draws flat vector shapes inside the given box. No photos.

def art_sky(draw, box, top=(16, 24, 48), bottom=(38, 68, 110)):
    x0, y0, x1, y1 = box
    h = y1 - y0
    for i in range(h):
        t = i / max(1, h - 1)
        c = tuple(int(top[k] + (bottom[k] - top[k]) * t) for k in range(3))
        draw.line([(x0, y0 + i), (x1, y0 + i)], fill=c)


def art_stars(draw, box, n=14, seed=7):
    x0, y0, x1, y1 = box
    import random
    rnd = random.Random(seed)
    for _ in range(n):
        x = rnd.randint(x0 + 3, x1 - 3)
        y = rnd.randint(y0 + 3, y1 - 3)
        r = rnd.choice([1, 1, 2])
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255))


def art_rocket(draw, box):
    art_sky(draw, box)
    art_stars(draw, box)
    x0, y0, x1, y1 = box
    cx = (x0 + x1) // 2
    w = (x1 - x0) // 5
    # ground
    draw.rectangle([x0, y1 - 12, x1, y1], fill=(52, 44, 34))
    # flame
    fy = y0 + (y1 - y0) * 3 // 5
    draw.polygon([(cx - w // 2, fy), (cx + w // 2, fy), (cx, y1 - 12)],
                 fill=(255, 140, 40))
    draw.polygon([(cx - w // 3, fy), (cx + w // 3, fy), (cx, y1 - 20)],
                 fill=(255, 220, 90))
    # body
    by = y0 + 12
    draw.rounded_rectangle([cx - w // 2, by, cx + w // 2, fy + 4], radius=w // 3,
                           fill=(240, 238, 232))
    draw.polygon([(cx - w // 2, by + 8), (cx + w // 2, by + 8), (cx, by - 10)],
                 fill=(163, 19, 19))
    draw.ellipse([cx - w // 4, by + 14, cx + w // 4, by + 14 + w // 2],
                 fill=(29, 78, 121))
    draw.rectangle([cx - w // 2 - 8, fy - 14, cx - w // 2, fy + 2], fill=(163, 19, 19))
    draw.rectangle([cx + w // 2, fy - 14, cx + w // 2 + 8, fy + 2], fill=(163, 19, 19))
    # smoke
    for sx, sy, sr in [(x0 + 14, y1 - 22, 9), (x1 - 16, y1 - 18, 11), (cx - 26, y1 - 14, 8)]:
        draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(220, 218, 210))


def art_asteroid(draw, box):
    art_sky(draw, box, top=(10, 12, 24), bottom=(24, 30, 52))
    art_stars(draw, box, n=18, seed=11)
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    rx, ry = (x1 - x0) // 3, (y1 - y0) // 3
    draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=(128, 122, 110))
    for ox, oy, orr, col in [(-rx // 2, -ry // 3, 9, (96, 90, 80)),
                             (rx // 3, ry // 4, 7, (96, 90, 80)),
                             (0, -ry // 6, 5, (150, 144, 132)),
                             (-rx // 4, ry // 2, 6, (110, 104, 94))]:
        draw.ellipse([cx + ox - orr, cy + oy - orr, cx + ox + orr, cy + oy + orr],
                     fill=col)
    # probe at top right
    px, py = x1 - 34, y0 + 14
    draw.rectangle([px - 12, py - 2, px - 4, py + 2], fill=(70, 90, 140))
    draw.rectangle([px + 4, py - 2, px + 12, py + 2], fill=(70, 90, 140))
    draw.rectangle([px - 4, py - 5, px + 4, py + 5], fill=(220, 220, 215))


def art_pharma(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(232, 240, 236))
    cx = (x0 + x1) // 2
    bw = max(9, (x1 - x0) // 7)
    bh = y1 - y0
    # bottle
    top = y0 + bh // 5
    bot = y1 - bh // 6
    draw.rectangle([cx - bw, top, cx + bw, bot], fill=(255, 255, 255),
                   outline=(29, 78, 121), width=2)
    draw.rectangle([cx - bw + 3, top - 8, cx + bw - 3, top], fill=(29, 78, 121))
    # label with cross
    ly = top + (bot - top) // 2 - 6
    draw.rectangle([cx - bw + 3, ly, cx + bw - 3, ly + 14], fill=(163, 19, 19))
    draw.rectangle([cx - 2, ly + 3, cx + 2, ly + 11], fill=(255, 255, 255))
    draw.rectangle([cx - 6, ly + 6, cx + 6, ly + 8], fill=(255, 255, 255))
    # capsules at the sides
    capw = max(7, (x1 - x0) // 9)
    for sgn in (-1, 1):
        px = cx + sgn * (bw + capw + 5)
        py = y0 + bh * 2 // 3
        draw.rounded_rectangle([px - capw, py - 5, px + capw, py + 5], radius=5,
                               fill=(240, 120, 60))
        draw.rounded_rectangle([px - capw, py - 5, px, py + 5], radius=5,
                               fill=(255, 255, 255))


def art_server(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(18, 26, 38))
    cx = (x0 + x1) // 2
    rw = (x1 - x0) // 2
    for i in range(3):
        ry = y0 + 14 + i * 26
        draw.rectangle([cx - rw, ry, cx + rw, ry + 20], fill=(44, 58, 78),
                       outline=(90, 110, 140))
        for j, col in enumerate([(90, 200, 120), (255, 200, 60), (90, 160, 255)]):
            draw.ellipse([cx - rw + 6 + j * 9, ry + 7, cx - rw + 12 + j * 9, ry + 13],
                         fill=col)
        draw.rectangle([cx + 8, ry + 8, cx + rw - 8, ry + 12], fill=(120, 140, 165))
    # rising chart
    pts = [(x0 + 8, y1 - 14), (x0 + 26, y1 - 26), (x0 + 44, y1 - 20),
           (x0 + 62, y1 - 34), (x1 - 10, y1 - 44)]
    draw.line(pts, fill=(90, 200, 120), width=3)
    draw.polygon([(x1 - 16, y1 - 50), (x1 - 6, y1 - 44), (x1 - 18, y1 - 38)],
                 fill=(90, 200, 120))


def art_ship(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle([x0, y0, x1, y0 + (y1 - y0) * 2 // 3], fill=(178, 214, 232))
    draw.rectangle([x0, y0 + (y1 - y0) * 2 // 3, x1, y1], fill=(46, 98, 140))
    for wy in (y0 + (y1 - y0) * 2 // 3 + 6, y0 + (y1 - y0) * 2 // 3 + 16):
        draw.line([(x0 + 4, wy), (x1 - 4, wy)], fill=(140, 190, 220), width=2)
    cx = (x0 + x1) // 2
    wy = y0 + (y1 - y0) * 2 // 3
    hw = (x1 - x0) * 0.42
    cw = (x1 - x0) * 0.16
    # containers
    cols = [(163, 19, 19), (29, 78, 121), (146, 106, 24), (14, 94, 86)]
    for i, col in enumerate(cols):
        cx0 = cx - hw + i * (2 * hw / 4)
        draw.rectangle([cx0, wy - 26, cx0 + cw, wy - 12],
                       fill=col, outline=(255, 255, 255))
        draw.rectangle([cx0 + cw * 0.25, wy - 38, cx0 + cw * 1.25, wy - 26],
                       fill=cols[(i + 2) % 4], outline=(255, 255, 255))
    # hull
    draw.polygon([(cx - hw, wy - 12), (cx + hw, wy - 12), (cx + hw * 0.8, wy + 6),
                  (cx - hw * 0.8, wy + 6)], fill=(25, 23, 19))
    draw.rectangle([cx + hw * 0.6, wy - 38, cx + hw * 0.85, wy - 12],
                   fill=(240, 238, 232))


def art_aid(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(238, 232, 216))
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    w = x1 - x0
    # crate
    cw = w * 0.27
    draw.rectangle([cx - cw, cy - 8, cx + cw, cy + 30], fill=(176, 138, 78),
                   outline=(90, 66, 30), width=2)
    draw.line([(cx - cw, cy + 11), (cx + cw, cy + 11)], fill=(90, 66, 30), width=2)
    draw.line([(cx, cy - 8), (cx, cy + 30)], fill=(90, 66, 30), width=2)
    # red cross flag above
    fw = w * 0.13
    draw.rectangle([cx - fw, cy - 34, cx + fw, cy - 10], fill=(255, 255, 255),
                   outline=(163, 19, 19), width=2)
    draw.rectangle([cx - 3, cy - 30, cx + 3, cy - 14], fill=(163, 19, 19))
    draw.rectangle([cx - fw + 4, cy - 25, cx + fw - 4, cy - 19], fill=(163, 19, 19))


def art_bank(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(232, 228, 214))
    cx = (x0 + x1) // 2
    bw = (x1 - x0) // 3
    draw.polygon([(cx - bw - 8, y0 + 30), (cx + bw + 8, y0 + 30), (cx, y0 + 10)],
                 fill=(29, 78, 121))
    for i in range(4):
        colx = cx - bw + i * (2 * bw // 3)
        draw.rectangle([colx, y0 + 32, colx + 8, y1 - 18], fill=(255, 253, 246),
                       outline=(29, 78, 121))
    draw.rectangle([cx - bw - 8, y1 - 18, cx + bw + 8, y1 - 10], fill=(29, 78, 121))
    f = font_serif(26)
    draw.text((cx - 9, y0 + 44), "€", font=f, fill=(146, 106, 24))


def art_radar(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(10, 30, 18))
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    r = min(x1 - x0, y1 - y0) // 2 - 4
    for rr in (r, r * 2 // 3, r // 3):
        draw.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=(60, 160, 100))
    draw.line([(cx - r, cy), (cx + r, cy)], fill=(60, 160, 100))
    draw.line([(cx, cy - r), (cx, cy + r)], fill=(60, 160, 100))
    draw.line([(cx, cy), (cx + r, cy - r)], fill=(140, 255, 170), width=2)
    for bx, by in [(cx + r // 2, cy - r // 4), (cx - r // 3, cy + r // 3),
                   (cx + r // 4, cy + r // 2)]:
        draw.ellipse([bx - 3, by - 3, bx + 3, by + 3], fill=(255, 80, 80))


def art_mine(draw, box):
    x0, y0, x1, y1 = box
    w = x1 - x0
    draw.rectangle([x0, y0, x1, y0 + (y1 - y0) // 2], fill=(178, 214, 232))
    draw.rectangle([x0, y0 + (y1 - y0) // 2, x1, y1], fill=(46, 98, 140))
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    # tanker
    draw.rectangle([x0 + 8, cy - 16, x1 - 8, cy - 4], fill=(90, 66, 30))
    draw.rectangle([x0 + 14, cy - 26, x0 + 30, cy - 16], fill=(240, 238, 232))
    # mine
    mx, my = cx + w * 0.18, cy + 14
    mr = max(6, w * 0.08)
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0), (-0.7, -0.7), (0.7, -0.7),
                   (-0.7, 0.7), (0.7, 0.7)]:
        draw.line([(mx, my), (mx + dx * (mr + 4), my + dy * (mr + 4))],
                  fill=(25, 23, 19), width=2)
    draw.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=(25, 23, 19))
    draw.ellipse([mx - mr * 0.4, my - mr * 0.5, mx + mr * 0.1, my],
                 fill=(120, 118, 110))


def art_cyber(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(16, 20, 34))
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    f = font_sans(13, 700)
    for i, txt in enumerate(["01", "10", "01", "11"]):
        draw.text((x0 + 6 + i * 22, y0 + 6), txt, font=f, fill=(60, 90, 140))
        draw.text((x0 + 6 + i * 22, y1 - 20), txt, font=f, fill=(60, 90, 140))
    # shield
    draw.polygon([(cx, cy - 22), (cx + 20, cy - 14), (cx + 20, cy + 2),
                  (cx, cy + 18), (cx - 20, cy + 2), (cx - 20, cy - 14)],
                 fill=(29, 78, 121), outline=(140, 190, 255))
    draw.rectangle([cx - 3, cy - 6, cx + 3, cy + 4], fill=(255, 255, 255))
    draw.ellipse([cx - 5, cy - 11, cx + 5, cy - 1], fill=(255, 255, 255))


def art_oil(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(240, 226, 196))
    cx = (x0 + x1) // 2
    # derrick
    draw.polygon([(cx - 26, y1 - 8), (cx - 8, y0 + 12), (cx + 8, y0 + 12),
                  (cx + 26, y1 - 8)], outline=(25, 23, 19), width=3)
    draw.line([(cx - 18, y1 - 30), (cx + 18, y1 - 30)], fill=(25, 23, 19), width=2)
    draw.line([(cx - 12, y0 + 30), (cx + 12, y0 + 30)], fill=(25, 23, 19), width=2)
    # barrel
    draw.rounded_rectangle([x1 - 34, y1 - 30, x1 - 10, y1 - 8], radius=3,
                           fill=(163, 19, 19))
    draw.line([(x1 - 34, y1 - 22), (x1 - 10, y1 - 22)], fill=(120, 14, 14), width=2)
    # flame
    draw.polygon([(x0 + 12, y0 + 26), (x0 + 20, y0 + 12), (x0 + 28, y0 + 26)],
                 fill=(255, 140, 40))


def art_gavel(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(238, 234, 222))
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    w = x1 - x0
    hw = w * 0.21
    # gavel head
    draw.rounded_rectangle([cx - hw, cy - 22, cx + hw, cy - 6], radius=5,
                           fill=(90, 66, 30))
    draw.rectangle([cx - hw - 4, cy - 22, cx - hw + 4, cy - 6], fill=(60, 44, 20))
    draw.rectangle([cx + hw - 4, cy - 22, cx + hw + 4, cy - 6], fill=(60, 44, 20))
    # handle
    draw.line([(cx, cy - 6), (cx + 14, cy + 26)], fill=(90, 66, 30), width=5)
    # sound block
    draw.rectangle([cx - hw, cy + 26, cx + hw, cy + 34], fill=(120, 96, 60))
    # dollar tag
    f = font_serif(22)
    draw.text((x0 + 6, y0 + 4), "$", font=f, fill=(146, 106, 24))


def art_film(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(30, 28, 26))
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    w = x1 - x0
    hw = w * 0.26
    # clapperboard
    draw.rectangle([cx - hw, cy - 18, cx + hw, cy + 22], fill=(255, 253, 246),
                   outline=(25, 23, 19), width=2)
    for i in range(4):
        x = cx - hw + i * (2 * hw / 4)
        draw.polygon([(x, cy - 18), (x + 2 * hw / 8, cy - 18),
                      (x + 2 * hw / 4, cy - 30), (x + 2 * hw / 8, cy - 30)],
                     fill=(25, 23, 19) if i % 2 == 0 else (255, 253, 246))
    draw.rectangle([cx - hw, cy - 32, cx + hw, cy - 18], outline=(25, 23, 19))
    draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=(163, 19, 19))
    draw.polygon([(cx - 4, cy - 5), (cx - 4, cy + 5), (cx + 6, cy)], fill=(255, 255, 255))


def art_ballot(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(232, 238, 240))
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    w = x1 - x0
    hw = w * 0.24
    # ballot paper going in
    draw.polygon([(cx - hw * 0.45, cy - 34), (cx + hw * 0.3, cy - 34),
                  (cx + hw * 0.05, cy - 8), (cx - hw * 0.65, cy - 8)],
                 fill=(255, 255, 255), outline=(29, 78, 121))
    draw.line([(cx - hw * 0.4, cy - 28), (cx + hw * 0.15, cy - 28)],
              fill=(163, 19, 19), width=2)
    draw.line([(cx - hw * 0.4, cy - 22), (cx + hw * 0.05, cy - 22)],
              fill=(163, 19, 19), width=2)
    # box
    draw.rectangle([cx - hw, cy - 8, cx + hw, cy + 30], fill=(29, 78, 121))
    draw.rectangle([cx - hw - 4, cy - 12, cx + hw + 4, cy - 6], fill=(20, 58, 92))
    # check mark
    draw.line([(cx - hw * 0.45, cy + 10), (cx - hw * 0.12, cy + 20),
               (cx + hw * 0.5, cy - 2)], fill=(255, 255, 255), width=4)


def art_blast(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(40, 32, 26))
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    import math
    r0 = min(x1 - x0, y1 - y0) // 2 - 4
    for r, col in [(r0, (255, 140, 40)), (r0 * 0.72, (255, 200, 60)),
                   (r0 * 0.42, (255, 240, 150))]:
        pts = []
        for i in range(16):
            ang = math.pi * i / 8
            rr = r if i % 2 == 0 else r * 0.55
            pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
        draw.polygon(pts, fill=col)
    for sx, sy, sr in [(x0 + 10, y0 + 10, 7), (x1 - 12, y1 - 12, 8), (x0 + 12, y1 - 10, 6)]:
        draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(120, 116, 108))


ART = {
    "rocket": art_rocket, "asteroid": art_asteroid, "pharma": art_pharma,
    "server": art_server, "ship": art_ship, "aid": art_aid, "bank": art_bank,
    "radar": art_radar, "mine": art_mine, "cyber": art_cyber, "oil": art_oil,
    "gavel": art_gavel, "film": art_film, "ballot": art_ballot,
    "blast": art_blast,
}


# ---------------------------------------------------------------- world map
# Simplified continent outlines in lon/lat, drawn equirectangular.

CONTINENTS = [
    # North America
    [(-168, 66), (-140, 70), (-125, 71), (-110, 68), (-95, 69), (-85, 66),
     (-80, 73), (-65, 60), (-55, 52), (-60, 47), (-70, 44), (-75, 39),
     (-80, 32), (-85, 29), (-90, 21), (-97, 16), (-105, 20), (-110, 23),
     (-117, 32), (-125, 40), (-125, 49), (-135, 58), (-150, 60), (-165, 60)],
    # Greenland
    [(-45, 60), (-30, 68), (-20, 70), (-30, 76), (-55, 76), (-58, 70)],
    # South America
    [(-80, 10), (-75, 5), (-60, 0), (-50, 0), (-35, -8), (-40, -20),
     (-48, -28), (-58, -38), (-65, -45), (-70, -54), (-73, -40), (-73, -20),
     (-80, -5)],
    # Africa
    [(-17, 15), (-10, 30), (0, 35), (10, 37), (20, 32), (32, 31), (35, 28),
     (43, 12), (51, 11), (48, 0), (40, -10), (35, -20), (30, -35), (20, -35),
     (15, -27), (12, -18), (8, -2), (9, 4), (-8, 5)],
    # Eurasia
    [(-10, 36), (-9, 43), (-2, 48), (0, 50), (5, 53), (8, 57), (18, 56),
     (21, 55), (28, 60), (30, 70), (40, 68), (55, 69), (70, 72), (90, 75),
     (110, 76), (130, 72), (150, 70), (170, 66), (178, 65), (170, 60),
     (162, 55), (158, 50), (142, 45), (140, 40), (130, 35), (127, 33),
     (120, 28), (110, 20), (105, 10), (100, 8), (95, 15), (90, 22), (80, 13),
     (77, 8), (72, 20), (66, 25), (60, 25), (57, 26), (52, 28), (50, 30),
     (48, 29), (44, 29), (40, 36), (36, 36), (30, 36), (26, 38), (23, 36),
     (19, 40), (15, 44), (12, 44), (8, 44), (3, 43), (-2, 37), (-9, 37)],
    # UK
    [(-5, 50), (-3, 53), (-5, 56), (-2, 58), (0, 53), (1, 51)],
    # Japan
    [(130, 31), (133, 34), (137, 35), (140, 38), (141, 42), (143, 44),
     (141, 45), (139, 41), (136, 37), (132, 33)],
    # Australia
    [(114, -22), (114, -30), (115, -35), (120, -34), (129, -32), (132, -32),
     (135, -35), (140, -38), (145, -38), (150, -37), (153, -32), (153, -27),
     (150, -23), (146, -19), (142, -15), (142, -11), (137, -12), (135, -15),
     (130, -13), (126, -14), (122, -17), (118, -20)],
    # SE Asia islands
    [(95, 5), (100, 0), (105, -5), (110, -7), (115, -8), (120, -10),
     (125, -9), (130, -3), (135, -4), (140, -8), (138, -2), (132, 0),
     (128, 2), (122, 0), (118, 0), (112, -2), (106, 0), (100, 2)],
    # New Zealand
    [(167, -45), (170, -43), (174, -41), (178, -38), (176, -35), (173, -35),
     (170, -40)],
]

LAT_TOP, LAT_BOT = 84, -58


def project(lon, lat, box):
    x0, y0, x1, y1 = box
    x = x0 + (lon + 180.0) / 360.0 * (x1 - x0)
    y = y0 + (LAT_TOP - lat) / (LAT_TOP - LAT_BOT) * (y1 - y0)
    return (x, y)


def draw_map(draw, box, pins):
    """pins: list of (number, lon, lat)."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(214, 230, 238))
    # graticule
    for lon in range(-150, 181, 30):
        px, _ = project(lon, 0, box)
        draw.line([(px, y0), (px, y1)], fill=(190, 208, 220), width=1)
    for lat in range(-30, 61, 30):
        _, py = project(0, lat, box)
        draw.line([(x0, py), (x1, py)], fill=(190, 208, 220), width=1)
    # continents
    for poly in CONTINENTS:
        pts = [project(lon, lat, box) for lon, lat in poly]
        draw.polygon(pts, fill=(196, 188, 164), outline=(120, 110, 88))
    # pins
    fnum = font_sans(10, 700)
    placed = []
    for n, lon, lat in pins:
        px, py = project(lon, lat, box)
        # nudge overlapping pins apart (Berlin x2, Washington x2)
        for (ox, oy) in placed:
            if abs(px - ox) < 14 and abs(py - oy) < 14:
                px += 13
                py -= 10
        placed.append((px, py))
        draw.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED,
                     outline=(255, 255, 255), width=1)
        tw = draw.textlength(str(n), font=fnum)
        draw.text((px - tw / 2, py - 6), str(n), font=fnum, fill=(255, 255, 255))


# ---------------------------------------------------------------- layout

def section_head(draw, x, y, w, text, right=""):
    f = font_cond(16)
    draw.rectangle([x, y, x + w, y + 18], fill=INK)
    draw.text((x + 8, y + 1), spaced(text.upper()), font=f, fill=(255, 255, 255))
    if right:
        fr = font_sans(10, 600)
        tw = draw.textlength(right, font=fr)
        draw.text((x + w - tw - 8, y + 4), right, font=fr, fill=(220, 215, 200))
    return y + 20


def render():
    from stories import (LEADS, MEDIUM, BRIEFS, NUMBERS, TIMELINE,
                         DATE_CHECK, DATE_CHECK_NOT_YET, TOTAL_STORIES)

    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 12  # margin

    # ---- masthead
    y = 8
    fk = font_cond(16)
    kicker = spaced("WEDNESDAY  ·  25 NOVEMBER 2026  ·  ONE PAGE  ·  ALL DRAWN, NO PHOTOS")
    tw = d.textlength(kicker, font=fk)
    d.text(((W - tw) / 2, y), kicker, font=fk, fill=MUTED)
    y += 20
    fname = font_serif(50)
    name = "THE WORLD IN ONE DAY"
    tw = d.textlength(name, font=fname)
    d.text(((W - tw) / 2, y), name, font=fname, fill=INK)
    y += 56
    d.line([(M, y), (W - M, y)], fill=RULE, width=3)
    d.line([(M, y + 4), (W - M, y + 4)], fill=RULE, width=1)
    y += 9
    fcount = font_sans(12, 700)
    counts = ("48 STORIES  ·  7 REGIONS  ·  NORTH AMERICA 6  ·  EUROPE 11  ·  "
              "MIDDLE EAST 8  ·  ASIA-PACIFIC 18  ·  LATIN AMERICA 1  ·  SPACE 2  ·  GLOBAL 2")
    tw = d.textlength(counts, font=fcount)
    d.text(((W - tw) / 2, y), counts, font=fcount, fill=RED)
    y += 18
    d.line([(M, y), (W - M, y)], fill=CARD_LINE, width=1)
    y += 5

    # ---- leads: 4 across
    y = section_head(d, M, y, W - 2 * M, "Top of the day",
                     "4 LEADS · ALL CONFIRMED")
    col_w = (W - 2 * M - 3 * 8) // 4
    lead_h = 168
    ftag = font_sans(9, 700)
    fhead = font_serif(18)
    fsum = font_sans(10, 400)
    for i, s in enumerate(LEADS):
        x = M + i * (col_w + 8)
        rrect(d, [x, y, x + col_w, y + lead_h], 3, fill=PAPER_CARD,
              outline=CARD_LINE, width=1)
        art_box = (x + 5, y + 5, x + col_w - 5, y + 70)
        ART[s["art"]](d, art_box)
        d.rectangle([x + 5, y + 70, x + col_w - 5, y + 71], fill=CARD_LINE)
        tx = x + 8
        ty = y + 75
        tag = "%d · %s · %s" % (s["n"], s["region"], s["field"])
        d.text((tx, ty), tag, font=ftag, fill=RED)
        lab = s["label"]
        lw = d.textlength(lab, font=ftag)
        d.text((x + col_w - 8 - lw, ty), lab, font=ftag, fill=BLUE)
        ty += 12
        ty = draw_wrapped(d, tx, ty, s["headline"], fhead, col_w - 16, INK,
                          leading=18, max_lines=2)
        ty += 1
        ty = draw_wrapped(d, tx, ty, s["summary"], fsum, col_w - 16, MUTED,
                          leading=11, max_lines=2)
        fsrc = font_sans(8, 600)
        d.text((tx, y + lead_h - 13), "SOURCE: " + s["source"], font=fsrc,
               fill=FAINT)
    y += lead_h + 6

    # ---- medium cards: 4 cols x 3 rows
    y = section_head(d, M, y, W - 2 * M, "More of the day",
                     "12 STORIES · NUMBERED 5–16")
    med_h = 90
    fmed_head = font_sans(12, 700)
    fmed_sum = font_sans(9, 400)
    for row in range(3):
        for col in range(4):
            s = MEDIUM[row * 4 + col]
            x = M + col * (col_w + 8)
            yy = y + row * (med_h + 6)
            rrect(d, [x, yy, x + col_w, yy + med_h], 3, fill=PAPER_CARD,
                  outline=CARD_LINE, width=1)
            abox = (x + 5, yy + 5, x + 61, yy + 61)
            ART[s["art"]](d, abox)
            tx = x + 67
            tw_ = col_w - 67 - 6
            ty = yy + 5
            tag = "%d · %s" % (s["n"], s["region"])
            d.text((tx, ty), tag, font=ftag, fill=RED)
            ty += 12
            ty = draw_wrapped(d, tx, ty, s["headline"], fmed_head, tw_, INK,
                              leading=14, max_lines=2)
            ty = draw_wrapped(d, tx, ty, s["summary"], fmed_sum, tw_, MUTED,
                              leading=11, max_lines=3)
            lab = "%s · %s" % (s["label"], s["source"])
            d.text((tx, yy + med_h - 12), lab, font=font_sans(8, 600),
                   fill=FAINT)
    y += 3 * med_h + 2 * 6 + 6

    # ---- map
    y = section_head(d, M, y, W - 2 * M, "Where it happened",
                     "PINS 1–16 MATCH THE STORY NUMBERS")
    map_h = 78
    pins = [(s["n"], s["pin"][0], s["pin"][1]) for s in LEADS + MEDIUM]
    # nudge the two Berlin pins and two Washington pins apart via draw_map
    draw_map(d, (M, y, W - M, y + map_h), pins)
    y += map_h + 6

    # ---- briefs: 4 cols x 8 rows, one line each
    y = section_head(d, M, y, W - 2 * M, "Also on 25 November",
                     "32 MORE STORIES · 17–48")
    fbrief = font_sans(10, 400)
    fbrief_n = font_sans(10, 700)
    fbrief_s = font_sans(8, 600)
    for row in range(8):
        for col in range(4):
            n, text, label, source, region = BRIEFS[row * 4 + col]
            x = M + col * (col_w + 8)
            yy = y + row * 12
            d.text((x, yy), "%d." % n, font=fbrief_n, fill=RED)
            nw = d.textlength("%d. " % n, font=fbrief_n)
            sw = d.textlength(source, font=fbrief_s)
            avail = col_w - nw - sw - 10
            t = trunc(d, text, fbrief, avail)
            d.text((x + nw, yy), t, font=fbrief, fill=INK)
            d.text((x + col_w - sw, yy), source, font=fbrief_s, fill=FAINT)
    y += 8 * 12 + 5

    # ---- numbers strip
    d.rectangle([M, y, W - M, y + 36], fill=INK)
    fnum_v = font_serif(14)
    fnum_l = font_sans(8, 600)
    seg_w = (W - 2 * M) / 5
    # two rows of five inside the strip: value on top, label below
    for i, (val, lab) in enumerate(NUMBERS):
        cx = M + (i % 5) * seg_w
        cy = y + (i // 5) * 18
        d.text((cx + 8, cy + 2), val, font=fnum_v, fill=(255, 220, 120))
        vw = d.textlength(val, font=fnum_v)
        d.text((cx + 12 + vw, cy + 5), lab, font=fnum_l, fill=(220, 215, 200))
    y += 42

    # ---- timeline + date check side by side
    half = (W - 2 * M - 8) // 2
    y0 = y
    # left: timeline
    yy = section_head(d, M, y, half, "The day in UTC", "")
    ftime = font_sans(10, 700)
    for t, txt in TIMELINE:
        d.text((M, yy), t, font=ftime, fill=RED)
        d.text((M + 74, yy), txt, font=fbrief, fill=INK)
        yy += 12
    # right: date check
    xr = M + half + 8
    yy2 = section_head(d, xr, y, half, "Date check — left out on purpose", "")
    for title, when in DATE_CHECK[:5]:
        line = "× " + title + " — " + when
        d.text((xr, yy2), trunc(d, line, fbrief, half - 4), font=fbrief,
               fill=MUTED)
        yy2 += 12
    d.text((xr, yy2), "Not yet: OPEC+ Sun 29 Nov · Cygnus NG-25 Sun 29 Nov",
           font=fbrief_s, fill=FAINT)
    y = max(yy, yy2) + 10

    # ---- footer
    d.line([(M, y), (W - M, y)], fill=RULE, width=2)
    y += 5
    ffoot = font_sans(9, 400)
    foot = ("SOURCES: REUTERS · AP · AFP · CNBC · ESA · CMSA · FTC · WSJ · BSE · "
            "BUSINESSLINE · THE GERMANY EYE · SANGAKU-JOURNAL · ALL ILLUSTRATIONS "
            "DRAWN FOR THIS PAGE — NO PHOTOGRAPHS · LABELS: CONFIRMED / REPORTED / "
            "CLAIM / OFFICIAL / FORECAST")
    y = draw_wrapped(d, M, y, foot, ffoot, W - 2 * M, MUTED, leading=10,
                     max_lines=2)
    y += 3
    fend = font_cond(13)
    end = spaced("THE WORLD IN ONE DAY  ·  WEDNESDAY 25 NOVEMBER 2026  ·  48 STORIES  ·  END")
    tw = d.textlength(end, font=fend)
    d.text(((W - tw) / 2, y), end, font=fend, fill=MUTED)
    y += 15

    if y > H:
        print("WARNING: content overflows by %d px" % (y - H), file=sys.stderr)
    return img


def main():
    img = render()
    out = os.path.join(HERE, "entry.png")
    img.save(out, optimize=True)
    size = os.path.getsize(out)
    print("wrote %s %d bytes %s" % (out, size, img.size))
    if size > 1048576:
        print("WARNING: over 1 MiB", file=sys.stderr)


if __name__ == "__main__":
    main()
