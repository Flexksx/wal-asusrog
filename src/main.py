import subprocess
import os
import json
import argparse

path_to_colors = os.path.expanduser("~/.cache/wal/colors.json")

colors = json.load(open(path_to_colors))


def set_static_color(colors: dict):
    color = colors["colors"]["color3"][1:]
    asusctl_command = f"asusctl led-mode static -c {color}"
    subprocess.run(asusctl_command.split(" "))


def set_breathe_color(colors: dict, set_speed="med"):
    color1 = colors["colors"]["color3"][1:]
    speed = set_speed
    asusctl_command = f"asusctl led-mode breathe -c {color1} -s {speed}"
    subprocess.run(asusctl_command.split(" "))


def set_strobe_color(colors: dict):
    color = colors["colors"]["color3"][1:]
    asusctl_command = f"asusctl led-mode pulse -c {color}"
    subprocess.run(asusctl_command.split(" "))


def main():
    parser = argparse.ArgumentParser(description="Control ASUS laptop LED modes using colors from wal.")
    parser.add_argument("mode", choices=["static", "breathe", "strobe"], help="LED mode to set")
    parser.add_argument("--speed", choices=["low", "med", "high"], default="med",
                        help="Speed for 'breathe' mode (default: med)")

    args = parser.parse_args()

    if args.mode == "static":
        set_static_color(colors)
    elif args.mode == "breathe":
        set_breathe_color(colors, set_speed=args.speed)
    elif args.mode == "strobe":
        set_strobe_color(colors)


if __name__ == "__main__":
    main()
