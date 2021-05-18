#!/usr/bin/env python3

#
# ~/.config/qtile/settings/bindings.py
#

import os.path
from libqtile.config import Click, Drag, Key, Match
from libqtile.xkeysyms import keysyms
from settings.lazy_functions import *
from settings.apps import DefaultApps


# Holds keyboard keys to make using special keys easer.
class KeysHolder:
    def __init__(self):
        # set attribute for every key found in Qtile's keysyms
        for key in keysyms.keys():
            self_key = key.upper()
            if key[0] in range(0, 9):
                # For numbers, prepend K
                self_key = "K" + self_key
            setattr(self, self_key, key)

        # Common keys
        self.ENTER = self.RETURN = "Return"
        self.TAB = "Tab"
        self.SPACE = "space"
        # Uncommon keys
        self.EXCLAM = "exclam"
        self.QUOTEDBL = "quotedbl"
        # Common mod keys
        self.ALT = "mod1"
        self.SUPER = "mod4"
        self.CTRL = "control"
        self.SHIFT = "shift"
        # Uncommon mod keys
        self.HYPER = "mod3"
        # Special keys
        self.PRINT = "Print"
        self.DELETE = "Delete"
        self.HOME = "Home"
        self.END = "End"
        # Audio keys
        self.AUD_NEXT = "XF86AudioNext"
        self.AUD_PREV = "XF86AudioPrev"
        self.AUD_PLAY = "XF86AudioPlay"
        self.AUD_STOP = "XF86AudioStop"
        self.VOL_UP = "XF86AudioRaiseVolume"
        self.VOL_DOWN = "XF86AudioLowerVolume"
        self.MUTE = "XF86AudioMute"


# Holds mouse buttons to make them easier to use/read
class MouseButtons:
    def __init__(self):
        self.LEFT = "Button1"
        self.MIDDLE = "Button2"
        self.RIGHT = "Button3"
        self.WHEEL_UP = "Button4"
        self.WHEEL_DOWN = "Button5"
        self.WHEEL_LEFT = "Button6"
        self.WHEEL_RIGHT = "Button7"
        self.PREV = "Button8"
        self.NEXT = "Button9"


