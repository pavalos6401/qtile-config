#!/usr/bin/env python3

#
# ~/.config/qtile/themes/spaceduck.py
#

wall_dir = '/home/pavalos/Pictures/wallpapers/spacecity.png'

def_font = 'Fira Sans'              # Default font
sym_font = 'FiraCode Nerd Font'  # Font for symbols

# Spaceduck theme
theme = dict(
    # Base colors
    red='e33400',
    orange='e39400',
    green='5ccc96',
    yellow='f2ce00',
    purple='b3a1e6',
    purple2='7a5ccc',
    dark_purple='30365F',
    dark_purple2='686f9a',
    cyan='00a3cc',
    magenta='ce6f8f',
    # Special colors
    background='0f111b',
    foreground='ecf0c1',
    visual_selection='1b1c36',
    cursor_line='16172d',
    # Coloration colors
    grey='818596',
    grey2='c1c3cc',
    pure_white='ffffff',
    pure_black='000000',
)

# Color schemes for widgets
color_schemes = [
    dict(
        background=[theme['background'], theme['background']],
        foreground=[theme['foreground'], theme['foreground']],
    ),
    dict(
        background=[theme['background'], theme['background']],
        foreground=[theme['foreground'], theme['foreground']],
    ),
]

# Default settings for groupbox widgets
groupbox_defaults = dict(
    # Text colors
    active=[theme['foreground'], theme['foreground']],
    inactive=[theme['dark_purple'], theme['dark_purple']],
    # Current screen colors
    highlight_method='line',
    highlight_color=[theme['visual_selection'], theme['visual_selection']],
    this_current_screen_border=theme['purple'],
    this_screen_border=theme['dark_purple2'],
    # Other screen colors
    other_current_screen_border=[theme['dark_purple'], theme['dark_purple']],
    other_screen_border=[theme['dark_purple2'], theme['dark_purple2']],
    # Urgent colors
    urgent_alert_method='text',
    urgent_text=[theme['red'], theme['red']],
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
    border_focus=theme['green'],
    border_normal=theme['background'],
    grow_amount=3,
)

# Default settings for tree tab layout
tree_tab_defaults = dict(
    font=def_font,
    sections=['FIRST', 'SECOND'],
    section_fontsize=11,
    bg_color=theme['background'],
    active_bg=theme['purple'],
    active_fg=theme['foreground'],
    inactive_bg=theme['dark_purple'],
    inactive_fg=theme['dark_purple2'],
    padding_y=6,
    section_top=10,
    panel_width=320,
)
