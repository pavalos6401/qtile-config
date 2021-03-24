#!/usr/bin/env python3

#
# ~/.config/qtile/config.py
#

from screens import screens
from keys import keys, mouse
from layouts import layouts, floating_layout
from groups import groups
from hooks import *

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
