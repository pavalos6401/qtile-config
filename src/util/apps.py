#
# ~/.config/qtile/src/util/apps.py
#

from libqtile import qtile

from src.util.settings import AppsConfig


class Apps:
    """Holds the commonly used apps and related functions."""

    def __init__(self) -> None:
        """Inits the attributes."""

        a = AppsConfig()
        for app, name in a.apps.items():
            setattr(self, app, name)

    def list_apps(self) -> dict[str, str]:
        """Lists the applications saved."""

        return vars(self)

    def open_app(self, app: str) -> None:
        """Opens the default app given the name."""

        if hasattr(self, app):
            qtile.cmd_spawn(getattr(self, app))

    def open_launcher(self) -> None:
        """Opens the default app launcher."""

        self.open_app("LAUNCHER")

    def open_volume_control(self) -> None:
        """Opens the default volume control app."""

        self.open_app("VOLUME")
