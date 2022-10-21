
import typing
from ..code.user_actions import UserActions


def __getattr__(name) -> typing.Any: ...

Class = typing.TypeVar('Class', bound=typing.Type)

class Context:
    """
        The Context class allows python definitions to be visible in the .talon files.
    """

    def __init__(self):
        """
            Example:
            ```
                from talon import Context
                context = Context()
            ```
        """
        ...
    
    def action_class(self, path: typing.Literal[
        "app", "browser", "code", "dictate", "edit", "user", "win"
    ]) -> typing.Callable[[Class], None]:
        """
            Use the decorated class as a source of actions for the action prefix.

            TODO: Fix up the type annotation to define that this must go on a class.

            Example:
            ```
                @context.action_class('prefix')
                class Actions:
                    def action_name():
                        print("Running actions.prefix.action_name()")
            ```
        """
        ...
    
    def action(self, path: typing.Literal[
        "app.???",
        "browser.???",
        "code.???",
        "dictate.???",
        "edit.undo",
        "edit.redo",
        "edit.???",
        "user.???",
        "win.???",
        ]) -> typing.Callable[[typing.Callable], None]:
        """
            Use the decorated function as an action for the action name.

            TODO: Fix up the type annotation to define that this must go on a function.

            Example:
            ```
                @ctx.action('prefix.action_name')
                def action_name():
                    print("Running actions.prefix.action_name()")
            ```
        """
        ...
    
    def capture(self, path: str, rule: str) -> typing.Callable[[typing.Callable], None]:
        """
            Use the decorated function to translate from a match rule to a value.

            TODO: Fix up the type annotation to define that this must go on a class.

            Example:
            ```
                @ctx.capture('number', rule='(one | two)')
                def number(m) -> int:
                    return 1 if m[0] == 'one' else 2
            ```
        """
        ...

    @property
    def matches(self) -> str:
        '''
        Describe when to activate this context. If not specified, the Context 
        is always active.

        You can assign to this property more than once and it will be ORed 
        together with the existing matches.
        
        Example:
        ```
            ctx.matches = r"""
            os: windows
            app.name: Slack
            """
        ```
        '''
        ...
    @matches.setter
    def matches(self, value: str) -> None: ...

    @property
    def lists(self) -> typing.Mapping[str, typing.Union[typing.Dict[str, str], typing.List[str]]]:
        """
        Expose a list of phrases to the .talon files for matching purposes.
        If the "list" is actually a dictionary, then the key is the pronunciation and the 
        value is the text the system will type.

        TODO: The key can have either a prefix of "user." or "self.".  It seems that "self." is 
        only used when a module in the same python file creates the list.  Not sure if
        there is a benefit of one over the other?

        Example:
        ```
            ctx.lists["user.listname"] = ["word", "word2"]
            ctx.lists["user.listname"] = {
                "pronunciation": "word",
            }
        ```
        """
        ...
    
    @property
    def settings(self) -> typing.Mapping[
        typing.Union[
            typing.Literal[
                "speech.timeout", # minimum silence time (in seconds) before speech is cut off, default 0.3
                "key_hold", # Duration (in milliseconds) to hold keys down before releasing it
            ],
            str
        ], typing.Any]:
        """
        Set a default or user defined setting to a value as long as the context matches.

        Example:
        ```
            ctx.settings = {
                "input_wait": 1.0,
            }
            # "dictate.word_map" is used by Talon's built-in default implementation of
            # `dictate.replace_words`, but supports only single-word replacements.
            # Multi-word phrases are ignored.
            ctx.settings["dictate.word_map"] = phrases_to_replace
        ```
        """
        ...
    
    @settings.setter
    def settings(self, value: typing.Mapping[str, typing.Any]) -> None:
        ...

    
    @property
    def tags(self) -> typing.List[str]:
        """
        Enable a set of tags while this Context matches.

        Example:
        ```
            ctx.tags = ["user.terminal"]
        ```
        """
        ...
    
    @tags.setter
    def tags(self, value: typing.List[str]) -> None:
        ...

    @property
    def commands(self) -> typing.Mapping[str, typing.Any]:
        """
        Return the commands defined by the Context.
        """
        ...
    
    @property
    def hotkeys(self) -> typing.Mapping[str, typing.Any]:
        """
        Return the hotkeys defined by the Context.
        """
        ...


