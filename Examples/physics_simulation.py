# Importing Libs
from Quartz.engine import Engine, SceneController, Pixel, DynamicBody, Vector2, FPSCounter
from Quartz.graphics_engine import GraphicsEngine, Color
from Quartz.world_builder import World

from time import sleep

# DynamicBody() controls how a Pixel() will interact with the physics of a World() basically if they obey physics,
no_collision_gravity = DynamicBody(False, True)
collision_no_gravity = DynamicBody(True, False)
no_collision_no_gravity = DynamicBody(False, False)
collision_gravity = DynamicBody(True, True)

# Pixel() the things in a world you can manipulate their positions or just delete them!
e = Pixel(" ", no_collision_no_gravity)
d = Pixel(Color.set_foreground(Color.fromRGB(0, 165, 255)) + "#", no_collision_no_gravity)
b = Pixel(Color.set_foreground(Color.fromHEX("#A52A2A")) + "X", collision_no_gravity)

# A World before it is put inside a class
my_world = [
    [b,b,b,b,b,b,b,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,d,e,b,b,b,b],
    [b,b,b,b,e,d,e,b,b,b,b],
    [b,b,b,b,e,d,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,e,e,e,b,b,b,b],
    [b,b,b,b,b,b,b,b,b,b,b]
]

# Assigning Engine()
game = Engine()
# Assigning SceneController()
sc = SceneController()
# Assigning FPSCounter()
fps_counter = FPSCounter()
# Starting the FPSCounter()
fps_counter.start()

# Creating a new scene using SceneController()
@sc.new_scene
def simulation():
    while(True):
        # Clearing the terminal
        GraphicsEngine.clear()

        # Creating a World() using the array from earlier
        new_world = World(my_world)

        # Putting Pixel()'s in the world without destroying the clone of the world (the clone is used to replace where the Top layer of pixels have been for a background etc)
        # Re-Create a new pixel so the Vector2 doesnt bug out
        p = Pixel(Color.set_foreground(Color.fromRGB(255, 165, 0)) + "#", collision_gravity)
        new_world.world[1][5] = p
        new_world.world[4][5] = p
        new_world.world[6][5] = p

        # Getting a pixel which is basically our player.
        tester = new_world.world[1][5]

        # How fast the game will run
        fps_cap = game.FPS(int(input("FPS? ")))

        # Start the World() so the DynamicBody()'s have a purpose
        new_world.start_threaded_ticking(fps_cap)

        while(True):
            # Clearing the terminal yet again
            GraphicsEngine.clear()

            # Drawing the entire world! if you have a HUGE world or a procedurally generating one I reccommend you use a Camera()
            new_world.draw_world()

            print(tester.had_collision())
            print(tester.Vector2)
            if tester.had_collision():
                print(tester.below().Texture)
                input("End")
                del new_world, p
                break
                
            # fps somewhat
            sleep(fps_cap)

# Assigns which scene to run when you start the game
game.on_run = lambda: sc.load_scene(0)

# Gives the terminal a name
game.title_bar = "Simulation"

# Starts the game
game.run()
