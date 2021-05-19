#!/usr/bin/env python3

#
# ~/.config/qtile/settings/screens.py
#

from Xlib import display as xdisplay
from libqtile import bar
from libqtile.config import Screen
from settings.theme import Wallpaper
from settings.widgets import WidgetsMaker


class ScreensMaker:
    def __init__(self):
        self.widgets_maker = WidgetsMaker()
        self.screens = None

    def count_monitors(self):
        num_monitors = 0
        try:
            display = xdisplay.Display()
            screen = display.screen()
            resources = screen.root.xrandr_get_screen_resources()

            for output in resources.outputs:
                monitor = display.xrandr_get_output_info(
                    output, resources.config_timestamp
                )
                preferred = False
                if hasattr(monitor, "preferred"):
                    preferred = monitor.preferred
                elif hasattr(monitor, "num_preferred"):
                    preferred = monitor.num_preferred
                if preferred:
                    num_monitors += 1
        except Exception as e:
            # Always set at least one monitor
            return 1
        else:
            return num_monitors

    def make_screens(self):
        # Initially set it to just the main monitor/screen
        self.screens = [
            Screen(
                wallpaper=Wallpaper.path,
                wallpaper_mode="fill",
                top=bar.Bar(
                    self.widgets_maker.make_main(),
                    32,
                    opacity=0.9,
                    margin=6,
                ),
            )
        ]

        # Check if there are more monitors
        for monitor in range(self.count_monitors() - 1):
            # If there are, add the screen for the other monitor(s)
            self.screens.append(
                Screen(
                    wallpaper=Wallpaper.path,
                    wallpaper_mode="fill",
                    top=bar.Bar(
                        self.widgets_maker.make_other(),
                        32,
                        opacity=0.9,
                        margin=6,
                    ),
                )
            )

        return self.screens
