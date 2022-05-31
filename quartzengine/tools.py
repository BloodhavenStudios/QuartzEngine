from threading import Thread
from time import sleep

__all__ = ("Switch", "loops")

class Switch(object):

    def __init__(self, toggle1, toggle2):
      self.toggles = [toggle1, toggle2]
      self.current_switch = 1
      self.toggle()

    def get(self):
      return self.toggles[self.current_switch]
    
    def toggle(self):
      if self.current_switch == 0:  self.current_switch += 1
      else:  self.current_switch = 0
      return self.toggles[self.current_switch]

class loops(Thread):

  @property
  def seconds(self):
    return self.seconds

  @seconds.setter
  def seconds(self, value: float):
    self.seconds = value

  def __init__(self):
    self.seconds = 0
    self.task = self.loop

  def loop(self):
    pass

  def start(self, *args, **kwargs):
    while True:
      self.loop()
      sleep(self.seconds)