import math
import src.config as cfg


def draw_circle(t, x, y, radius, fill=None, border=None, border_width=1):
    t.penup()
    t.goto(x, y - radius)
    t.setheading(0)

    if border:
        t.pencolor(border)
        t.pensize(border_width)
        t.pendown()
    else:
        t.penup()

    if fill:
        t.fillcolor(fill)
        t.begin_fill()

    t.circle(radius)

    if fill:
        t.end_fill()
    t.penup()


def draw_dial_background(t, plate_number="KL 13 AY 4411"):
    t.clear()

    # Gauge dial ticks around circumference
    for deg in range(0, 360, 10):
        rad = math.radians(deg)
        major = deg % 30 == 0
        r_inner = 230
        r_outer = 244 if major else 236

        x1 = r_inner * math.cos(rad)
        y1 = r_inner * math.sin(rad)
        x2 = r_outer * math.cos(rad)
        y2 = r_outer * math.sin(rad)

        t.penup()
        t.goto(x1, y1)
        t.pencolor("#434e61" if major else "#1c222c")
        t.pensize(2.5 if major else 1.2)
        t.pendown()
        t.goto(x2, y2)
        t.penup()

    draw_circle(t, 0, 0, 248, border="#141821", border_width=1)

    # Top header text
    t.goto(0, 312)
    t.pencolor("#93a1b5")
    t.write("B A Y E R I S C H E   M O T O R E N   W E R K E", align="center", font=("Segoe UI", 11, "bold"))

    if plate_number:
        t.goto(0, 288)
        t.pencolor("#536074")
        t.write(f"VEHICLE: {plate_number}", align="center", font=("Segoe UI", 9, "bold"))


def draw_bezel(t, is_sport_mode=False):
    t.clear()

    # Optional M-Sport tri-color accent arcs
    if is_sport_mode:
        stripes = [
            (cfg.M_LIGHT_BLUE, 218, -60, 60),
            (cfg.M_DARK_BLUE, 224, -55, 55),
            (cfg.M_RED, 230, -50, 50),
        ]
        for color, radius, start_ang, end_ang in stripes:
            t.pencolor(color)
            t.pensize(4)
            t.penup()
            for ang in range(start_ang, end_ang + 1, 3):
                rad = math.radians(ang)
                x = radius * math.cos(rad)
                y = radius * math.sin(rad)
                if ang == start_ang:
                    t.goto(x, y)
                    t.pendown()
                else:
                    t.goto(x, y)
            t.penup()

    # Chrome bevel ring layers
    draw_circle(t, 0, 0, cfg.R_OUTER_BEZEL, fill=cfg.BEZEL_DARK, border="#3c4656", border_width=2)
    draw_circle(t, 0, 0, cfg.R_OUTER_RIM, fill=cfg.BEZEL_LIGHT)
    draw_circle(t, 0, 0, cfg.R_INNER_BEZEL, fill=cfg.RING_BLACK, border=cfg.BEZEL_DARK, border_width=2)

    # Inner chrome border
    draw_circle(t, 0, 0, cfg.R_RING_INNER + 3, fill=cfg.BEZEL_MID)
    draw_circle(t, 0, 0, cfg.R_ROUNDEL + 2, fill=cfg.BEZEL_LIGHT)


def render_curved_typography(screen):
    """
    Standard turtle.write() does not support text rotation angles.
    We interact with Tkinter's canvas directly via screen.getcanvas().
    Note: Tkinter's Y axis points downwards, so turtle (x, y) becomes canvas (x, -y).
    """
    canvas = screen.getcanvas()
    canvas.delete("bmw_lettering")

    # Character, angle along circular band, tilt angle
    letters = [
        ("B", 135, 45),
        ("M", 90, 0),
        ("W", 45, -45),
    ]

    for char, deg, tilt in letters:
        rad = math.radians(deg)
        cx = cfg.R_TEXT * math.cos(rad)
        cy = -cfg.R_TEXT * math.sin(rad)

        # Drop shadow for depth
        canvas.create_text(
            cx + 2,
            cy + 2,
            text=char,
            fill="#05070a",
            font=("Arial", 38, "bold"),
            angle=tilt,
            tags="bmw_lettering",
        )
        # Main text face
        canvas.create_text(
            cx,
            cy,
            text=char,
            fill="#ffffff",
            font=("Arial", 38, "bold"),
            angle=tilt,
            tags="bmw_lettering",
        )

    canvas.tag_raise("bmw_lettering")


