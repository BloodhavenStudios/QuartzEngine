# 📐 Geometry
Handles `Vec2` Objects for `Pixel`'s, `Frame`'s, and `Camera`'s
```py
Quartz.Engine.Vec2(...)
```
```py
Quartz.Engine.Vec2(
    x: int,
    y: int
)
```

## Contents
[**Arguments**](#arguments)

[**Methods**](#methods)
- [\_\_init\_\_](#\_\_init\_\_)
- [\_\_call\_\_](#\_\_call\_\_)
- [\_\_str\_\_](#\_\_str\_\_)

## Arguments

### \_\_init\_\_
Sets up the `Vec2` based on parameters
```py
def __init__(self, x: int, y: int) -> None:
    self.x = x
    self.y = y
```

### \_\_call\_\_
Returns `Vec2.x` and `Vec2.y` on call
```py
def __call__(self):
    return (self.x, self.y)
```

### \_\_str\_\_
Returns `Vec2.x` and `Vec2.y` as a string
```py
def __str__(self):
    return f"({self.x}, {self.y})"
```    

<div style="width: 100%; margin-bottom: 7.5px;display: flex; justify-content: space-between;">
    <a href="#📐-geometry" style="width: 100%; height: 2rem; background-color: #151B23; color: white; border-radius: 7.5px; padding: 10px; text-align: center; font-size: 16px; font-weight: 400;">Back to Top</a>
</div>
<div style="width: 100%; display: flex; justify-content: space-between;">
    <a href="CAMERA.md" style="display: flex; justify-content: center; align-items: center; width: 100%; height: 3rem; background-color: #151B23; color: white; border-radius: 7.5px; padding: 10px; text-align: center; font-size: 16px; font-weight: 400;">Back to Camera</a>
</div>