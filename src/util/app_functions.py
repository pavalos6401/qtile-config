#
# ~/.config/qtile/src/util/app_functions.py
#

from libqtile import qtile


def kill_window() -> None:
    """Kills focused window."""

    qtile.cmd_spawn("xdotool getwindowfocus windowkill")
