#!/bin/sh

#
# ~/.config/qtile/scripts/select-shot-clip.sh
#

maim -su | xclip -selection clipboard -t image/png
