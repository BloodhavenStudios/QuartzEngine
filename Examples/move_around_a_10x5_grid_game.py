from Quartz import *
from getkey import getkey, keys
from time import sleep

# Create a DynamicBody()
db = DynamicBody(False, False)

# Create Pixels
e = Pixel(Color.set_background(Color.fromRGB(255,255,255)) + " " + Color.reset(), db)
player = Pixel(Color.set_foreground(Color.fromRGB(0,0,0)) + " " + Color.reset(), db)

# Create a 10x5 array
map = [[e] * 10 for _ in range(5)]

# Creating a new world
world = World(map)
# Setting the player in the centerish of the world
world.world[2][4] = player

# assigning Engine() and SceneController()
engine = Engine()
sc = SceneController()

# Creating a new_scene
@sc.new_scene
def game():
    while(True):
        # Clearing Terminal
        GraphicsEngine.clear()

        # Drawing World
        world.draw_world()

        # Printing the Vector2 of the player Pixel()
        print(f"Vec2: {player.Vector2}")

        # Using getkey libary
        # You can remove the False to make it less flickery since theres no gravity
        key = getkey(False)
        if key == keys.UP:
            player.move("UP", 1)
        elif key == keys.DOWN:
            player.move("DOWN", 1)
        elif key == keys.LEFT:
            player.move("LEFT", 1)
        elif key == keys.RIGHT:
            player.move("RIGHT", 1)

        # resting to prevent lag
        # Can remove if you remove False from getkey()
        sleep(fps_cap)

# Set FPS
fps_cap = engine.FPS(10)

# Select first scene to run
engine.on_run = lambda: sc.load_scene(0)
# Set terminal title
engine.title_bar = "Move Around A 10x5 Grid Game"

# VERY IMPORTANT or else the player wont move
# start the Thread() for the world to update Vector2() of Pixel()'s
world.start_threaded_ticking(fps_cap)

# Run the game
engine.run()
