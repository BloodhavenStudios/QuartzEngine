
class RGB:

    __slots__ = "_r", "_g", "_b"

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value: int):
        self._r = value

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value: int):
        self._g = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value: int):
        self._b = value

    def __init__(self, r: int, g: int, b: int) -> 255:
        self._r = r
        self._g = g
        self._b = b

    def __call__(self):
        return (self.r, self.g, self.b)

    def set(self, r: int, g: int, b: int):
        if r > 255 and g > 255 and b > 255:
            raise EnvironmentError()
        self._r = r
        self._g = g
        self._b = b

    def set_from_hex(self, hexcode: str):
        hexcode = hexcode.lstrip("#")
        r = int(hexcode[0:2], 16)
        g = int(hexcode[2:4], 16)
        b = int(hexcode[4:6], 16)
        self.set(r, g, b)

def set_fg(RGB: RGB):
    return f"\033[38;2;{RGB.r};{RGB.g};{RGB.b}m"

def set_bg(RGB: RGB):
    return f"\033[48;2;{RGB.r};{RGB.g};{RGB.b}m"

def reset():
    return "\033[0m"