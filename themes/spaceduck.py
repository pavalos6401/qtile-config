#!/usr/bin/env python3

#
# ~/.config/qtile/themes/spaceduck.py
#


class Wallpaper:
    folder = "~/Pictures/wallpapers"
    path = f"{folder}/spacecity.png"


class Fonts:
    default = "Fira Sans"
    symbols = "FiraCode Nerd Font"


class Colors:
    # Base colors
    red = "#E33400"
    orange = "#E39400"
    green = "#5CCC96"
    yellow = "#F2CE00"
    purple = "#B3A1E6"
    purple2 = "#7A5CCC"
    dark_purple = "#30365F"
    dark_purple2 = "#686F9A"
    cyan = "#00A3CC"
    magenta = "#CE6F8F"
    # Special colors
    background = "#0F111B"
    foreground = "#ECF0C1"
    visual_selection = "#1B1C36"
    cursor_line = "#16172D"
    # Coloration colors
    grey = "#818596"
    grey2 = "#C1C3CC"
    pure_white = "#FFFFFF"
    pure_black = "#000000"


class LayoutSchemes:
    # Default settings for any layout
    default = dict(
        margin=6,
        border_width=3,
        border_focus=Colors.green,
        border_normal=Colors.background,
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
        bg_color=Colors.background,
        active_bg=Colors.purple,
        active_fg=Colors.foreground,
        inactive_bg=Colors.dark_purple,
        inactive_fg=Colors.dark_purple2,
        padding_y=6,
        section_top=10,
        panel_width=320,
    )


class WidgetSchemes:
    # Default settings for all widgets
    widget_defaults = dict(
        font=Fonts.default,
        fontsize=12,
        padding=6,
        foreground=Colors.foreground,
        background=Colors.background,
    )

    # Default settings for GroupBox widgets
    groupbox_defaults = dict(
        **default,
        # Text colors
        active=Colors.foreground,
        inactive=Colors.dark_purple,
        # Current screen colors
        highlight_method="line",
        highlight_color=Colors.visual_selection,
        this_current_screen_border=Colors.purple,
        this_screen_border=Colors.dark_purple2,
        # Other screen colors
        other_current_screen_border=Colors.dark_purple,
        other_screen_border=Colors.dark_purple2,
        # Urgent colors
        urgent_alert_method="text",
        urgent_text=Colors.red,
    )

    # Defaults for CurrentScreen widgets
    current_screen = dict(
        **default,
        active_color=Colors.green,
        inactive_color=Colors.red,
    )
