#!/usr/bin/env python3

#
# ~/.config/qtile/settings/groups.py
#

from libqtile.config import Group, Match, Key
from libqtile.lazy import lazy
from settings.keys import keys, KeysHolder


class GroupsMaker:
    def __init__(self):
        # Dictionary of group labels, with their respective settings
        self.groups_settings = dict(
            web=dict(layout="monadtall", matches=[]),
            dev=dict(layout="monadtall", matches=[Match(wm_class=["code"])]),
            doc=dict(layout="monadtall", matches=[]),
            chat=dict(
                layout="stack",
                matches=[
                    Match(wm_class=["discord"]),
                    Match(wm_class=["zoom"]),
                    Match(wm_class=["skype"]),
                ],
            ),
            mus=dict(layout="monadtall", matches=[Match(wm_class=["spotify"])]),
            vid=dict(layout="max", matches=[Match(wm_class=["vlc"])]),
            gam=dict(
                layout="tile",
                matches=[
                    Match(wm_class=["Steam"]),
                    Match(wm_class=["lutris"]),
                    Match(wm_class=["supertuxkart"]),
                    Match(wm_class=["xonotic-sdl"]),
                ],
            ),
            sys=dict(layout="monadtall", matches=[]),
            vm=dict(
                layout="treetab",
                matches=[
                    Match(wm_class=["virt-manager"]),
                    Match(wm_class=["remote-viewer"]),
                ],
            ),
        )
        self.groups = None
        self.keybindings = None
        self.k = KeysHolder()

    def make_groups(self):
        self.groups = []
        num = 1
        for k, v in self.groups_settings.items():
            self.groups.append(
                Group(f"{num}", layout=v["layout"], label=k, matches=v["matches"])
            )
            num += 1
        return self.groups

    def make_keybindings(self):
        self.keybindings = []
        # Create the keybindings related to groups
        for i in self.groups:
            self.keybindings.extend(
                [
                    # super + name = switch to group
                    Key(
                        [self.k.SUPER],
                        i.name,
                        lazy.group[i.name].toscreen(),
                        desc="Switch to group {}".format(i.name),
                    ),
                    # super + shift + name = move focused window to group
                    Key(
                        [self.k.SUPER, self.k.SHIFT],
                        i.name,
                        lazy.window.togroup(i.name),
                        desc="Move focused window to group {}".format(i.name),
                    ),
                ]
            )
        return self.keybindings


# Temporary, moving to a more OOP structure
groups_maker = GroupsMaker()

# Groups I find useful in my workflow
groups = groups_maker.make_groups()

# Add group-related bindings to the keybindings
keys.extend(groups_maker.make_keybindings())
