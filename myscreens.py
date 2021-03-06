from libqtile import bar, widget, qtile
from libqtile.config import Screen
from libqtile.utils import guess_terminal
import os


terminal = guess_terminal()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(padding=3, linewidth=0, background="#2f343f"),
                widget.Image(
                    filename="~/.config/qtile/python-white.png",
                    margin=3,
                    background="#2f343f",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("rofi -show combi")
                    },
                ),
                widget.Sep(padding=4, linewidth=0, background="#2f343f"),
                widget.GroupBox(
                    highlight_method="line",
                    this_screen_border="#5294e2",
                    this_current_screen_border="#5294e2",
                    active="#ffffff",
                    inactive="#848e96",
                    background="#2f343f",
                ),
                widget.TextBox(text="", padding=0, fontsize=28, foreground="#2f343f"),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(
                    foreground="#99c0de",
                    fmt="{}",
                    max_chars=50,
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground="#ffffff",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(terminal + " -e yay -Syu")
                    },
                    background="#2f343f",
                ),
                widget.Systray(icon_size=20),
                widget.DF(
                    partition="/home",
                    # visible_on_warn=False,
                    format=" {p} {uf}{m}|{r:.0f}%",
                ),
                widget.CryptoTicker(crypto="BTC", currency="USD"),
                widget.CryptoTicker(crypto="ADA", currency="USD"),
                widget.TextBox(text="", padding=0, fontsize=28, foreground="#2f343f"),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=28,
                    foreground="#2f343f",
                ),
                widget.TextBox(text="", padding=0, fontsize=28, foreground="#2f343f"),
                widget.Clock(
                    format=" %d-%m-%Y %a %H:%M",
                    # format=" %d-%m-%Y %a %H:%M",
                    background="#2f343f",
                    foreground="#9bd689",
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=28,
                    foreground="#2f343f",
                ),
                widget.Battery(format="{char} {percent:2.0%}"),
                widget.TextBox(
                    text="",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            os.path.expanduser("~/.config/rofi/powermenu.sh")
                        )
                    },
                    foreground="#e39378",
                ),
            ],
            20,  # height in px
            background="#404552",  # background color
        ),
    ),
]
