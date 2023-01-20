from Quartz.engine import Engine, GameObject, RigidBody
from Quartz.map import Map
from Quartz.input import Input

from colorama import Fore

P = GameObject(texture=Fore.RED + "●" + Fore.RESET)

e = GameObject(texture=" ")
g = GameObject(texture=Fore.GREEN + "#" + Fore.RESET)
d = GameObject(texture=Fore.LIGHTYELLOW_EX + "#" + Fore.RESET)

map = [
[e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],
[e,e,g,g,g,g,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],
[g,g,d,d,d,d,g,e,P,e,e,e,g,g,g,g,e,e,e,e,e,e,e,e],
[d,d,d,d,d,d,d,g,g,g,g,g,d,d,d,d,g,g,g,g,e,e,e,e],
[d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,g,g,g,g,g],
[d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d]
]

map = Map(map)

Input = Input()

class Game(Engine):
    
    def setup(self):
        self.SceneManager.LoadScene(0)
        
    def root(self):
        map.DrawMap()
        
        print(P.X)
        print(P.Y)
        
game = Game()
game.title = "My Game"
game.run()