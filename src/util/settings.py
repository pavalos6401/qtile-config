#
# ~/.config/qtile/src/util/settings.py
#


from pathlib import Path
from toml import load

from src.util.paths import basic_config


config: dict = {}
with open(basic_config, "r") as f:
    config = load(f)


class SectionConfig:
    """Base class to get a section of the config."""

    def __init__(self, section: str) -> None:
        """Inits the attributes."""

        self.section: str = section
        setattr(self, section, dict())
        if self.section in config:
            setattr(self, section, config[section])

        for sub, val in getattr(self, section).items():
            setattr(self, sub, val)


class AppsConfig(SectionConfig):
    """SectionConfig implementation for 'apps' section."""

    def __init__(self) -> None:
        """See base class."""

        super().__init__("apps")


class GroupsConfig(SectionConfig):
    """SectionConfig implementation for 'groups' section."""

    def __init__(self) -> None:
        """See base class."""

        super().__init__("groups")


class ThemeConfig(SectionConfig):
    """SectionConfig implementation for 'theme' section."""

    def __init__(self) -> None:
        """See base class."""

        super().__init__("theme")

        self.wallpaper: dict = {"path": None}
        if (
            "wallpaper" in self.theme
            and self.theme["wallpaper"]
            and "path" in self.theme["wallpaper"]
            and self.theme["wallpaper"]["path"]
        ):
            self.wallpaper = self.theme["wallpaper"]

        self.fonts: dict = {}
        if "fonts" in self.theme:
            self.fonts = self.theme["fonts"]

        self.layouts: dict = {}
        if "layouts" in self.theme:
            self.layouts = self.theme["layouts"]

        self.widgets: dict = {}
        if "widgets" in self.theme:
            self.widgets = self.theme["widgets"]