class Module:
    """
        The Module class allows python definitions to be visible in the .talon files.
    """

    def __init__(self):
        """
            Example:
            ```
                from talon import Module
                mod = Module()
            ```
        """
        ...
    

    def action_class(self) -> typing.Callable[[Class], None]:
        """
            Use the decorated class as a source of actions for the "user" prefix.

            TODO: Fix up the type annotation to define that this must go on a class.

            Example:
            ```
                @mod.action_class
                class Actions:
                    def action_name():
                        print("Running actions.user.action_name()")
            ```
        """
        ...
    
    def capture(self, rule: str) -> typing.Callable[[typing.Callable], None]:
        """
            Use the decorated function to translate from a match rule to a value.

            Note that this uses the function name for the capture name.

            TODO: Fix up the type annotation to define that this must go on a class.

            Example:
            ```
                @ctx.capture(rule='(one | two)')
                def number(m) -> int:
                    return 1 if m[0] == 'one' else 2
            ```
        """
        ...
    
    def scope(self, func: typing.Callable[[], typing.Dict]) -> None:
        """
            Use the decorated function to define values that can be matched in the criteria of .talon files.

            Note that this uses the function name for the capture name.

            TODO: Fix up the type annotation to define that this must go on a class.

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
        """
        ...

    def setting(self, name: str, type: typing.Type, default: typing.Any, desc: str) -> SettingDecl:
        """
            Create a user defined setting that can be set via the Context#settings or
            via the settings() entry in a .talon file.

            Example:
            ```python
                mod.setting(
                    "i3_mod_key",
                    type=str,
                    default="super",
                    desc="The default key to use for i3wm commands",
                )
            ```
        """
    
    def list(self, name: str, desc: str) -> None:
        """
            Define a list that can be used for matching purposes.

            Example:
            ```
                mod = Module()
                mod.list("letter", desc="The spoken phonetic alphabet")
                mod.list("symbol_key", desc="All symbols from the keyboard")
                mod.list("arrow_key", desc="All arrow keys")
                mod.list("number_key", desc="All number keys")
                mod.list("modifier_key", desc="All modifier keys")
                mod.list("function_key", desc="All function keys")
                mod.list("special_key", desc="All special keys")
                mod.list("punctuation", desc="words for inserting punctuation into text")

                ctx = Context()
                modifier_keys = {
                    # If you find 'alt' is often misrecognized, try using 'alter'.
                    "alt": "alt",  #'alter': 'alt',
                    "control": "ctrl",  #'troll':   'ctrl',
                    "shift": "shift",  #'sky':     'shift',
                    "super": "super",
                }
                if app.platform == "mac":
                    modifier_keys["command"] = "cmd"
                    modifier_keys["option"] = "alt"
                ctx.lists["self.modifier_key"] = modifier_keys
                alphabet = dict(zip(default_alphabet, letters_string))
                ctx.lists["self.letter"] = alphabet

            ```
        """
        ...
    
    def mode(self, name: str, desc: str) -> None:
        """
        Define a mode that can be used for condition matching of .talon files.

        Example:
        ```python
            from talon import Context, Module, actions, imgui, registry

            mod = Module()
            mod.list("help_contexts", desc="list of available contexts")
            mod.mode("help", "mode for commands that are available only when help is visible")
        ```

        ```talon
            mode: user.help
            -
            help next$: user.help_next()
            help previous$: user.help_previous()
            help <number>$: user.help_select_index(number - 1)
            help return$: user.help_return()
            help refresh$: user.help_refresh()
            help close$: user.help_hide()
        ```
        """
    
    def tag(self, name: str, desc: str) -> None:
        '''
        Define a tag that can be used for condition matching of .talon files.

        Example:
        ```python
            from talon import Context, Module

            # --- Tag definition ---
            mod = Module()
            mod.tag("emoji", desc="Emoji, ascii emoticons and kaomoji")

            # Context matching
            ctx = Context()
            ctx.matches = """
            tag: user.emoji
            """
        ```
        '''

