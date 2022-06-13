from .display import display
from .errorhandler import *

import json
import os
from sys import stdout
from time import sleep
from getkey import getkey, keys

__all__ = ["Engine"]

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

    self.keys = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e",
                 "f": "f", "g": "g", "h": "h", "i": "i", "j": "j",
                 "k": "k", "l": "l", "m": "m", "n": "n", "o": "o",
                 "p": "p", "q": "q", "r": "r", "s": "s", "t": "t",
                 "u": "u", "v": "v", "w": "w", "x": "x", "y": "y",
                 "z": "z", "space": keys.SPACE, "tab": keys.TAB}
    
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

  def getkey(self):
    key = getkey()
    return self.keys[key.lower()]
    
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
    Display.write(text)
    stdout.flush()
    input()

  def save(self, data):
    with open("savedata.json", "w") as f:  json.dump(data, f, indent=4)

  def load(self):
    with open("savedata.json", "r") as f:  data = json.load(f)
    return data

  def start(self):
    self.setup()
    try:
      if os.name == "nt":  os.system(f"title {str(self.terminal_name)}")
      else:  os.system("""echo -n -e "\033]0;{}\007""".format(str(self.terminal_name)))
    except:  pass
    self.scenes[0]()