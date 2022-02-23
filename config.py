from typing import List  # noqa: F401

from libqtile import bar, layout, widget, qtile

# from libqtile import layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import subprocess
import os

# from myscreens import screens

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "b", lazy.hide_show_bar(), desc="Toggle hide/show the bar"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_floating(),
        desc="Toggle floating",
    ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key(
    #     [mod, "shift"],
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show combi"), desc="spawn rofi"),
    Key(
        [mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget",
    ),
    Key(
        [mod],
        "x",
        lazy.spawn("slock"),
        desc="Locks the screen with slock - suckless.org",
    ),
    Key(
        [mod, "shift"],
        "z",
        lazy.spawn("systemctl suspend"),
        desc="Suspends the computer screen with slock and a systemd service at /etc/systemd/system/slock@.service",
    ),
    # Fn Keys:
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("xbacklight -inc 20"),
        desc="Increase display brightness",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("xbacklight -dec 20"),
        desc="Increase display brightness",
    ),
    # Launch apps key bindings:
    Key(
        [mod, "shift"],
        "Return",
        lazy.spawn(f"{terminal} -e ranger"),
        desc="Launches Ranger file manager",
    ),
    Key(
        [mod, "shift"], "p", lazy.spawn("pcmanfm"), desc="Launches pcmanfm file manager"
    ),
]

# Groups config
groups = [Group(i) for i in "123456789"]
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

# Layouts config
layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=2),
    layout.Max(),
]

widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="win0"), # Pycharm launching screen
    ]
)


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.65),
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
                widget.Systray(),
                widget.Clock(format="%d-%m-%Y %a %H:%M"),
                widget.Battery(
                    battery=1,
                    charge_char="",
                    discharge_char="",
                    empty_char="",
                    full_char="",
                    unknown_char="",
                    font="JetBrains Mono",
                    foreground="#ffffff",
                    format="{char} {percent:2.0%} {hour:d}:{min:02d}",
                    low_percentage=0.2,
                    low_foreground="#FF0000",
                    show_short_text=False,
                    hide_threshold=0.8,
                ),
                widget.QuickExit(
                    default_text="[⏻]",
                    font="JetBrains Mono",
                    countdown_format="[{} s]",
                ),
            ],
            24,
            # background="#404552",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=[ "ff00ff", "000000", "ff00ff", "000000", ],  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# colors = [
#     ["#282c34", "#282c34"],  # panel background
#     ["#3d3f4b", "#434758"],  # background for current screen tab
#     ["#ffffff", "#ffffff"],  # font color for group names
#     ["#ff5555", "#ff5555"],  # border line color for current tab
#     [
#         "#74438f",
#         "#74438f",
#     ],  # border line color for 'other tabs' and color for 'odd widgets'
#     ["#4f76c7", "#4f76c7"],  # color for the 'even widgets'
#     ["#e1acff", "#e1acff"],  # window name
#     ["#ecbbfb", "#ecbbfb"],  # backbround for inactive screens
# ]


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
