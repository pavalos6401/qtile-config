#
# ~/.config/qtile/src/util/scripts.py
#

from src.util.paths import scripts_folder


class ScriptsHolder:
    """Class to hold scripts."""

    def __init__(self) -> None:
        """Inits the attributes."""

        for script in scripts_folder.iterdir():
            setattr(self, script.stem, str(script))
