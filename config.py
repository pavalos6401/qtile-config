#!/usr/bin/env python3

#
# ~/.config/qtile/config.py
#

from src.util.apps import Apps
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
from src.util.io import KeysHolder, MouseHolder
from src.util.settings import ThemeConfig
from src.util.scripts import ScriptsHolder


# Config settings
a: Apps = Apps()
k: KeysHolder = KeysHolder()
s: ScriptsHolder = ScriptsHolder()
m: MouseHolder = MouseHolder()
t: ThemeConfig = ThemeConfig()

# Main config makers
screens_maker: ScreensMaker = ScreensMaker(t)
keys_maker: KeysMaker = KeysMaker(a, k, s)
mouse_maker: MouseMaker = MouseMaker(k, m)
layouts_maker: LayoutsMaker = LayoutsMaker(t)
groups_maker: GroupsMaker = GroupsMaker()

# Init config
keys = keys_maker.init_keys()
screens = screens_maker.init_screens()
layouts = layouts_maker.init_layouts()
floating_layout = layouts_maker.init_floating_layout()
groups = groups_maker.init_groups()
keys = keys_maker.init_groups(groups)
mouse = mouse_maker.init_mouse()

# Other settings
dgroups_key_binder = None
dgroups_app_rules: list = []
follow_mouse_focus: bool = True
bring_front_click: bool = False
cursor_warp: bool = False
auto_fullscreen: bool = True
focus_on_window_activation: str = "smart"

wmname: str = "LG3D"
