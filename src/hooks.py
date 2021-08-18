#
# ~/.config/qtile/src/hooks.py
#

from subprocess import call

from libqtile import hook

from src.util.paths import scripts_folder


@hook.subscribe.startup_once
def autostart() -> None:
    call([scripts_folder / "autostart.sh"])


@hook.subscribe.client_new
def float_firefox(window) -> None:
    wm_class = window.window.get_wm_class()
    w_name = window.window.get_name()
    if wm_class == ("Places", "firefox") and w_name == "Library":
        window.floating = True


@hook.subscribe.client_new
def float_pycharm(window) -> None:
    wm_class = window.window.get_wm_class()
    w_name = window.window.get_name()
    if (
        wm_class == ("jetbrains-pycharm-ce", "jetbrains-pycharm-ce") and w_name == " "
    ) or (wm_class == ("java-lang-Thread", "java-lang-Thread") and w_name == "win0"):
        window.floating = True


@hook.subscribe.client_new
def float_steam(window) -> None:
    wm_class = window.window.get_wm_class()
    w_name = window.window.get_name()
    if wm_class == ("Steam", "Steam") and (
        w_name != "Steam"
        or w_name == "Friends List"
        or w_name == "Screenshot Uploader"
        or w_name.startswith("Steam - News")
        or "PMaxSize" in window.window.get_wm_normal_hints().get("flags", ())
    ):
        window.floating = True

