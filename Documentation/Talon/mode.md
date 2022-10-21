[[Talon]] [[mode]]s can be set via [[Python]].

There is a set of default modes:
* command
* dictation
* sleep

Also, any number of user defined modes can be enabled. The user defined modes have a prefix of "user.".




___

[[talon]] [[mode]]s can be set via [[Python]].
```python
actions.mode.enable("user.{}".format(language))
```

And can be disabled via python.
```python
        for __, lang in extension_lang_map.items():
            actions.mode.disable("user.{}".format(lang))
```

I don't see any way to list the currently active modes. So I will need to keep track of what modes are possible myself.

Talon modes can be set and cleared in talon.
```talon
[enable] debug mode:
    mode.enable("user.gdb")
disable debug mode:
    mode.disable("user.gdb")

^dictation mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")
^command mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
```

Looks like user defined modes have to start with `user.`?

Actions can be defined per mode scope.
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

Modes can be used in a talon file to define [[tag]].
```talon
os: linux
# XXX - this matches .gdb files atm
#win.title: /gdb/
tag: terminal
mode: user.gdb
-
tag(): user.gdb
tag(): user.debugger

##
# Generic debugger actions
##

# Code execution
action(user.debugger_step_into): "stepi\n"
action(user.debugger_step_over): "nexti\n"
action(user.debugger_step_line): "step\n"
action(user.debugger_step_over_line): "next\n"
action(user.debugger_step_out): "finish\n"
until <number>: "until {number}"
```