class SettingDecl:
    def get(self) -> typing.Any():
        """Get the current value of the setting."""
        ...

class AppActions:
    def notify(body: str = ..., title: str = ..., subtitle: str = ..., sound: bool = ...): ...
    def name() -> str: ...
    def bundle() -> str: ...
    def path() -> str: ...
    def executable() -> str: ...
    def window_open() -> None: ...
    def window_close() -> None: ...
    def window_next() -> None: ...
    def window_previous() -> None: ...
    def window_hide() -> None: ...
    def window_hide_others() -> None: ...
    def tab_open() -> None: ...
    def tab_close() -> None: ...
    def tab_next() -> None: ...
    def tab_previous() -> None: ...
    def tab_detach() -> None: ...
    def tab_reopen() -> None: ...
    def preferences() -> None: ...


class BrowserActions:
    def open_private_window() -> None: ...
    def focus_search() -> None: ...
    def focus_address() -> None: ...
    def focus_page() -> None: ...
    def address() -> str: ...
    def title() -> str: ...
    def reload() -> None: ...
    def reload_hard() -> None: ...
    def reload_hardest() -> None: ...
    def go(url: str): ...
    def go_forward() -> None: ...
    def go_back() -> None: ...
    def go_home() -> None: ...
    def go_blank() -> None: ...
    def bookmark() -> None: ...
    def bookmark_tabs() -> None: ...
    def bookmarks() -> None: ...
    def bookmarks_bar() -> None: ...
    def toggle_dev_tools() -> None: ...
    def submit_form() -> None: ...
    def show_history() -> None: ...
    def show_downloads() -> None: ...
    def show_extensions() -> None: ...
    def show_clear_cache() -> None: ...


class CodeActions:
    def language() -> str: ...
    def toggle_comment() -> None: ...
    def select_scope() -> None: ...
    def extend_scope_start() -> None: ...
    def extend_scope_end() -> None: ...
    def extend_scope_out() -> None: ...
    def extend_scope_in() -> None: ...
    def extend_scope_next() -> None: ...
    def extend_scope_previous() -> None: ...
    def scope_start() -> None: ...
    def scope_end() -> None: ...
    def scope_out() -> None: ...
    def scope_in() -> None: ...
    def scope_next() -> None: ...
    def scope_previous() -> None: ...
    def rename(name: str): ...
    def complete() -> None: ...


