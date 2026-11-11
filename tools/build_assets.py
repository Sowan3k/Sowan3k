#!/usr/bin/env python3
"""Draws every graphic in assets/ for the profile README.

Run from the repo root:  python3 tools/build_assets.py

Everything is plain SVG with CSS animation, so GitHub can show it as an image.
Each graphic comes in two widths: 880 for desktop and 440 for phones.

Text is set in Times New Roman. If Pillow and Liberation Serif (which has the
same letter widths) are installed, every line is measured and pinned to that
width, so a phone without Times New Roman cannot push text out of its box.
"""
import glob
import html
import pathlib
import random

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"

# Palette: near-black cards, GitHub's contribution greens.
BG, PANEL, EMPTY, TEXTCELL, LINE = "#09090b", "#101013", "#1a1a1f", "#26262c", "#27272a"
FG, SOFT, MUTED, DIM = "#fafafa", "#d4d4d8", "#a1a1aa", "#71717a"
G1, G2, G3, G4, HI = "#0e4429", "#006d32", "#26a641", "#38e062", "#b9f6ca"
CHIPBG = "#0f2a17"
FONT = "'Times New Roman', Times, 'Liberation Serif', 'Nimbus Roman', serif"

# ---------------------------------------------------------------- text ----

try:
    from PIL import ImageFont

    def _find(name):
        hits = glob.glob(f"/usr/share/fonts/**/{name}", recursive=True)
        return hits[0] if hits else None

    _FILES = {
        (False, False): _find("LiberationSerif-Regular.ttf"),
        (True, False): _find("LiberationSerif-Bold.ttf"),
        (False, True): _find("LiberationSerif-Italic.ttf"),
        (True, True): _find("LiberationSerif-BoldItalic.ttf"),
    }
    _CACHE = {}

    def measure(s, size, b=False, i=False, ls=0.0):
        path = _FILES.get((b, i))
        if not path:
            return 0.0
        key = (path, 200)
        if key not in _CACHE:
            _CACHE[key] = ImageFont.truetype(path, 200)
        return _CACHE[key].getlength(s) * size / 200 + ls * len(s)

except Exception:  # Pillow missing: text is left to flow naturally.

    def measure(s, size, b=False, i=False, ls=0.0):
        return 0.0


def esc(s):
    return html.escape(str(s), quote=True)


