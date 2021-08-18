#
# ~/.config/qtile/src/util/paths.py
#

from os import PathLike
from pathlib import Path


ROOT_DIR: PathLike = Path("~/.config/qtile").expanduser()

scripts_folder: PathLike = ROOT_DIR / "scripts"

config_folder: PathLike = ROOT_DIR / "settings"

basic_config: PathLike = config_folder / "basic.toml"