class EditActions:
    def save() -> None: ...
    def save_all() -> None: ...
    def print() -> None: ...
    def undo() -> None: ...
    def redo() -> None: ...
    def cut() -> None: ...
    def copy() -> None: ...
    def paste() -> None: ...
    def paste_match_style() -> None: ...
    def delete() -> None: ...
    def select_none() -> None: ...
    def select_all() -> None: ...
    def select_word() -> None: ...
    def select_sentence() -> None: ...
    def select_paragraph() -> None: ...
    def select_line(n: int = ...): ...
    def select_lines(a: int, b: int): ...
    def extend_column(n: int): ...
    def extend_line(n: int): ...
    def extend_left() -> None: ...
    def extend_right() -> None: ...
    def extend_up() -> None: ...
    def extend_down() -> None: ...
    def extend_file_start() -> None: ...
    def extend_file_end() -> None: ...
    def extend_line_up() -> None: ...
    def extend_line_down() -> None: ...
    def extend_line_start() -> None: ...
    def extend_line_end() -> None: ...
    def extend_page_up() -> None: ...
    def extend_page_down() -> None: ...
    def extend_again() -> None: ...
    def extend_word_left() -> None: ...
    def extend_word_right() -> None: ...
    def extend_sentence_previous() -> None: ...
    def extend_sentence_next() -> None: ...
    def extend_sentence_start() -> None: ...
    def extend_sentence_end() -> None: ...
    def extend_paragraph_previous() -> None: ...
    def extend_paragraph_next() -> None: ...
    def extend_paragraph_start() -> None: ...
    def extend_paragraph_end() -> None: ...
    def jump_column(n: int): ...
    def jump_line(n: int): ...
    def left() -> None: ...
    def right() -> None: ...
    def up() -> None: ...
    def down() -> None: ...
    def file_start() -> None: ...
    def file_end() -> None: ...
    def line_start() -> None: ...
    def line_end() -> None: ...
    def line_up() -> None: ...
    def line_down() -> None: ...
    def page_up() -> None: ...
    def page_down() -> None: ...
    def move_again() -> None: ...
    def word_left() -> None: ...
    def word_right() -> None: ...
    def sentence_previous() -> None: ...
    def sentence_next() -> None: ...
    def sentence_start() -> None: ...
    def sentence_end() -> None: ...
    def paragraph_previous() -> None: ...
    def paragraph_next() -> None: ...
    def paragraph_start() -> None: ...
    def paragraph_end() -> None: ...
    def zoom_in() -> None: ...
    def zoom_out() -> None: ...
    def zoom_reset() -> None: ...
    def line_insert_up() -> None: ...
    def line_insert_down() -> None: ...
    def line_swap_up() -> None: ...
    def line_swap_down() -> None: ...
    def line_clone() -> None: ...
    def selection_clone() -> None: ...
    def indent_more() -> None: ...
    def indent_less() -> None: ...
    def delete_line() -> None: ...
    def delete_word() -> None: ...
    def delete_sentence() -> None: ...
    def delete_paragraph() -> None: ...
    def find(text: str = ...): ...
    def find_next() -> None: ...
    def find_previous() -> None: ...
    def selected_text() -> str: ...


class ModeActions:
    def enable(mode: str): ...
    def disable(mode: str): ...

class PathActions:
    def talon_app() -> str: ...
    def talon_user() -> str: ...
    def talon_home() -> str: ...
    def user_home() -> str: ...

class SpeechActions:
    def enabled() -> bool: ...
    def enable() -> None: ...
    def disable() -> None: ...
    def toggle(value: bool = ...): ...
    def set_microphone(name: str): ...
    def record_flac() -> None: ...
    def record_wav() -> None: ...
    def replay(path: str): ...

class WinActions:
    def filename() -> str: ...
    def file_ext() -> str: ...
    def title() -> str: ...

