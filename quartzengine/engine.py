# Get Modules
from .display import display
from .errorhandler import *

import json
import os
from sys import stdout
from time import sleep

try:
  from getkey import getkey, keys
except ImportError:
  try:
    os.system("pip install git+https://github.com/li-rupert/getkey")
  except:
    input("Cannot install dependency. Please make sure you have git installed on your computer.")


# Define class
__all__ = ["Engine"]


# Main Game Engine
class Engine(object):

  @property
  def title(self):
    return self.name

  @title.setter
  def title(self, value: str):
    self.name = value

  def __init__(self):
    self.name = f"QuartzEngine | {os.path.basename(__file__)}"
    self.Display = display()

    self.keys = {
      "a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g",
      "h": "h", "i": "i", "j": "j", "k": "k", "l": "l", "m": "m", "n": "n",
      "o": "o", "p": "p", "q": "q", "r": "r", "s": "s", "t": "t", "u": "u",
      "v": "v", "w": "w", "x": "x", "y": "y", "z": "z",
                 
      "escape": keys.ESCAPE, "\x1b": keys.ESCAPE,
      "backspace": keys.BACKSPACE, "\x08": keys.BACKSPACE,
      "space": keys.SPACE, " ": keys.SPACE,
      "tab": keys.TAB, "\t": keys.TAB,
      "enter": keys.ENTER,
      "up_arrow": keys.UP,
      "down_arrow": keys.DOWN,
      "left_arrow": keys.LEFT,
      "right_arrow": keys.RIGHT}
    
    self.scenes = [self.root]
    self.current_scene = 0

  def setup(self):
    pass

  def root(self):
    print("Default Scene")

  def set_scene(self, scene=None):
    if scene == None:
      if self.current_scene != len(self.scenes):
        self.current_scene += 1
        print(self.Display.reset + "")
        self.Display.clear()
        self.scenes[self.current_scene]()
    else:
      if scene != len(self.scenes):
        print(self.Display.reset)
        self.Display.clear()
        self.current_scene = scene
        self.scenes[scene]()
    try:
      a = self.scenes[scene] 
    except:
      raise SceneException(scene)

  def key(self, key):
    press = getkey()
    try:
      if key == self.keys[key]:
        if press == key:
          return True
        else:
          return False
    except:
      pass
    
  def rest(self, duration=None):
    
    timedict = {"s": 1, "m": 60, "h": 3600}
    smh = duration[-1:]
    
    if duration == None:
      raise RestException(duration)
    elif smh not in timedict:
      raise RestException(smh)
    else:
      smhduration = ""
      for char in duration:
        if char != smh:  smhduration += char
        else:  break
      smhduration = int(smhduration)

      if smh == "s":  time = smhduration
      elif smh == "m":  time = int(timedict["m"] * smhduration)
      elif smh == "h":  time = int(timedict["h"] * smhduration)
      
      return sleep(time)
    
  def on_error(self, text):
    self.Display.write(text)
    stdout.flush()
    input()

  def save(self, data):
    with open("savedata.json", "w") as f:
      json.dump(data, f, indent=4)

  def load(self):
    with open("savedata.json", "r") as f:
      data = json.load(f)
    return data

  def start(self):
    self.setup()
    if os.name == "nt":
      os.system(f"title {str(self.terminal_name)}")
    self.scenes[0]()
