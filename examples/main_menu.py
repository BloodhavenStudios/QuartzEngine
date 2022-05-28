from QuartzEngine.quartzengine import Engine   # Main Game Engine
from QuartzEngine import display as quartz     # Display module for colors and misc
from QuartzEngine.menu import Menu             # Makes menu

class Game(Engine):
  
  def setscenes(self):
    self.scenes = [self.menu]

  def menu(self):

    quartz.write("Game Title")

    menu = Menu(app=Game(),
                scene=0,
                options=["play", "quit"],
                design="=>",
                input_text="=> (")
    menu.on_use(1, action=lambda: print("play"))
    menu.on_use(2, action=lambda: print("Quit"))

Game.title = ""