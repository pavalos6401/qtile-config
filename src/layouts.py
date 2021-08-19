#
# ~/.config/qtile/src/layouts.py
#

from libqtile import layout

from src.util.settings import ThemeConfig


class LayoutsMaker:
    """Creates the layouts to be used."""

    def __init__(self, t: ThemeConfig) -> None:
        """Inits the attributes."""

        self.t: ThemeConfig = t
        self.layouts: list = []
        self.floating_layout: layout.Floating = None

    def init_layouts(self) -> list:
        """Creates and returns the layouts used."""

        if not self.layouts:
            self.layouts = [
                # layout.Bsp(**self.t.layouts["default"]),
                layout.Columns(**self.t.layouts["default"], num_columns=3),
                layout.Floating(**self.t.layouts["floating"]),
                layout.Max(**self.t.layouts["default"]),
                # layout.Matrix(**self.t.layouts["default"]),
                layout.MonadTall(**self.t.layouts["default"]),
                # layout.MonadWide(**self.t.layouts["default"]),
                # layout.RatioTile(**self.t.layouts["default"]),
                layout.Stack(**self.t.layouts["default"]),
                layout.Tile(**self.t.layouts["default"]),
                # layout.TreeTab(**self.t.layouts["default"]),
                # layout.VerticalTile(**self.t.layouts["default"]),
                # layout.Zoomy(**self.t.layouts["default"]),
            ]

        return self.layouts

    def init_floating_layout(self) -> layout.Floating:
        """Creates and returns the floating layout used."""

        if self.floating_layout is None:
            self.floating_layout = layout.Floating(
                auto_float_typesR=[
                    # Run the utility `xprop`
                    # to see the wm class and name of an X client
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
                **self.t.layouts["floating"],
            )

        return self.floating_layout
