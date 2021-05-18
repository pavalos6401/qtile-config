#!/usr/bin/env python3

#
# ~/.config/qtile/config.py
#

from settings.screens import ScreensMaker
from settings.bindings import BindingsMaker
from settings.layouts import LayoutsMaker
from settings.groups import GroupsMaker
from settings.hooks import *

screens_maker = ScreensMaker()
bindings_maker = BindingsMaker()
layouts_maker = LayoutsMaker()
groups_maker = GroupsMaker()

screens = screens_maker.make_screens()

layouts = layouts_maker.make_layouts()

floating_layout = layouts_maker.make_floating_layout()

groups = groups_maker.make_groups()

keys = bindings_maker.make_keys(groups)
mouse = bindings_maker.make_mouse()


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
