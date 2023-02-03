from typing import Optional

import asyncio
from sys import stdout

__all__: tuple[str, ...] = ("Map",)

"""
Example Map

b = GameObject("■")
e = GameObject(" ")

map = [
[e,e,b,b,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,]
[b,b,b,b,b,b,b,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,b,e,]
[b,b,b,b,b,b,b,b,b,b,b,e,e,e,e,e,b,b,b,b,e,b,b,b,e,e,e,e,e,e,e,b,b,]
[b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,]
"""

class Map(object):

    def __init__(self, map: list=None):
        self.map = map
    
    def __call__(self):
        Yy = 0
        Xx = 0
        for y in self.map:
            for x in y:
                x.X = Xx
                x.Y = Yy
                x.update_Vector2()
                
                asyncio.run(self.handle_object(x))
                
                Xx += 1
            Yy += 1
            Xx = 0

    async def handle_object(self, object):
        if object.rigidbody.uses_gravity:
            below = self.map[object.Y+1][object.X]
            await asyncio.sleep(1)
            if below.texture not in object.rigidbody.collides_with:
                self.map[object.Y][object.X] = " "
                object.Y += 1
                below = object.texture

    def DrawMap(self):
        for y in self.map:
            for x in y:
                stdout.flush()
                stdout.write(x.texture)
            print("")
        print("")
