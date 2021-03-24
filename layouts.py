#!/usr/bin/env python3

#
# ~/.config/qtile/layouts.py
#

from libqtile import layout
from themes.nord import layout_defaults, tree_tab_defaults

# Floating windows share the same defaults
floating_layout_defaults = layout_defaults.copy()
# Except for the border - floating windows have no border
floating_layout_defaults['border_width'] = 0

# Layouts i commonly use, with unused ones commented out
layouts = [
    layout.MonadTall(**layout_defaults),
    layout.Max(**layout_defaults),
    layout.Tile(**layout_defaults, expand=False),
    layout.Stack(**layout_defaults, num_stacks=2),
    layout.TreeTab(**tree_tab_defaults),
    layout.Floating(**floating_layout_defaults),
    # layout.Zoomy(**layout_defaults),
    # layout.Bsp(**layout_defaults),
    # layout.Columns(**layout_defaults),
    # layout.Matrix(**layout_defaults),
    # layout.MonadWide(**layout_defaults),
    # layout.RatioTile(**layout_defaults),
    # layout.VerticalTile(**layout_defaults),
]

# Floating layout for windows that should default to floating
floating_layout = layout.Floating(auto_float_typesR=[
    # Run the utility `xprop` to see the wm class and name of an X client
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'notify'},
    {'wmclass': 'popup_menu'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitkm
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
], **floating_layout_defaults)
