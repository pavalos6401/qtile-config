#!/usr/bin/env python3

#
# ~/.config/qtile/settings/apps.py
#


# Default apps
class DefaultApps:
    def __init__(self):
        self.EDITOR = "emacs"
        self.LAUNCHER = "rofi -show drun"
        self.LOCKER = "light-locker-command -l"
        self.TERM = "alacritty"
        self.WEB = "google-chrome-stable"
