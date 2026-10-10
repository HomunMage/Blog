#!/usr/bin/env python3
"""Generate the Alchemy Flow diagram (SVG only).

    python3 _tools/gen-alchemy-flow-svg.py

Writes: blob/Programming/2026-08-01-alchemy-flow.svg (published asset)

Layout is COMPUTED, not hand-placed:
  * The only knobs are W, H, MARGIN, GAP, PAD and the font sizes.
  * The three lanes are equal columns derived from W — change W and the
    columns resize and reposition themselves.
  * Every commit (trunk or branch) is one entry in EVENTS, in chronological
    order; its y position falls out of its index in the list. Chronology
    cannot be drawn wrong — reordering EVENTS is the only way to move a dot.
  * Text offsets derive from font size, dot radius and PAD; horizontal line
    start/ends derive from estimated text widths.

Prod/release never branches or merges — it only fast-forwards its pointer to
a tag that already exists on main, so it is drawn as flat horizontal marks:
no diagonal, no vertical connector.
"""

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_SVG = ROOT / "blob/Programming/2026-08-01-alchemy-flow.svg"

# ------------------------------------------------------------- the knobs ----
W, H = 800, 800
MARGIN, GAP, PAD = 15, 30, 10
GREEN, BLUE, PINK = "#22c55e", "#4f7cff", "#a21caf"
BG = "#0b0f14"
DIM = 0.45                     # opacity of "history continues" context commits

F_CAP   = 16                   # lane caption (top)
F_LABEL = 20                   # version tags / prod pointer
F_SMALL = 15                   # annotations: fix bug, fast-forward, branch/merge
F_NAME  = 30                   # lane names (bottom)
LINE_W, DOT_R, MERGE_R = 5, 8, 11

# ------------------------------------------------- derived lane geometry ----
LANE_W = (W - 2 * MARGIN - 2 * GAP) / 3          # 3 equal columns, by definition
LANE_TOP, LANE_H = MARGIN, H - 2 * MARGIN


def lane_x(i): return MARGIN + i * (LANE_W + GAP)
def lane_cx(i): return lane_x(i) + LANE_W / 2


PROD, MAIN = lane_cx(0), lane_cx(1)
STEM = lane_x(2) + LANE_W * 0.33   # feature stem left of lane center so the
                                   # caption block fits inside the lane

# ------------------------------------------------------------- the story ----
# One entry per commit, oldest -> newest. Kind: "main", "A" (feature/xxx
# work), "B" (feature/yyy work). Flags: "tag", "merge", "dim".
EVENTS = [
    ("main", "1.3.3", "dim"),
    ("main", "1.3.4", "tag"),        # branch point of feature/xxx
    ("A", "", ""),
    ("A", "", ""),
    ("A", "", ""),
    ("main", "1.4.0", "tag merge"),  # feature/xxx lands
    ("main", "1.4.1", ""),
    ("main", "1.4.2", ""),
    ("main", "1.4.3", "tag"),        # <- prod fast-forwards here
    ("main", "1.4.4", "tag"),        # branch point of feature/yyy
    ("B", "", ""),
    ("B", "", ""),
    ("main", "1.5.0", "tag merge"),  # feature/yyy lands
    ("main", "1.5.1", "dim"),
]
BRANCH_A, MERGE_A = "1.3.4", "1.4.0"
BRANCH_B, MERGE_B = "1.4.4", "1.5.0"
PROD_NOW, PROD_WAS = "1.4.3", "1.3.4"
FIX_SPAN = ("1.4.0", "1.4.1")        # the segment annotated "fix bug"

# --------------------------------------------- vertical timeline (derived) ---
# The frame (graph_top, graph_bot) comes from lane geometry alone: below the
# caption, above the lane name. STEP then fills that fixed frame exactly —
# it is total space divided by total weight, never a chosen number.
# Gaps get a weight: a full step (1.0) wherever a branch connects to main
# (branch-out, merge-back), but a compressed step (WORK_SHRINK) between two
# consecutive commits *within the same feature branch* — that inner history
# is supporting detail, not the throughline, so it can sit closer together
# than the main-axis events around it.
WORK_SHRINK = 0.7
name_lh = F_NAME * 1.15
name_base2 = LANE_TOP + LANE_H - PAD - F_NAME * 0.25   # "(prod)" baseline
name_base1 = name_base2 - name_lh                      # "release" baseline
graph_top = LANE_TOP + PAD + F_CAP + 2 * PAD           # below the caption text
graph_bot = name_base1 - F_NAME - PAD                  # above the lane names
ARROW_LEN = 3 * PAD                                    # main line tip overshoot

