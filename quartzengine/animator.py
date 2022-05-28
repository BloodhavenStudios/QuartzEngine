from sys import stdout
from time import sleep
from .display import Display

class Animation(object):

  def __init__(self, animation=None):
    self.animation = animation

  def process_errors(self):
    if self.animation == None:  return "Animation not provided"
    elif self.animation == []:  return "No frames to animate"

  def render(self, delay_between_frames=1, loop=1):
    self.process_errors()
    for i in range(loop):
      for frame in self.animation:
        Display.clear()
        print(f"{frame}")
        sleep(delay_between_frames)
      Display.clear()