from getkey import getkey, keys

__all__: tuple[str, ...] = ("Input",)

class Input:

    def __init__(self):

        self.keys = {
            "a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g",
            "h": "h", "i": "i", "j": "j", "k": "k", "l": "l", "m": "m", "n": "n",
            "o": "o", "p": "p", "q": "q", "r": "r", "s": "s", "t": "t", "u": "u",
            "v": "v", "w": "w", "x": "x", "y": "y", "z": "z",

            "up_arrow": keys.UP,
            "down_arrow": keys.DOWN,
            "left_arrow": keys.LEFT,
            "right_arrow": keys.RIGHT,

            f"{keys.UP}": keys.UP,
            f"{keys.DOWN}": keys.DOWN,
            f"{keys.LEFT}": keys.LEFT,
            f"{keys.RIGHT}": keys.RIGHT,
            
            "escape": keys.ESCAPE, "\x1b": keys.ESCAPE,
            "backspace": keys.BACKSPACE, "\x08": keys.BACKSPACE,
            "space": keys.SPACE, " ": keys.SPACE,
            "tab": keys.TAB, "\t": keys.TAB,
            "enter": keys.ENTER
        }

    def GetKey(self):
        get = getkey()

        if get in self.keys:
            return self.keys[get]
        else:
            return get