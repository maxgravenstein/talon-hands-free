from talon.voice import Context, Key, press, Str

ctx = Context('microsoft_word')

ctx.keymap({
    #From https://support.office.com/en-us/article/Keyboard-shortcuts-in-Word-for-Mac-3256d48a-7967-475d-be81-a6e3e1284b25#bkmk_edittext11

    'find': Key('cmd-f'),
    
    'increase size': Key('cmd-]'),
    'decrease size': Key('cmd-['),
    'font preferences': Key('cmd-d'),
    'bold': Key('cmd-b'),
    'italics': Key('cmd-i'),
    'underline': Key('cmd-u'),
    'strike through': Key('cmd-shift-x'),
    'subscript': Key('cmd-='),
    'superscript': Key('cmd-shift-+'),

    'left line': Key('cmd-l'),
    'center': Key('cmd-e'),
    'right line': Key('cmd-r'),
    'justify': Key('cmd-j'),

    'double spacing': Key('cmd-2'),
    'sngle spacing': Key('cmd-1'),

    #'jump left': Key('alt-left'),
    #'jump right': Key('alt-right'),
    #"bagel": Key("cmd-left"), #beginning of line
    #"eel": Key("cmd-right"), #end of line
    
    'select all': Key('cmd-a'),
    'select leftward': Key('alt-shift-left'),
    'select rightward': Key('alt-shift-right'),
    
    'dell leftward': Key('cmd-backspace'),
    'dell rightward': Key('cmd-delete'),

    'thesaurus': Key('ctrl-alt-cmd-r'),
    'page break': Key('cmd-return'),

    'cut': Key('cmd-x'),
    'copy': Key('cmd-c'),
    'paste': Key('cmd-v'),
    
    'print': Key('cmd-p'),
})