def draw_roundel(t, angle):
    t.clear()

    # 1. Base white disc
    draw_circle(t, 0, 0, cfg.R_ROUNDEL, fill=cfg.BMW_WHITE)

    # 2. Quadrants: Blue at angle and angle + 180
    for offset in (0, 180):
        t.penup()
        t.goto(0, 0)
        t.setheading(angle + offset)
        t.forward(cfg.R_ROUNDEL)
        t.left(90)
        t.fillcolor(cfg.BMW_BLUE)
        t.pencolor(cfg.BMW_BLUE)
        t.pensize(1)
        t.pendown()
        t.begin_fill()
        t.circle(cfg.R_ROUNDEL, 90)
        t.goto(0, 0)
        t.end_fill()
        t.penup()

    # 3. Spoke lines
    t.pencolor(cfg.DIVIDER_COLOR)
    t.pensize(2.5)
    for spoke in [angle, angle + 90, angle + 180, angle + 270]:
        rad = math.radians(spoke)
        t.goto(0, 0)
        t.pendown()
        t.goto(cfg.R_ROUNDEL * math.cos(rad), cfg.R_ROUNDEL * math.sin(rad))
        t.penup()

    # 4. Outer rim outline
    t.goto(0, -cfg.R_ROUNDEL)
    t.setheading(0)
    t.pencolor(cfg.BEZEL_LIGHT)
    t.pensize(2)
    t.pendown()
    t.circle(cfg.R_ROUNDEL)
    t.penup()

    # 5. Sheen arc
    t.pencolor("#ffffff")
    t.pensize(2.2)
    r_sheen = cfg.R_ROUNDEL - 5
    for a in range(70, 155, 3):
        rad = math.radians(a)
        x = r_sheen * math.cos(rad)
        y = r_sheen * math.sin(rad)
        if a == 70:
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)
    t.penup()

    # 6. Center hub button
    draw_circle(t, 0, 0, 5, fill=cfg.BEZEL_MID, border=cfg.BEZEL_DARK, border_width=1)
    draw_circle(t, 0, 0, 2.5, fill="#ffffff")


def draw_hud(t, current_rpm, cruise_rpm, is_sport, is_paused, direction):
    t.clear()

    bar_y = -275
    bar_w = 340
    bar_h = 10

    # Track background
    t.penup()
    t.goto(-bar_w / 2, bar_y)
    t.fillcolor("#131720")
    t.pencolor("#212836")
    t.pensize(1)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(bar_w)
        t.left(90)
        t.forward(bar_h)
        t.left(90)
    t.end_fill()
    t.penup()

    # RPM bar fill
    fill_ratio = min(max(current_rpm / cfg.MAX_RPM, 0.02), 1.0)
    active_w = bar_w * fill_ratio

    if current_rpm >= 6000:
        bar_color = "#e53e3e"
    elif current_rpm >= 4000:
        bar_color = "#dd6b20"
    elif is_sport:
        bar_color = cfg.M_LIGHT_BLUE
    else:
        bar_color = "#3182ce"

    t.goto(-bar_w / 2, bar_y)
    t.fillcolor(bar_color)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(active_w)
        t.left(90)
        t.forward(bar_h)
        t.left(90)
    t.end_fill()
    t.penup()

    mode_label = "M-SPORT" if is_sport else "CRUISE"
    state_label = "PAUSED" if is_paused else "RUNNING"
    dir_label = "CW" if direction < 0 else "CCW"

    t.goto(0, bar_y - 25)
    t.pencolor("#e2e8f0")
    t.write(
        f"ENGINE: {int(current_rpm):,} RPM  |  BASE: {int(cruise_rpm)} RPM  |  MODE: {mode_label}  |  DIR: {dir_label}  |  {state_label}",
        align="center",
        font=("Segoe UI", 10, "bold"),
    )

    t.goto(0, bar_y - 50)
    t.pencolor("#64748b")
    t.write(
        "[Click / Enter] Rev Engine    [Space] Pause    [Up/Down] Cruise RPM    [M] Sport Mode    [R] Reverse    [Esc] Quit",
        align="center",
        font=("Segoe UI", 9, "normal"),
    )
