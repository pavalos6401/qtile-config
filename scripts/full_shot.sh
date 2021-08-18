#!/bin/sh

#
# ~/.config/qtile/scripts/full-shot.sh
#

_now=$(date +"%Y_%m_%d-%H_%M_%S")
_file="${HOME}/Pictures/screenshots/full-${_now}.png"
maim -u "${_file}"
