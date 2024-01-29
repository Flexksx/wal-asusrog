import subprocess
import os
import json
path_to_colors = os.path.expanduser("~/.cache/wal/colors.json")

colors = json.load(open(path_to_colors))
print(colors)


def set_static_color(colors:dict):
    color= colors["colors"]["color3"][1:]
    asusctl_command = f"asusctl led-mode static -c {color}"
    subprocess.run(asusctl_command.split(" "))


def set_breathe_color(colors:dict):
    color1 = colors["colors"]["color0"][1:]
    color2 = colors["colors"]["color5"][1:]
    asusctl_command = f"asusctl led-mode breathe -C {color1} -c {color2}"
    subprocess.run(asusctl_command.split(" "))


def set_strobe_color(colors:dict):
    color = colors["colors"]["color3"][1:]
    asusctl_command = f"asusctl led-mode pulse -c {color}"
    subprocess.run(asusctl_command.split(" "))



set_strobe_color(colors)