from .errorhandler import *
from sys import stdout

class Map(object):

  def __init__(self,
               map: list=None, width: int=None, height: int=None,
               char_map: dict=None,
               player=None):

    self.map = map

    self.char_map = char_map

    wall = False
    nav = False
    misc = False
    
    for key in self.char_map:
      if key == "wall":  wall = True
      if key == "navigatable":  nav = True
      if key == "misc_objects":  misc = True
    keys = [wall, nav, misc]

    for key in keys:
      if key == False:
        raise MapException(message=f"{key} is not in char_map. please put key in char_map.")
    
    self.player = player
    self.width = width
    self.height = height

  def display(self):
    current_key = 0
    for i in range(self.height):
      for i in range(self.width):
        stdout.flush()
        stdout.write(self.map[current_key])
        current_key += 1
      print("")