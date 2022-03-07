#!/bin/sh

# Setting Background image
feh --bg-scale --randomize /home/crazytelli/pictures/wallpapers/*.jpg

# Using pywal to set colorscheme matching the image
# wal -i /home/crazytelli/pictures/wallpapers/c4hLdu3.jpg
# You can create a function for this in your shellrc (.bashrc, .zshrc).
# wal-tile() {
#     wal -n -i "$@"
#     feh --bg-tile "$(< "${HOME}/.cache/wal/wal")"
# }

# Usage:
# wal-tile "/home/crazytelli/pictures/wallpapers/c4hLdu3.jpg"

picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Network Manager
nm-applet & disown

# Blueman - bluetooth applet
blueman-applet & disown

udiskie -ns --file-manager=$FILEMANAGER & disown

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
# eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
