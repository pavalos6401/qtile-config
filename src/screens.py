#
# ~/.config/qtile/src/screens.py
#

from libqtile.bar import Bar
from libqtile.config import Screen

from src.util.settings import ThemeConfig
from src.util.widgets import WidgetsMaker


class ScreensMaker:
    """Creates the screens to be used."""

    def __init__(self) -> None:
        """Inits the attributes."""
        
        self.t: ThemeConfig = ThemeConfig()
        self.widgets_maker: WidgetsMaker = WidgetsMaker()
        self.screens: list[Screen] = []

    def init_screens(self) -> list[Screen]:
        """Creates and returns the screens to be used."""

        if not self.screens:
            self.screens = [
                Screen(
                    wallpaper=self.t.wallpaper["path"],
                    wallpaper_mode="fill",
                    top=Bar(
                        self.widgets_maker.init_widgets(),
                        32,
                        opacity=0.95,
                        margin=6,
                    ),
                ),
            ]

        return self.screens

