#
# ~/.config/qtile/src/util/paths.py
#

from pathlib import Path


ROOT_DIR: Path = Path("~/.config/qtile").expanduser()

scripts_folder: Path = ROOT_DIR / "scripts"

config_folder: Path = ROOT_DIR / "settings"

basic_config: Path = config_folder / "basic.toml"
