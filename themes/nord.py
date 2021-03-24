#!/usr/bin/env python3

#
# ~/.config/qtile/themes/nord.py
#

wall_dir = '/home/pavalos/Pictures/wallpapers/archlinux.png'

def_font = 'Source Sans Pro'           # Default font
sym_font = 'SourceCodePro Nerd Font'  # Font for symbols

# Nord theme colors
theme = dict(
    # Polar Night
    nord0='2E3440',  # background
    nord1='3B4252',  # elevated, more prominent or focused elements
    nord2='434C5E',  # line selection / highlight
    nord3='4C566A',  # indent- and wrap guide marker
    # Snow Storm
    nord4='D8DEE9',  # foreground
    nord5='E5E9F0',  # subtle/inconspicuous text elements
    nord6='ECEFF4',  # elevated elements
    # Frost
    nord7='8FBCBB',  # stand out
    nord8='88C0D0',  # primary elements
    nord9='81A1C1',  # secondary elements
    nord10='5E81AC',  # tertiary elements
    # Aurora
    nord11='BF616A',  # red
    nord12='D08770',  # orange
    nord13='EBCB8B',  # yellow
    nord14='A3BE8C',  # green
    nord15='B48EAD',  # purple
)

# Color schemes for widgets
color_schemes = [
    dict(
        background=[theme['nord1'], theme['nord1']],
        foreground=[theme['nord4'], theme['nord4']],
    ),
    dict(
        background=[theme['nord1'], theme['nord1']],
        foreground=[theme['nord4'], theme['nord4']],
    ),
]

# Default settings for groupbox widgets
groupbox_defaults = dict(
    # Text colors
    active=theme['nord4'],
    inactive=theme['nord3'],
    # Highlight colors
    highlight_method='line',
    highlight_color=theme['nord2'],
    # Focused screen
    this_current_screen_border=theme['nord7'],
    other_current_screen_border=theme['nord8'],
    # Unfocused screen colors
    this_screen_border=theme['nord9'],
    other_screen_border=theme['nord10'],
    # Urgent colors
    urgent_alert_method='text',
    urgent_text=theme['nord11'],
)

# Defaults for CurrentScreen widgets
current_screen_defaults = dict(
    active_color=theme['nord14'],
    inactive_color=theme['nord11'],
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
    border_focus=theme['nord8'],
    border_normal=theme['nord0'],
    grow_amount=3,
)

# Default settings for tree tab layout
tree_tab_defaults = dict(
    font=def_font,
    sections=['FIRST', 'SECOND'],
    section_fontsize=11,
    bg_color=theme['nord0'],
    active_bg=theme['nord2'],
    active_fg=theme['nord4'],
    inactive_bg=theme['nord2'],
    inactive_fg=theme['nord3'],
    padding_y=6,
    section_top=10,
    panel_width=320,
)
