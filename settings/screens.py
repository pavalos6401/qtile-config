#!/usr/bin/env python3

#
# ~/.config/qtile/screens.py
#

from libqtile.config import Screen
from libqtile import widget, bar
from Xlib import display as xdisplay
from settings.theme import Wallpaper, WidgetSchemes


# Widgets for main screen/monitor
bar_widgets = [
    widget.Spacer(
        **WidgetSchemes.default,
        length=6,
    ),
    widget.CurrentLayoutIcon(
        **WidgetSchemes.default,
        scale=0.6,
    ),
    widget.GroupBox(
        **WidgetSchemes.groupbox,
        disable_drag=True,
    ),
    widget.WindowName(
        **WidgetSchemes.default,
    ),
    widget.Systray(
        **WidgetSchemes.default,
    ),
    widget.Clock(**WidgetSchemes.default, format="%Y-%m-%d %a %I:%M %p"),
    widget.QuickExit(
        **WidgetSchemes.default,
    ),
    widget.Spacer(
        **WidgetSchemes.default,
        length=6,
    ),
]

# Widgets for other screens/monitors
second_bar_widgets = [
    widget.Spacer(
        **WidgetSchemes.default,
        length=6,
    ),
    widget.CurrentLayoutIcon(
        **WidgetSchemes.default,
        scale=0.6,
    ),
    widget.GroupBox(
        **WidgetSchemes.groupbox,
        disable_drag=True,
    ),
    widget.Spacer(
        **WidgetSchemes.default,
        length=16,
    ),
    widget.WindowName(
        **WidgetSchemes.default,
    ),
    widget.Clock(
        **WidgetSchemes.default,
        format="%Y-%m-%d %a %I:%M %p",
    ),
    widget.CurrentScreen(
        **WidgetSchemes.current_screen,
        active_text="active",
        inactive_text="inactive",
    ),
    widget.Spacer(
        **WidgetSchemes.default,
        length=6,
    ),
]

# Initially set the screens to just the main screen/monitor
screens = [
    Screen(
        wallpaper=Wallpaper.path,
        wallpaper_mode="fill",
        top=bar.Bar(
            bar_widgets,
            32,
            opacity=0.9,
            margin=6,
        ),
    ),
]


# Function that returns how many monitors are active
def get_num_monitors():
    num_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
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


# Check if there are more monitors
if get_num_monitors() > 1:
    # If there are, add the screen for the secondary monitor
    screens.append(
        Screen(
            wallpaper=Wallpaper.path,
            wallpaper_mode="fill",
            top=bar.Bar(
                second_bar_widgets,
                32,
                opacity=0.9,
                margin=6,
            ),
        )
    )