def n(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def T(x, y, s, size, *, b=False, i=False, fill=FG, anchor="start", ls=0.0, cls="", extra=""):
    """One line of text. Returns (svg, width)."""
    w = measure(s, size, b, i, ls)
    a = f'x="{n(x)}" y="{n(y)}" font-size="{n(size)}" fill="{fill}"'
    if b:
        a += ' font-weight="700"'
    if i:
        a += ' font-style="italic"'
    if ls:
        a += f' letter-spacing="{n(ls)}"'
    if anchor != "start":
        a += f' text-anchor="{anchor}"'
    if w:
        a += f' textLength="{n(w)}" lengthAdjust="spacingAndGlyphs"'
    if cls:
        a += f' class="{cls}"'
    if extra:
        a += " " + extra
    return f"<text {a}>{esc(s)}</text>", (w or size * 0.46 * len(s) + ls * len(s))


def t(*args, **kw):
    return T(*args, **kw)[0]


def cell(x, y, size, fill=None, cls="", style="", rx=None):
    a = f'x="{n(x)}" y="{n(y)}" width="{n(size)}" height="{n(size)}" rx="{n(rx if rx is not None else size * 0.24)}"'
    if fill:
        a += f' fill="{fill}"'
    if cls:
        a += f' class="{cls}"'
    if style:
        a += f' style="{style}"'
    return f"<rect {a}/>"


def doc(w, h, title, desc, css, body, defs="", glow=True):
    g = (
        f'<g clip-path="url(#card)"><circle cx="{w - 60}" cy="0" r="{min(300, int(w * 0.62))}" fill="url(#glow)"/></g>'
        if glow
        else ""
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t d">
<title id="t">{esc(title)}</title>
<desc id="d">{esc(desc)}</desc>
<defs>
<clipPath id="card"><rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="15"/></clipPath>
<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{G4}" stop-opacity="0.10"/><stop offset="1" stop-color="{G4}" stop-opacity="0"/></radialGradient>
<linearGradient id="pulse" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{G4}" stop-opacity="0"/><stop offset="0.8" stop-color="{G4}"/><stop offset="1" stop-color="{HI}"/></linearGradient>
{defs}</defs>
<style>
text {{ font-family: {FONT}; }}
.pulse {{ animation: pulse 2s ease-in-out infinite; }}
@keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: .3; }} }}
{css}
@media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} .motion {{ display: none; }} }}
</style>
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="15" fill="{BG}"/>
{g}
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="15" fill="none" stroke="{LINE}"/>
{body}
</svg>
"""


def chip(x_right, y, label, dot=False, left=None):
    """A small green pill. Anchored by its right edge, or its left edge if given."""
    txt, w = T(0, 0, label, 11, b=True, fill=G4, ls=1.5)
    pad = 28 if dot else 16
    pw = w + pad + 14
    x = left if left is not None else x_right - pw
    out = [f'<rect x="{n(x)}" y="{n(y)}" width="{n(pw)}" height="26" rx="13" fill="{CHIPBG}" stroke="{G4}" stroke-opacity="0.35"/>']
    if dot:
        out.append(f'<circle class="pulse" cx="{n(x + 15)}" cy="{n(y + 13)}" r="3.2" fill="{G4}"/>')
    out.append(t(x + pad, y + 17.2, label, 11, b=True, fill=G4, ls=1.5))
    return "\n".join(out)


# ---------------------------------------------------------------- hero ----

GLYPH = {
    "S": [".###.", "#...#", "#....", ".###.", "....#", "#...#", ".###."],
    "O": [".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "W": ["#...#", "#...#", "#...#", "#.#.#", "#.#.#", "#.#.#", ".#.#."],
    "A": [".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "N": ["#...#", "##..#", "##..#", "#.#.#", "#..##", "#..##", "#...#"],
}

ROTATE = [
    ("DocIntel", "invoices read by Gemini, checked in Python"),
    ("BahasaBot", "a Malay tutor that won Silver at PIXEL 2026"),
    ("Virtual Zara", "an n8n agent across five business systems"),
    ("ChargeWatch", "Android battery alerts with no backend"),
]


def hero(narrow=False):
    rng = random.Random(11)
    if narrow:
        W, H = 440, 448
        cols, pitch, size, start = 35, 12, 9.5, 1
        gx, gy = (W - (cols * pitch - (pitch - size))) / 2, 284
    else:
        W, H = 880, 424
        cols, pitch, size, start = 41, 19, 15, 4
        gx, gy = 70, 180
    rx = size * 0.25

    name_cells, count = [], 0
    for li, ch in enumerate("SOWAN"):
        for r, row in enumerate(GLYPH[ch]):
            for c, bit in enumerate(row):
                if bit != "#":
                    continue
                col = start + li * 7 + c
                lvl = rng.choices([4, 3], [84, 16])[0]
                t0 = 0.5 + (col - start) * 0.08 + r * 0.025
                tw = 5 + (col - start + r) * 0.07
                name_cells.append(
                    cell(gx + col * pitch, gy + r * pitch, size, cls=f"n l{lvl}", style=f"animation-delay:{t0:.2f}s,{tw:.2f}s", rx=rx)
                )
                count += 1

    noise = []
    if not narrow:
        edge = [(c, r) for c in (0, 1, 39, 40) for r in range(7)]
        for k, (c, r) in enumerate(rng.sample(edge, 8)):
            fill = (G1, G2, G1, G1)[k % 4]
            noise.append(cell(gx + c * pitch, gy + r * pitch, size, fill=fill, cls="noise", style=f"animation-delay:{(k * 0.9) % 6:.1f}s", rx=rx))

    grid_w = cols * pitch - (pitch - size)
    sweep_x = gx + start * pitch - 5
    body = []

    if narrow:
        body.append(t(24, 46, "SOFTWARE ENGINEER · DHAKA, UTC+6", 11.5, b=True, fill=G4, ls=2.2))
        body.append(chip(0, 62, "OPEN TO AI ENGINEERING ROLES", dot=True, left=24))
        body.append(t(22, 144, "Noor Mohammad", 43, b=True))
        body.append(t(22, 188, "Sowan", 43, b=True, i=True, fill=G4))
        body.append(t(24, 222, "I build AI automation and the", 18, fill=SOFT))
        body.append(t(24, 245, "full-stack systems around it.", 18, fill=SOFT))
    else:
        body.append(t(40, 50, "SOFTWARE ENGINEER · DHAKA, UTC+6", 12.5, b=True, fill=G4, ls=2.6))
        body.append(chip(W - 40, 31, "OPEN TO AI ENGINEERING ROLES", dot=True))
        s1, w1 = T(38, 106, "Noor Mohammad", 46, b=True)
        body.append(s1)
        body.append(t(38 + w1 + 13, 106, "Sowan", 46, b=True, i=True, fill=G4))
        body.append(t(40, 138, "I build AI automation and the full-stack systems around it.", 18.5, fill=SOFT))
        months = ["Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
        for k, m in enumerate(months):
            body.append(t(gx + round(k * 4.75) * pitch, gy - 10, m, 12, fill=DIM))
        for r, d in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
            body.append(t(40, gy + r * pitch + 12, d, 12, fill=DIM))

    body.append(f'<rect x="{n(gx)}" y="{n(gy)}" width="{n(cols * pitch)}" height="{n(7 * pitch)}" fill="url(#grid)"/>')
    body += noise + name_cells
    body.append(
        f'<rect class="sweep motion" x="{n(sweep_x)}" y="{n(gy - 6)}" width="3" height="{n(7 * pitch + 7)}" rx="1.5" fill="{HI}"/>'
    )

    ly = gy + 7 * pitch + (17 if narrow else 20)
    right = gx + grid_w
    more, mw = T(right, ly, "More", 12, fill=DIM, anchor="end")
    body.append(more)
    lx = right - mw - 8
    for k, fill in enumerate((G4, G3, G2, G1, EMPTY)):
        lx -= 11
        body.append(cell(lx, ly - 10, 11, fill=fill, rx=2.6))
        lx -= 4
    body.append(t(lx - 4, ly, "Less", 12, fill=DIM, anchor="end"))

    line1 = f"{count} squares, drawn by a script in this repo."
    if narrow:
        body.append(t(24, ly + 30, line1, 13.5, i=True, fill=MUTED))
        body.append(t(24, ly + 49, "No backdated commits.", 13.5, i=True, fill=MUTED))
    else:
        body.append(t(gx, ly, line1 + " No backdated commits.", 13.5, i=True, fill=MUTED))
        ry = H - 30
        body.append(f'<path d="M40 {ry - 9} l7 4.5 l-7 4.5 z" fill="{G4}"/>')
        for k, (name, what) in enumerate(ROTATE):
            s, w = T(56, ry, name, 15, b=True)
            body.append(f'<g class="rot{" r1" if k == 0 else ""}" style="animation-delay:{k * 4}s">{s}{t(56 + w + 7, ry, what, 15, fill=MUTED)}</g>')

    css = f"""
