#!/usr/bin/env python3

#
# ~/.config/qtile/settings/widgets.py
#

from libqtile.widget import (
    # Battery,
    # CapsNumLockIndicator,
    # CheckUpdates,
    Clock,
    # CurrentLayout,
    CurrentLayoutIcon,
    GroupBox,
    # Memory,
    # Net,
    # Prompt,
    Sep,
    Spacer,
    Systray,
    TaskList,
    TextBox,
    # ThermalSensor,
    QuickExit,
    Volume,
    WindowCount,
    WindowName,
    # Wlan,
)
from settings.apps import *
from settings.bindings import MouseButtons
from settings.theme import WidgetSchemes, Colors, Fonts


class WidgetsMaker:
    def __init__(self):
        self.m = MouseButtons()
        self.main_widgets = None
        self.other_widgets = None

    def make_main(self):
        # Widgets for primary screen/monitor
        if self.main_widgets is None:
            self.main_widgets = [
                Spacer(
                    **WidgetSchemes.spacer,
                    length=6,
                ),
                TextBox(
                    **WidgetSchemes.launcher,
                    text="",
                    mouse_callbacks={self.m.LEFT: open_launcher},
                ),
                Spacer(
                    **WidgetSchemes.spacer,
                    length=6,
                ),
                GroupBox(
                    **WidgetSchemes.groupbox,
                    disable_drag=True,
                ),
                CurrentLayoutIcon(
                    **WidgetSchemes.current_layout_icon,
                ),
                Spacer(
                    **WidgetSchemes.spacer,
                    length=6,
                ),
                WindowName(
                    **WidgetSchemes.windowname,
                    empty_group_string="Desktop",
                    mouse_callbacks={self.m.MIDDLE: kill_window},
                ),
                Spacer(
                    **WidgetSchemes.spacer,
                ),
                Systray(
                    **WidgetSchemes.default,
                ),
                Spacer(
                    **WidgetSchemes.spacer,
                    length=6,
                ),
                Volume(
                    **WidgetSchemes.volume,
                    mouse_callbacks={self.m.RIGHT: open_volume_control},
                    fmt="墳 {}",
                ),
                Clock(
                    **WidgetSchemes.calendar,
                    format=" %a, %b %d",
                ),
                Clock(
                    **WidgetSchemes.clock,
                    format=" %H:%M",
                ),
                QuickExit(
                    **WidgetSchemes.quickexit,
                    default_text="",
                    countdown_format="{}",
                ),
                Spacer(
                    **WidgetSchemes.spacer,
                    length=6,
                ),
            ]

        return self.main_widgets

    def make_other(self):
        # Widgets for other screen/monitor
        if self.other_widgets is None:
            self.other_widgets = [
                Spacer(
                    **WidgetSchemes.default,
                    length=6,
                ),
                CurrentLayoutIcon(
                    **WidgetSchemes.current_layout_icon,
                ),
                GroupBox(
                    **WidgetSchemes.groupbox,
                    disable_drag=True,
                ),
                Spacer(
                    **WidgetSchemes.default,
                    length=16,
                ),
                WindowName(
                    **WidgetSchemes.default,
                ),
                Clock(
                    **WidgetSchemes.default,
                    format="%Y-%m-%d %a %I:%M %p",
                ),
                CurrentScreen(
                    **WidgetSchemes.current_screen,
                    active_text="active",
                    inactive_text="inactive",
                ),
                Spacer(
                    **WidgetSchemes.default,
                    length=6,
                ),
            ]

        return self.other_widgets
