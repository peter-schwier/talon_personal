# dot talon

The [[dot talon]] files describe the voice commands.

* Matching specific applications, window titles, [[mode]]s or [[tag]]s.
* Define voice commands.
* Define global hotkeys. All platforms support hotkeys as of [0.3.0 (Jul 7, 2022)](https://talonvoice.com/dl/latest/changelog.html).
* Implement [[action]]s based on current [[matching criteria]].  Actually, no.  This is supposedly [deprecated](https://talon.wiki/unofficial_talon_docs/).
* Set [[settings]].
* Enable [[tag]]s.

The [[dot talon]] files have two portions split by a line that is only a minus sign ("-").
* The first portion defines the [[matching criteria]] of the file.
* The second portion activates [[tag]]s, sets [[settings]], and defines [[hotkey]]s, [[action]]s, and [[voice command]]s.

Example:
```talon
# activate this .talon file if the current app name is "Chrome"
# you can find app names by running ui.apps() in the REPL
app.name: Chrome
-
# key_wait increases the delay when pressing keys (milliseconds)
# this is useful if an app seems to jumble or drop keys
settings():
    key_wait = 4.0

# activate the global tag "browser"
tag(): browser

# define some voice commands
hello chrome: "hello world"
switch tab: key(ctrl-tab)
go to google:
    # note: use key(cmd-t) on Mac
    key(ctrl-t)
    insert("google.com")
    key(enter)
```

