# action

Actions are custom chunks of code that can be run inside talon files, usually scoped to a [[tag]].
```talon
tag: user.messaging
-
# Navigation
previous (workspace | server): user.messaging_workspace_previous()
next (workspace | server): user.messaging_workspace_next()
channel: user.messaging_open_channel_picker()
channel <user.text>:
    user.messaging_open_channel_picker()
    insert(user.formatted_text(user.text, "ALL_LOWERCASE"))
channel up: user.messaging_channel_previous()
channel down: user.messaging_channel_next()
([channel] unread last | gopreev): user.messaging_unread_previous()
([channel] unread next | goneck): user.messaging_unread_next()
go (find | search): user.messaging_open_search()
mark (all | workspace | server) read: user.messaging_mark_workspace_read()
mark channel read: user.messaging_mark_channel_read()
upload file: user.messaging_upload_file()

```

Actions can be defined in talon files like below.
```talon
os: windows
os: linux
app: slack
#todo: some sort of plugin, consolidate with teams or something?
-
tag(): user.messaging
# Workspaces
workspace <number>: key("ctrl-{number}")
action(user.messaging_workspace_previous): key(ctrl-shift-tab)
action(user.messaging_workspace_next): key(ctrl-tab)
# Channel
(slack | lack) [channel] info: key(ctrl-shift-i)
action(user.messaging_open_channel_picker): key(ctrl-k)
action(user.messaging_channel_previous): key(alt-up)
action(user.messaging_channel_next): key(alt-down)
action(user.messaging_unread_previous): key(alt-shift-up)
action(user.messaging_unread_next): key(alt-shift-down)
# Navigation
(move | next) focus: key(ctrl-`)
[next] (section | zone): key(f6)
(previous | last) (section | zone): key(shift-f6)
```

Actions can also be defined in python files like below.
```python
from talon import Context, Module, actions, ui

ctx = Context()

ctx.matches = r"""
mode: user.gdb
"""


@ctx.action_class("user")
class user_actions:
    def debugger_clear_breakpoint_id(number_small: int):
        actions.insert(f"d br {number_small}\n")

    def debugger_disable_breakpoint_id(number_small: int):
        actions.insert(f"disable br {number_small}\n")

    def debugger_enable_breakpoint_id(number_small: int):
        actions.insert(f"enable br {number_small}\n")
```

There also seems to be a set of default action classes.
```python
@ctx.action_class("browser")
class browser_actions:
    def go(url: str):
        actions.browser.focus_address()
        actions.sleep("50ms")
        actions.insert(url)
        actions.key("enter")
```
```talon
tag: user.tabs
-
tab (open | new): app.tab_open()
tab last: app.tab_previous()
tab next: app.tab_next()
tab close: app.tab_close()
tab reopen: app.tab_reopen()
go tab <number>: user.tab_jump(number)
go tab final: user.tab_final()
```

You can also call actions from the python code.
```python
from talon import Context, actions, ui, Module, app, clip
from typing import List, Union

is_mac = app.platform == "mac"

ctx = Context()
mod = Module()

mod.apps.eclipse = """
os: windows
and app.name: eclipse.exe
"""

ctx.matches = r"""
app: eclipse
"""

@ctx.action_class("user")
class user_actions:

    def select_previous_occurrence(text: str):
        actions.edit.find(text)
        actions.sleep("100ms")
        actions.key("alt-b alt-f enter esc")

    def select_next_occurrence(text: str):
        actions.edit.find(text)
        actions.sleep("100ms")
        actions.key("alt-f alt-o esc")
```