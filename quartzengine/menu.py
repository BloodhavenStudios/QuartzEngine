class Menu(object):

  def __init__(self, app, scene, options, design, input_text):

    self.app = app
    self.scene = scene
    
    self.options = options
    self.makeOptions = [""]

    if options == []:
      pass
    else:
      i = 1
      for option in self.options:
        self.makeOptions.append(option)
        print(f"{i}{design} {option}")
        i += 1

    self.choicePick = input(f"{input_text} ")

  def on_use(self, option=None, action=None):
    i=1
    for Option in self.options:
      if option != len(self.choicePick):
        self.app.set_scene(int(self.scene))
      elif int(self.choicePick) == int(option):
        action()
        break
      elif int(self.choicePick) != int(option):
        self.app.set_scene(int(self.scene))
      else:  i += 1