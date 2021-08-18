#
# ~/.config/qtile/src/util/io.py
#

from libqtile.backend.x11.xkeysyms import keysyms


class KeysHolder:
    """Holds keyboard keys to make using keys consistent."""

    def __init__(self) -> None:
        """Inits the keys holder."""

        # Set attribute for every key found in Qtile's keysyms
        for key in keysyms.keys():
            self_key = key.upper()
            if key.isnumeric() and int(key) in range(0, 10):
                # For numbers, prepend K
                self_key = "K" + self_key
            setattr(self, self_key, key)

        # Modifier keys
        self.ALT = self.MOD1 = "mod1"
        self.HYPER = self.MOD3 = "mod3"
        self.SUPER = self.MOD4 = "mod4"
        self.CTRL = self.CONTROL = "control"
        self.SHIFT = "shift"
        # Common keys
        self.ENTER = self.RETURN
        self.DEL = self.DELETE
        # Special keys
        self.EXCLAMATION = self.EXCLAM
        self.DOUBLE_QUOTE = self.QUOTEDBL
        # Audio keys
        self.AUDIO_NEXT = self.AUD_NEXT = self.XF86AUDIONEXT
        self.AUDIO_PREV = self.AUD_PREV = self.XF86AUDIOPREV
        self.AUDIO_PLAY = self.AUD_PLAY = self.XF86AUDIOPLAY
        self.AUDIO_STOP = self.AUD_STOP = self.XF86AUDIOSTOP
        self.AUDIO_MUTE = self.AUD_MUTE = self.XF86AUDIOMUTE
        self.AUDIO_RAISE = self.AUD_RAISE = self.XF86AUDIORAISEVOLUME
        self.AUDIO_LOWER = self.AUD_LOWER = self.XF86AUDIOLOWERVOLUME


class MouseHolder:
    """Holds mouse buttons to make using buttons consistent."""

    def __init__(self) -> None:
        """Inits the mouse buttons holder."""

        # Common keys
        self.L = self.LEFT = "Button1"
        self.M = self.MIDDLE = "Button2"
        self.R = self.RIGHT = "Button3"
        # Wheel keys
        self.W_U = self.WHEEL_UP = "Button4"
        self.W_D = self.WHEEL_DOWN = "Button5"
        self.W_L = self.WHEEL_LEFT = "Button6"
        self.W_R = self.WHEEL_RIGHT = "Button7"
        # Extra keys
        self.PREV = self.PREVIOUS = "Button8"
        self.NEXT = "Button9"
