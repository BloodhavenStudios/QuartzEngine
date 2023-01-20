from .input import Input
from colorama import Fore

__all__ = ["Menu"]

Input = Input()

class Menu(object):

  def __init__(self, engine, options, select):

    self.engine = engine
    self.options = options
    self.current_selected = 0

    color = self.engine.Display.white
    if select in self.engine.Display.colours:
      color = select

    if self.options == []:
      pass

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



class Pool(object):

  def __init__(self, loot_table: dict=None):
    self.loot_table = loot_table
    self.chances = []

  def process_errors(self):
    
    if self.loot_table == None:
      raise PoolException(message="loot_pool not provided.")

    total = 0
    for key in self.loot_table:
      total += self.loot_table[key]
    if total >= 99:
      raise PoolException(message="Pool total is under 100 please keep the total loot pool at 100")
    if total >= 101:
      raise PoolException(message="Pool total is over 100 please keep the total loot pool at 100")

  def roll(self):
    self.process_errors()

    self.loot_table = []
    for key in self.loot_table:
      percent = self.loot_table[key]
      for i in range(percent):  self.chances.append(key)

    return choice(self.chances)
    else:
      for option, i in enumerate(self.options):
        if self.current_selected == i:
          print(color + option + self.engine.Display.reset)
        else:
          print(option)

    selected = False
    while not selected:
      if self.engine.key("w") or self.engine.key("up_arrow"):
        if self.current_selected != 0 and self.current_selected != int(len(self.options)-1):
          self.current_selected += 1
      if self.engine.key("s") or self.engine.key("down_arrow"):
        if self.current_selected != 0 and self.current_selected != int(len(self.options)-1):
          self.current_selected -= 1
      if self.engine.key("enter") or self.engine.key("space"):
        selected = True
        break
    
  def on_click(self, option, func):
    if self.selected == self.options[option]:
      func()
    else:
      pass

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



class Pool(object):

  def __init__(self, loot_table: dict=None):
    self.loot_table = loot_table
    self.chances = []

  def process_errors(self):
    
    if self.loot_table == None:
      raise PoolException(message="loot_pool not provided.")

    total = 0
    for key in self.loot_table:
      total += self.loot_table[key]
    if total >= 99:
      raise PoolException(message="Pool total is under 100 please keep the total loot pool at 100")
    if total >= 101:
      raise PoolException(message="Pool total is over 100 please keep the total loot pool at 100")

  def roll(self):
    self.process_errors()

    self.loot_table = []
    for key in self.loot_table:
      percent = self.loot_table[key]
      for i in range(percent):  self.chances.append(key)

    return choice(self.chances)