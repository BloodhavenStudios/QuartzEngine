""" Handle's Pixel's the building blocks of your game. """
from typing import TYPE_CHECKING
import functools
from enum import Enum
if TYPE_CHECKING:
    from Quartz.Engine.Dynamics import Dynamics
    from Quartz.Engine.Frame import Frame
from Quartz.Engine.Geometry import Vec2

class Pixel:
    """ Object to manipulate inside Frame's """

    def on_texture_change(self, func):
        self.event_handlers["on_texture_change"].append(func)
        return func

    def on_type_change(self, func):
        self.event_handlers["on_type_change"].append(func)
        return func

    def on_dynamics_change(self, func):
        self.event_handlers["on_dynamics_change"].append(func)
        return func

    def on_frame_change(self, func):
        self.event_handlers["on_frame_change"].append(func)
        return func

    def on_position_change(self, func):
        self.event_handlers["on_position_change"].append(func)
        return func

    def on_scale_change(self, func):
        self.event_handlers["on_scale_change"].append(func)
        return func

    def on_layer_change(self, func):
        self.event_handlers["on_layer_change"].append(func)
        return func

    def on_cluster_change(self, func):
        self.event_handlers["on_cluster_change"].append(func)
        return func

    class Direction(Enum):
        UP = "up"
        DOWN = "down"
        LEFT = "left"
        RIGHT = "right"

    @property
    def texture(self):
        return self._texture

    @texture.setter
    def texture(self, value: str):
        before = self._texture
        self._texture = value
        for event in self.event_handlers.get("on_texture_change"):
            event(before, value)

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value: str):
        before = self._type
        self._type = value
        for event in self.event_handlers.get("on_type_change"):
            event(before, value)

    @property
    def dynamics(self):
        return self._dynamics

    @dynamics.setter
    def dynamics(self, value: "Dynamics"):
        before = self._dynamics
        self._dynamics = value
        for event in self.event_handlers.get("on_dynamics_change"):
            event(before, value)

    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, value: "Frame"):
        before = self._frame
        self._frame = value
        for event in self.event_handlers.get("on_frame_change"):
            event(before, value)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value: "Vec2"):
        before = self._position
        self._position = value
        for event in self.event_handlers.get("on_position_change"):
            event(before, value)

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value: "Vec2"):
        before = self._scale
        self._scale = value
        self._set_scale()
        for event in self.event_handlers.get("on_scale_change"):
            event(before, value)

    @property
    def layer(self):
        return self._layer

    @layer.setter
    def layer(self, value: int):
        before = self._layer
        self._layer = value
        for event in self.event_handlers.get("on_layer_change"):
            event(before, value)

    @property
    def cluster(self):
        return self._cluster

    @cluster.setter
    def cluster(self, value: int):
        before = self._cluster
        self._cluster = value
        for event in self.event_handlers.get("on_cluster_change"):
            event(before, value)

    __slots__ = "_texture", "_type", "_dynamics", "_frame", "_position", "_scale", "_layer", "_cluster", "children_pixels", "event_handlers"

    def __init__(
        self,
        texture: str | str,
        dynamics: "Dynamics",
        frame: "Frame",
        position: "Vec2",
        scale: "Vec2",
        layer: int = 1,
        cluster: str=None,
        sub_pixel: bool = False
    ) -> str:
        self._texture = texture
        self._type = "Single" if sub_pixel is False else "Child" 
        self._dynamics = dynamics
        self._frame = frame
        self._position = position
        self._scale = scale
        self._layer = layer
        self._cluster = cluster
        
        self.children_pixels = list()

        self.event_handlers = {
            "on_texture_change": [],
            "on_type_change": [],
            "on_dynamics_change": [],
            "on_frame_change": [],
            "on_position_change": [],
            "on_scale_change": [],
            "on_layer_change": [],
            "on_cluster_change": []
        }

        self._set_scale()

        if self._is_child():
            self.cluster = type(self).__name__

        if sub_pixel == False:
            self.frame.pixels.append(self)
            self._type = "Parent" if self.children_pixels != list() else "Single"

    def __call__(self) -> str:
        # Return self.Texture
        return self._texture

    def __str__(self) -> str:
        # Return self.Texture
        return self._texture

    def _is_child(self):
        return isinstance(self, Pixel) and self.__class__ is not Pixel

    def _set_scale(self):
        self.children_pixels = list()

        if self._scale.x != 1 or self._scale.y != 1:
            for x_scale in range(self._scale.x):
                for y_scale in range(self._scale.y):
                    position = Vec2(self.position.x + x_scale, self.position.y - y_scale)
                    child_pixel = Pixel(
                        self.texture, self.dynamics, self.frame, position, Vec2(1, 1), self.layer, sub_pixel=True
                    )
                    self.children_pixels.append(child_pixel)

        self._type = "Parent" if self.children_pixels != list() else "Single"

    def move(self, direction) -> "Vec2":
        """Moves a Pixel in a set direction."""
        delta = {
            Pixel.Direction.UP: (0, -1),
            Pixel.Direction.DOWN: (0, 1),
            Pixel.Direction.LEFT: (-1, 0),
            Pixel.Direction.RIGHT: (1, 0)
        }.get(direction, (0, 0))

        # Update positions for the pixel and its children
        self.position.x += delta[0]
        self.position.y += delta[1]
        for child_pixel in self.children_pixels:
            child_pixel.position.x += delta[0]
            child_pixel.position.y += delta[1]

        return self.position()
