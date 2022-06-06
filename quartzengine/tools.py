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
      else:  self.current_swit ch = 0
      return self.toggles[self.current_switch]

class loops(object):
  
  @property
	def seconds(self):
		return self._seconds
		
	@seconds.setter
	def seconds(self, value: float):
		self._seconds = value
	
	def __init__(self):
		self._seconds = 0.0
		
	def loop(self):
		pass
		
	def loop_process(self):
		while True:
			self.loop()
			sleep(self._seconds)
			
	def start(self):
		thread = Thread(target=self.loop_process, daemon=True)
		thread.start()