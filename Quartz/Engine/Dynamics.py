""" Handles Dynamics to manipulate how Pixel's interact with other Pixel's. """

class Dynamics:
    """ Object for manipulating how Pixel's interact with other Pixel's. """

    __slots__ = "is_collidable", "collidable_pixels", "non_collidable_pixels", "gravity_force"

    def __init__(
        self,
        is_collidable: bool,
        collidable_pixels: list,
        non_collidable_pixels: list,
        gravity_force: int
    ) -> None:
        self.is_collidable = is_collidable
        self.collidable_pixels = collidable_pixels
        self.non_collidable_pixels = non_collidable_pixels
        self.gravity_force = gravity_force