.n {{ transform-box: fill-box; transform-origin: center; animation: pop .55s cubic-bezier(.2,1.5,.4,1) backwards, wave4 7s linear infinite; }}
.l4 {{ fill: {G4}; }}
.l3 {{ fill: {G3}; animation-name: pop, wave3; }}
.l2 {{ fill: {G2}; animation-name: pop, wave2; }}
@keyframes pop {{ 0% {{ opacity: 0; transform: scale(.2); }} 60% {{ opacity: 1; transform: scale(1.18); fill: {HI}; }} 100% {{ opacity: 1; transform: scale(1); }} }}
@keyframes wave4 {{ 0%, 9%, 100% {{ fill: {G4}; }} 4% {{ fill: {HI}; }} }}
@keyframes wave3 {{ 0%, 9%, 100% {{ fill: {G3}; }} 4% {{ fill: #7ee2a0; }} }}
@keyframes wave2 {{ 0%, 9%, 100% {{ fill: {G2}; }} 4% {{ fill: {G3}; }} }}
.noise {{ animation: tw 6s ease-in-out infinite; }}
@keyframes tw {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: .3; }} }}
.sweep {{ animation: sw 2.9s .45s linear both; }}
@keyframes sw {{ 0% {{ transform: translateX(0); opacity: 0; }} 6%, 94% {{ opacity: .85; }} 100% {{ transform: translateX({n(33 * pitch + 4)}px); opacity: 0; }} }}
.rot {{ opacity: 0; animation: rot 16s linear infinite backwards; }}
.r1 {{ opacity: 1; }}
@keyframes rot {{ 0% {{ opacity: 0; transform: translateY(5px); }} 3%, 22% {{ opacity: 1; transform: translateY(0); }} 25%, 100% {{ opacity: 0; transform: translateY(-5px); }} }}
"""
    defs = f'<pattern id="grid" x="{n(gx)}" y="{n(gy)}" width="{pitch}" height="{pitch}" patternUnits="userSpaceOnUse"><rect width="{size}" height="{size}" rx="{n(rx)}" fill="#151519"/></pattern>'
    desc = (
        "Software engineer in Dhaka, open to AI engineering roles. I build AI automation and the full-stack systems "
        "around it. A contribution graph whose squares spell SOWAN."
    )
    return doc(W, H, "Noor Mohammad Sowan", desc, css, "\n".join(body), defs)


# -------------------------------------------------------------- banners ----

ICONS = {
    "about": ["..#..", ".###.", "..#..", ".###.", "#####"],
    "build": ["....#", "...##", "..###", ".####", "#####"],
    "featured": ["..#..", ".###.", "#####", ".###.", "..#.."],
    "more": ["##.##", "##.##", ".....", "##.##", "##.##"],
    "stack": ["#####", ".....", "#####", ".....", "#####"],
    "github": ["....#", "..#.#", "..#.#", "#.#.#", "#.#.#"],
    "contact": ["#####", "##.##", "#.#.#", "#...#", "#####"],
}


def banner(key, idx, title, narrow=False):
    W, H = (440, 52) if narrow else (880, 60)
    ix, iy = (16, 11) if narrow else (24, 15)
    body = []
    for r, row in enumerate(ICONS[key]):
        for c, bit in enumerate(row):
            body.append(cell(ix + c * 6, iy + r * 6, 5, fill=G4 if bit == "#" else EMPTY, rx=1.2))
    tx = ix + 42
    body.append(t(tx, H / 2 + 5, idx, 15, i=True, fill=G4))
    s, w = T(tx + 26, H / 2 + (8 if narrow else 9.5), title, 22 if narrow else 25, b=True)
    body.append(s)

    x0 = tx + 26 + w + 26
    pitch, size = 12, 7
    count = int((W - 24 - x0) // pitch)
    cy = H / 2 - size / 2
    for k in range(count):
        op = 0.12 + 0.88 * ((k + 1) / count) ** 1.6
        body.append(cell(x0 + k * pitch, cy, size, fill=G2, style=f"opacity:{op:.2f}", rx=1.8))
    css = ""
    if count > 3:
        dur = count * 0.11 + 2.2
        move = (count - 1) * pitch
        css = f"""
.run {{ animation: run {dur:.2f}s steps({count - 1}, end) infinite; }}
@keyframes run {{ 0% {{ transform: translateX(0); opacity: 0; }} 8% {{ opacity: 1; }} {int(100 * count * 0.11 / dur)}% {{ transform: translateX({move}px); opacity: 1; }} {int(100 * count * 0.11 / dur) + 4}%, 100% {{ transform: translateX({move}px); opacity: 0; }} }}
"""
        body.append(cell(x0, cy, size, fill=HI, cls="run motion", rx=1.8))
    return doc(W, H, title, f"Section {idx}: {title}", css, "\n".join(body), glow=False)


# --------------------------------------------------------------- method ----

STEPS = [
    ("Requirements", "what it must do", ["#######", "#.....#", "#.###.#", "#.....#", "#.###.#", "#.....#", "#######"]),
    ("Rules", "CLAUDE.md", ["..###..", ".#...#.", ".#...#.", "#######", "###.###", "###.###", "#######"]),
    ("Phases", "PHASES.md", [".....##", ".....##", "...####", "...####", ".######", ".######", "#######"]),
    ("Build", "Claude Code", [".......", "..#.#..", ".#...#.", "#.....#", ".#...#.", "..#.#..", "......."]),
    ("Log", "STATUS · DECISIONS", [".......", "#.#####", ".......", "#.#####", ".......", "#.#####", "......."]),
    ("Test, ship", "CI, then deploy", [".......", "......#", ".....##", "#...##.", "##.##..", ".###...", "..#...."]),
]


def method(narrow=False):
    if narrow:
        W, H = 440, 372
        centers = [(80 + (k % 3) * 140, 104 + (k // 3) * 152) for k in range(6)]
    else:
        W, H = 880, 212
        centers = [(92 + k * 139.2, 104) for k in range(6)]
    cycle = 7.0
    body = [t(24 if narrow else 40, 46, "SPEC FIRST, THEN PHASE BY PHASE", 11.5 if narrow else 12.5, b=True, fill=G4, ls=2.2 if narrow else 2.6)]
    if not narrow:
        body.append(t(W - 40, 46, "nothing gets built before it is written down", 14, i=True, fill=MUTED, anchor="end"))
        x0, x1 = centers[0][0], centers[-1][0]
        body.append(f'<path d="M{n(x0)} 104 H{n(x1)}" stroke="{LINE}" stroke-width="2"/>')
        body.append(
            f'<clipPath id="track"><rect x="{n(x0)}" y="100" width="{n(x1 - x0)}" height="8"/></clipPath>'
            f'<g clip-path="url(#track)"><rect class="runner motion" x="{n(x0 - 70)}" y="103" width="70" height="2" fill="url(#pulse)"/></g>'
        )
    span = centers[-1][0] - centers[0][0] if not narrow else 1
    for k, (title, sub, icon) in enumerate(STEPS):
        cx, cy = centers[k]
        delay = (centers[k][0] - centers[0][0]) / (span + 70) * cycle * 0.85 if not narrow else k * 1.0
        body.append(
            f'<rect class="pan" style="animation-delay:{delay:.2f}s" x="{n(cx - 29)}" y="{n(cy - 29)}" width="58" height="58" rx="12"/>'
        )
        for r, row in enumerate(icon):
            for c, bit in enumerate(row):
                if bit == "#":
                    body.append(cell(cx - 20.5 + c * 6, cy - 20.5 + r * 6, 5, cls="ic", style=f"animation-delay:{delay:.2f}s", rx=1.2))
        body.append(t(cx, cy - 37, f"0{k + 1}", 12.5, b=True, i=True, fill=G4, anchor="middle"))
        body.append(t(cx, cy + 51, title, 16.5, b=True, anchor="middle"))
        body.append(t(cx, cy + 70, sub, 13, i=True, fill=MUTED, anchor="middle"))
    css = f"""
.pan {{ fill: {PANEL}; stroke: {LINE}; stroke-width: 1.2; animation: pan {cycle}s linear infinite backwards; }}
.ic {{ fill: {G3}; animation: ic {cycle}s linear infinite backwards; }}
@keyframes pan {{ 0% {{ stroke: {LINE}; }} 2%, 16% {{ stroke: {G4}; }} 30%, 100% {{ stroke: {LINE}; }} }}
@keyframes ic {{ 0% {{ fill: {G3}; }} 2%, 16% {{ fill: {HI}; }} 30%, 100% {{ fill: {G3}; }} }}
.runner {{ animation: go {cycle}s linear infinite; }}
@keyframes go {{ 0% {{ transform: translateX(0); opacity: 1; }} 85% {{ transform: translateX({n(span + 70)}px); opacity: 1; }} 86%, 100% {{ transform: translateX({n(span + 70)}px); opacity: 0; }} }}
"""
    desc = "Six steps in order: requirements, rules in CLAUDE.md, phases in PHASES.md, build with Claude Code, log in STATUS.md and DECISIONS.md, then test in CI and ship."
    return doc(W, H, "How I build", desc, css, "\n".join(body), glow=False)


# ---------------------------------------------------------------- cards ----


def metrics(items, W, y, narrow, first_green=True):
    out = []
    if narrow:
        for k, (big, cap) in enumerate(items):
            x = 24 + (k % 2) * 200
            yy = y + (k // 2) * 62
            out.append(t(x, yy, big, 26, b=True, fill=G4 if (k == 0 and first_green) else FG))
            out.append(t(x, yy + 19, cap, 12.5, fill=MUTED))
    else:
        xs = [40, 250, 460, 670]
        for k, (big, cap) in enumerate(items):
            out.append(t(xs[k], y, big, 28, b=True, fill=G4 if (k == 0 and first_green) else FG))
            out.append(t(xs[k], y + 19, cap, 12.5, fill=MUTED))
    return out


def docintel(narrow=False):
    rng = random.Random(5)
    W, H = (440, 758) if narrow else (880, 362)
    L = 24 if narrow else 40
    body = []
    if narrow:
        body.append(t(L, 46, "FEATURED BUILD · NOVEMBER 2026", 11.5, b=True, fill=G4, ls=2.2))
        body.append(chip(0, 62, "BUILT IN 5 DAYS, ON A PHONE", left=L))
        body.append(t(L - 1, 136, "DocIntel", 40, b=True))
        body.append(t(L, 166, "Reads invoices from PDFs, scans,", 17.5, fill=SOFT))
        body.append(t(L, 188, "phone photos, Excel and CSV.", 17.5, fill=SOFT))
        body.append(t(L, 214, "Gemini reads the fields.", 17.5, i=True, fill=MUTED))
        body.append(t(L, 236, "Python checks every number.", 17.5, i=True, fill=MUTED))
        px, py, pw, ph, pitch, size, cols, rows = L, 256, 392, 104, 14, 9, 26, 6
    else:
        body.append(t(L, 50, "FEATURED BUILD · NOVEMBER 2026", 12.5, b=True, fill=G4, ls=2.6))
        body.append(chip(W - 40, 31, "BUILT IN 5 DAYS, ON A PHONE"))
        body.append(t(L - 1, 102, "DocIntel", 40, b=True))
        body.append(t(L, 131, "Reads invoices from PDFs, scans, phone photos, Excel and CSV.", 17.5, fill=SOFT))
        body.append(t(L, 154, "Gemini reads the fields. Python checks every number.", 17.5, i=True, fill=MUTED))
        px, py, pw, ph, pitch, size, cols, rows = 612, 72, 228, 92, 8, 5, 26, 9

    # The invoice: dim squares are text, brighter ones are the eight fields.
    ox = px + (pw - (cols * pitch - (pitch - size))) / 2
    oy = py + (ph - (rows * pitch - (pitch - size))) / 2
    body.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="10" fill="{PANEL}" stroke="{LINE}"/>')
    field_rows = [0, 1, 2, 3, 5, 6, 7, 8] if rows == 9 else [0, 1, 1, 2, 3, 4, 5, 5]
    fields, used = {}, {}
    for k, r in enumerate(field_rows):
        ln = rng.choice([3, 4, 5])
        left_side = used.get(r, 0) == 1
        c0 = rng.randint(1, 4) if left_side else cols - ln - rng.randint(0, 2)
        used[r] = used.get(r, 0) + 1
        for c in range(c0, c0 + ln):
            fields[(r, c)] = k
    cycle, t_start, t_len = 8.0, 0.4, 3.2
    css_rows = []
    for r in range(rows):
        p = (t_start + (r + 0.5) / rows * t_len) / cycle * 100
        css_rows.append(
            f".f{r} {{ animation: f{r} {cycle}s linear infinite; }}\n"
            f"@keyframes f{r} {{ 0%, {p:.1f}% {{ fill: #3a3a42; }} {p + 1.5:.1f}% {{ fill: {HI}; }} {p + 5:.1f}%, 90% {{ fill: {G4}; }} 95%, 100% {{ fill: #3a3a42; }} }}"
        )
        length = rng.randint(cols // 3, cols - 2)
        for c in range(cols):
            x, y = ox + c * pitch, oy + r * pitch
            if (r, c) in fields:
                body.append(cell(x, y, size, fill=G4, cls=f"f{r}", rx=size * 0.22))
            elif c < length and rng.random() > 0.22 and not any((r, cc) in fields for cc in (c - 1, c + 1)):
                body.append(cell(x, y, size, fill=TEXTCELL, rx=size * 0.22))
    move = rows * pitch - (pitch - size)
    body.append(
        f'<rect class="scan motion" x="{n(ox - 4)}" y="{n(oy - 2)}" width="{n(cols * pitch - (pitch - size) + 8)}" height="1.6" rx=".8" fill="{HI}"/>'
    )

    stages = [("Ingest", "PyMuPDF · OpenCV"), ("OCR", "Tesseract, vision"), ("Extract", "Gemini + evidence"), ("Validate", "11 Decimal rules"), ("Review, search", "queue · pgvector")]
    if narrow:
        body.append(t(W - L, py + ph + 20, "eight fields, each checked against its source", 12.5, i=True, fill=DIM, anchor="end"))
        y0 = py + ph + 38
        for k, (a, b_) in enumerate(stages):
            y = y0 + k * 42
            body.append(f'<rect class="box" style="animation-delay:{k * 0.9:.2f}s" x="{L}" y="{y}" width="{W - 2 * L}" height="34" rx="10"/>')
            body.append(t(L + 14, y + 22, a, 15.5, b=True))
            body.append(t(W - L - 14, y + 22, b_, 13, i=True, fill=MUTED, anchor="end"))
        my = y0 + 5 * 42 + 44
        body.append(f'<path d="M{L} {my - 34} H{W - L}" stroke="{LINE}"/>')
    else:
        body.append(t(W - 40, py + ph + 18, "eight fields, each checked against its source text", 12.5, i=True, fill=DIM, anchor="end"))
        body.append(f'<path d="M40 228 H840" stroke="{LINE}" stroke-width="2"/>')
        body.append(
            '<clipPath id="track"><rect x="40" y="224" width="800" height="8"/></clipPath>'
            '<g clip-path="url(#track)"><rect class="runner motion" x="-40" y="227" width="80" height="2" fill="url(#pulse)"/></g>'
        )
        for k, (a, b_) in enumerate(stages):
            x = 40 + k * 163
            body.append(f'<rect class="box" style="animation-delay:{k * 0.89:.2f}s" x="{x}" y="198" width="148" height="60" rx="10"/>')
            body.append(t(x + 14, 224, a, 15.5, b=True))
            body.append(t(x + 14, 243, b_, 12.5, i=True, fill=MUTED))
        my = 315
        body.append(f'<path d="M40 280 H840" stroke="{LINE}"/>')
    body += metrics(
        [("91 / 91", "synthetic invoices correct"), ("439", "tests in CI, 95% coverage"), ("12 / 12", "planted errors caught"), ("~$0.0015", "per invoice, paid tier")],
        W, my, narrow,
    )
    css = f"""
{chr(10).join(css_rows)}
.scan {{ animation: scan {cycle}s linear infinite; }}
@keyframes scan {{ 0%, 5% {{ transform: translateY(0); opacity: 0; }} 6% {{ opacity: .9; }} 45% {{ transform: translateY({n(move + 3)}px); opacity: .9; }} 46%, 100% {{ transform: translateY({n(move + 3)}px); opacity: 0; }} }}
.box {{ fill: {PANEL}; stroke: {LINE}; stroke-width: 1.2; animation: box 6s linear infinite backwards; }}
@keyframes box {{ 0% {{ stroke: {LINE}; }} 3%, 18% {{ stroke: {G4}; }} 34%, 100% {{ stroke: {LINE}; }} }}
.runner {{ animation: go 6s linear infinite; }}
@keyframes go {{ 0% {{ transform: translateX(0); opacity: 1; }} 80% {{ transform: translateX(880px); opacity: 1; }} 81%, 100% {{ transform: translateX(880px); opacity: 0; }} }}
"""
    desc = (
        "Reads invoices from PDFs, scans, phone photos, Excel and CSV. A scan line passes over an invoice and eight fields "
        "turn green. Pipeline: ingest, OCR, extract, validate, review and search. All fields correct on 91 of 91 synthetic "
        "invoices, 439 tests in CI with 95% coverage, 12 of 12 planted errors caught, about 0.0015 US dollars per invoice."
    )
    return doc(W, H, "DocIntel, an AI document intelligence system", desc, css, "\n".join(body))


def bahasabot(narrow=False):
    W, H = (440, 712) if narrow else (880, 362)
    L = 24 if narrow else 40
    body = []
    if narrow:
        body.append(t(L, 46, "FINAL-YEAR PROJECT", 11.5, b=True, fill=G4, ls=2.2))
        body.append(t(L, 64, "SILVER AWARD, PIXEL 2026", 11.5, b=True, fill=G4, ls=2.2))
        body.append(chip(0, 80, "LIVE DEMO", dot=True, left=L))
        body.append(t(L - 1, 154, "BahasaBot", 40, b=True))
        body.append(t(L, 184, "A Malay tutor for international", 17.5, fill=SOFT))
        body.append(t(L, 206, "students at Malaysian public", 17.5, fill=SOFT))
        body.append(t(L, 228, "universities.", 17.5, fill=SOFT))
        px, py, pw, ph, pitch, size = L, 250, 392, 104, 9.6, 7
    else:
        body.append(t(L, 50, "FINAL-YEAR PROJECT · SILVER AWARD, PIXEL 2026", 12.5, b=True, fill=G4, ls=2.6))
        body.append(chip(W - 40, 31, "LIVE DEMO", dot=True))
        body.append(t(L - 1, 102, "BahasaBot", 40, b=True))
        body.append(t(L, 131, "A Malay tutor for international students", 17.5, fill=SOFT))
        body.append(t(L, 154, "at Malaysian public universities.", 17.5, i=True, fill=MUTED))
        px, py, pw, ph, pitch, size = 540, 72, 300, 92, 6.9, 5

    # The race: 39 squares are 78 seconds, one square is the cached repeat.
    body.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="10" fill="{PANEL}" stroke="{LINE}"/>')
    ix = px + (pw - (39 * pitch - (pitch - size))) / 2
    r1, r2 = py + ph * 0.24, py + ph * 0.68
    body.append(t(ix, r1, "a new course", 13, i=True, fill=MUTED))
    body.append(t(px + pw - (ix - px), r1, "78 s", 13, b=True, anchor="end"))
    body.append(t(ix, r2, "the same topic again", 13, i=True, fill=MUTED))
    body.append(t(px + pw - (ix - px), r2, "280 ms", 13, b=True, fill=G4, anchor="end"))
    cycle, t0 = 10.0, 0.6
    frames = []
    for k in range(39):
        p = (t0 + k * 0.1) / cycle * 100
        frames.append(
            f".c{k} {{ animation: c{k} {cycle}s linear infinite; }}\n"
            f"@keyframes c{k} {{ 0%, {p:.1f}% {{ fill: {TEXTCELL}; }} {p + 0.8:.1f}% {{ fill: {HI}; }} {p + 3:.1f}%, 86% {{ fill: {G3}; }} 92%, 100% {{ fill: {TEXTCELL}; }} }}"
        )
        body.append(cell(ix + k * pitch, r1 + 8, size, fill=G3, cls=f"c{k}", rx=size * 0.22))
        if k:
            body.append(cell(ix + k * pitch, r2 + 8, size, fill=EMPTY, rx=size * 0.22))
    p = (t0 + 0.02) / cycle * 100
    frames.append(
        f".once {{ animation: once {cycle}s linear infinite; }}\n"
        f"@keyframes once {{ 0%, {p:.1f}% {{ fill: {TEXTCELL}; }} {p + 0.8:.1f}% {{ fill: {HI}; }} {p + 3:.1f}%, 86% {{ fill: {G4}; }} 92%, 100% {{ fill: {TEXTCELL}; }} }}"
    )
    body.append(cell(ix, r2 + 8, size, fill=G4, cls="once", rx=size * 0.22))

    feats = [("RAG chatbot", "LangChain · pgvector · SSE"), ("Course generator", "concurrent Gemini calls, cached"), ("Adaptive quiz", "BPS-1 to BPS-4, last 3 attempts")]
    items = [("78 s → 280 ms", "repeat course generation"), ("~$0.11", "est. cost per user a month"), ("4.3 / 5", "in-app rating, 30 users"), ("46 / 46", "functional tests passed")]
    if narrow:
        body.append(t(W - L, py + ph + 20, "played 20 times faster than it happened", 12.5, i=True, fill=DIM, anchor="end"))
        y0 = py + ph + 38
        for k, (a, b_) in enumerate(feats):
            y = y0 + k * 58
            body.append(f'<rect x="{L}" y="{y}" width="{W - 2 * L}" height="50" rx="10" fill="{PANEL}" stroke="{LINE}" stroke-width="1.2"/>')
            body.append(t(L + 14, y + 21, a, 15.5, b=True))
            body.append(t(L + 14, y + 39, b_, 12.5, i=True, fill=MUTED))
        dots = (W - L - 36, y0 + 16)
        my = y0 + 3 * 58 + 40
        body.append(f'<path d="M{L} {my - 34} H{W - L}" stroke="{LINE}"/>')
        big, cap = items[0]
        body.append(t(L, my, big, 26, b=True, fill=G4))
        body.append(t(L, my + 19, cap, 12.5, fill=MUTED))
        for k, (big, cap) in enumerate(items[1:]):
            x = L + (k % 3) * 134
            body.append(t(x, my + 62, big, 24, b=True))
            body.append(t(x, my + 80, cap.replace("est. cost per user a month", "per user a month").replace("in-app rating, 30 users", "rating, 30 users").replace("functional tests passed", "tests passed"), 12.5, fill=MUTED))
    else:
        body.append(t(W - 40, py + ph + 18, "played 20 times faster than it happened", 12.5, i=True, fill=DIM, anchor="end"))
        for k, (a, b_) in enumerate(feats):
            x = 40 + k * 272
            body.append(f'<rect x="{x}" y="198" width="256" height="60" rx="10" fill="{PANEL}" stroke="{LINE}" stroke-width="1.2"/>')
            body.append(t(x + 14, 224, a, 15.5, b=True))
            body.append(t(x + 14, 243, b_, 12.5, i=True, fill=MUTED))
        dots = (262, 219)
        body.append(f'<path d="M40 280 H840" stroke="{LINE}"/>')
        xs = [40, 285, 480, 670]
        for k, (big, cap) in enumerate(items):
            body.append(t(xs[k], 315, big, 28, b=True, fill=G4 if k == 0 else FG))
            body.append(t(xs[k], 334, cap, 12.5, fill=MUTED))
    for k in range(3):
        body.append(f'<circle class="dot" style="animation-delay:{k * 0.2:.1f}s" cx="{dots[0] + k * 9}" cy="{dots[1]}" r="2.6"/>')
    css = f"""
{chr(10).join(frames)}
.dot {{ fill: {G4}; animation: dot 1.4s ease-in-out infinite; }}
@keyframes dot {{ 0%, 60%, 100% {{ opacity: .25; }} 30% {{ opacity: 1; }} }}
"""
    desc = (
        "Final-year project, Silver Award at PIXEL 2026. A RAG chatbot, a course generator and an adaptive quiz. Two rows of "
        "squares race: a new course takes 78 seconds, the same topic again takes 280 milliseconds. Estimated cost about 0.11 "
        "US dollars per user per month. In-app rating 4.3 out of 5 from 30 users. 46 of 46 functional tests passed."
    )
    return doc(W, H, "BahasaBot, a Malay language learning platform", desc, css, "\n".join(body))


# ---------------------------------------------------------------- stack ----

BUILDS = ["DocIntel", "BahasaBot", "Vindeshi Express", "ChargeWatch", "Evently", "My Bibi", "Grab demo", "Virtual Zara"]
DI, BB, VE, CW, EV, MB, GR, VZ = range(8)
# Read off each project's dependency files. Virtual Zara comes from the internship letter.
STACK_A = [
    ("LANGUAGES", None),
    ("Python", [DI, BB, MB]),
    ("TypeScript", [DI, BB, VE, EV, MB]),
    ("JavaScript", [GR, VZ]),
    ("Kotlin", [CW]),
    ("AI AND AUTOMATION", None),
    ("Gemini API", [DI, BB]),
    ("LangChain", [BB]),
    ("pgvector", [DI, BB]),
    ("Tesseract · OpenCV", [DI]),
    ("Ollama", [MB]),
    ("n8n", [VZ]),
    ("OpenAI API", [VZ]),
    ("FRONTEND AND MOBILE", None),
    ("Next.js · React", [DI, BB, VE, EV, MB]),
    ("Tailwind CSS", [DI, BB, VE, EV, MB]),
    ("Android SDK", [CW]),
]
STACK_B = [
    ("BACKEND AND DATA", None),
    ("FastAPI", [DI, BB, MB]),
    ("PostgreSQL", [DI, BB, VE, EV]),
    ("SQLAlchemy", [DI, BB, MB]),
    ("Supabase", [DI]),
    ("Prisma", [VE, EV]),
    ("Redis", [BB]),
    ("SQLite", [MB]),
    ("Node.js · Express", [GR]),
    ("WebSocket", [GR]),
    ("TESTING AND DELIVERY", None),
    ("pytest", [DI]),
    ("Vitest · Playwright", [VE]),
    ("GitHub Actions", [DI, VE, CW]),
    ("Docker", [DI, BB, MB]),
    ("Vercel", [DI, BB, VE, EV]),
    ("Render", [DI, BB, GR]),
    ("Sentry", [BB]),
]


def stack(narrow=False):
    if narrow:
        W, pitch, size, top = 440, 24, 17, 176
        blocks = [(186, 198, STACK_A + STACK_B)]
        rows_max = len(STACK_A) + len(STACK_B)
    else:
        W, pitch, size, top = 880, 19, 13, 170
        blocks = [(200, 212, STACK_A), (618, 630, STACK_B)]
        rows_max = max(len(STACK_A), len(STACK_B))
    H = top + rows_max * pitch + (74 if narrow else 54)
    L = 24 if narrow else 40
    body = [t(L, 46 if narrow else 50, "TOOLS BY BUILD", 11.5 if narrow else 12.5, b=True, fill=G4, ls=2.2 if narrow else 2.6)]
    if not narrow:
        body.append(t(W - 40, 50, "a lit square means the tool is in that build", 14, i=True, fill=MUTED, anchor="end"))
    for lab_x, x0, rows in blocks:
        for j, name in enumerate(BUILDS):
            cx = x0 + j * pitch + size / 2
            body.append(
                f'<g transform="translate({n(cx - 2)} {top - 12}) rotate(-52)">'
                + t(0, 0, name, 13 if not narrow else 14, i=True, fill=MUTED, cls="hd", extra=f'style="animation-delay:{j * 2}s"')
                + "</g>"
            )
        for r, (name, used) in enumerate(rows):
            y = top + r * pitch
            if used is None:
                body.append(t(lab_x, y + size - 2.5, name, 10.5, b=True, fill=G4, anchor="end", ls=1.8))
                continue
            body.append(t(lab_x, y + size - 1.5, name, 14 if not narrow else 15, fill=SOFT, anchor="end"))
            for j in range(8):
                if j in used:
                    d = 0.3 + j * 0.16 + r * 0.02
                    body.append(cell(x0 + j * pitch, y, size, cls="on", style=f"animation-delay:{d:.2f}s,{j * 2 + 3}s"))
                else:
                    body.append(cell(x0 + j * pitch, y, size, fill=EMPTY))
            body.append(t(x0 + 8 * pitch + 3, y + size - 1.5, str(len(used)), 12.5, fill=DIM))
    fy = top + rows_max * pitch + 26
    if narrow:
        body.append(t(L, fy, "Read off each project's dependency files.", 13, i=True, fill=MUTED))
        body.append(t(L, fy + 18, "Virtual Zara comes from my internship letter.", 13, i=True, fill=MUTED))
    else:
        body.append(t(L, fy, "Read off each project's dependency files. The Virtual Zara column comes from my internship letter.", 13.5, i=True, fill=MUTED))
    css = f"""
.on {{ fill: {G3}; transform-box: fill-box; transform-origin: center; animation: pop .45s cubic-bezier(.2,1.5,.4,1) backwards, col 16s linear infinite; }}
@keyframes pop {{ 0% {{ opacity: 0; transform: scale(.2); }} 60% {{ opacity: 1; transform: scale(1.15); }} 100% {{ opacity: 1; transform: scale(1); }} }}
@keyframes col {{ 0%, 12.5%, 100% {{ fill: {G3}; }} 1.5%, 10% {{ fill: #7df59b; }} }}
.hd {{ animation: hd 16s linear infinite; }}
@keyframes hd {{ 0%, 12.5%, 100% {{ fill: {MUTED}; }} 1.5%, 10% {{ fill: {G4}; }} }}
"""
    used_by = {}
    for name, used in STACK_A + STACK_B:
        if used:
            for j in used:
                used_by.setdefault(BUILDS[j], []).append(name)
    desc = "A grid of tools against builds. " + " ".join(f"{b}: {', '.join(v)}." for b, v in used_by.items())
    return doc(W, H, "Tools by build", desc, css, "\n".join(body))


# --------------------------------------------------------------- footer ----


def footer(narrow=False):
    W, H = (440, 246) if narrow else (880, 150)
    L = 24 if narrow else 40
    cols, pitch, size = (30, 13, 9) if narrow else (24, 13, 9)
    gx = (W - (cols * pitch - (pitch - size))) / 2 if narrow else W - 40 - (cols * pitch - (pitch - size))
    gy = 136 if narrow else 30
    body = [
        t(L - 1, 62 if narrow else 66, "Say hello.", 36, b=True),
        t(L, 92 if narrow else 97, "nurmohammadsowan119@gmail.com", 17.5, fill=G4),
        t(L, 114 if narrow else 121, "Dhaka, UTC+6. Open to relocation and remote work.", 14, i=True, fill=MUTED),
        f'<rect x="{n(gx)}" y="{n(gy)}" width="{n(cols * pitch)}" height="{n(7 * pitch)}" fill="url(#grid)"/>',
    ]
    for c in range(cols):
        body.append(cell(gx + c * pitch, gy, size, fill=G4 if c % 3 else G3, cls="bob", style=f"animation-delay:-{c * 0.17:.2f}s"))
    css = f"""
.bob {{ animation: bob 1.9s steps(6, end) infinite alternate; }}
@keyframes bob {{ from {{ transform: translateY(0); }} to {{ transform: translateY({6 * pitch}px); }} }}
"""
    defs = f'<pattern id="grid" x="{n(gx)}" y="{n(gy)}" width="{pitch}" height="{pitch}" patternUnits="userSpaceOnUse"><rect width="{size}" height="{size}" rx="{n(size * 0.24)}" fill="{EMPTY}"/></pattern>'
    return doc(W, H, "Say hello", "Email nurmohammadsowan119@gmail.com. Dhaka, UTC+6. Open to relocation and remote work.", css, "\n".join(body), defs, glow=False)


def button(label, primary=False):
    W, H = 196, 46
    fill, stroke, ink, mark = (G4, G4, BG, BG) if primary else (PANEL, LINE, FG, G4)
    s, w = T(0, 0, label, 16, b=True, fill=ink)
    total = 14 + 10 + w + 10 + 9
    x = (W - total) / 2
    body = [f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="13" fill="{fill}" stroke="{stroke}"/>']
    for k, (c, r) in enumerate(((0, 0), (1, 0), (0, 1), (1, 1))):
        body.append(cell(x + c * 7, 16.5 + r * 7, 6, fill=mark, style=f"opacity:{(1, .55, .55, 1)[k]}", rx=1.4))
    body.append(t(x + 24, 28.5, label, 16, b=True, fill=ink))
    ax = x + 24 + w + 9
    body.append(f'<path d="M{n(ax)} 27 l8 -8 m-6 0 h6 v6" fill="none" stroke="{ink}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>')
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc(label)}">'
        f"<style>text {{ font-family: {FONT}; }}</style>" + "".join(body) + "</svg>\n"
    )


# ----------------------------------------------------------------- main ----

SECTIONS = [
    ("about", "01", "About"),
    ("build", "02", "How I build"),
    ("featured", "03", "Featured"),
    ("more", "04", "More builds"),
    ("stack", "05", "Stack"),
    ("github", "06", "GitHub"),
]


def main():
    OUT.mkdir(exist_ok=True)
    files = {}
    for name, fn in (("hero", hero), ("method", method), ("docintel", docintel), ("bahasabot", bahasabot), ("stack", stack), ("footer", footer)):
        files[f"{name}.svg"] = fn(False)
        files[f"{name}-narrow.svg"] = fn(True)
    for key, idx, title in SECTIONS:
        files[f"section-{key}.svg"] = banner(key, idx, title, False)
        files[f"section-{key}-narrow.svg"] = banner(key, idx, title, True)
    for key, label, primary in (("email", "Email", True), ("linkedin", "LinkedIn", False), ("portfolio", "Portfolio", False), ("pexels", "Pexels", False)):
        files[f"btn-{key}.svg"] = button(label, primary)
    for name, svg in files.items():
        (OUT / name).write_text(svg, encoding="utf-8")
    print(f"wrote {len(files)} files to {OUT}")


if __name__ == "__main__":
    main()
