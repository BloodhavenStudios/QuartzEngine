from sys import stdout

__all__ = ["Map"]

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

    def DrawMap(self):
        for y in self.map:
            for x in y:
                stdout.flush()
                stdout.write(x.texture)
        print("")