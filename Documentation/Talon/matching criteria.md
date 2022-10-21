# matching criteria

The following requirements can be set:

`os`

require specific operating systems; currently either `linux`, `mac`, or `windows`

`tag`

require a specific tag

`mode`

only active for specific talon modes (like `command`, `dictation`, `sleep` et al.)

`app`

match applications by explicitly declared, well-known name

`app.name`

match applications by name (TODO where does Talon read this out?)

`app.exe`

match applications by executable, like `/usr/lib/firefox/firefox` or `firefox.exe`

`app.bundle`

match applications by their MacOS bundle, like `com.mozilla.Firefox`

`title`

match a window title

`code.language`

specify a currently active programming language

`language`

specify the particular human language (e.g. `pt_BR`, `en`) for the file. Defaults to `en` if not specified. Currently only needed for multilingual webspeech.

`hostname`

match the ‘hostname’ of your machine (from the `hostname` CLI command on Linux/Mac). Useful if you want to have a single set of custom config but have some machine-specific parts.

Also, you can define custom "scopes" using `Module#scope`.

Example:
```python
    from talon import Module, ui

    mod = Module()


    @mod.scope
    def scope():
        return {"running": {app.name.lower() for app in ui.apps()}}


    ui.register("app_launch", scope.update)
    ui.register("app_close", scope.update)
```
and
```talon
    user.running: amethyst
    -
    window next: key("alt-shift-j")
    window previous: key("alt-shift-k")
```

Each individual header line has the format `[and] [not] <requirement or scope name>: (<literal match value> | /<regex match value>/<python regex flags>)` where `[]` indicates an optional token, `(|)` indicates exclusive options, and `<>` a special segment. Some examples of valid lines are `title: foo`, `title: /foo/i`, `and tag: user.bar`, `not tag: /foo/`, and `and not tag: user.foo`.

We’ve already indicated what requirements and scopes are, so lets move on to the matcher part (on the right of the ‘:’). This can either be a literal string match like `title: foo` (matching a window whose entire title is ‘foo’), or a regular expression. The regular expression engine essentially uses the Python `re.search()` function to see if the value of the requirement or scope matches. So for the `title: /foo/i` example we’d match any window whose title had the string ‘foo’ in it in a case insensitive manner (due to the ‘i’ flag). For requirement types that have multiple values (tag and mode), Talon iterates through each active tag or mode and matches the header line if any of those match the regex or string literal.

The next thing to talk about is what happens when we have multiple lines in the context header. Talon lets you combine these together as a composite matcher following specific rules. In the following examples the comment contains an expression describing what the rule will match, e.g. `paint_app or (windows and not notepad_app)`. In this case the expression would match the when the app `paint_app` is active or the operating system is `windows` and the app `notepad_app` is not active.


```
# paint_app or notepad_app
app: paint_app
app: notepad_app
```

```
# (paint_app or notepad_app) and windows
app: paint_app
os: windows
app: notepad_app
```

```
# (paint_app and windows) or notepad_app
app: paint_app
and os: windows
app: notepad_app
```

```
# paint_app and not windows
app: paint_app
not os: windows
```

So without modifiers, requirements of the same type (e.g. two apps) are OR-ed together. Requirements of different types (e.g. ‘app’ and ‘os’) are AND-ed together. The ‘and’ modifier looks at the previous requirement and merges with it to make a compound expession. The ‘not’ modifier just negates the condition.




#### Rules

Rules have a versatile syntax that is like a word based regex:

| Syntax | Description | Matches |
| --- | --- | --- |
| `foo` | Words | “foo” |
| `[foo]` | Optional | “foo” or null (nothing) |
| `foo*` | Zero or more | “”, “foo”, “foo foo”, … |
| `foo+` | One or more | “foo”, “foo foo”, … |
| `foo|bar` | Choice | “foo”, “bar” |
| `(foo)` | Precedence/grouping | “foo” |
| `{some_list}` | [List](https://talon.wiki/unofficial_talon_docs/#lists) | Depends on the list. |
| `<some_capture>` | [Capture](https://talon.wiki/unofficial_talon_docs/#captures) | Depends on the capture. |
| `^foo` | Start anchor | See below |
| `foo$` | End anchor | See below |
