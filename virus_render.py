import turtle
import math
import time

# ─── Window Setup ──────────────────────────────────────────────────────────────
screen = turtle.Screen()
screen.title("Bio-Digital Virus Render")
screen.bgcolor("#0a0a0f")
screen.setup(width=800, height=800)
# tracer(1, delay_ms) — every 1 step, 18 ms pause = smooth visible animation
screen.tracer(1, 18)

# ─── Helper: create a turtle with common settings ──────────────────────────────
def make_pen(color, width=1, speed=6):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(speed)      # 1=slowest … 10=fast  (0=instant, avoided here)
    t.penup()
    t.color(color)
    t.width(width)
    return t

# ─── 1. OUTER ENVELOPE (lipid bilayer) ─────────────────────────────────────────
def draw_circle_at(pen, x, y, radius, steps=120):
    pen.goto(x, y - radius)
    pen.pendown()
    for i in range(steps + 1):
        angle = math.radians(i * 360 / steps)
        pen.goto(x + radius * math.sin(angle),
                 y - radius * math.cos(angle))
    pen.penup()

outer = make_pen("#1a6b3c", 3, speed=4)
draw_circle_at(outer, 0, 0, 160)

inner_mem = make_pen("#22a85c", 2, speed=4)
draw_circle_at(inner_mem, 0, 0, 145)

# ─── 2. SPIKE PROTEINS ─────────────────────────────────────────────────────────
spike_pen = make_pen("#39ff6a", 2, speed=5)

NUM_SPIKES    = 28
SPIKE_BASE_R  = 155
SPIKE_TIP_R   = 210

for i in range(NUM_SPIKES):
    angle = math.radians(i * 360 / NUM_SPIKES)
    bx = SPIKE_BASE_R * math.cos(angle)
    by = SPIKE_BASE_R * math.sin(angle)
    tx = SPIKE_TIP_R  * math.cos(angle)
    ty = SPIKE_TIP_R  * math.sin(angle)

    # Stalk
    spike_pen.goto(bx, by)
    spike_pen.pendown()
    spike_pen.goto(tx, ty)
    spike_pen.penup()

    # Bulbous head
    head_pen = make_pen("#00ff88", 1, speed=8)
    head_pen.goto(tx, ty - 9)
    head_pen.pendown()
    head_pen.fillcolor("#00cc66")
    head_pen.begin_fill()
    head_pen.circle(9)
    head_pen.end_fill()
    head_pen.penup()

# ─── 3. CAPSID SHELL ───────────────────────────────────────────────────────────
capsid_pen = make_pen("#0d7a44", 1, speed=6)

NUM_FACETS = 18
CAPSID_R   = 130
for i in range(NUM_FACETS):
    a1   = math.radians(i       * 360 / NUM_FACETS)
    a2   = math.radians((i + 1) * 360 / NUM_FACETS)
    amid = math.radians((i + .5)* 360 / NUM_FACETS)

    p1     = (CAPSID_R * math.cos(a1),   CAPSID_R * math.sin(a1))
    p2     = (CAPSID_R * math.cos(a2),   CAPSID_R * math.sin(a2))
    inner_r = 100 if i % 2 == 0 else 115
    pm      = (inner_r * math.cos(amid), inner_r * math.sin(amid))

    capsid_pen.goto(*p1);  capsid_pen.pendown()
    capsid_pen.goto(*pm)
    capsid_pen.goto(*p2)
    capsid_pen.goto(*p1)
    capsid_pen.penup()

# ─── 4. NUCLEOCAPSID CORE ──────────────────────────────────────────────────────
core_pen = make_pen("#006622", 2, speed=4)
draw_circle_at(core_pen, 0, 0, 90)

core_fill = make_pen("#004d1a", 1, speed=4)
core_fill.goto(0, -90)
core_fill.pendown()
core_fill.fillcolor("#041a0d")
core_fill.begin_fill()
core_fill.circle(90)
core_fill.end_fill()
core_fill.penup()

# ─── 5. RNA STRAND (coiled inside core) ────────────────────────────────────────
rna_pen = make_pen("#00ff99", 1, speed=10)
rna_pen.goto(0, 0)
rna_pen.pendown()
for step in range(400):
    rna_angle = step * 37
    rna_r     = step * 0.2
    if rna_r > 82:
        break
    rx = rna_r * math.cos(math.radians(rna_angle))
    ry = rna_r * math.sin(math.radians(rna_angle))
    rna_pen.goto(rx, ry)
rna_pen.penup()

# ─── 6. MATRIX PROTEINS (dots) ─────────────────────────────────────────────────
matrix_pen = make_pen("#17d468", 1, speed=9)
NUM_MATRIX = 60
for i in range(NUM_MATRIX):
    angle = math.radians(i * 360 / NUM_MATRIX + 6)
    mr = 135
    mx = mr * math.cos(angle)
    my = mr * math.sin(angle)
    matrix_pen.goto(mx, my - 3)
    matrix_pen.pendown()
    matrix_pen.fillcolor("#17d468")
    matrix_pen.begin_fill()
    matrix_pen.circle(3)
    matrix_pen.end_fill()
    matrix_pen.penup()

# ─── 7. LABEL ──────────────────────────────────────────────────────────────────
label = make_pen("#39ff6a", 1, speed=6)
label.goto(0, -265)
label.write("SARS-CoV-2  •  Bio-Digital Render", align="center",
            font=("Courier", 11, "bold"))

legend_items = [
    (240, 220, "#39ff6a", "Spike protein (S)"),
    (240, 195, "#17d468", "Matrix protein (M)"),
    (240, 170, "#0d7a44", "Capsid shell"),
    (240, 145, "#006622", "Nucleocapsid"),
    (240, 120, "#00ff99", "RNA genome"),
]
for lx, ly, col, text in legend_items:
    dot = make_pen(col, 1, speed=9)
    dot.goto(lx, ly)
    dot.pendown()
    dot.fillcolor(col)
    dot.begin_fill()
    dot.circle(5)
    dot.end_fill()
    dot.penup()

    lbl = make_pen("#4dffaa", 1, speed=9)
    lbl.goto(lx + 14, ly - 4)
    lbl.write(text, font=("Courier", 9, "normal"))

print("[+] Virus structure render complete.")
screen.exitonclick()
