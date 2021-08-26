#
# ~/.config/qtile/src/groups.py
#

from libqtile.config import Group, Match

from src.util.settings import GroupsConfig


class GroupsMaker:
    """Makes the groups to be used."""

    def __init__(self) -> None:
        """Inits the attributes."""

        self.groups_settings: GroupsConfig = GroupsConfig()
        self.groups: list[Group] = []

    def init_groups(self) -> list[Group]:
        """Inits and returns the groups."""

        if not self.groups:
            self.groups = [
                Group(
                    f"{group['num']}",
                    layout=group["layout"],
                    label=group["icon"],
                    matches=[Match(wm_class=[m]) for m in group["matches"]],
                )
                for group in self.groups_settings.groups.values()
            ]

        return self.groups
