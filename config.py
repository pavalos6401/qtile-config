#!/usr/bin/env python3

#
# ~/.config/qtile/config.py
#

from src.bindings import KeysMaker, MouseMaker
from src.groups import GroupsMaker
from src.hooks import (
    autostart,
    float_firefox,
    float_pycharm,
    float_steam,
)
from src.layouts import LayoutsMaker
from src.screens import ScreensMaker


screens_maker: ScreensMaker = ScreensMaker()
keys_maker: KeysMaker = KeysMaker()
mouse_maker: MouseMaker = MouseMaker()
layouts_maker: LayoutsMaker = LayoutsMaker()
groups_maker: GroupsMaker = GroupsMaker()

keys: list = keys_maker.init_keys()

screens: list = screens_maker.init_screens()

layouts: list = layouts_maker.init_layouts()
floating_layout = layouts_maker.init_floating_layout()

groups: list = groups_maker.init_groups()
keys = keys_maker.init_groups(groups)

mouse: list = mouse_maker.init_mouse()


dgroups_key_binder = None
dgroups_app_rules: list = []
follow_mouse_focus: bool = True
bring_front_click: bool = False
cursor_warp: bool = False
auto_fullscreen: bool = True
focus_on_window_activation: str = "smart"

wmname: str = "LG3D"

