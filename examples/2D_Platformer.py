from Quartz.engine import Engine, GameObject, RigidBody
from Quartz.map import Map
from Quartz.input import Input

from colorama import Fore
from time import sleep

P = GameObject(texture=Fore.RED + "●" + Fore.RESET)

e = GameObject(texture=" ")
g = GameObject(texture=Fore.GREEN + "#" + Fore.RESET)
d = GameObject(texture=Fore.LIGHTYELLOW_EX + "#" + Fore.RESET)

map = [
[e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],
[e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],
[e,e,g,g,g,g,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,g,g,g,g,g,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],
[g,g,d,d,d,d,g,e,P,e,e,e,g,g,g,g,e,e,e,e,e,e,e,e,e,g,g,g,d,d,d,d,d,g,g,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],
[d,d,d,d,d,d,d,g,g,g,g,g,d,d,d,d,g,g,g,g,e,e,e,e,g,d,d,d,d,d,d,d,d,d,d,g,g,g,g,g,g,g,g,g,g,g,e,e,e,e],
[d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,g,g,g,g,g,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,g,g,g,g],
[d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d]
]

map = Map(map)

Input = Input()

class Game(Engine):
    
    def setup(self):
        self.SceneManager.LoadScene(0)
        
    def root(self):
        while(True):
            self.GraphicsEngine.clear()
            print("QuartzEngine Beta\nUse 'a' and 'd' to move")
            map.DrawMap()
            map()

            r = map.map[P.Y][int(P.X+1)]
            c = map.map[P.Y][int(P.X)]
            l = map.map[P.Y][int(P.X-1)]
            print("'" + l.texture + "'", "\t", c.texture, "\t", "'" + r.texture + "'")

            print("Player X, Y: " + str(P.Vector2))

            key = Input.GetKey()
            if key == Input.keys["a"]:
                if map.map[P.Y][int(P.X-1)] != g:
                    map.map[P.Y][int(P.X-1)] = P
                    map.map[P.Y][P.X] = e
            if key == Input.keys["d"]:
                if map.map[P.Y][int(P.X+1)] != g:
                    map.map[P.Y][int(P.X+1)] = P
                    map.map[P.Y][P.X] = e
            if key == Input.keys["space"]:
                map.map[P.Y-1][int(P.X)] = P
                map.map[P.Y][P.X] = e

            sleep(0.01)
        
game = Game()
game.title = "QuartzEngine Testing"
game.run()