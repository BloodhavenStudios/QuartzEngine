# 🖼️ Frame
Object to store `Pixel`'s inside of so they do something.
```py
class Quartz.Engine.Frame(...)
```
```py
class Quartz.Engine.Frame(
    backdrop: str | Pixel
)
```

## Contents
[**Arguments**](#arguments)

[**Methods**](#methods)
- [\_\_init\_\_](#\_\_init\_\_)
- [get_pixels](#get_pixels)
- [get_pixels_position](#get_pixels_position)
- [get_pixels_position_as_string](#get_pixels_position_as_string)
- [get_pixels_by_cluster](#get_pixels_by_cluster)

## Arguments
`backdrop`: What the background of the `Frame` looks like. 

## Methods

### \_\_init\_\_
Sets up the `Frame` based on parameters
```py
def __init__(self, backdrop: "Pixel") -> None:
    self.backdrop = backdrop
    self.pixels = list()
    self.cameras = set()
```

### get_pixels
Returns every `Pixel` placed on the `Frame`
```py
def get_pixels(self) -> list:
    return self.pixels
```

### get_pixels_position
Returns every `Pixel` in each `Vec2` Position
```py
def get_pixels_position(self) -> dict:
    positions = {}
    for pixel in self.get_pixels():
        positions.setdefault(pixel.position, []).append(pixel)
    return positions
```

### get_pixels_position_as_string
Returns every `Pixel` in each `Vec2` Position in string format
```py
def get_pixels_position_as_string(self) -> dict:
    positions, pos_string = {}, ""
    for pixel in self.get_pixels():
        positions.setdefault(pixel.position(), []).append(pixel())
    return positions
```

### get_pixels_by_cluster
Returns every `Pixel` in a specific cluster placed on this `Frame`.
```py
def get_pixel_by_cluster(self, cluster: str) -> set:
    pixels = self.get_pixels()
    target_pixels = list()
    for pixel in pixels:
        if pixel.cluster == cluster:
            target_pixels.append(pixel)
    return target_pixels
```

<div style="width: 100%; margin-bottom: 7.5px;display: flex; justify-content: space-between;">
    <a href="#⬇️-dynamics" style="width: 100%; height: 2rem; background-color: #151B23; color: white; border-radius: 7.5px; padding: 10px; text-align: center; font-size: 16px; font-weight: 400;">Back to Top</a>
</div>
<div style="width: 100%; display: flex; justify-content: space-between;">
    <a href="DYNAMICS.md" style="display: flex; justify-content: center; align-items: center; width: 47%; height: 3rem; background-color: #151B23; color: white; border-radius: 7.5px; padding: 10px; text-align: center; font-size: 16px; font-weight: 400;">Back to Dynamics</a>
    <a href="CAMERA.md" style="display: flex; justify-content: center; align-items: center; width: 47%; height: 3rem; background-color: #151B23; color: white; border-radius: 7.5px; padding: 10px; text-align: center; font-size: 16px; font-weight: 400;">Next To Camera</a>
</div>