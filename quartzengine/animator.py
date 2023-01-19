from sys import stdout
from time import sleep
from .errorhandler import *

__all__ = ["Animation"]

class Animation(object):

  def __init__(self, engine=None, animation=None):
    self.animation = animation
    self.engine = engine
  
  def process_errors(self):
    if self.engine == None:
      raise AnimationException(message="Engine is NoneType.")
    if self.animation == None:
      raise AnimationException(message="Animation is NoneType.")
    if self.animation == []:
      raise AnimationException(message="Animation: {}, does not have any animatiable frames.".format(self.animation))

  def render(self, delay_between_frames=1, loop=1):
    self.process_errors()
    
    for i in range(loop):
      for frame in self.animation:
        self.engine.Display.clear()
        print(f"{frame}")
        sleep(delay_between_frames)
      self.engine.Display.clear()