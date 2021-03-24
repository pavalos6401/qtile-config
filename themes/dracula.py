#!/usr/bin/env python3

#
# ~/.config/qtile/themes/dracula.py
#

wall_dir = ''

def_font = 'Fira Sans'           # Default font
sym_font = 'FiraCode Nerd Font'  # Font for symbols

# Dracula theme colors
theme = dict(
    background='282a36',
    current_line='44475a',
    selection='44475a',
    foreground='f8f8f2',
    comment='6272a4',
    cyan='8be9fd',
    green='50fa7b',
    orange='ffb86c',
    pink='ff79c6',
    purple='bd93f9',
    red='ff5555',
    yellow='f1fa8c',
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
    inactive=[theme['comment'], theme['comment']],
    # Current screen colors
    highlight_method='line',
    highlight_color=[theme['selection'], theme['selection']],
    this_current_screen_border=theme['purple'],
    # Other screen colors
    other_screen_border=[theme['backgound'], theme['background']],
    other_current_screen_border=[theme['background'], theme['background']],
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
    border_focus=theme['pink'],
    border_normal=theme['background'],
    grow_amount=3,
)

# Default settings for tree tab layout
tree_tab_defaults = dict(
    font=def_font,
    sections=['FIRST', 'SECOND'],
    section_fontsize=11,
    bg_color=theme['background'],
    active_bg=theme['selection'],
    active_fg=theme['foreground'],
    inactive_bg=theme['selection'],
    inactive_fg=theme['comment'],
    padding_y=6,
    section_top=10,
    panel_width=320,
)
