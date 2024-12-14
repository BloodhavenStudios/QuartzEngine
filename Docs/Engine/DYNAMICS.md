# ⬇️ Dynamics
Manipulates how `Pixel`'s interact with other `Pixel`'s.
```py
class Quartz.Engine.Dynamics(...)
```
```py
class Quartz.Engine.Dynamics(
    is_collidable: bool,
    collidable_pixels: list,
    non_collidable_pixels: list,
    gravity_force: int
)
```

## Contents
[**Arguments**](#arguments)

[**Methods**](#methods)
- [\_\_init\_\_](#\_\_init\_\_)

## Arguments
`is_collidable`: Boolean that decides if the `Dynamics` allow the attached `Pixel` to Collide with other Collidable `Pixel`'s

`collidable_pixels`: List of valid collidable `Pixel`'s

`non_collidable_pixels`: List of invalid collidable `Pixel`'s even if they have `is_collidable` set to true

`gravity_force`: The weight of gravity against the `Pixel` if set to 0 the pixel doesn't have gravity on it. 

## Methods

### \_\_init\_\_
Sets up `Dynamics` based on parameters
```py
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
```

<div style="width: 100%; margin-bottom: 7.5px;display: flex; justify-content: space-between;">
    <a href="#⬇️-dynamics" style="width: 100%; height: 2rem; background-color: #151B23; color: white; border-radius: 7.5px; padding: 10px; text-align: center; font-size: 16px; font-weight: 400;">Back to Top</a>
</div>
<div style="width: 100%; display: flex; justify-content: space-between;">
    <a href="PIXEL.md" style="display: flex; justify-content: center; align-items: center; width: 47%; height: 3rem; background-color: #151B23; color: white; border-radius: 7.5px; padding: 10px; text-align: center; font-size: 16px; font-weight: 400;">Back to Pixel</a>
    <a href="FRAME.md" style="display: flex; justify-content: center; align-items: center; width: 47%; height: 3rem; background-color: #151B23; color: white; border-radius: 7.5px; padding: 10px; text-align: center; font-size: 16px; font-weight: 400;">Next To Frame</a>
</div>