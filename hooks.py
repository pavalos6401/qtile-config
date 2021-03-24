#!/usr/bin/env python3

#
# ~/.config/qtile/hooks.py
#

from libqtile import hook
import subprocess


@hook.subscribe.startup_once
def autostart():
    subprocess.call(["/home/pavalos/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.client_new
def float_firefox(window):
    wm_class = window.window.get_wm_class()
    w_name = window.window.get_name()
    if wm_class == ("Places", "firefox") and w_name == "Library":
        window.floating = True


@hook.subscribe.client_new
def float_pycharm(window):
    wm_class = window.window.get_wm_class()
    w_name = window.window.get_name()
    if (
        (
            wm_class == ("jetbrains-pycharm-ce", "jetbrains-pycharm-ce")
            and w_name == " "
        )
        or (
            wm_class == ("java-lang-Thread", "java-lang-Thread")
            and w_name == "win0"
        )
    ):
        window.floating = True


@hook.subscribe.client_new
def float_steam(window):
    wm_class = window.window.get_wm_class()
    w_name = window.window.get_name()
    if (
        wm_class == ("Steam", "Steam")
        and (
            w_name != "Steam"
            or w_name == "Friends List"
            or w_name == "Screenshot Uploader"
            or w_name.startswith("Steam - News")
            or "PMaxSize" in window.window.get_wm_normal_hints().get("flags", ())
        )
    ):
        window.floating = True
