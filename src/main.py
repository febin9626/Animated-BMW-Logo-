import argparse
import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from src.config import AppConfig
from src.app import BMWLogoApp


def parse_args():
    parser = argparse.ArgumentParser(
        description="Interactive BMW logo animation with engine telemetry."
    )
    parser.add_argument(
        "--plate",
        type=str,
        default="KL 13 AY 4411",
        help="Vehicle registration plate displayed on header",
    )
    parser.add_argument(
        "--cruise-rpm",
        type=float,
        default=120.0,
        help="Base cruise speed in RPM",
    )
    parser.add_argument(
        "--sport",
        action="store_true",
        help="Launch directly in BMW M-Sport mode",
    )
    parser.add_argument(
        "--skip-intro",
        action="store_true",
        help="Skip the opening perimeter drawing animation",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    config = AppConfig(
        plate_number=args.plate,
        cruise_rpm=args.cruise_rpm,
        start_in_sport=args.sport,
        skip_intro=args.skip_intro,
    )
    app = BMWLogoApp(config)
    app.run()


if __name__ == "__main__":
    main()
