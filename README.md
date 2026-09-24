# Animated BMW Logo & Instrument Cluster

An interactive BMW emblem and instrument cluster animation built with Python's standard library (`turtle` and `tkinter`). It features a continuous rotating center roundel, throttle rev response with smooth deceleration, live telemetry, and an optional ///M-Sport mode.

---

## Technical Highlights

- **Decoupled Layer Architecture**: Python's `turtle` library normally flickers when clearing and redrawing complex scenes. To keep rendering at 60 FPS without stutter, the scene is divided across distinct turtle layers (background dial, static chrome bezel, spinning roundel, and telemetry HUD). Only the rotating roundel and HUD redraw every frame.
- **Curved Typography via Tkinter Canvas**: Standard `turtle.write()` does not support text rotation angles. To position the `B`, `M`, and `W` letters radially along the curved upper bezel, the code accesses Tkinter's underlying canvas directly (`screen.getcanvas().create_text()`), mapping Turtle's center-origin coordinate system to Tkinter's screen coordinates.
- **Rev Physics & Decay**: Clicking or pressing Enter spikes engine RPM to 6,800. Revs decay exponentially back to base cruising speed over subsequent frames.

---

## Controls

| Key / Input | Action | Details |
| :--- | :--- | :--- |
| **Mouse Click / Enter** | Rev Throttle | Surges RPM to 6,800 redline with smooth decay |
| **Spacebar** | Pause / Resume | Freezes or unfreezes rotation |
| **Up Arrow** | Speed Up | Increases cruising RPM (+30) |
| **Down Arrow** | Slow Down | Decreases cruising RPM (-30) |
| **M** | M-Sport Mode | Toggles tri-color racing stripes and high-RPM profile |
| **R** | Reverse Spin | Flips rotation between clockwise and counter-clockwise |
| **Esc / Q** | Quit | Closes the application window cleanly |

---

## Usage & CLI Options

Run directly with Python 3:

```bash
python3 main.py
```

### Command-Line Arguments

You can customize the vehicle plate banner, cruise speed, or start options directly:

```bash
# Custom registration plate and cruise speed
python3 main.py --plate "KL 13 AY 4411" --cruise-rpm 180

# Launch directly in M-Sport mode, skipping intro sequence
python3 main.py --sport --skip-intro
```

| Flag | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `--plate` | `str` | `KL 13 AY 4411` | Custom vehicle plate text on top header |
| `--cruise-rpm` | `float` | `120.0` | Default cruising rotation speed |
| `--sport` | `flag` | `False` | Launch directly in M-Sport performance mode |
| `--skip-intro` | `flag` | `False` | Skip opening border drawing animation |

---

## Requirements

- Python 3.8+
- Standard library only (`turtle`, `tkinter`, `math`, `argparse`, `dataclasses`). No third-party packages required.

---

## License & Disclaimer

This project is licensed under the [MIT License](LICENSE).

> **Disclaimer**: BMW and the BMW roundel logo are registered trademarks of Bayerische Motoren Werke AG. This is an independent educational programming demonstration and is not affiliated with, endorsed by, or sponsored by BMW AG.

