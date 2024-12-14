""" Handles the Frame for putting Pixel's inside. """
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Quartz.Engine.Pixel import Pixel

class Frame:
    """ Object to put Pixels inside of like the old World() object """

    __slots__ = "backdrop", "pixels", "cameras"

    def __init__(self, backdrop: "Pixel") -> None:
        self.backdrop = backdrop
        self.pixels = list()
        self.cameras = set()

    def get_pixels(self) -> list:
        """ Returns every pixel placed on this Frame """
        return self.pixels

    def get_pixels_position(self) -> dict:
        """ Returns every pixel in each Vec2 Position """
        positions = {}
        for pixel in self.get_pixels():
            positions.setdefault(pixel.position, []).append(pixel)
        return positions

    def get_pixels_position_as_string(self) -> dict:
        """ Returns every pixel in each Vec2 Position in string format """
        positions, pos_string = {}, ""
        for pixel in self.get_pixels():
            positions.setdefault(pixel.position(), []).append(pixel())
        return positions

    def get_pixels_by_cluster(self, cluster: str) -> set:
        """ Returns every pixel in a specific cluster placed on this Frame. """
        pixels = self.get_pixels()
        target_pixels = list()
        for pixel in pixels:
            if pixel.cluster == cluster:
                target_pixels.append(pixel)
        return target_pixels
