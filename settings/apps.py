#!/usr/bin/env python3

#
# ~/.config/qtile/settings/apps.py
#

from libqtile import qtile

# Default apps
class DefaultApps:
    EDITOR = "emacs"
    LAUNCHER = "rofi -show drun"
    LOCKER = "light-locker-command -l"
    TERM = "alacritty"
    WEB = "qutebrowser"


def open_launcher():
    qtile.cmd_spawn(DefaultApps.LAUNCHER)


def kill_window():
    qtile.cmd_spawn("xdotool getwindowfocus windowkill")