N = len(EVENTS)
weights = [
    WORK_SHRINK if EVENTS[i - 1][0] == EVENTS[i][0] and EVENTS[i][0] in ("A", "B")
    else 1.0
    for i in range(1, N)
]
cum = [0.0]
for w in weights:
    cum.append(cum[-1] + w)
STEP = (graph_bot - graph_top - ARROW_LEN) / cum[-1]


def y_of(t): return graph_bot - cum[t] * STEP


trunk, work_a, work_b = [], [], []
for t, (kind, label, flags) in enumerate(EVENTS):
    if kind == "main":
        trunk.append((y_of(t), label, flags))
    elif kind == "A":
        work_a.append(y_of(t))
    else:
        work_b.append(y_of(t))

Y = {label: y for y, label, _ in trunk}

# ---------------------------------------------------------------- helpers ---
out = []
add = out.append


def est_w(s, size, bold=False):
    """Rough text width — used to compute where lines may start/stop."""
    return len(s) * size * (0.50 if bold else 0.52)


def mid(y, size):
    """Baseline that vertically centers text of `size` on line/dot at y."""
    return y + size * 0.35


def line(x1, y1, x2, y2, color, w=LINE_W, dash=None, arrow=None, opacity=None):
    a = f' marker-end="url(#a-{arrow})"' if arrow else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' opacity="{opacity}"' if opacity else ""
    add(f'<path d="M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}" fill="none" '
        f'stroke="{color}" stroke-width="{w}" stroke-linecap="round"{d}{a}{o}/>')


def curve(x1, y1, cx1, cy1, cx2, cy2, x2, y2, color, arrow=None):
    a = f' marker-end="url(#a-{arrow})"' if arrow else ""
    add(f'<path d="M{x1:.1f},{y1:.1f} C{cx1:.1f},{cy1:.1f} {cx2:.1f},{cy2:.1f} '
        f'{x2:.1f},{y2:.1f}" fill="none" stroke="{color}" stroke-width="{LINE_W}" '
        f'stroke-linecap="round"{a}/>')


def dot(x, y, color, r=DOT_R, ring=False, opacity=None):
    o = f' opacity="{opacity}"' if opacity else ""
    if ring:
        add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{BG}" '
            f'stroke="{color}" stroke-width="4"{o}/>')
    else:
        add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"{o}/>')


def text(x, y, s, color, size, bold=False, anchor="start", opacity=None, italic=False):
    b = ' font-weight="700"' if bold else ""
    i = ' font-style="italic"' if italic else ""
    o = f' opacity="{opacity}"' if opacity else ""
    add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{color}" '
        f'text-anchor="{anchor}"{b}{i}{o}>{s}</text>')


# ------------------------------------------------------------------ lanes ----
for i, (color, cap, n1, n2) in enumerate([
    (GREEN, "only fast-forwards to a tag", "release", "(prod)"),
    (BLUE,  "always deployable",           "main",    "(stage)"),
    (PINK,  "short-lived, disposable",     "feature", "(dev)"),
]):
    add(f'<rect x="{lane_x(i):.1f}" y="{LANE_TOP}" width="{LANE_W:.1f}" '
        f'height="{LANE_H}" rx="8" fill="none" stroke="{color}" stroke-width="6"/>')
    text(lane_cx(i), LANE_TOP + PAD + F_CAP, cap, color, F_CAP, anchor="middle")
    text(lane_cx(i), name_base1, n1, color, F_NAME, bold=True, anchor="middle")
    text(lane_cx(i), name_base2, n2, color, F_NAME, bold=True, anchor="middle")

# ------------------------------------------------------------------- main ----
line(MAIN, y_of(0), MAIN, graph_top, BLUE, arrow="blue")
# offset by ARROW_LEN (already the named clearance the arrowhead needs) in
# both axes, so the label can't land on the marker regardless of its size
text(MAIN + ARROW_LEN, graph_top + ARROW_LEN, "next cycle&#8230;", BLUE, F_SMALL)
for y, label, flags in trunk:
    op = DIM if "dim" in flags else None
    dot(MAIN, y, BLUE, MERGE_R if "merge" in flags else DOT_R,
        ring=("tag" in flags and "merge" not in flags), opacity=op)
    # version labels sit LEFT of the trunk line
    text(MAIN - DOT_R - PAD, mid(y, F_LABEL), label, BLUE,
         F_LABEL, bold="tag" in flags, anchor="end", opacity=op)

