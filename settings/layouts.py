#!/usr/bin/env python3

#
# ~/.config/qtile/layouts.py
#

from libqtile import layout
from settings.theme import LayoutSchemes


class LayoutsMaker:
    def __init__(self):
        self.layouts = None
        self.floating_layout = None

    def make_layouts(self):
        # Layouts I commonly use, with unused ones commented out
        if self.layouts is None:
            self.layouts = [
                layout.MonadTall(**LayoutSchemes.default),
                layout.Max(**LayoutSchemes.default),
                layout.Tile(**LayoutSchemes.default, expand=False),
                layout.Stack(**LayoutSchemes.default, num_stacks=2),
                layout.TreeTab(**LayoutSchemes.tree_tab),
                layout.Floating(**LayoutSchemes.floating),
                # layout.Zoomy(**LayoutSchemes.default),
                # layout.Bsp(**LayoutSchemes.default),
                # layout.Columns(**LayoutSchemes.default),
                # layout.Matrix(**LayoutSchemes.default),
                # layout.MonadWide(**LayoutSchemes.default),
                # layout.RatioTile(**LayoutSchemes.default),
                # layout.VerticalTile(**LayoutSchemes.default),
            ]

        return self.layouts

    def make_floating_layout(self):
        # Floating layout for windows that should default to floating
        if self.floating_layout is None:
            self.floating_layout = layout.Floating(
                auto_float_typesR=[
                    # Run the utility `xprop` to see the wm class and name of an X client
                    {"wmclass": "confirm"},
                    {"wmclass": "dialog"},
                    {"wmclass": "download"},
                    {"wmclass": "error"},
                    {"wmclass": "file_progress"},
                    {"wmclass": "notification"},
                    {"wmclass": "notify"},
                    {"wmclass": "popup_menu"},
                    {"wmclass": "splash"},
                    {"wmclass": "toolbar"},
                    {"wmclass": "confirmreset"},  # gitk
                    {"wmclass": "makebranch"},  # gitk
                    {"wmclass": "maketag"},  # gitkm
                    {"wname": "branchdialog"},  # gitk
                    {"wname": "pinentry"},  # GPG key password entry
                    {"wmclass": "ssh-askpass"},  # ssh-askpass
                ],
                **LayoutSchemes.floating
            )

        return self.floating_layout


# Temporary, moving to a more OOP approach
layouts_maker = LayoutsMaker()

# Layouts i commonly use, with unused ones commented out
layouts = layouts_maker.make_layouts()

# Floating layout for windows that should default to floating
floating_layout = layouts_maker.make_floating_layout()
