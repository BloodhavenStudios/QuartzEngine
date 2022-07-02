
__all__ = ["Menu"]

class Menu(object):

  def __init__(self, engine, options, select):

    self.engine = engine
    self.options = options
    self.current_selected = 0
    if select in self.engine.Display.colours:
      color = self.engine.Display.select

    if self.options == []:
      pass
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
    if self.selected == option:
      func()
    else:
      pass