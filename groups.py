#!/usr/bin/env python3

#
# ~/.config/qtile/groups.py
#

from libqtile.config import Group, Match, Key
from libqtile.lazy import lazy

from keys import k, keys

# Dictionary with window rules.
# Places windows that match to the appropriate group.
matches_rule = {
    'web': [],
    'dev': [Match(wm_class=["code"])],
    'doc': [],
    'chat': [Match(wm_class=["discord"]), Match(wm_class=["zoom"]),
             Match(wm_class=["skype"])],
    'mus': [Match(wm_class=["spotify"])],
    'vid': [Match(wm_class=["vlc"])],
    'gam': [Match(wm_class=["Steam"]), Match(wm_class=["lutris"]),
            Match(wm_class=["supertuxkart"]), Match(wm_class=["xonotic-sdl"])],
    'sys': [],
    'vm': [Match(wm_class=["virt-manager"]), Match(wm_class=["remote-viewer"])],
}

# Groups I find useful in my workflow
groups = [
    Group('1', layout='monadtall', label='web', matches=matches_rule['web']),
    Group('2', layout='monadtall', label='dev', matches=matches_rule['dev']),
    Group('3', layout='monadtall', label='doc', matches=matches_rule['doc']),
    Group('4', layout='stack', label='chat', matches=matches_rule['chat']),
    Group('5', layout='monadtall', label='mus', matches=matches_rule['mus']),
    Group('6', layout='max', label='vid', matches=matches_rule['vid']),
    Group('7', layout='tile', label='gam', matches=matches_rule['gam']),
    Group('8', layout='monadtall', label='sys', matches=matches_rule['sys']),
    Group('9', layout='treetab', label='vm', matches=matches_rule['vm']),
]

# Add group-related bindings to the keybindings
for i in groups:
    keys.extend([
        # super + name = switch to group
        Key([k.SUPER], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
        # super + shift + name = move focused window to group
        Key([k.SUPER, k.SHIFT], i.name, lazy.window.togroup(i.name),
            desc="Move focused window to group {}".format(i.name)),
    ])
