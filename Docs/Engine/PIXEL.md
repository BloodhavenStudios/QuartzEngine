
# 🟥 Pixel
Object to manipulate inside Frame's
```py
class Quartz.Engine.Pixel(...)
```
```py
class Quartz.Engine.Pixel(
    texture: str,
    dynamics: Quartz.Engine.Dynamics.Dynamics,
    frame: Quartz.Engine.Frame.Frame,
    position: Quartz.Engine.Geometry.Vec2,
    scale: Quartz.Engine.Geometry.Vec2,
    layer: int,
    cluster: str,
    sub_pixel: bool
)
```

## Contents
[**Arguments**](#arguments)

[**Methods**](#methods)
- [\_\_init\_\_](#\_\_init\_\_)
- [\_\_call\_\_](#\_\_call\_\_)
- [\_\_str\_\_](#\_\_str\_\_)
- [_is_child](#_is_child)
- [_set_scale](#_set_scale)
- [move](#move)

[**Events**](#events)
- [on_texture_change](#on_texture_change)
- [on_type_change](#on_type_change)
- [on_dynamics_change](#on_dynamics_change)
- [on_frame_change](#on_frame_change)
- [on_position_change](#on_position_change)
- [on_scale_change](#on_scale_change)
- [on_layer_change](#on_layer_change)
- [on_cluster_change](#on_cluster_change)

## Arguments
`texture`: String that shown for the "texture" of the object once rendered by a `Camera`.

`dynamics`: Manipulates how this `Pixel` interact with other `Pixel`'s.

`frame`: Object to store the `Pixel` so the pixel does something.

`position`: The position the `Pixel` is at on the frame.

`scale`: The scale (size) of the `Pixel`. Scale does not accept negative values inside the Vec2.

`layer`: The layer of the `Frame` the `Pixel` is on.

`cluster`: A family to relate it to other `Pixel`'s like: "parents"

`sub_pixel`: Shouldn't be changed unless it is a child of a parent `Pixel`.

## Methods

### \_\_init\_\_
Sets up the `Pixel` based on parameters
```py
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
```

### \_\_call\_\_
Returns `Pixel.texture` on call
```py
def __call__(self) -> str:
    return self._texture
```

### \_\_str\_\_
Returns `Pixel.texture` as a string
```py
def __str__(self) -> str:
    return self._texture
```

### _is_child
Determines if the `Pixel` is a child of a parent `Pixel`.
```py
def _is_child(self):
    return isinstance(self, Pixel) and self.__class__ is not Pixel
```


### _set_scale
Scales an object based on current scale value
```py
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
```

### move
Moves a `Pixel` in a set direction
```py
def move(self, direction: Pixel.Direction) -> "Vec2":
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
```

## Events
Pixels have auto triggering Events via wrappers

### on_texture_change
Runs after `Pixel.texture` is changed
```py
@Pixel.on_texture_change
def on_texture_change(before, after):
    before_texture_change = before
    after_texture_change = after
```

### on_type_change
Runs after `Pixel.type` is changed
```py
@Pixel.on_type_change
def on_type_change(before, after):
    before_type_change = before
    after_type_change = after
```

### on_dynamics_change
Runs after `Pixel.dynamics` is changed
```py
@Pixel.on_dynamics_change
def on_dynamics_change(before, after):
    before_dynamics_change = before
    after_dynamics_change = after
```

### on_frame_change
Runs after `Pixel.frame` is changed
```py
@Pixel.on_frame_change
def on_frame_change(before, after):
    before_frame_change = before
    after_frame_change = after
```

### on_position_change
Runs after `Pixel.position` is changed
```py
@Pixel.on_position_change
def on_position_change(before, after):
    before_position_change = before
    after_position_change = after
```

### on_scale_change
Runs after `Pixel.scale` is changed
```py
@Pixel.on_scale_change
def on_scale_change(before, after):
    before_scale_change = before
    after_scale_change = after
```

### on_layer_change
Runs after `Pixel.layer` is changed
```py
@Pixel.on_layer_change
def on_layer_change(before, after):
    before_layer_change = before
    after_layer_change = after
```

### on_cluster_change
Runs after `Pixel.cluster` is changed
```py
@Pixel.on_cluster_change
def on_cluster_change(before, after):
    before_cluster_change = before
    after_cluster_change = after
```
<div style="width: 100%; margin-bottom: 7.5px;display: flex; justify-content: space-between;">
    <a href="#🟥-pixel" style="width: 100%; height: 2rem; background-color: #151B23; color: white; border-radius: 7.5px; padding: 10px; text-align: center; font-size: 16px; font-weight: 400;">Back to Top</a>
</div>
<div style="width: 100%; display: flex; justify-content: space-between;">
    <a href="CONTENTS.md" style="display: flex; justify-content: center; align-items: center; width: 47%; height: 3rem; background-color: #151B23; color: white; border-radius: 7.5px; padding: 10px; text-align: center; font-size: 16px; font-weight: 400;">Back to Contents</a>
    <a href="DYNAMICS.md" style="display: flex; justify-content: center; align-items: center; width: 47%; height: 3rem; background-color: #151B23; color: white; border-radius: 7.5px; padding: 10px; text-align: center; font-size: 16px; font-weight: 400;">Next To Dynamics</a>
</div>