class Actions:
    app: AppActions
    browser: BrowserActions
    code: CodeActions
    edit: EditActions
    mode: ModeActions
    path: PathActions
    speech: SpeechActions
    user: UserActions
    win: WinActions

    def print(obj: typing.Any): ...
    def auto_format(text: str) -> str: ...
    def mouse_move(x: float, y: float): ...
    def mouse_click(button: int = ...): ...
    def mouse_drag(button: int = ...): ...
    def mouse_release(button: int = ...): ...
    def mouse_scroll(y: float = ..., x: float = ..., by_lines: bool = ...): ...
    def mouse_x() -> float: ...
    def mouse_y() -> float: ...
    def mimic(text: str): ...

    def skip(self) -> None:
        """This is a null operation to blank out an action."""
        ...

    def insert(self, s: str) -> None:
        """Insert the text."""

    def auto_insert(self, s: str) -> None: ...

    def key(self, keys: str) -> None:
        """
            Type the keys.

            The Talon `key()` action allows you to press, hold, and release virtual keyboard keys. You can use it in `.talon` files directly, and most of the time don’t need to quote the argument. For example `key(ctrl-f)` is equivalent to `key("ctrl-f")` in .talon files. In Python you do need to quote the argument and can use the action like this:

            ```
            from talon import actions
            actions.key("ctrl-f")
            ```

            Here’s some of the syntax you can use with the action:

            -   `key("f")` - Presses the f key.
            -   `key("ctrl-t")` - Presses and holds down the control key, then presses t, then releases everything.
            -   `key("\\"")` - Presses the “ key.
            -   `key("ctrl-shift-alt-option-super-t")` - Presses and holds down the control, shift, alt, super (windows key or cmd key on mac), and option keys, then presses t, then releases everything. Note how you can apply multiple modifiers by connecting them with hyphens.
            -   `key("left delete")` - Presses the left arrow key, then the delete key.
            -   `key("ctrl:down")` - Presses and holds the control key. You can use “ctrl:up” to release the key later in the same or a a subsequent key() call. You can use `:up` and `:down` with any key, not just modifiers like control.
            -   `key("tab:3")` - Presses the tab key three times.

            Some key names are listed above, and some directly map to what is inserted (e.g. `key(1)` presses the number 1 key). Some key names are not obvious. A partial table of key names with descriptions follows.

            | Key name(s) | Description |
            | --- | --- |
            | a z 0 9 - + ( ) etc. | Presses the key corresponding to the symbol |
            | left right up down | Arrow keys |
            | backspace bksp | The backspace key (delete character to left) |
            | delete del | The delete key (delete character to right) |
            | escape esc | The escape key |
            | pgup pageup pgdown pagedown | The page up and page down keys |
            | return enter | The enter key |
            | tab space | The tab and space keys |
            | home end | The home and end keys |
            | alt super ctrl shift | Can be held down with e.g. `key("shift:down")` (and released with :up) |
            | ralt rctrl rshift | The key on the right hand side of the keyboard |
            | capslock scroll\_lock insert | Persistent mode switch keys |
            | f1 f2 … f35 | The f1 to f35 keys, many of these are probably not on your keyboard, but are nonetheless available |
            | mute voldown volup play stop play\_pause prev next rewind fast\_forward | Media keys |
            | altgr | Can be combined with another key to add accents, e.g. `key("altgr:down e altgr:up")` produces “é”. The dead\_\* keys might suit you better though. |
            | menu help sysreq printscr compose | Miscellaneous keys |
            | brightness\_up brightness\_down | Screen brightness control |
            | backlight\_up backlight\_down backlight\_toggle | Maybe keyboard backlight controls? |
            | keypad\_0 keypad\_1 … keypad\_9 | The number keys on a keypad |
            | keypad\_clear keypad\_enter keypad\_separator keypad\_decimal keypad\_plus keypad\_multiply keypad\_divide keypad\_minus keypad\_equals | Other keypad keys |
            | dead\_grave dead\_acute dead\_circumflex dead\_tilde dead\_macron dead\_breve dead\_abovedot dead\_diaeresis dead\_cedilla | Keys which causes the next key pressed to be accented. For example `key("dead_acute e")` produces “é”. |
            | dead\_perispomeni dead\_abovering dead\_doubleacute dead\_caron dead\_ogonek dead\_voiced\_sound dead\_semivoiced\_sound dead\_belowdot dead\_hook dead\_horn dead\_iota dead\_stroke dead\_abovecomma dead\_psili dead\_abovereversedcomma dead\_dasia dead\_doublegrave dead\_belowring dead\_belowmacron dead\_belowcircumflex dead\_belowtilde dead\_belowbreve dead\_belowdiaeresis dead\_invertedbreve dead\_belowcomma dead\_currency dead\_lowline dead\_aboveverticalline dead\_belowverticalline dead\_longsolidusoverlay dead\_a dead\_e dead\_i dead\_o dead\_u dead\_small\_schwa dead\_capital\_schwa dead\_greek | Other keys which accent the next key pressed |

        """
        ...
    
    def sleep(self, duration: typing.Union[float, str]):
        """
            Sleep is a built in function and takes arguments of 
            the (<float>|<integer><suffix>) form. Float allows
            specifying (fractions) of a second. 
            The <integer><suffix> form can be '1m', '5s', '500ms', '1000000us' etc.
            Be aware sleeping in this way will prevent Talon 
            from processing voice commands until the sleep is over.
        """
        ...
    
    def list(self) -> typing.List[typing.Any]:
        """List of all loaded actions."""
        ...

    def find(self, name: str) -> typing.List[typing.Any]:
        """Searches the name, documentation, and code implementing an action for
        the given substring. Prints out a list of matches."""


    # TODO: Define the rest.
    # speech.toggle() ?

