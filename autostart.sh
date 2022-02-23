#!/bin/sh
# feh --bg-scale /usr/share/endeavouros/backgrounds/endeavouros-wallpaper.png
feh --bg-scale --randomize /home/crazytelli/pictures/wallpapers/*.jpg
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
