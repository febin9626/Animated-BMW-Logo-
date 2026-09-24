from dataclasses import dataclass

# Color definitions
BG_COLOR = "#0b0d13"
GAUGE_RING = "#171b24"
BEZEL_DARK = "#232936"
BEZEL_MID = "#8a96a8"
BEZEL_LIGHT = "#e8edf5"
RING_BLACK = "#101319"
DIVIDER_COLOR = "#ccd4e0"

# Official BMW Roundel colors
BMW_BLUE = "#0066B1"
BMW_WHITE = "#FFFFFF"

# BMW M-Sport heritage tri-colors
M_LIGHT_BLUE = "#00a3e0"
M_DARK_BLUE = "#00205b"
M_RED = "#e21a21"

# Geometry radii (pixels)
R_OUTER_BEZEL = 208
R_OUTER_RIM = 202
R_INNER_BEZEL = 194
R_RING_INNER = 120
R_ROUNDEL = 114
R_TEXT = 157

# Timing and performance
FRAME_INTERVAL_MS = 16
DEFAULT_CRUISE_RPM = 120.0
SPORT_CRUISE_RPM = 240.0
MAX_RPM = 7000.0
REV_BURST_RPM = 6800.0


@dataclass
class AppConfig:
    plate_number: str = "KL 13 AY 4411"
    width: int = 840
    height: int = 800
    cruise_rpm: float = DEFAULT_CRUISE_RPM
    start_in_sport: bool = False
    skip_intro: bool = False
