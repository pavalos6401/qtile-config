#!/bin/sh

#
# ~/.config/qtile/scripts/autostart.sh
#

light-locker &
picom &
redshift-gtk &
nm-applet &
emacs --daemon &
1password --silent &
gnome-keyring-daemon --start &
