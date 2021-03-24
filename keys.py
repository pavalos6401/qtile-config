#!/usr/bin/env python3

#
# ~/.config/qtile/keys.py
#

from libqtile.config import Click, Drag, Key, Match
from libqtile.lazy import lazy
from libqtile.xkeysyms import keysyms


# Easier to use for special keys
class KeysHolder:
    def __init__(self):
        # set attribute for every key found in Qtile's keysyms
        for key in keysyms.keys():
            self_key = key.upper()
            if key[0] in range(0, 9):
                # For numbers, prepend K
                self_key = 'K' + self_key
            setattr(self, self_key, key)

        # Common keys
        self.ENTER = self.RETURN = 'Return'
        self.TAB = 'Tab'
        self.SPACE = 'space'
        # Uncommon keys
        self.EXCLAM = self.EXCLAMATION = 'exclam'
        self.QUOTEDBL = 'quotedbl'
        # Common mod keys
        self.ALT = self.MOD1 = 'mod1'
        self.SUPER = self.MOD4 = 'mod4'
        self.CTRL = self.CONTROL = 'control'
        self.SHIFT = 'shift'
        # Uncommon mod keys
        self.HYPER = self.MOD3 = 'mod3'
        # Special keys
        self.PRINT = 'Print'
        self.DELETE = 'Delete'
        self.HOME = 'Home'
        self.END = 'End'
        # Audio keys
        self.AUD_NEXT = self.AUDIO_NEXT = 'XF86AudioNext'
        self.AUD_PREV = self.AUDIO_PREV = 'XF86AudioPrev'
        self.AUD_PLAY = self.AUDIO_PLAY = 'XF86AudioPlay'
        self.AUD_STOP = self.AUDIO_STOP = 'XF86AudioStop'
        self.VOL_UP = self.AUDIO_RAISE_VOL = 'XF86AudioRaiseVolume'
        self.VOL_DOWN = self.AUDIO_LOWER_VOL = 'XF86AudioLowerVolume'
        self.MUTE = self.AUDIO_MUTE = 'XF86AudioMute'


# Easier to use mouse callbacks
class MouseButtons:
    LEFT = BUTTON1 = 'Button1'
    MIDDLE = BUTTON2 = 'Button2'
    RIGHT = BUTTON3 = 'Button3'
    WHEEL_UP = BUTTON4 = 'Button4'
    WHEEL_DOWN = BUTTON5 = 'Button5'
    WHEEL_LEFT = BUTTON6 = 'Button6'
    WHEEL_RIGHT = BUTTON7 = 'Button7'
    PREV = BUTTON8 = 'Button8'
    NEXT = BUTTON9 = 'Button9'


# Default apps
class DefaultApps:
    TERM = 'kitty'
    WEB = 'firefox'
    LAUNCHER = 'rofi -show drun'
    EMACS = 'emacs'


k = KeysHolder()    # Holder for key buttons
m = MouseButtons()  # Holder for mouse buttons
a = DefaultApps()   # Holder for default apps

# Directories for useful shortcuts
SCRIPTS = '/home/pavalos/.config/qtile/scripts'


# Bring all floating windows to the top
# Useful when floating windows are lost
@lazy.function
def float_to_front(qtile):
    for group in qtile.groups:
        for window in group.windows:
            if window.floating:
                window.cmd_bring_to_front()


