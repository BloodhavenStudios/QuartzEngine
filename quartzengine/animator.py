from sys import stdout
from time import sleep
from .display import Display
from .errorhandler import *

class Animation(object):

  def __init__(self, animation=None):
    self.animation = animation

  def process_errors(self):
    if self.animation == None:  return raise AnimationException(message="Animation is NoneType.")
    elif self.animation == []:  return raise AnimationException(message="Animation: {}, does not have any animatiable frames.".format(self.animation))

  def render(self, delay_between_frames=1, loop=1):
    self.process_errors()
    
    for i in range(loop):
      for frame in self.animation:
        Display.clear()
        print(f"{frame}")
        sleep(delay_between_frames)
      Display.clear()