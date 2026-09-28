# Animated BMW Logo

This project is an interactive BMW Logo animation made using Python's standard libraries, mainly Turtle and Tkinter. The logo features a continuously rotating centre, responsive engine rev control, real-time telemetry HUD, and an optional M-Sport Mode.

---

## Technical Highlights

- **Separate Layers**: The Turtle library can flicker when redrawing complex scenes. To prevent this and keep animations smooth at 60 FPS, the rendering is divided across independent turtle layers (background dial, chrome bezel, spinning roundel, and HUD). Only the rotating centre and HUD update on each frame.
- **Curved Typography**: Standard `turtle.write()` cannot rotate text at arbitrary angles. Tkinter Canvas is used directly (`screen.getcanvas().create_text()`) to place and tilt the B, M, and W letters along the upper curved bezel.
- **Rev Control & Deceleration**: Clicking or pressing Enter spikes engine RPM to 6,800. The RPM decays smoothly back down to the cruising speed, simulating rotational momentum.

---

## Controls

| Key / Input | Action | Details |
| :--- | :--- | :--- |
| **Mouse Click / Enter** | Rev Throttle | Surges RPM to 6,800 redline with smooth decay |
| **Spacebar** | Pause / Resume | Freezes or unfreezes rotation |
| **Up Arrow** | Speed Up | Increases cruising RPM (+30) |
| **Down Arrow** | Slow Down | Decreases cruising RPM (-30) |
| **M** | M-Sport Mode | Toggles tri-color racing stripes and sport profile |
| **R** | Reverse Spin | Flips rotation between clockwise and counter-clockwise |
| **Esc / Q** | Quit | Closes the application cleanly |

---

## Usage

Run directly with Python 3:

```bash
python3 src/main.py
```

### Options

```bash
# Custom registration plate and cruise speed
python3 src/main.py --plate "KL 13 AY 4411" --cruise-rpm 180

# Launch directly in M-Sport mode without intro animation
python3 src/main.py --sport --skip-intro
```

| Flag | Default | Description |
| :--- | :--- | :--- |
| `--plate` | `KL 13 AY 4411` | Custom vehicle plate text on top header |
| `--cruise-rpm` | `120.0` | Default cruising rotation speed in RPM |
| `--sport` | `False` | Launch directly in M-Sport performance mode |
| `--skip-intro` | `False` | Skip opening perimeter drawing animation |

---

## Requirements

- Python 3.8+
- Standard library only (`turtle`, `tkinter`, `math`, `argparse`, `dataclasses`). Zero external dependencies required.

---

## Disclaimer

> **Disclaimer**: BMW and the BMW roundel logo are registered trademarks of Bayerische Motoren Werke AG. This is an independent educational programming demonstration and is not affiliated with, endorsed by, or sponsored by BMW AG.