# "fix bug" on the free right-hand side, centered on its trunk segment
fy = (Y[FIX_SPAN[0]] + Y[FIX_SPAN[1]]) / 2
text(MAIN + DOT_R + PAD, mid(fy, F_SMALL), "fix bug", BLUE, F_SMALL,
     italic=True, opacity="0.85")


# --------------------------------------------------------- feature branches --
def feature_branch(name, branch_tag, merge_tag, works):
    yb, ym = Y[branch_tag], Y[merge_tag]
    line(MAIN, yb, STEM, works[0], PINK)
    line(STEM, works[0], STEM, works[-1], PINK)
    line(STEM, works[-1], MAIN + MERGE_R + PAD * 0.6, ym + 2, PINK, arrow="pink")
    for y in works:
        dot(STEM, y, PINK)
    # caption block: right-anchored at the lane's inner edge so it always
    # stays inside the lane; vertically centered on the stem
    cx = lane_x(2) + LANE_W - PAD
    cy = mid((works[0] + works[-1]) / 2, F_SMALL)
    lh = F_SMALL * 1.5
    text(cx, cy - lh, name, PINK, F_LABEL, bold=True, anchor="end")
    text(cx, cy, f"branch at {branch_tag}", PINK, F_SMALL, anchor="end", opacity="0.85")
    text(cx, cy + lh, f"merge &#8594; {merge_tag}", PINK, F_SMALL, anchor="end", opacity="0.85")


feature_branch("feature/xxx", BRANCH_A, MERGE_A, work_a)
feature_branch("feature/yyy", BRANCH_B, MERGE_B, work_b)

# ------------------------------------------------------------------- prod ----
# Flat horizontal marks only. Text sits on the line's level, at the lane's
# left edge; the line starts where the text ends.
x0 = lane_x(0) + PAD

def tag_left_edge(tag):
    """Where a trunk version label starts — prod lines must stop before it."""
    return MAIN - DOT_R - PAD - est_w(tag, F_LABEL, bold=True) - PAD


def prod_row(tag, label_size, bold, opacity, dash=None):
    """One prod pointer: label at the lane edge, then an unbroken line to the
    tag, with "fast-forward" floating below the line (never touching it)."""
    y = Y[tag]
    label = f"prod = {tag}"
    text(x0, mid(y, label_size), label, GREEN, label_size, bold=bold, opacity=opacity)
    x1 = x0 + est_w(label, label_size, bold=bold) + PAD * 1.6
    x2 = tag_left_edge(tag)
    line(x1, y, x2, y, GREEN, w=4 if dash else LINE_W, dash=dash,
         arrow="green", opacity=opacity)
    # right-aligned at the green lane's own rightmost edge, not the line's end
    # (the line/arrow continues on past the lane boundary, into the gap)
    text(lane_x(0) + LANE_W - PAD, y + F_SMALL + PAD, "fast-forward", GREEN,
         F_SMALL, italic=True, anchor="end", opacity=opacity)


prod_row(PROD_NOW, F_LABEL, True, None)
prod_row(PROD_WAS, F_SMALL, False, "0.6", dash="10 8")

# ------------------------------------------------------------------- emit ----
markers = "".join(
    f'<marker id="a-{n}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
    f'markerHeight="6" orient="auto-start-reverse">'
    f'<path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
    for n, c in (("green", GREEN), ("blue", BLUE), ("pink", PINK))
)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"
     role="img" aria-label="Alchemy Flow: two feature branches leave and rejoin main as tagged merges ({BRANCH_A} to {MERGE_A}, then {BRANCH_B} to {MERGE_B}); prod never branches or merges, it only fast-forwards its pointer from tag {PROD_WAS} straight to tag {PROD_NOW}, drawn as flat horizontal marks">
<title>Alchemy Flow</title>
<!-- generated by _tools/gen-alchemy-flow-svg.py - do not edit by hand -->
<defs>{markers}</defs>
<g font-family="ui-sans-serif, -apple-system, Segoe UI, Helvetica, Arial, sans-serif">
{chr(10).join(out)}
</g>
</svg>
'''

OUT_SVG.parent.mkdir(parents=True, exist_ok=True)
OUT_SVG.write_text(svg, encoding="utf-8")
print(f"wrote {OUT_SVG} ({len(svg)} bytes, {len(out)} elements)")
print(f"  lanes: 3 x {LANE_W:.1f}px, gap {GAP}, canvas {W}x{H}, step {STEP:.1f}px")
