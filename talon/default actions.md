
```talon
os: windows
app: chrome
-
tag(): browser
tag(): user.tabs
#action(browser.address):

action(browser.bookmark):
	key(ctrl-d)

action(browser.bookmark_tabs):
	key(ctrl-shift-d)
	
action(browser.bookmarks):
	key(ctrl-shift-o)
  
action(browser.bookmarks_bar):
	key(ctrl-shift-b)

action(browser.focus_address): 
	key(ctrl-l)
	
#action(browser.focus_page):

action(browser.focus_search):
	browser.focus_address()

action(browser.go_blank):
	key(ctrl-n)
	
action(browser.go_back):
	key(alt-left)

action(browser.go_forward):
	key(alt-right)
	
action(browser.go_home):
	key(alt-home)

action(browser.open_private_window):
	key(ctrl-shift-n)

action(browser.reload):
	key(ctrl-r)

action(browser.reload_hard):
	key(ctrl-shift-r)

#action(browser.reload_hardest):
	
action(browser.show_clear_cache):
	key(ctrl-shift-delete)
  
action(browser.show_downloads):
	key(ctrl-j)

#action(browser.show_extensions)

action(browser.show_history):
	key(ctrl-h)
	
action(browser.submit_form):
	key(enter)

#action(browser.title)

action(browser.toggle_dev_tools):
	key(ctrl-shift-i)
```

```talon
#custom eclipse commands go here
app: eclipse
-
tag(): user.find_and_replace
tag(): user.line_commands
# tag(): user.multiple_cursors
# tag(): user.snippets
tag(): user.splits
tag(): user.tabs
#talon app actions
action(app.tab_close): key(ctrl-w)
action(app.tab_next): key(ctrl-pagedown)
action(app.tab_previous): key(ctrl-pageup)
#action(app.tab_reopen): 
action(app.window_close): key(alt-f4)
action(app.window_open): key(alt-w n)
#talon code actions
action(code.toggle_comment): key(ctrl-7)

#talon edit actions
action(edit.indent_more): key(tab)
action(edit.indent_less): key(shift-tab)
action(edit.save_all): key(ctrl-shift-s)
```

```talon
os: windows
app: microsoft_edge
-
tag(): browser
tag(): user.tabs
#action(browser.address):

action(browser.bookmark):
	key(ctrl-d)

action(browser.bookmark_tabs):
	key(ctrl-shift-d)
	
action(browser.bookmarks):
	key(ctrl-shift-o)
  
action(browser.bookmarks_bar):
	key(ctrl-shift-b)

action(browser.focus_address): 
	key(ctrl-l)
	
#action(browser.focus_page):

action(browser.focus_search):
	browser.focus_address()

action(browser.go_blank):
	key(ctrl-n)
	
action(browser.go_back):
	key(alt-left)

action(browser.go_forward):
	key(alt-right)
	
action(browser.go_home):
	key(alt-home)

action(browser.open_private_window):
	key(ctrl-shift-p)

action(browser.reload):
	key(ctrl-r)

action(browser.reload_hard):
	key(shift-f5)

#action(browser.reload_hardest):
	
action(browser.show_clear_cache):
	key(ctrl-shift-delete)
  
action(browser.show_downloads):
	key(ctrl-j)

#action(browser.show_extensions)

action(browser.show_history):
	key(ctrl-h)
	
action(browser.submit_form):
	key(enter)

#action(browser.title)

action(browser.toggle_dev_tools):
	key(ctrl-shift-i)
```

```talon
app: firefox
-
tag(): browser
tag(): user.tabs

# TODO
#action(browser.address):
#action(browser.title):

action(browser.focus_search):
	browser.focus_address()

action(browser.submit_form):
	key(enter)

tab search:
  browser.focus_address()
  insert("% ")
tab search <user.text>$:
  browser.focus_address()
  insert("% {text}")
  key(down)
```

