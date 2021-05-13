# qtile-config

## Mod keys

- `super` = "windows" button

## Keybindings

### Layout controls

| Keys          | Description            |
| ------------- | ---------------------- |
| `super`+`tab` | Toggle between layouts |

### Focus controls

| Keys            | Description                                   |
| --------------- | --------------------------------------------- |
| `super`+`space` | Switch window focus to other pane(s) of stack |
| `super`+`k`     | Move focus up in stack pane                   |
| `super`+`j`     | Move focus down in stack pane                 |
| `super`+`h`     | Move focus left in stack pane                 |
| `super`+`l`     | Move focus right in stack pane                |

### Move window controls

| Keys                    | Description                        |
| ----------------------- | ---------------------------------- |
| `super`+`shift`+`space` | Swap panes of split stack          |
| `super`+`shift`+`k`     | Move window up in current stack    |
| `super`+`shift`+`j`     | Move window down in current stack  |
| `super`+`shift`+`h`     | Move window left in current stack  |
| `super`+`shift`+`l`     | Move window right in current stack |

### Resize window controls

| Keys                | Description                                                        |
| ------------------- | ------------------------------------------------------------------ |
| `super`+`m`         | Toggle between min and max sizes                                   |
| `super`+`shift`+`m` | Toggle fullscreen                                                  |
| `super`+`ctrl`+`k`  | Expand window (monadtall) or increase number in master pane (tile) |
| `super`+`ctrl`+`j`  | Shrink window (monadtall) or decrease number in master pane (tile) |

### Other window controls

| Keys                    | Description                                     |
| ----------------------- | ----------------------------------------------- |
| `super`+`f`             | Toggle floating mode on focused window          |
| `super`+`shift`+`f`     | Move floating windows to front                  |
| `super`+`shift`+`enter` | Toggle between split and unsplit sides of stack |
| `super`+`n`             | Normalize window size ratios                    |
| `super`+`w`             | Close focused window                            |

### App controls

| Keys            | Description                                           |
| --------------- | ----------------------------------------------------- |
| `super`+`r`     | Open default launcher (e.g. dmenu or rofi)            |
| `super`+`enter` | Open default terminal (e.g. alacritty or kitty)       |
| `super`+`b`     | Open default browser (e.g. chrome, firefox, or brave) |
| `super`+`e`     | Open default editor (e.g. emacs)                      |

### Screenshot controls

| Keys                    | Description                   |
| ----------------------- | ----------------------------- |
| `print`                 | Clip selected area screenshot |
| `super`+`print`         | Save selected area screenshot |
| `super`+`shift`+`print` | Save fullscreen screenshot    |

### Volume controls

| Keys          | Description         |
| ------------- | ------------------- |
| `volume-up`   | Raise volume (by 2) |
| `volume-down` | Lower volume (by 2) |
| `volume-mute` | Toggle mute         |

### Qtile controls

| Keys               | Description          |
| ------------------ | -------------------- |
| `super`+`ctrl`+`r` | Restart qtile config |
| `super`+`ctrl`+`q` | Exit/Quit qtile      |

## Mousebindings

### Window controls

| Keys             | Description                                  |
| ---------------- | -------------------------------------------- |
| `super`+`left`   | Drag window (turned into floating windows)   |
| `super`+`right`  | Resize window (turned into floating windows) |
| `super`+`right`  | Resize window (turned into floating windows) |
| `super`+`middle` | Bring floating window to the front           |

### Group controls

| Keys                  | Description              |
| --------------------- | ------------------------ |
| `super`+`scroll-up`   | Change to next group     |
| `super`+`scroll-down` | Change to previous group |