actions = Actions()
registry: typing.Any = object() # TODO
scope: typing.Any = object() # TODO
settings: typing.Any = object() # TODO
# settings.list()

storage: typing.Any = object() # TODO

class App:
    def register(self, topic: typing.Literal["ready", "launch", "startup"], cb: typing.Callable) -> None:
        """
            Register for an application event.

            * ready: Talon is ready. Your callback will be called after 
            Talon launch and during script reloads.

            * launch: Talon launched. Your callback will only be called 
            immediately after Talon launch.

            * startup: Talon launched during system startup.

            ```python
                from talon import app

                def app_ready():
                    print("Talon is ready")
                app.register("ready", app_ready)
            ```
        """
        ...

    def unregister(self, topic: typing.Literal["ready", "launch", "startup"], cb: typing.Callable) -> None:
        """
            Unregister a previously registered event.

            ```python
                from talon import app

                def app_ready():
                    print("Talon is ready")
                    app.unregister("ready", app_ready)
                app.register("ready", app_ready)
            ```
        """
        ...
    
    def notify(self, 
            title: typing.Optional[str] = None, 
            subtitle: typing.Optional[str] = None, 
            body: typing.Optional[str] = None, 
            sound: bool = False
    ):
        """Display a desktop notification."""
        ...

app = App()


class Clip:
    """
        Clipboard handling code.

        TODO: Document the .mime() and .set_mime() functions with the MimeData class.
    """
    def has_mode(self, mode: typing.Literal["main", "select", "find"]) -> bool:
        """Check if a clipboard mode is supported."""
        ...

    def text(self, mode: typing.Literal["main", "select", "find"] = "main") -> typing.Optional[str]:
        """Get the text content of the clipboard."""
        ...

    def set_text(self, s: str, mode: typing.Literal["main", "select", "find"] = "main") -> None:
        """Set the text content of the clipboard."""
        ...
    
    def get(self) -> typing.Optional[str]:
        """
            Get the text content of the clipboard.

            I suspect this is deprecated.
        """
        ...
        
    def revert(self) -> typing.Generator[None, None, None]:
        '''
        Restore the old text of the clipboard after running a block.
        ```python
            from talon import clip

            def paste(text: str):
                """Pastes text and preserves clipboard"""

                with clip.revert():
                    clip.set_text(text)
                    actions.edit.paste()
                    # sleep here so that clip.revert doesn't revert the clipboard too soon
                    actions.sleep("150ms")

        ```
        '''
        
    def capture(self) -> typing.Generator[Clip, None, None]:
        '''
        Capture a change in the clipboard, then restore the old contents.

        TODO: Not sure if you need to call `.get()` or or `.text()` afterwards.

        ```python
            from talon import clip
            
            def selected_text() -> str:
                with clip.capture() as s:
                    actions.edit.copy()
                try:
                    return s.text()
                except clip.NoChange:
                    return ""

            def file_manager_terminal_here():
                actions.key("ctrl-l")
                with clip.capture() as path:
                    actions.edit.copy()
                ui.launch(path="gnome-terminal", args=[f"--working-directory={path.get()}"])
        ```
        '''

clip = Clip()

class Fs:
    def watch(path: str, cb: typing.Callback[[str, object], None]) -> None: ...
    def unwatch(path: str, cb: typing.Callback[[str, object], None]) -> None: ...

fs: Fs = Fs()
noise: typing.Any = object() # TODO

class UiWindow:
    id: int
    title: str
    doc: str
    hidden: bool

class UiApp:
    pid: int
    name: str
    company: str
    path: str
    exe: str
    bundle: str
    cmdline: typing.Sequence[str]
    background: bool
    platform: typing.Literal["windows"]

class Ui:
    def active_window() -> UiWindow: ...
    def register(self, event: typing.Literal["app_launch", "app_close"], cb: typing.Callable): ...
    def apps(self, bundle: typing.Optional[str] = None, background: typing.Optional[bool] = None) -> typing.Iterable[UiApp]: ...

ui: Ui = Ui()