```talon
os: windows
app: firefox
-
action(app.tab_next): key(ctrl-pagedown)
action(app.tab_previous): key(ctrl-pageup)

action(browser.bookmark):
	key(ctrl-d)

action(browser.bookmark_tabs):
	key(ctrl-shift-d)
	
action(browser.bookmarks):
	key(ctrl-shift-b)
  
action(browser.bookmarks_bar):
	key(alt-v)
	sleep(50ms)
	key(t)
	sleep(50ms)
	key(b)

action(browser.focus_address): 
	key(ctrl-l)
	
#action(browser.focus_page):

action(browser.go_blank):
	key(ctrl-n)
	
action(browser.go_back):
	key(alt-left)

action(browser.go_forward):
	key(alt-right)
	
action(browser.go_home):
	key(alt-home)

action(browser.open_private_window):
	key(ctrl-shift-p)

action(browser.reload):
	key(ctrl-r)

action(browser.reload_hard):
	key(ctrl-shift-r)

#action(browser.reload_hardest):
	
action(browser.show_clear_cache):
	key(ctrl-shift-delete)
  
action(browser.show_downloads):
	key(ctrl-j)

action(browser.show_extensions):
	key(ctrl-shift-a)

action(browser.show_history):
	key(ctrl-h)
	
action(browser.toggle_dev_tools):
	key(ctrl-shift-i)
```

```talon
# Requires https://plugins.jetbrains.com/plugin/10504-voice-code-idea
app: jetbrains
-
tag(): user.line_commands
tag(): user.multiple_cursors
tag(): user.splits 
tag(): user.tabs

#talon app actions (+custom tab actions)
action(user.tab_final): user.idea("action GoToLastTab")
action(app.tab_next): user.idea("action NextTab")
action(app.tab_previous): user.idea("action PreviousTab")

action(app.tab_close): user.idea("action CloseContent")
action(app.tab_reopen): user.idea("action ReopenClosedTab")
#talon code actions
action(code.toggle_comment): user.idea("action CommentByLineComment")

#talon edit actions
action(edit.copy): user.idea("action EditorCopy")
action(edit.cut): user.idea("action EditorCut")
action(edit.delete): user.idea("action EditorBackSpace")
action(edit.paste): user.idea("action EditorPaste")
action(edit.find_next): user.idea("action FindNext")
action(edit.find_previous): user.idea("action FindPrevious")
action(edit.find): user.idea("action Find")
action(edit.line_clone):  user.idea("action EditorDuplicate")
action(edit.line_swap_down):  user.idea("action MoveLineDown")
action(edit.line_swap_up):  user.idea("action MoveLineUp")
action(edit.indent_more): user.idea("action EditorIndentLineOrSelection")
action(edit.indent_less): user.idea("action EditorUnindentSelection")
action(edit.select_line): user.idea("action EditorSelectLine")
action(edit.select_word): user.idea("action EditorSelectWord")
action(edit.select_all): user.idea("action $SelectAll")
action(edit.file_start): user.idea("action EditorTextStart")
action(edit.file_end): user.idea("action EditorTextEnd")
action(edit.extend_file_start): user.idea("action EditorTextStartWithSelection")
action(edit.extend_file_end): user.idea("action EditorTextEndWithSelection")

```

```talon
os: linux
tag: terminal
-
tag(): user.file_manager
#todo: generic tab commands
#tag(): tabs
action(edit.page_down):
  key(shift-pagedown)
action(edit.page_up):
  key(shift-pageup)
action(edit.paste):
  key(ctrl-shift-v)
action(edit.copy):
  key(ctrl-shift-c)

run last:
  key(up)
  key(enter)
rerun <user.text>:
  key(ctrl-r)
  insert(text)
rerun search:
  key(ctrl-r)
kill all:
  key(ctrl-c)

# XXX - these are specific to certain terminals only and should move into their
# own <term name>.talon file
action(edit.find):
  key(ctrl-shift-f)
action(edit.word_left):
  key(ctrl-w left)
action(edit.word_right):
  key(ctrl-w right)
action(app.tab_open):
  key(ctrl-shift-t)
action(app.tab_close):
  key(ctrl-shift-w)
action(app.tab_next):
  key(ctrl-pagedown)
action(app.tab_previous):
  key(ctrl-pageup)
action(app.window_open):
  key(ctrl-shift-n)
go tab <number>:
  key("alt-{number}")
```

```talon
os: windows
os: linux
-
#app.preferences()

action(app.tab_close):
	key(ctrl-w)
	
#action(app.tab_detach):
#  Move the current tab to a new window
  
action(app.tab_next):
	key(ctrl-tab)
	
action(app.tab_open):
	key(ctrl-t)
	
action(app.tab_previous):
	key(ctrl-shift-tab)
	
action(app.tab_reopen):
	key(ctrl-shift-t)
	
action(app.window_close):
	key(alt-f4)
	
action(app.window_hide):
	key(alt-space n)
	
action(app.window_hide_others):
	key(win-d alt-tab)
	
#requires easy window switcher or equivalent (built into most Linux)
action(app.window_next): 
	key(alt-`)

