#!/usr/bin/env python3

#
# ~/.config/qtile/settings/apps.py
#

from libqtile import qtile

# Default apps
class DefaultApps:
    EDITOR = "emacs -c -a emacs"
    LAUNCHER = "rofi -show drun"
    LOCKER = "light-locker-command -l"
    TERM = "alacritty"
    WEB = "qutebrowser"
    VOLUME = "pavucontrol"


def open_launcher():
    qtile.cmd_spawn(DefaultApps.LAUNCHER)


def open_volume_control():
    qtile.cmd_spawn(DefaultApps.VOLUME)


def kill_window():
    qtile.cmd_spawn("xdotool getwindowfocus windowkill")
