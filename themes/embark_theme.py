#!/usr/bin/env python3

#
# ~/.config/qtile/themes/embark_theme.py
#


class Wallpaper:
    folder = "~/Pictures/wallpapers"
    path = f"{folder}/magic-forest.jpg"


class Fonts:
    default = "Fira Sans"
    symbols = "FiraCode Nerd Font"


class Colors:
    # Space Colors
    space0 = ("#100E23",)
    space1 = ("#1E1C31",)
    space2 = ("#2D2B40",)
    space3 = ("#3E3859",)
    space4 = ("#585273",)
    # Astral colors
    astral0 = ("#8A889D",)
    astral1 = ("#CBE3E7",)
    # Nebula colors
    red = ("#F48FB1",)
    dark_red = ("#F02E6E",)
    green = ("#A1EFD3",)
    dark_green = ("#62D196",)
    yellow = ("#FFE6B3",)
    dark_yellow = ("#F2B482",)
    blue = ("#91DDFF",)
    dark_blue = ("#65B2FF",)
    purple = ("#D4BFFF",)
    dark_purple = ("#A37ACC",)
    cyan = ("#87DFEB",)
    dark_cyan = ("#63F2F1",)


class LayoutSchemes:
    # Default settings for any layout
    defaults = dict(
        margin=6,
        border_width=3,
        border_focus=Colors.dark_cyan,
        border_normal=Colors.space1,
        grow_amount=3,
    )

    # Default settings for Floating layout
    floating = dict(
        border_width=0,
        grow_amount=3,
    )

    # Default settings for TreeTab layout
    tree_tab = dict(
        font=Fonts.default,
        sections=["FIRST", "SECOND"],
        section_fontsize=11,
        bg_color=Colors.space1,
        active_bg=Colors.purple,
        inactive_bg=Colors.dark_purple,
        inactive_fg=Colors.astral1,
        padding_y=6,
        section_top=10,
        panel_width=320,
    )


class WidgetSchemes:
    # Default settings for all other widgets
    defaults = dict(
        font=Fonts.default,
        fontsize=12,
        padding=6,
        foreground=[Colors.astral1, Colors.astral0],
        background=[Colors.space1, Colors.space0],
    )

    # Default settings for GroupBox widgets
    groupbox = dict(
        **default,
        # Text colors
        active=[Colors.astral0, Colors.astral1],
        inactive=[Colors.astral0, Colors.space4],
        # Current screen colors
        highlight_method="line",
        highlight_color=[Colors.space2, Colors.space0],
        this_current_screen_border=Colors.dark_cyan,
        # Other screen colors
        other_screen_border=Colors.astral0,
        other_current_screen_border=Colors.astral0,
        # Urgent colors
        urgent_alert_method="text",
        urgent_text=[Colors.red, Colors.dark_red],
    )

    # Defaults for CurrentScreen widgets
    current_screen = dict(
        **default,
        active_color=Colors.green,
        inactive_color=Colors.red,
    )
