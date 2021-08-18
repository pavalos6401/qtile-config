#
# ~/.config/qtile/src/bindings.py
#

from libqtile.config import Click, Drag, Key, Match
from libqtile.lazy import lazy

from src.util import paths
from src.util.apps import Apps
from src.util.io import KeysHolder, MouseHolder
from src.util.lazy_functions import float_to_front
from src.util.scripts import ScriptsHolder


class KeysMaker:
    """Makes the keybindings."""

    def __init__(self) -> None:
        """Inits the attributes."""

        self.a: Apps = Apps()
        self.k: KeysHolder = KeysHolder()
        self.s: ScriptsHolder = ScriptsHolder()
        self.keys: list[Key] = []

    def init_keys(self) -> list[Key]:
        """Inits and returns the keybindings."""

        if not self.keys:
            self.keys = [
                # Layout controls
                Key(
                    [self.k.SUPER],
                    self.k.TAB,
                    lazy.next_layout(),
                    desc="Toggle between layouts",
                ),
                # Change focus
                Key(
                    [self.k.SUPER],
                    self.k.SPACE,
                    lazy.layout.next(),
                    desc="Switch window focus to other pane(s) of stack",
                ),
                Key(
                    [self.k.SUPER],
                    self.k.K,
                    lazy.layout.up(),
                    desc="Move focus up in stack pane",
                ),
                Key(
                    [self.k.SUPER],
                    self.k.J,
                    lazy.layout.down(),
                    desc="Move focus down in stack pane",
                ),
                Key(
                    [self.k.SUPER],
                    self.k.H,
                    lazy.layout.left(),
                    desc="Move focus left in stack pane",
                ),
                Key(
                    [self.k.SUPER],
                    self.k.L,
                    lazy.layout.right(),
                    desc="Move focus right in stack pane",
                ),
                # Move window
                Key(
                    [self.k.SUPER, self.k.SHIFT],
                    self.k.SPACE,
                    lazy.layout.rotate(),
                    lazy.layout.flip(),
                    desc="Swap panes of split stack",
                ),
                Key(
                    [self.k.SUPER, self.k.SHIFT],
                    self.k.K,
                    lazy.layout.shuffle_up(),
                    lazy.layout.section_up(),
                    desc="Move window up in current stack",
                ),
                Key(
                    [self.k.SUPER, self.k.SHIFT],
                    self.k.J,
                    lazy.layout.shuffle_down(),
                    lazy.layout.section_down(),
                    desc="Move window down in current stack",
                ),
                Key(
                    [self.k.SUPER, self.k.SHIFT],
                    self.k.H,
                    lazy.layout.shuffle_left(),
                    desc="Move window left in current stack",
                ),
                Key(
                    [self.k.SUPER, self.k.SHIFT],
                    self.k.L,
                    lazy.layout.shuffle_right(),
                    desc="Move window right in current stack",
                ),
                # Resize window or increase number in master (tile)
                Key(
                    [self.k.SUPER],
                    self.k.M,
                    lazy.layout.maximize(),
                    desc="Toggle between min and max sizes",
                ),
                Key(
                    [self.k.SUPER, self.k.SHIFT],
                    self.k.M,
                    lazy.window.toggle_fullscreen(),
                    desc="Toggle fullscreen",
                ),
                Key(
                    [self.k.SUPER, self.k.CTRL],
                    self.k.K,
                    lazy.layout.grow(),
                    lazy.layout.increase_nmaster(),
                    desc=(
                        "Expand window (monadtall), increase number in master pane (tile)"
                    ),
                ),
                Key(
                    [self.k.SUPER, self.k.CTRL],
                    self.k.J,
                    lazy.layout.shrink(),
                    lazy.layout.decrease_nmaster(),
                    desc=(
                        "Shrink window (monadtall), decrease number in master pane (tile)"
                    ),
                ),
                # Toggle floating
                Key(
                    [self.k.SUPER],
                    self.k.F,
                    lazy.window.toggle_floating(),
                    desc="Toggle floating mode on focused window",
                ),
                # Move floating windows to front
                Key(
                    [self.k.SUPER, self.k.SHIFT],
                    self.k.F,
                    float_to_front,
                    desc="Move floating windows to front",
                ),
                # Toggle split
                Key(
                    [self.k.SUPER, self.k.SHIFT],
                    self.k.ENTER,
                    lazy.layout.toggle_split(),
                    desc="Toggle between split and unsplit sides of stack",
                ),
                # Reset windows/layout
                Key(
                    [self.k.SUPER],
                    self.k.N,
                    lazy.layout.normalize(),
                    desc="Normalize window size ratios",
                ),
                # Close window
                Key(
                    [self.k.SUPER],
                    self.k.W,
                    lazy.window.kill(),
                    desc="Close focused window",
                ),
                # Apps
                Key(
                    [self.k.SUPER],
                    self.k.R,
                    lazy.spawn(self.a.LAUNCHER),
                    desc="Open default launcher",
                ),
                Key(
                    [self.k.SUPER],
                    self.k.ENTER,
                    lazy.spawn(self.a.TERM),
                    desc="Open default terminal",
                ),
                Key(
                    [self.k.SUPER],
                    self.k.B,
                    lazy.spawn(self.a.WEB),
                    desc="Open default browser",
                ),
                Key(
                    [self.k.SUPER],
                    self.k.E,
                    lazy.spawn(self.a.EDITOR),
                    desc="Open default editor",
                ),
                # Screenshots
                Key(
                    [],
                    self.k.PRINT,
                    lazy.spawn(self.s.select_shot_clip),
                    desc="Clip selected area screenshot",
                ),
                Key(
                    [self.k.SUPER],
                    self.k.PRINT,
                    lazy.spawn(self.s.select_shot),
                    desc="Save selected area screenshot",
                ),
                Key(
                    [self.k.SUPER, self.k.SHIFT],
                    self.k.PRINT,
                    lazy.spawn(self.s.full_shot),
                    desc="Save fullscreen screenshot",
                ),
                # Volume controls
                Key(
                    [],
                    self.k.AUDIO_RAISE,
                    lazy.spawn("pamixer -i 2"),
                    desc="Raise volume",
                ),
                Key(
                    [],
                    self.k.AUDIO_LOWER,
                    lazy.spawn("pamixer -d 2"),
                    desc="Lower volume",
                ),
                Key(
                    [],
                    self.k.AUDIO_MUTE,
                    lazy.spawn("pamixer -t"),
                    desc="Toggle mute",
                ),
                # Lock screen
                Key(
                    [self.k.SUPER, self.k.CTRL],
                    self.k.L,
                    lazy.spawn(self.a.LOCKER),
                    desc="Lock screen",
                ),
                # Restart qtile
                Key(
                    [self.k.SUPER, self.k.CTRL],
                    self.k.R,
                    lazy.restart(),
                    desc="Restart qtile config",
                ),
                # Quit qtile
                Key(
                    [self.k.SUPER, self.k.CTRL],
                    self.k.Q,
                    lazy.shutdown(),
                    desc="Exit qtile",
                ),
            ]

        return self.keys

    def init_groups(self, groups) -> list[Key]:
        """Adds group bindings to the keybindings and returns keybindings."""

        for group in groups:
            self.keys.extend(
                [
                    # super + name = switch to group
                    Key(
                        [self.k.SUPER],
                        group.name,
                        lazy.group[group.name].toscreen(),
                        desc=f"Switch to group {group.name}",
                    ),
                    # super + shift + name = move focused window to group
                    Key(
                        [self.k.SUPER, self.k.SHIFT],
                        group.name,
                        lazy.window.togroup(group.name),
                        desc=f"Move focused window to group {group.name}",
                    ),
                ]
            )

        return self.keys


