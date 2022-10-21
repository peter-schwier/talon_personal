
I'm probaby going to borrow ideas from [[ShortTalk -- home page]] and http://redstartsystems.com/uttercommand.

I like the idea of leveraging [[Custom web commands with WebDriver  Hands-Free Coding]] in my command set.

Alternate alphabet? ` "arch brov chair dell etch fomp goof hark ice jinks koop lug mowsh nerb ork pooch quash rosh souk teek unks verge womp trex yang zooch"` from https://github.com/wolfmanstout/wolfmanstout_talon/blob/64c717aff20211c3a0c70c30cb48249231767720/code/keys.py#L9


Design decisions for my setup.

1. On first launch "help" will open a help dialog. That help dialog will guide you through editing a file to hide the "help" command on future launches.
2. After that first launch, "talon help show" will open the help dialog with context specific information.
3. In the help menu, normal navigation is disabled while you navigate the help menu and will remain open until you "talon help close".
4. Few commands are single words or unscoped.  Most commands are conditional based on application, tag, or mode, and are scoped by requiring multiple words. Ex. "tab new", "tab close".
5. The application will let users set the modes.
6. The application will infer the tags from the mode and the applications/os.
7. The application will do commands by tag and application/os.

| Condition(s) | Phrase                     | Effect             | Notes                                                                   |
| ------------ | -------------------------- | ------------------ | ----------------------------------------------------------------------- |
| mode: all    | `^talon sleep [<phrase>]$` | `speech.disable()` | The ` [<phrase>]$` means it will swallow and discard any other phrases. |
| mode: all    | `^talon wake up$`          | `speech.enable()`  | The three words means it is less likely to be said accidentally.        |


Built in modes?
1. `all`
2. `sleep`
3. `command`
4. `dictation`
5. All other modes are prefixed with `user.`