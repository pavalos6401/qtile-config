#!/usr/bin/env python3

#
# ~/.config/qtile/config.py
#

from settings.screens import screens
from settings.keys import keys, mouse
from settings.layouts import layouts, floating_layout
from settings.groups import groups
from settings.hooks import *

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
