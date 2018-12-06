from talon import macos, ui, os
from talon.voice import Context, Key

ctx = Context('aux_keys')
ctx.keymap({
    'brightness down': Key('brightness_down'),
    'brightness up': Key('brightness_up'),
    
    'mission control': lambda m: macos.dock_notify('com.apple.expose.awake'),
    'apps': lambda m: ui.launch(bundle='com.apple.launchpad.launcher'),

    'backlight down': Key('backlight_down'),
    'backlight up': Key('backlight_up'),

    'rewind': Key('rewind'),
    'play | pause': Key('play'),
    'fast forward': Key('fast_forward'),

    'mute': Key('mute'),
    'volume down': Key('volume_down'),
    'volume up': Key('volume_up'),
    
    'eff one': Key('f1'),
    'eff two': Key('f2'),
    'eff three': Key('f3'),
    'eff four': Key('f4'),
    'eff five': Key('f5'),
    'eff six': Key('f6'),
    'eff seven': Key('f7'),
    'eff eight': Key('f8'),
    'eff nine': Key('f9'),
    'eff ten': Key('f10'),
    'eff eleven': Key('f11'),
    'eff twelve': Key('f12'),
})