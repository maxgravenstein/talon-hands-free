# Talon voice commands for interacting with the Finder
# John S. Cooper  jcooper@korgrd.com

from talon.voice import Context, Key, Rep, Str, press
from talon import clip
from .std import text, join_words, parse_words

def select_text_to_left_of_cursor(m, cursorKey, clipboardSelectKey='shift-home'):
	key = join_words(parse_words(m)).lower()
	with clip.capture() as clipboardText:
		press(clipboardSelectKey, wait=20000)
		press('cmd-c', wait=20000)
		press('right', wait=20000)
	searchText = clipboardText.get().lower()
	result = searchText.rfind(key)
	if result == -1:
		return False
	# cursor over to the found key text and select the matching text
	for i in range(result, len(searchText) - len(key)):
		press(cursorKey, wait=0)
	for i in range(0, len(key)):
		press('shift-left', wait=0)
	return True

def select_text_to_right_of_cursor(m, cursorKey, clipboardSelectKey='shift-end'):
	key = join_words(parse_words(m)).lower()
	with clip.capture() as clipboardText:
		press(clipboardSelectKey, wait=20000)
		press('cmd-c', wait=20000)
		press('left', wait=20000)
	searchText = clipboardText.get().lower()
	result = searchText.find(key)
	if result == -1:
		return False
	# cursor over to the found key text and select the matching text
	for i in range(0, result):
		press(cursorKey, wait=0)
	for i in range(0, len(key)):
		press('shift-right', wait=0)
	return True

def select_text_on_same_line(m):
	key = join_words(parse_words(m)).lower()
	# first check to the left of the cursor
	if select_text_to_left_of_cursor(m, cursorKey='left', clipboardSelectKey='shift-ctrl-a') == False:
		# if nothing found, then check to the right of the cursor
		select_text_to_right_of_cursor(m, cursorKey='right', clipboardSelectKey='shift-ctrl-e')

ctx = Context('Find')
ctx.keymap({
    '(find text | marco) <dgndictation> [over]': [Key("cmd-f"), text, Key("enter")],
    '(find text | marco)': Key("cmd-f"),
    '(find selected text | find selection | sell find)': Key("cmd-e cmd-f enter"),
    '(find next | marnek)': Key('cmd-g'),
    '(find preev | marpreev)': Key('cmd-shift-g'),
    'set selection': Key('cmd-e'),
    'set replacement': Key('cmd-shift-e'),
    '(replace selected text | replace selection | sell find ace)': Key('cmd-e cmd-alt-f'),
    '(replace text | find ace)': Key('cmd-alt-f'),
    'close window': Key('cmd-w'),
    'quit window': Key('cmd-q'),
    '(crew | find right) <dgndictation> [over]': lambda m: select_text_to_right_of_cursor(m, cursorKey='right'),
    '(selcrew | crew select | sell find right) <dgndictation> [over]': lambda m: select_text_to_right_of_cursor(m, cursorKey='shift-right'),
    '(trail | find left) <dgndictation> [over]': lambda m: select_text_to_left_of_cursor(m, cursorKey='left'),
    '(seltrail | trail select | sell find left) <dgndictation> [over]': lambda m: select_text_to_left_of_cursor(m, cursorKey='shift-left'),
    'kerleck <dgndictation> [over]': select_text_on_same_line,
	"marthis": [
            Key("alt-right"),
            Key("shift-alt-left"),
            Key("cmd-f"),
            Key("enter"),
        ],
})
