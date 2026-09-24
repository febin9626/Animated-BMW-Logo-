# Animated BMW Logo

This project is an interactive BMW Logo animation made using Python's Standard libraries, mainly Turtle and Tkinter. The logo has a continuously rotating centre, smooth engine rev control, live information on the screen, and an optional M-Sport Mode.

## Technical Highlights

- **SEPEREATE LAYERS**: The Turtle library can sometimes flicker when a lot of things are redrawn. To avoid this and keep the animation smooth, the project is divided into different layers such as the background, BMW logo, rotating centre and information display. Only the parts that need changes are updated continuously.
- **Curved Text**: The normal turtle.write() function cannot rotate text at different angles. So, Tkinter Canvas is used to place the B, M and W letters around the upper part of the logo. This makes the text follow the curved shape of the logo
- **Rev Control aand Deceleration**: When the user clicks or presses Enter, the engine RPM increases up to 6,800 RPM. After that, the RPM slowly comes back to the normal cruising speed, giving a smooth rev effect.

---

## Controls

**Mouse Click / Enter** : Rev Throttle
**Spacebar** : Pause / Resume (for rotation)
**Up Arrow** : Speed Up 
**Down Arrow** : Slow Down
**M** : M-Sport Mode ; Toggles tri-color racing stripes and high-RPM profile
**R** : Reverse Spin ; Flips rotation between clockwise and Anti-clockwise
**Esc / Q** : Quit ; Closes the application window
---

## Usage & CLI Options

Run directly with Python 3:

```bash
python3 main.py
```
## Requirements

- Python 3.8+
- Standard library only (`turtle`, `tkinter`, `math`, `argparse`, `dataclasses`). No third-party packages required.

---

## License & Disclaimer

This project is licensed under the [MIT License](LICENSE).

> **Disclaimer**: BMW and the BMW roundel logo are registered trademarks of Bayerische Motoren Werke AG. This is an independent educational programming demonstration and is not affiliated with, endorsed by, or sponsored by BMW AG.

