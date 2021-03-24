#!/usr/bin/env python3

#
# ~/.config/qtile/themes/embark_theme.py
#

wall_dir = '/home/pavalos/Pictures/wallpapers/magic-forest.jpg'

def_font = 'Fira Sans'               # Default font
sym_font = 'FiraCode Nerd Font'  # Font for symbols

# Embark theme colors
theme = dict(
    # Space Colors
    space0='100e23',
    space1='1e1c31',
    space2='2d2b40',
    space3='3e3859',
    space4='585273',
    # Astral colors
    astral0='8a889d',
    astral1='cbe3e7',
    # Nebula colors
    red='f48fb1',
    dark_red='f02e6e',
    green='a1efd3',
    dark_green='62d196',
    yellow='ffe6b3',
    dark_yellow='f2b482',
    blue='91ddff',
    dark_blue='65b2ff',
    purple='d4bfff',
    dark_purple='a37acc',
    cyan='87dfeb',
    dark_cyan='63f2f1',
)

# Color schemes for widgets
color_schemes = [
    dict(
        background=[theme['space1'], theme['space0']],
        foreground=[theme['astral1'], theme['astral0']],
    ),
    dict(
        background=[theme['space1'], theme['space0']],
        foreground=[theme['astral1'], theme['astral0']],
    ),
]

# Default settings for groupbox widgets
groupbox_defaults = dict(
    # Text colors
    active=[theme['astral0'], theme['astral1']],
    inactive=[theme['astral0'], theme['space4']],
    # Current screen colors
    highlight_method='line',
    highlight_color=[theme['space2'], theme['space0']],
    this_current_screen_border=theme['dark_cyan'],
    # Other screen colors
    other_screen_border=[theme['astral0'], theme['astral0']],
    other_current_screen_border=[theme['astral0'], theme['astral0']],
    # Urgent colors
    urgent_alert_method='text',
    urgent_text=[theme['red'], theme['dark_red']],
)

# Defaults for CurrentScreen widgets
current_screen_defaults = dict(
    active_color=theme['green'],
    inactive_color=theme['red'],
)

# Default settings for all other widgets
widget_defaults = dict(
    font=def_font,
    fontsize=12,
    padding=6,
)


# Default settings for any layout
layout_defaults = dict(
    margin=6,
    border_width=3,
    border_focus=theme['dark_cyan'],
    border_normal=theme['space1'],
    grow_amount=3,
)

# Default settings for tree tab layout
tree_tab_defaults = dict(
    font=def_font,
    sections=['FIRST', 'SECOND'],
    section_fontsize=11,
    bg_color=theme['space1'],
    active_bg=theme['purple'],
    inactive_bg=theme['dark_purple'],
    inactive_fg=theme['astral1'],
    padding_y=6,
    section_top=10,
    panel_width=320,
)
