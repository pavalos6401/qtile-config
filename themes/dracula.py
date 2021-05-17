#!/usr/bin/env python3

#
# ~/.config/qtile/themes/dracula.py
#


class Wallpaper:
    folder = "~/Pictures/wallpapers"
    path = ""  # Haven't found a wallpaper


class Fonts:
    default = "Fira Sans"
    symbols = "FiraCode Nerd Font


class Colors:
    background = "#282A36"
    current_line = "#44475A",
    selection = "#44475A",
    foreground = "#F8F8F2",
    comment = "#6272A4",
    cyan = "#8BE9FD",
    green ="#50FA7B",
    orange = "#FFB86C",
    pink = "#FF79C6",
    purple = "#BD93F9",
    red = "#FF5555",
    yellow = "#F1FA8C",


class LayoutSchemes:
    # Default settings for any layout
    layout_defaults = dict(
        margin=6,
        border_width=3,
        border_focus=Colors.pink,
        border_normal=Colors.background,
        grow_amount=3,
    )

    # Default settings for Floating layout
    floating = dict(
        border_width = 0,
        grow_ammount = 3,
    )

    # Default settings for TreeTab layout
    tree_tab_defaults = dict(
        font=Fonts.default,
        sections=["FIRST", "SECOND"],
        section_fontsize=11,
        bg_color=Colors.background,
        active_bg=Colors.selection,
        active_fg=Colors.foreground,
        inactive_bg=Colors.selection,
        inactive_fg=Colors.comment,
        padding_y=6,
        section_top=10,
        panel_width=320,
    )


class WidgetSchemes:
    # Default settings for all other widgets
    default = dict(
        font = Fonts.default,
        fontsize = 12,
        padding = 6,
        foreground = Colors.foreground,
        background = Colors.background,
    )

    # Default settings for GroupBox widgets
    groupbox = dict(
        **default,
        # Text colors
        active=Colors.foreground,
        inactive=Colors.comment,
        # Current screen colors
        highlight_method="line",
        highlight_color=Colors.selection,
        this_current_screen_border=Colors.purple,
        # Other screen colors
        other_screen_border=Colors.backgound,
        other_current_screen_border=Colors.background,
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

