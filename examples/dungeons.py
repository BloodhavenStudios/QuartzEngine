from QuartzEngine.quartzengine import Engine
from QuartzEngine.animator import Animation
from QuartzEngine.menu import Menu
from QuartzEngine import display as quartz

class Game(Engine):

  def setscenes(self):
    self.scenes = [self.test_key]
  
  def test_key(self):
    print("use 'w'")
    key = self.getkey("Enter a key: ")
    if key == self.keys["w"]:
      print("Used w")
    else:
      print("Invalid")

Game().start()