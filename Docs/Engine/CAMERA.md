# 📹 Camera
Object to handle rendering `Frame`'s
```py
class Quartz.Engine.Camera(...)
```
```py
class Quartz.Engine.Camera(
    frame: Frame,
    position: Vec2,
    scale: Vec2,
    border: str
)
```

## Contents
[**Arguments**](#arguments)

[**Methods**](#methods)
- [\_\_init\_\_](#\_\_init\_\_)

## Arguments
`frame`: The `Frame` to render

`position`: Where the center of the `Camera` is positioned on the `Frame`

`scale`: The size of the lens of the `Camera` or scale of how much it sees

`border`: The outside of the frame of the camera If left as None no border will be showed.

## Methods

### \_\_init\_\_
Sets up the `Camera` based on parameters
```py
def __init__(
    self,
    frame: "Frame",
    position: "Vec2",
    scale: "Vec2",
    border: str = None
):
    self.frame = frame
    self.position = position
    self.scale = scale
    self.border = border
```

### render
Renders the `Frame` and `Pixel`'s inside of it, selecting the highest layer pixel per position.
```py
def render(self):
    # Calculate rendering bounds
    half_width, half_height = self.scale.x // 2, self.scale.y // 2
    start_x, end_x = self.position.x - half_width, self.position.x + half_width
    start_y, end_y = self.position.y - half_height, self.position.y + half_height

    # Combine parent and child pixel positions
    pixel_positions = self.frame.get_pixels_position()
    for position, pixels in pixel_positions.items():
        for pixel in pixels:
            if pixel.type == "Parent":
                for child_pixel in pixel.children_pixels:
                    pixel_positions.setdefault(child_pixel.position, set()).add(child_pixel)

    # Build the render buffer
    render_buffer = []
    if self.border: render_buffer.append(self.border * (self.scale.x + 3))  # Top border

    for y in range(start_y, end_y + 1):
        row = [self.border] if self.border else []
        for x in range(start_x, end_x + 1):
            highest_layer_pixel = max(
                (
                    pixel
                    for position, pixels in pixel_positions.items()
                    for pixel in pixels
                    if position.x == x and position.y == y
                ),
                key=lambda p: p.layer,
                default=None,
            )
            row.append(highest_layer_pixel.texture if highest_layer_pixel else self.frame.backdrop)
        if self.border:
            row.append(self.border)  # Right border
        render_buffer.append("".join(row))

    if self.border:
        render_buffer.append(self.border * (self.scale.x + 3))  # Bottom border

    # Print the render buffer
    print("\n".join(render_buffer))
```

<div style="width: 100%; margin-bottom: 7.5px;display: flex; justify-content: space-between;">
    <a href="#📹-camera" style="width: 100%; height: 2rem; background-color: #151B23; color: white; border-radius: 7.5px; padding: 10px; text-align: center; font-size: 16px; font-weight: 400;">Back to Top</a>
</div>
<div style="width: 100%; display: flex; justify-content: space-between;">
    <a href="FRAME.md" style="display: flex; justify-content: center; align-items: center; width: 47%; height: 3rem; background-color: #151B23; color: white; border-radius: 7.5px; padding: 10px; text-align: center; font-size: 16px; font-weight: 400;">Back to Frame</a>
    <a href="GEOMETRY.md" style="display: flex; justify-content: center; align-items: center; width: 47%; height: 3rem; background-color: #151B23; color: white; border-radius: 7.5px; padding: 10px; text-align: center; font-size: 16px; font-weight: 400;">Next To Geometry</a>
</div>