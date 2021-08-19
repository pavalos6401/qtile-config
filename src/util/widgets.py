#
# ~/.config/qtile/src/util/widgets.py
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
    PulseVolume,
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

from src.util.apps import Apps
from src.util.app_functions import kill_window
from src.util.io import MouseHolder
from src.util.settings import ThemeConfig


class WidgetsMaker:
    """Creates the widgets used for the bar."""

    def __init__(self) -> None:
        """Inits the attributes."""

        self.a: Apps = Apps()
        self.m: MouseHolder = MouseHolder()
        self.t: ThemeConfig = ThemeConfig()
        self.widgets: list = []

    def init_widgets(self) -> list:
        """Inits and returns the widgets to be used."""

        if not self.widgets:
            self.widgets = [
                Spacer(
                    **self.t.widgets["default"],
                    length=6,
                ),
                TextBox(
                    **{**self.t.widgets["default"], **self.t.widgets["launcher"]},
                    font=self.t.fonts["symbols"],
                    text="",
                    mouse_callbacks={self.m.LEFT: self.a.open_launcher},
                ),
                Spacer(
                    **self.t.widgets["default"],
                    length=6,
                ),
                GroupBox(
                    **{
                        **self.t.widgets["default"],
                        **self.t.widgets["groupbox"],
                    },
                    font=self.t.fonts["symbols"],
                    disable_drag=True,
                ),
                CurrentLayoutIcon(
                    **{
                        **self.t.widgets["default"],
                        **self.t.widgets["current_layout_icon"],
                    },
                ),
                Spacer(
                    **self.t.widgets["default"],
                    length=6,
                ),
                WindowName(
                    **{
                        **self.t.widgets["default"],
                        **self.t.widgets["windowname"],
                    },
                    font=self.t.fonts["default"],
                    empty_group_string="Desktop",
                    mouse_callbacks={self.m.MIDDLE: kill_window},
                ),
                Spacer(
                    **self.t.widgets["default"],
                ),
                Systray(
                    **self.t.widgets["default"],
                    font=self.t.fonts["symbols"],
                ),
                Spacer(
                    **self.t.widgets["default"],
                    length=6,
                ),
                PulseVolume(
                    **{
                        **self.t.widgets["default"],
                        **self.t.widgets["volume"],
                    },
                    font=self.t.fonts["symbols"],
                    mosue_callbacks={self.m.RIGHT: self.a.open_volume_control},
                    fmt="墳 {}",
                ),
                Clock(
                    **{
                        **self.t.widgets["default"],
                        **self.t.widgets["calendar"],
                    },
                    font=self.t.fonts["symbols"],
                    format=" %a, %b %d",
                ),
                Clock(
                    **{
                        **self.t.widgets["default"],
                        **self.t.widgets["clock"],
                    },
                    font=self.t.fonts["symbols"],
                    format=" %H:%M",
                ),
                QuickExit(
                    **{
                        **self.t.widgets["default"],
                        **self.t.widgets["quickexit"],
                    },
                    font=self.t.fonts["symbols"],
                    default_text="",
                    countdown_format="{}",
                ),
                Spacer(
                    **self.t.widgets["default"],
                    length=6,
                ),
            ]

        return self.widgets
