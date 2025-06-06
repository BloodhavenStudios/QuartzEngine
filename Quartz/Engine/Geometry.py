""" Handles Vec2 Objects for Pixel's, Frame's, and Camera's """

class Vec2:
    """ Object for Positioning or Scaling Pixel's, Frame's, or Camera's """

    __slots__ = "x", "y"

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __call__(self):
        return (self.x, self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
