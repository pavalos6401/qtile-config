#!/usr/bin/env python3

#
# ~/.config/qtile/settings/groups.py
#

from libqtile.config import Group, Match
from libqtile.lazy import lazy


class GroupsMaker:
    def __init__(self):
        # Dictionary of group labels, with their respective settings
        self.groups_settings = dict(
            web=dict(
                layout="monadtall",
                matches=[],
                icon="爵",
            ),
            dev=dict(
                layout="monadtall",
                matches=[
                    Match(wm_class=["code"]),
                ],
                icon="",
            ),
            doc=dict(
                layout="monadtall",
                matches=[],
                icon="",
            ),
            chat=dict(
                layout="stack",
                matches=[
                    Match(wm_class=["discord"]),
                    Match(wm_class=["zoom"]),
                    Match(wm_class=["skype"]),
                ],
                icon="",
            ),
            mus=dict(
                layout="monadtall",
                matches=[
                    Match(wm_class=["spotify"]),
                ],
                icon="",
            ),
            vid=dict(
                layout="max",
                matches=[
                    Match(wm_class=["vlc"]),
                    Match(wm_class=["mpv"]),
                ],
                icon="",
            ),
            gam=dict(
                layout="tile",
                matches=[
                    Match(wm_class=["Steam"]),
                    Match(wm_class=["lutris"]),
                    Match(wm_class=["supertuxkart"]),
                    Match(wm_class=["xonotic-sdl"]),
                ],
                icon="",
            ),
            sys=dict(
                layout="monadtall",
                matches=[],
                icon="",
            ),
            vm=dict(
                layout="treetab",
                matches=[
                    Match(wm_class=["virt-manager"]),
                    Match(wm_class=["remote-viewer"]),
                ],
                icon="",
            ),
        )
        self.groups = None

    def make_groups(self):
        self.groups = []
        num = 1
        for k, v in self.groups_settings.items():
            self.groups.append(
                Group(
                    f"{num}",
                    layout=v["layout"],
                    label=v["icon"],
                    matches=v["matches"],
                )
            )
            num += 1
        return self.groups