# Keyboard shortcuts
keys = [
    # Layout controls
    Key([k.SUPER], k.TAB, lazy.next_layout(), desc='Toggle between layouts'),
    # Change focus
    Key([k.SUPER], 'space', lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'),
    Key([k.SUPER], 'k', lazy.layout.up(),
        desc='Move focus up in stack pane'),
    Key([k.SUPER], 'j', lazy.layout.down(),
        desc='Move focus down in stack pane'),
    Key([k.SUPER], 'h', lazy.layout.left(),
        desc='Move focus left in stack pane'),
    Key([k.SUPER], 'l', lazy.layout.right(),
        desc='Move focus right in stack pane'),
    # Move window
    Key([k.SUPER, k.SHIFT], 'space', lazy.layout.rotate(),
        lazy.layout.flip(), desc='Swap panes of split stack'),
    Key([k.SUPER, k.SHIFT], 'k', lazy.layout.shuffle_up(),
        lazy.layout.flip_up(), desc='Move window up in current stack'),
    Key([k.SUPER, k.SHIFT], 'j', lazy.layout.shuffle_down(),
        lazy.layout.flip_down(), desc='Move window down in current stack'),
    Key([k.SUPER, k.SHIFT], 'h', lazy.layout.shuffle_left(),
        lazy.layout.flip_left(), desc='Move window left in current stack'),
    Key([k.SUPER, k.SHIFT], 'l', lazy.layout.shuffle_right(),
        lazy.layout.flip_right(), desc='Move window right in current stack'),
    # Resize window or increase number in master (tile)
    Key([k.SUPER], 'm', lazy.layout.maximize(),
        desc='Toggle between min and max sizes'),
    Key([k.SUPER, k.SHIFT], 'm', lazy.window.toggle_fullscreen(),
        desc='Toggle fulscreen'),
    Key([k.SUPER, k.CTRL], 'k', lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (monadtall), increase number in master pane (tile)'),
    Key([k.SUPER, k.CTRL], 'j', lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (monadtall), decrease number in master pane (tile)'),
    # Toggle floating
    Key([k.SUPER], 'f', lazy.window.toggle_floating(),
        desc='Toggle floating mode on focused window'),
    # Move floating windows to front
    Key([k.SUPER, k.SHIFT], 'f', float_to_front,
        desc='Move floating windows to front'),
    # Toggle split
    Key([k.SUPER, k.SHIFT], k.ENTER, lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'),
    # Reset windows/layout
    Key([k.SUPER], 'n', lazy.layout.normalize(),
        desc='Normalize window size ratios'),
    # Close window
    Key([k.SUPER], 'w', lazy.window.kill(), desc='Close focused window'),

    # Apps
    Key([k.SUPER], 'r', lazy.spawn(a.LAUNCHER), desc='Open default launcher'),
    Key([k.SUPER], k.ENTER, lazy.spawn(a.TERM), desc='Open default terminal'),
    Key([k.SUPER], 'b', lazy.spawn(a.WEB), desc='Open default browser'),
    Key([k.SUPER], 'e', lazy.spawn(a.EMACS), desc='Open emacs'),

    # Screenshots
    Key([], k.PRINT, lazy.spawn(f"'{SCRIPTS}/select-shot-clip.sh'"),
        desc='Clip selected area screenshot'),
    Key([k.SUPER], k.PRINT, lazy.spawn(f"'{SCRIPTS}/select-shot.sh'"),
        desc='Save selected area screenshot'),
    Key([k.SUPER, k.SHIFT], k.PRINT, lazy.spawn(f"'{SCRIPTS}/full-shot.sh'"),
        desc='Save fullscreen screenshot'),

    # Volume controls
    Key([], k.VOL_UP, lazy.spawn('pamixer -i 2'), desc='Raise volume'),
    Key([], k.VOL_DOWN, lazy.spawn('pamixer -d 2'), desc='Lower volume'),
    Key([], k.MUTE, lazy.spawn('pamixer -t'), desc='Toggle mute'),

    # Restart qtile
    Key([k.SUPER, k.CTRL], 'r', lazy.restart(), desc='Restart qtile config'),
    # Quit qtile
    Key([k.SUPER, k.CTRL], 'q', lazy.shutdown(), desc='Exit qtile'),
]

mouse = [
    # Drag windows (turns into a floating window)
    Drag([k.SUPER], m.LEFT, lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    # Resize windows (turns into a floating window)
    Drag([k.SUPER], m.RIGHT, lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    # Bring a floating window to the front
    Click([k.SUPER], m.MIDDLE, lazy.window.bring_to_front()),
    # Change group
    Click([k.SUPER], m.WHEEL_UP, lazy.screen.next_group()),
    Click([k.SUPER], m.WHEEL_DOWN, lazy.screen.prev_group()),
]