action(app.window_open):
	key(ctrl-n)

#requires easy window switcher or equivalent (built into most Linux)
action(app.window_previous): 
	key(alt-shift-`)
```

```talon
os: windows
os: linux
-
action(edit.copy):
	key(ctrl-c)

action(edit.cut):
	key(ctrl-x)

action(edit.delete):
	key(backspace)

action(edit.delete_line):
	edit.select_line()
	edit.delete()

#action(edit.delete_paragraph):

#action(edit.delete_sentence):

action(edit.delete_word):
	edit.select_word()
	edit.delete()

action(edit.down):
	key(down)

#action(edit.extend_again):

#action(edit.extend_column):

action(edit.extend_down):
	key(shift-down)

action(edit.extend_file_end):
	key(shift-ctrl-end)

action(edit.extend_file_start):
	key(shift-ctrl-home)

action(edit.extend_left):
	key(shift-left)

#action(edit.extend_line):

action(edit.extend_line_down):
	key(shift-down)

action(edit.extend_line_end):
	key(shift-end)

action(edit.extend_line_start):
	key(shift-home)

action(edit.extend_line_up):
	key(shift-up)

action(edit.extend_page_down):
	key(shift-pagedown)

action(edit.extend_page_up):
	key(shift-pageup)

#action(edit.extend_paragraph_end):
#action(edit.extend_paragraph_next()):
#action(edit.extend_paragraph_previous()):
#action(edit.extend_paragraph_start()):

action(edit.extend_right):
	key(shift-right)

#action(edit.extend_sentence_end):
#action(edit.extend_sentence_next):
#action(edit.extend_sentence_previous):
#action(edit.extend_sentence_start):

action(edit.extend_up):
	key(shift-up)

action(edit.extend_word_left):
	key(ctrl-shift-left)

action(edit.extend_word_right):
	key(ctrl-shift-right)

action(edit.file_end):
	key(ctrl-end)

action(edit.file_start):
	key(ctrl-home)

action(edit.find):
	key(ctrl-f)
	actions.insert(text)

action(edit.find_next):
	key(f3)
#action(edit.find_previous):

action(edit.indent_less):
	key(home delete)

action(edit.indent_more):
	key(home tab)

#action(edit.jump_column(n: int)
#action(edit.jump_line(n: int)

action(edit.left):
	key(left)

action(edit.line_down):
	key(down home)

action(edit.line_end):
	key(end)

action(edit.line_insert_down):
	key(end enter)

action(edit.line_insert_up):
	key(home enter up)

action(edit.line_start):
	key(home)

action(edit.line_up):
	key(up home)

#action(edit.move_again):

action(edit.page_down):
	key(pagedown)

action(edit.page_up):
	key(pageup)

#action(edit.paragraph_end):
#action(edit.paragraph_next):
#action(edit.paragraph_previous):
#action(edit.paragraph_start):

action(edit.paste):
	key(ctrl-v)

#action(paste_match_style):

action(edit.print):
	key(ctrl-p)

action(edit.redo):
	key(ctrl-y)

action(edit.right):
	key(right)

action(edit.save):
	key(ctrl-s)

action(edit.save_all):
	key(ctrl-shift-s)

action(edit.select_all):
	key(ctrl-a)

action(edit.select_line):
	key(end shift-home)

#action(edit.select_lines(a: int, b: int)):

action(edit.select_none):
	key(right)

#action(edit.select_paragraph):
#action(edit.select_sentence):

action(edit.select_word):
	key(ctrl-left ctrl-shift-right)

#action(edit.selected_text): -> str
#action(edit.sentence_end):
#action(edit.sentence_next):
#action(edit.sentence_previous):
#action(edit.sentence_start):

action(edit.undo):
	key(ctrl-z)

action(edit.up):
	key(up)

action(edit.word_left):
	key(ctrl-left)

action(edit.word_right):
	key(ctrl-right)

action(edit.zoom_in):
	key(ctrl-+)

action(edit.zoom_out):
	key(ctrl--)

action(edit.zoom_reset):
	key(ctrl-0)
```
