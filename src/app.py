import turtle
import src.config as cfg
from src.graphics import (
    draw_dial_background,
    draw_bezel,
    render_curved_typography,
    draw_roundel,
    draw_hud,
)


class BMWLogoApp:
    def __init__(self, config: cfg.AppConfig):
        self.config = config
        self.cruise_rpm = config.cruise_rpm
        self.current_rpm = config.cruise_rpm
        self.angle = 0.0
        self.direction = -1
        self.is_sport = config.start_in_sport
        self.is_paused = False
        self.is_running = True
        self.intro_done = config.skip_intro
        self.intro_step = 0

        self.setup_display()
        self.bind_events()

    def setup_display(self):
        self.screen = turtle.Screen()
        self.screen.setup(self.config.width, self.config.height)
        self.screen.title("BMW Dashboard - Animated Logo & Telemetry")
        self.screen.bgcolor(cfg.BG_COLOR)
        self.screen.tracer(0)
        
        self.bg_turtle = self._create_layer_turtle()
        self.bezel_turtle = self._create_layer_turtle()
        self.roundel_turtle = self._create_layer_turtle()
        self.hud_turtle = self._create_layer_turtle()
        self.intro_turtle = self._create_layer_turtle()

    def _create_layer_turtle(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        return t

    def bind_events(self):
        self.screen.listen()
        self.screen.onscreenclick(self.on_click)
        self.screen.onkey(lambda: self.on_click(0, 0), "Return")
        self.screen.onkey(self.toggle_pause, "space")
        self.screen.onkey(lambda: self.adjust_cruise_rpm(30), "Up")
        self.screen.onkey(lambda: self.adjust_cruise_rpm(-30), "Down")
        self.screen.onkey(self.toggle_sport, "m")
        self.screen.onkey(self.toggle_sport, "M")
        self.screen.onkey(self.reverse_direction, "r")
        self.screen.onkey(self.reverse_direction, "R")
        self.screen.onkey(self.close, "Escape")
        self.screen.onkey(self.close, "q")
        self.screen.onkey(self.close, "Q")

    def on_click(self, x, y):
        if not self.intro_done:
            self.finish_intro()
            return
        self.current_rpm = cfg.REV_BURST_RPM
        self.render_hud()

    def toggle_pause(self):
        if not self.intro_done:
            self.finish_intro()
            return
        self.is_paused = not self.is_paused
        self.render_hud()

    def toggle_sport(self):
        if not self.intro_done:
            self.finish_intro()
            return

        self.is_sport = not self.is_sport
        if self.is_sport:
            self.cruise_rpm = max(self.cruise_rpm, cfg.SPORT_CRUISE_RPM)
            self.current_rpm = 5800.0
        else:
            self.cruise_rpm = cfg.DEFAULT_CRUISE_RPM

        draw_bezel(self.bezel_turtle, self.is_sport)
        render_curved_typography(self.screen)
        self.render_hud()

    def adjust_cruise_rpm(self, delta):
        if not self.intro_done:
            self.finish_intro()
            return
        self.cruise_rpm = max(30.0, min(self.cruise_rpm + delta, 800.0))
        self.current_rpm = max(self.current_rpm, self.cruise_rpm)
        self.render_hud()

    def reverse_direction(self):
        if not self.intro_done:
            self.finish_intro()
            return
        self.direction *= -1
        self.render_hud()

    def close(self):
        self.is_running = False
        try:
            self.screen.bye()
        except Exception:
            pass

    def render_hud(self):
        draw_hud(
            self.hud_turtle,
            self.current_rpm,
            self.cruise_rpm,
            self.is_sport,
            self.is_paused,
            self.direction,
        )

    def finish_intro(self):
        self.intro_done = True
        self.intro_turtle.clear()
        draw_dial_background(self.bg_turtle, self.config.plate_number)
        draw_bezel(self.bezel_turtle, self.is_sport)
        render_curved_typography(self.screen)
        draw_roundel(self.roundel_turtle, 0)
        self.render_hud()
        self.screen.ontimer(self.update_loop, cfg.FRAME_INTERVAL_MS)

    def run_intro_step(self):
        if not self.is_running or self.intro_done:
            return

        self.intro_step += 1

        if self.intro_step <= 18:
            arc_angle = self.intro_step * 20
            self.intro_turtle.pencolor(cfg.BEZEL_LIGHT)
            self.intro_turtle.pensize(3)
            self.intro_turtle.penup()
            self.intro_turtle.goto(0, -cfg.R_OUTER_RIM)
            self.intro_turtle.setheading(0)
            self.intro_turtle.pendown()
            self.intro_turtle.circle(cfg.R_OUTER_RIM, arc_angle)
        elif self.intro_step == 20:
            self.intro_turtle.clear()
            draw_dial_background(self.bg_turtle, self.config.plate_number)
            draw_bezel(self.bezel_turtle, self.is_sport)
            render_curved_typography(self.screen)
            draw_roundel(self.roundel_turtle, 0)
            self.render_hud()
        elif self.intro_step >= 26:
            self.finish_intro()
            return

        self.screen.update()
        self.screen.ontimer(self.run_intro_step, 30)

    def update_loop(self):
        if not self.is_running:
            return

        if self.current_rpm > self.cruise_rpm:
            self.current_rpm = self.cruise_rpm + (self.current_rpm - self.cruise_rpm) * 0.94
            if self.current_rpm - self.cruise_rpm < 2.0:
                self.current_rpm = self.cruise_rpm
        elif self.current_rpm < self.cruise_rpm:
            self.current_rpm = self.cruise_rpm

        if not self.is_paused:
            deg_per_frame = (self.current_rpm * 0.1) * self.direction
            self.angle = (self.angle + deg_per_frame) % 360
            draw_roundel(self.roundel_turtle, self.angle)

        self.render_hud()
        self.screen.update()
        self.screen.ontimer(self.update_loop, cfg.FRAME_INTERVAL_MS)

    def run(self):
        if self.intro_done:
            self.finish_intro()
        else:
            self.run_intro_step()

        try:
            turtle.mainloop()
        except (turtle.Terminator, KeyboardInterrupt):
            pass
