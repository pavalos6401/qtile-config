#!/usr/bin/env python3

#
# ~/.config/qtile/themes/nord.py
#

import os.path


class Wallpaper:
    folder = "~/Pictures/wallpapers"
    path = f"{folder}/the-great-wave.png"


class Fonts:
    default = "Source Sans Pro"
    symbols = "Sauce Code Pro Nerd Font"


class Colors:
    # Polar Night
    nord0 = "#2E3440"  # Background
    nord1 = "#3B4252"  # Elevated, more prominent or focused elements
    nord2 = "#434C5E"  # Line selection / highlight
    nord3 = "#4C566A"  # Indent- and wrap guide marker
    # Snow Storm
    nord4 = "#D8DEE9"  # Foreground
    nord5 = "#E5E9F0"  # Subtle/inconspicuous text elements
    nord6 = "#ECEFF4"  # Elevated elements
    # Frost
    nord7 = "#8FBCBB"  # Stand out
    nord8 = "#88C0D0"  # Primary elements
    nord9 = "#81A1C1"  # Secondary elements
    nord10 = "#5E81AC"  # Tertiary elements
    # Aurora
    nord11 = "#BF616A"  # Red
    nord12 = "#D08770"  # Orange
    nord13 = "#EBCB8B"  # Yellow
    nord14 = "#A3BE8C"  # Green
    nord15 = "#B48EAD"  # Purple


class LayoutSchemes:
    # Default settings for all layouts
    default = dict(
        margin=6,
        border_width=3,
        border_focus=Colors.nord8,
        border_normal=Colors.nord0,
        grow_amount=3,
    )

    # Default settings for Floating layouts
    floating = dict(
        border_width=0,
        grow_amount=3,
    )

    # Default settings for TreeTab layouts
    tree_tab = dict(
        font=Fonts.default,
        sections=["FIRST", "SECOND"],
        section_fontsize=11,
        bg_color=Colors.nord0,
        active_bg=Colors.nord2,
        active_fg=Colors.nord4,
        inactive_bg=Colors.nord2,
        inactive_fg=Colors.nord3,
        padding_y=6,
        section_top=10,
        panel_width=320,
    )


class WidgetSchemes:
    # Default settings for all widgets
    default = dict(
        font=Fonts.symbols,
        fontsize=14,
        padding=6,
        foreground=Colors.nord4,
        background=Colors.nord0,
    )

    icon = dict(
        font=Fonts.symbols,
        fontsize=16,
        padding=6,
        foreground=Colors.nord4,
        background=Colors.nord0,
    )

    calendar = dict(
        font=Fonts.symbols,
        fontsize=16,
        padding=6,
        foreground=Colors.nord13,
        background=Colors.nord0,
    )

    clock = dict(
        font=Fonts.symbols,
        fontsize=16,
        padding=6,
        foreground=Colors.nord14,
        background=Colors.nord0,
    )

    # Settings for Icon TextBox
    launcher = dict(
        font=Fonts.symbols,
        fontsize=18,
        padding=6,
        foreground=Colors.nord9,
        background=Colors.nord0,
    )

    windowcount = dict(
        font=Fonts.symbols,
        fontsize=14,
        padding=6,
        foreground=Colors.nord7,
        background=Colors.nord0,
    )

    windowname = dict(
        font=Fonts.default,
        fontsize=14,
        padding=6,
        foreground=Colors.nord7,
        background=Colors.nord0,
    )

    quickexit = dict(
        font=Fonts.symbols,
        fontsize=18,
        padding=6,
        foreground=Colors.nord10,
        background=Colors.nord0,
    )

    # CurrentLayoutIcon scheme
    current_layout_icon = dict(
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons/nord")],
        foreground=Colors.nord4,
        background=Colors.nord0,
        padding=6,
        scale=0.6,
    )

    # Settings for GroupBox widgets
    groupbox = dict(
        font=Fonts.symbols,
        fontsize=18,
        padding=8,
        foreground=Colors.nord8,
        background=Colors.nord0,
        borderwidth=0,
        # Text colors
        active=Colors.nord4,
        inactive=Colors.nord3,
        # Highlight colors
        highlight_method="text",
        highlight_color=Colors.nord2,
        # Focused screen
        this_current_screen_border=Colors.nord7,
        other_current_screen_border=Colors.nord8,
        # Unfocused screen colors
        this_screen_border=Colors.nord9,
        other_screen_border=Colors.nord10,
        # Urgent colors
        urgent_alert_method="text",
        urgent_text=Colors.nord11,
    )

    # Defaults for CurrentScreen widgets
    current_screen = dict(
        **default,
        active_color=Colors.nord14,
        inactive_color=Colors.nord11,
    )
