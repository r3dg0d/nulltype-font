# Using NullType in terminals and editors

Install it first (see README). Font family name: **`NullType`**. Variable family: **`NullType`** (fontconfig exposes the named instances).
NullType is monospaced (`post.isFixedPitch` = 1, every advance identical), so terminals that filter for monospace fonts list it.

## kitty (`~/.config/kitty/kitty.conf`)
```conf
font_family      family="NullType"
bold_font        auto
italic_font      auto
bold_italic_font auto
font_size        13.0
font_features NullType-Regular -calt
```
## Alacritty (`~/.config/alacritty/alacritty.toml`, 0.13+ TOML)
```toml
[font]
size = 13.0
normal = { family = "NullType", style = "Regular" }
bold = { family = "NullType", style = "Bold" }
italic = { family = "NullType", style = "Italic" }
bold_italic = { family = "NullType", style = "Bold Italic" }
```
## foot (`~/.config/foot/foot.ini`)
```ini
[main]
font=NullType:size=12
```
## WezTerm (`~/.wezterm.lua`)
```lua
local wezterm = require 'wezterm'
return {
  font = wezterm.font('NullType', { weight = 'Regular' }),
  harfbuzz_features = { "calt=1", "zero=0" },
  font_size = 13.0,
}
```
## Ghostty (`~/.config/ghostty/config`)
```ini
font-family = NullType
font-size = 13
font-feature = -calt
```
## GNOME Terminal / Ptyxis
```sh
gsettings set org.gnome.desktop.interface monospace-font-name 'NullType 12'
```
## VS Code (`settings.json`)
```json
{
  "editor.fontFamily": "'NullType', monospace",
  "editor.fontLigatures": "'calt'",
  "terminal.integrated.fontFamily": "'NullType'"
}
```
## Neovim GUIs (Neovide etc.)
```lua
vim.o.guifont = "NullType:h13"
```
## Emacs
```elisp
(set-face-attribute 'default nil :family "NullType" :height 130)
```
## Powerline / Starship
U+E0A0–E0A2 and U+E0B0–E0B3 are included natively. No patching is needed for classic Powerline separators. Full Nerd Font icon sets are **not** included.
