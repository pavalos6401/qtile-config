# Qtile Config

## About

Qtile is a "full-featured, hackable tiling window manager written and configured
in Python". See the official [GitHub repository](https://github.com/qtile/qtile)
for more info.

My qtile config is split across various python files, to ease with readibility
and with configurability.

![screenshot](./screenshot.png)

For details on the keybindings, see the [documentation](./doc/keybindings.md)

## Requirements

Package: `qtile`

- Fonts: `adobe-source-code-pro-fonts`, `nerd-fonts-complete` (AUR)
- Screenshots: `maim`, `xclip`
- Browser: `qutebrowser`
- Terminal: `alacritty`
- Launcher: `rofi`
- Compositor: `picom`
- Volume control: `pamixer`
- Screen information: `python-xlib`
- Locker: `light-locker`
- Applets: `network-manager-applet`, `pasystray`, `redshift`

## Installation

1. Install requirements
2. Clone the repository into `~/.config/qtile`
