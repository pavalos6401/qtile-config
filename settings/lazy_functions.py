#!/usr/bin/env python3

#
# ~/.config/qtile/settings/lazy_functions.py
#

from libqtile.lazy import lazy

# Bring all floating windows to the top
# Useful when floating windows are lost
@lazy.function
def float_to_front(qtile):
    for group in qtile.groups:
        for window in group.windows:
            if window.floating:
                window.cmd_bring_to_front()
