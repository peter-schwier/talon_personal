
A talon file has a context at the top and then a set of matches to actions.

The context at the top can be extended by python code to define application aliases.
```python
from talon import Context, actions, ui, Module

mod = Module()
ctx = Context()

apps = mod.apps
apps.notepad_plus_plus = """
os: windows
and app.name: Notepad++ : a free (GNU) source code editor
os: windows
and app.name: notepad++.exe
"""

ctx.matches = r"""
app: notepad_plus_plus
"""


@ctx.action_class("win")
class win_actions:
    def filename():
        title = actions.win.title()
        result = title.split(" - ")[0]
        if "." in result:
            # print(result.split("\\")[-1])
            return result.split("\\")[-1]
        return ""
```