class MouseMaker:
    """Makes the mouse bindings."""

    def __init__(self) -> None:
        """Inits the attributes."""

        self.k: KeysHolder = KeysHolder()
        self.m: MouseHolder = MouseHolder()
        self.mouse: list = []

    def init_mouse(self) -> list:
        """Inits and returns the mouse bindings."""

        if not self.mouse:
            self.mouse = [
                # Drag windows (turns into a floating window)
                Drag(
                    [self.k.SUPER],
                    self.m.LEFT,
                    lazy.window.set_position_floating(),
                    start=lazy.window.get_position(),
                ),
                # Resize windows (turns into a floating window)
                Drag(
                    [self.k.SUPER],
                    self.m.RIGHT,
                    lazy.window.set_size_floating(),
                    start=lazy.window.get_size(),
                ),
                # Bring a floating window to the front
                Click(
                    [self.k.SUPER],
                    self.m.MIDDLE,
                    lazy.window.bring_to_front(),
                ),
                # Change group
                Click(
                    [self.k.SUPER],
                    self.m.WHEEL_UP,
                    lazy.screen.next_group(),
                ),
                Click(
                    [self.k.SUPER],
                    self.m.WHEEL_DOWN,
                    lazy.screen.prev_group(),
                ),
            ]

        return self.mouse