class KeysMaker:
    def __init__(self):
        self.scripts_path = os.path.expanduser("~/.config/qtile/scripts")
        self.a = DefaultApps()
        self.k = KeysHolder()
        self.keys = None

    def make_keys(self):
        # Keyboard shortcuts
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
                "space",
                lazy.layout.next(),
                desc="Switch window focus to other pane(s) of stack",
            ),
            Key(
                [self.k.SUPER],
                "k",
                lazy.layout.up(),
                desc="Move focus up in stack pane",
            ),
            Key(
                [self.k.SUPER],
                "j",
                lazy.layout.down(),
                desc="Move focus down in stack pane",
            ),
            Key(
                [self.k.SUPER],
                "h",
                lazy.layout.left(),
                desc="Move focus left in stack pane",
            ),
            Key(
                [self.k.SUPER],
                "l",
                lazy.layout.right(),
                desc="Move focus right in stack pane",
            ),
            # Move window
            Key(
                [self.k.SUPER, self.k.SHIFT],
                "space",
                lazy.layout.rotate(),
                lazy.layout.flip(),
                desc="Swap panes of split stack",
            ),
            Key(
                [self.k.SUPER, self.k.SHIFT],
                "k",
                lazy.layout.shuffle_up(),
                lazy.layout.flip_up(),
                desc="Move window up in current stack",
            ),
            Key(
                [self.k.SUPER, self.k.SHIFT],
                "j",
                lazy.layout.shuffle_down(),
                lazy.layout.flip_down(),
                desc="Move window down in current stack",
            ),
            Key(
                [self.k.SUPER, self.k.SHIFT],
                "h",
                lazy.layout.shuffle_left(),
                lazy.layout.flip_left(),
                desc="Move window left in current stack",
            ),
            Key(
                [self.k.SUPER, self.k.SHIFT],
                "l",
                lazy.layout.shuffle_right(),
                lazy.layout.flip_right(),
                desc="Move window right in current stack",
            ),
            # Resize window or increase number in master (tile)
            Key(
                [self.k.SUPER],
                "m",
                lazy.layout.maximize(),
                desc="Toggle between min and max sizes",
            ),
            Key(
                [self.k.SUPER, self.k.SHIFT],
                "m",
                lazy.window.toggle_fullscreen(),
                desc="Toggle fullscreen",
            ),
            Key(
                [self.k.SUPER, self.k.CTRL],
                "k",
                lazy.layout.grow(),
                lazy.layout.increase_nmaster(),
                desc="Expand window (monadtall), increase number in master pane (tile)",
            ),
            Key(
                [self.k.SUPER, self.k.CTRL],
                "j",
                lazy.layout.shrink(),
                lazy.layout.decrease_nmaster(),
                desc="Shrink window (monadtall), decrease number in master pane (tile)",
            ),
            # Toggle floating
            Key(
                [self.k.SUPER],
                "f",
                lazy.window.toggle_floating(),
                desc="Toggle floating mode on focused window",
            ),
            # Move floating windows to front
            Key(
                [self.k.SUPER, self.k.SHIFT],
                "f",
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
                "n",
                lazy.layout.normalize(),
                desc="Normalize window size ratios",
            ),
            # Close window
            Key(
                [self.k.SUPER],
                "w",
                lazy.window.kill(),
                desc="Close focused window",
            ),
            # Apps
            Key(
                [self.k.SUPER],
                "r",
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
                "b",
                lazy.spawn(self.a.WEB),
                desc="Open default browser",
            ),
            Key(
                [self.k.SUPER],
                "e",
                lazy.spawn(self.a.EDITOR),
                desc="Open default editor",
            ),
            # Screenshots
            Key(
                [],
                self.k.PRINT,
                lazy.spawn(f"'{self.scripts_path}/select-shot-clip.sh'"),
                desc="Clip selected area screenshot",
            ),
            Key(
                [self.k.SUPER],
                self.k.PRINT,
                lazy.spawn(f"'{self.scripts_path}/select-shot.sh'"),
                desc="Save selected area screenshot",
            ),
            Key(
                [self.k.SUPER, self.k.SHIFT],
                self.k.PRINT,
                lazy.spawn(f"'{self.scripts_path}/full-shot.sh'"),
                desc="Save fullscreen screenshot",
            ),
            # Volume controls
            Key(
                [],
                self.k.VOL_UP,
                lazy.spawn("pamixer -i 2"),
                desc="Raise volume",
            ),
            Key(
                [],
                self.k.VOL_DOWN,
                lazy.spawn("pamixer -d 2"),
                desc="Lower volume",
            ),
            Key(
                [],
                self.k.MUTE,
                lazy.spawn("pamixer -t"),
                desc="Toggle mute",
            ),
            # Lock screen
            Key(
                [self.k.SUPER, self.k.CTRL],
                "l",
                lazy.spawn(self.a.LOCKER),
                desc="Lock screen",
            ),
            # Restart qtile
            Key(
                [self.k.SUPER, self.k.CTRL],
                "r",
                lazy.restart(),
                desc="Restart qtile config",
            ),
            # Quit qtile
            Key(
                [self.k.SUPER, self.k.CTRL],
                "q",
                lazy.shutdown(),
                desc="Exit qtile",
            ),
        ]

        return self.keys

    # Add keybindings related to the groups
    def add_group_bindings(self, groups):
        # Create the keybindings related to groups
        for i in groups:
            self.keys.extend(
                [
                    # super + name = switch to group
                    Key(
                        [self.k.SUPER],
                        i.name,
                        lazy.group[i.name].toscreen(),
                        desc=f"Switch to group {i.name}",
                    ),
                    # super + shift + name = move focused window to group
                    Key(
                        [self.k.SUPER, self.k.SHIFT],
                        i.name,
                        lazy.window.togroup(i.name),
                        desc=f"Move focused window to group {i.name}",
                    ),
                ]
            )
        return self.keys


class MouseMaker:
    def __init__(self):
        self.k = KeysHolder()
        self.m = MouseButtons()
        self.mouse = None

    def make_mouse(self):
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


class BindingsMaker:
    def __init__(self):
        self.keys_maker = KeysMaker()
        self.mouse_maker = MouseMaker()

    def make_keys(self, groups):
        self.keys_maker.make_keys()
        return self.keys_maker.add_group_bindings(groups)

    def make_mouse(self):
        return self.mouse_maker.make_mouse()
