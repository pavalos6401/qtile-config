#!/usr/bin/env python3

#
# ~/.config/qtile/screens.py
#

from libqtile.config import Screen
from libqtile import widget, bar
from Xlib import display as xdisplay
from themes.nord import wall_dir, groupbox_defaults, current_screen_defaults, widget_defaults, color_schemes

color_scheme = color_schemes[1]

# Default settings for widgets
extesnion_defaults = widget_defaults.copy()

# Widgets for main screen/monitor
bar_widgets = [
    widget.Spacer(
        **color_scheme,
        length=6,
    ),
    widget.CurrentLayoutIcon(
        **color_scheme,
        scale=0.6,
    ),
    widget.GroupBox(
        **widget_defaults,
        **color_scheme,
        **groupbox_defaults,
        disable_drag=True,
    ),
    widget.WindowName(
        **widget_defaults,
        **color_scheme,
    ),
    widget.Systray(
        **widget_defaults,
        **color_scheme,
    ),
    widget.Clock(
        **widget_defaults,
        **color_scheme,
        format='%Y-%m-%d %a %I:%M %p'
    ),
    widget.QuickExit(
        **widget_defaults,
        **color_scheme,
    ),
    widget.Spacer(
        **color_scheme,
        length=6,
    ),
]

# Widgets for other screens/monitors
second_bar_widgets = [
    widget.Spacer(
        **color_scheme,
        length=6,
    ),
    widget.CurrentLayoutIcon(
        **color_scheme,
        scale=0.6,
    ),
    widget.GroupBox(
        **widget_defaults,
        **color_scheme,
        **groupbox_defaults,
        disable_drag=True,
    ),
    widget.Spacer(
        **color_scheme,
        length=16,
    ),
    widget.WindowName(
        **widget_defaults,
        **color_scheme,
    ),
    widget.Clock(
        **widget_defaults,
        **color_scheme,
        format='%Y-%m-%d %a %I:%M %p'
    ),
    widget.CurrentScreen(
        **widget_defaults,
        **color_scheme,
        **current_screen_defaults,
        active_text='active',
        inactive_text='inactive',
    ),
    widget.Spacer(
        **color_scheme,
        length=6,
    ),
]

# Initially set the screens to just the main screen/monitor
screens = [
    Screen(
        wallpaper=wall_dir,
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
            monitor = display.xrandr_get_output_info(
                output, resources.config_timestamp)
            preferred = False
            if hasattr(monitor, 'preferred'):
                preferred = monitor.preferred
            elif hasattr(monitor, 'num_preferred'):
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
            wallpaper=wall_dir,
            top=bar.Bar(
                second_bar_widgets,
                32,
                opacity=0.9,
                margin=6,
            ),
        )
    )
