#!/bin/bash

# Source the colors.sh file
source ~/.cache/wal/colors.sh

set_static_color() {
    local color="$1"
    asusctl_command="asusctl led-mode static -c $color"
    eval "$asusctl_command"
}

set_breathe_color() {
    local color="$1"
    local speed="$2"
    asusctl_command="asusctl led-mode breathe -c $color"

    if [ -n "$speed" ]; then
        asusctl_command+=" -s $speed"
    fi

    eval "$asusctl_command"
}

set_strobe_color() {
    local color="$1"
    asusctl_command="asusctl led-mode pulse -c $color"
    eval "$asusctl_command"
}

main() {
    mode="$1"
    s="$2"

    case "$mode" in
        static)
            set_static_color "${color3:1}"
        ;;
        breathe)
            set_breathe_color "${color3:1}" "$s"
        ;;
        strobe)
            set_strobe_color "${color3:1}"
        ;;
        help)
            echo "Usage: $0 <mode> [s]"
            echo "Modes:"
            echo "  static: Set the keyboard to a static color."
            echo "  breathe: Set the keyboard to breathe a color."
            echo "  strobe: Set the keyboard to strobe a color."
            echo "Speeds:"
            echo "  low: Slow speed."
            echo "  med: Medium speed."
            echo "  high: Fast speed."
        ;;
        *)
            echo "Error: Invalid mode. Choose from static, breathe, or strobe."
            exit 1
        ;;
    esac
}

# Parse command line arguments
if [ "$#" -lt 1 ]; then
    echo "Error: Missing arguments. Usage: $0 <mode> [speed]"
    exit 1
fi

main "$@"
