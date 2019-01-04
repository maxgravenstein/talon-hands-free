from talon.voice import Context, Key
from os import system

ctx = Context("navigation")

keymap = {
    # Application navigation
    "spotlight": Key("cmd-space"), #open up spotlight/other application launcher
    "next app": Key("cmd-tab"),
    "last app": Key("cmd-shift-tab"), #switch to the last app
    "minimize": Key("cmd-m"), #minimize application
    
    "next space": Key("cmd-alt-ctrl-right"),
    "last space": Key("cmd-alt-ctrl-left"),

    "new window": Key("cmd-n"),
    "close window": Key("cmd-shift-w"),
    "next window": Key("cmd-`"),
    "last window": Key("cmd-shift-`"),
    "show windows": Key("ctrl-down"),
    "window space right": Key("cmd-alt-ctrl-right"),
    "window space left": Key("cmd-alt-ctrl-left"),
    # deleting
    '(snip line | delete line)': Key('cmd-right cmd-backspace'),
    "steffi": Key("alt-ctrl-backspace"),
    "stippy": Key("alt-ctrl-delete"),
    "kite": Key("alt-delete"), #delete word right
    "snip left": Key("cmd-shift-left delete"), #delete line left of cursor
    "snip right": Key("cmd-shift-right delete"), #delete line right of cursor
    "slurp": Key("backspace delete"),
    "trough": Key("alt-backspace"),
    "slurpies": Key("alt-backspace alt-delete"),
    # moving
    "scroll down": [Key("down")] * 30, #scroll down
    "scroll up": [Key("up")] * 30, #scroll up
    "page up": [Key("pageup")], #scroll down by one view
    "page down": [Key("pagedown")], #scroll up by one view
    "scroll way down": Key("cmd-down"), #scroll to the bottom of file
    "scroll way up": Key("cmd-up"), #scroll to the top of file
    "shocker": [Key("cmd-left enter up")], #create a new line above and insert cursor on new line

    "tarsh": Key("shift-tab"), #unindent line of code
    "slap": [Key("cmd-right enter")],
    "jump left word": Key("alt-left"), #word left
    "jump word": Key("alt-right"), #word right
    "eel": Key("cmd-right"), #end of line
    "derek": Key("cmd-right space"),
    "bagel": Key("cmd-left"), #beginning of line
    # selecting
    "select all": Key("cmd-a"), #all
    "shreepway": Key("cmd-shift-up"), #all left and above cursor
    "shroomway": Key("cmd-shift-down"), #all right and below cursor
    "select left": Key("cmd-shift-left"), #line left
    "select right": Key("cmd-shift-right"), #line right
    
    "shreep": Key("shift-up"), #left to cursor position line above
    "shroom": Key("shift-down"), #right to cursor position line below
    "(schrim | shift left)": Key("shift-left"), #selects one space left
    "(shrish | shift right)": Key("shift-right"), #selects on space right
    
    "select word left": Key("alt-shift-left"),
    "select word right": Key("alt-shift-right"),

    "cut": Key("cmd-x"),
    "copy": Key("cmd-c"),
    "paste": Key("cmd-v"),
    # zooming
    "zoom in": Key("cmd-="),
    "zoom out": Key("cmd--"),
    "zoom normal": Key("cmd-0"),
    }

ctx.keymap(keymap)
