from typing import Optional

import os
import tkinter as tk
from tkinter.font import Font
import time
import threading

from .graphics_engine import *
from .error_handler import *

__all__: tuple[str, ...] = (
    "FPSCounter",
    "Vector2",
    "DynamicBody",
    "Pixel",
    "Camera",
    "SceneController",
    "Engine",
)



class FPSCounter:
    def __init__(self):
        self.frame_count = 0
        self.start_time = time.time()
        self.running = True

        self.root = None
        self.fps_label = None

    def create_window(self):
        self.root = tk.Tk()
        self.root.title("FPS Counter")

        bold_font = Font(family="Arial", size=12, weight="bold")
        self.fps_label = tk.Label(self.root, text="FPS: 0", font=bold_font)
        self.fps_label.pack()
        self.root.mainloop()

    def calculate_fps(self):
        while self.running:
            # Calculate the elapsed time for each frame
            elapsed_time = time.time() - self.start_time

            # Increment the frame count
            self.frame_count += 1

            # Update the FPS every second
            if elapsed_time >= 1.0:
                fps = self.frame_count / elapsed_time
                self.fps_label.config(text=f"FPS: {fps:.2f}")

                # Reset the frame count and start time
                self.frame_count = 0
                self.start_time = time.time()

            # Delay for a short interval (adjust as needed)
            time.sleep(0.01)

    def start(self):
        threading.Thread(target=self.create_window).start()
        threading.Thread(target=self.calculate_fps).start()



class Vector2:

    def __init__(self, posX: int, posY: int):
        """
         Initializes the position of the Vector2 object. This is called by __init__ and should not be called directly.
         
         Args:
         	 posX: Position of the Vector2 object in the x axis
         	 posY: Position of the Vector2 object in the y axis
        """

        self.posX = posX
        self.posY = posY

    def __call__(self):
        """
         Returns the x and y coordinates of the Vector2 object. This is useful for debugging the code that calls this method.
         
         
         Returns: 
         	 A tuple of ( x y ) coordinates of the Vector2 object
        """

        return (self.posX, self.posY)

    @staticmethod
    def new(posX: int=int, posY: int=int):
        """
         Create a new instance of : class : ` Vector2 `. This is useful for unit tests that don't need to know the type of vector being created.

         Args:
             posX: the posX position in the world
             posY: the posY position in the world
         
         Returns: 
         	 A new instance of : class : ` Vector2 `
        """

        return Vector2(posX, posY)



class DynamicBody:
    """
     Initializes the object with collision information. This is called by __init__ and should not be called directly
         
     Args:
     	 has_collision: Whether or not the object has collision.
     	 has_gravity: Whether or not the object has gravity.
    """

    def __init__(self, has_collision: bool, has_gravity: bool):
        """
         Initializes the object with collision information. This is called by __init__ and should not be called directly
         
         Args:
         	 has_collision: Whether or not the object has collision.
         	 has_gravity: Whether or not the object has gravity.
        """
        
        self.has_collision = has_collision
        self.has_gravity = has_gravity



class Pixel(object):
    """
     Initialize the object with the given parameters. This is the constructor for the class.
         
     Args:
     	 Texture: The unicode the texture will be.
     	 DynamicBody: The class that will be used to set the Pixel's DynamicBody.
    """
    
    def __init__(self, Texture: str, DynamicBody: type[DynamicBody]):
        """
         Initialize the object with the given parameters. This is the constructor for the class.
         
         Args:
         	 Texture: The unicode the texture will be.
         	 DynamicBody: The class that will be used to set the Pixel's DynamicBody.
        """
        
        self.Texture = Texture
        self.DynamicBody = DynamicBody
        self.World = None
        self.Vector2 = Vector2.new()

    def __eq__(self, other):
        if isinstance(other, Pixel):
            return self.Texture == other.Texture and \
                   self.DynamicBody == other.DynamicBody and \
                   self.Vector2 == other.Vector2
        return False
    
    def update_Vector2(self, vector2: type[Vector2]):
        if not isinstance(vector2, Vector2):
            raise ValueError("Must be a valid `Vector2()`")
        self.Vector2 = (vector2()[0], vector2()[1])

    def had_collision(self, direction: str=None):
        direction = direction.lower() if direction is not None else None
        
        if (direction == "above" and self.above().DynamicBody.has_collision) or \
           (direction == "below" and self.below().DynamicBody.has_collision) or \
           (direction == "left" and self.leftto().DynamicBody.has_collision) or \
           (direction == "right" and self.rightto().DynamicBody.has_collision) or \
           (direction is None and (self.above().DynamicBody.has_collision or \
                                   self.below().DynamicBody.has_collision or \
                                   self.leftto().DynamicBody.has_collision or \
                                   self.rightto().DynamicBody.has_collision)):
            return True
        else:
            return False

    def above(self):
        """
         Gives object above the pixel in the map
    
         Requires:
            World to have threaded ticking enabled.

         Returns:
            type[Pixel]: Pixel above this pixel on the World()
        """

        try:
            return self.World.world[self.Vector2[1]-1][self.Vector2[0]]
        except IndexError:
            return None
        
    def below(self):
        """
         Gives object below the pixel in the map
    
         Requires:
            World to have threaded ticking enabled.

         Returns:
            type[Pixel]: Pixel below this pixel on the World()
        """

        try:
            return self.World.world[self.Vector2[1]+1][self.Vector2[0]]
        except IndexError:
            return None

    def leftto(self):
        """
         Gives object left of the pixel in the map
    
         Requires:
            World to have threaded ticking enabled.

         Returns:
            type[Pixel]: Pixel left of this pixel on the World()
        """

        try:
            return self.World.world[self.Vector2[1]][self.Vector2[0]-1]
        except IndexError:
            return None
        
    def rightto(self):
        """
         Gives object right of the pixel in the map
    
         Requires:
            World to have threaded ticking enabled.

         Returns:
            type[Pixel]: Pixel right of this pixel on the World()
        """
        
        try:
            return self.World.world[self.Vector2[1]][self.Vector2[0]+1]
        except IndexError:
            return None

    def move(self, direction: str, amount: int) -> None:
        """
         Moves the pixel in the direction specified by the direction and amount. This is equivalent to a move in 2D space but with 1 pixel at the top left and 2 pixels at the bottom right
        
         Args:
             direction - The direction to move the pixel
             amount - The amount by which to move the pixel
        
         Returns:
             The pixel that was moved in the specified direction or
        """
        
        # Raise ValueError if direction and amount are None.
        if None in (direction, amount):
            raise ValueError(f"""{"'direction'" if direction is None else ""} {", " if direction and amount is None else ""} {"'amount'" if direction is None else ""}  Cannot be None""")
        
        # Raise an error if the Pixel is not inside a valid World.
        if self.World is None:
            raise ValueError("The Pixel() must be inside a valid World() to use this.")

        direction = direction.upper()

        x, y = self.Vector2[0], self.Vector2[1]

        try:
            
            if direction == "UP":
                self.World.world[y][x] = self.World.world_clone[y][x]
                self.World.world[y-amount][x] = self
            elif direction == "DOWN":
                self.World.world[y][x] = self.World.world_clone[y][x]
                self.World.world[y+amount][x] = self
            elif direction == "LEFT":
                if self.Vector2[0] != 0:
                    self.World.world[y][x] = self.World.world_clone[y][x]
                    self.World.world[y][x-amount] = self
            elif direction == "RIGHT":
                if self.Vector2[0] != len(self.World.world[self.Vector2[1]])-1:
                    self.World.world[y][x] = self.World.world_clone[y][x]
                    self.World.world[y][x+amount] = self
        except IndexError:
            pass



class Camera:

    def __init__(self, tracking, fov: int) -> None:
        self.tracking = tracking
        self.fov = fov

    def display(self):
        tracking_x = -1
        tracking_y = -1
        world_width = self.fov * 2 + 1
        world_height = self.fov * 2 + 1

        # Find the position of the tracking element
        for y, row in enumerate(self.tracking.World.world):
            for x, element in enumerate(row):
                if element == self.tracking:
                    tracking_y = y
                    tracking_x = x
                    break
            if tracking_y != -1:
                break

        if tracking_x == -1 or tracking_y == -1:
            print("Tracking element not found.")
            return

        for y in range(world_height):
            for x in range(world_width):
                if 0 <= tracking_y - self.fov + y < len(self.tracking.World.world) and 0 <= tracking_x - self.fov + x < len(self.tracking.World.world[0]):
                    pixel = self.tracking.World.world[tracking_y - self.fov + y][tracking_x - self.fov + x].Texture
                    print(pixel, end="")
                else:
                    pass
            print()


class SceneController:

    def __init__(self):
        """
         Initialize the scenes. This is called by __init__ and should not be called directly
        """

        self.scenes = []
        self.current_scene_index = 0

    def new_scene(self, func):
        """
         Decorator to add a scene to the scene list.
         
         Args:
         	 func: function that takes a context and returns a scene
         
         Returns: 
         	 a function that adds the scene to the scene list
        """
        
        def new_scene(*args, **kwargs):
            """ Add a new scene to the scenes list. """
            self.scenes.append(func)
        return new_scene()
    
    def load_scene(self, scene=None):
        if scene is None:
            raise Exception("No scene selection provided.")
        
        if scene == "++" and self.current_scene_index + 1 < len(self.scenes):
            self.current_scene_index += 1
            GraphicsEngine.clear()
            self.scenes[self.current_scene_index]()
            return

        try:
            scene = int(scene)
            if 0 <= scene < len(self.scenes):
                GraphicsEngine.clear()
                self.current_scene_index = scene
                self.scenes[scene]()
                return
            raise SceneException(scene, f"Scene index {scene} is out of range.")
        except ValueError:
            for index, scene_func in enumerate(self.scenes):
                if scene_func.__name__ == scene:
                    GraphicsEngine.clear()
                    self.current_scene_index = index
                    scene_func()
                    return
            raise SceneException(scene, f"Scene '{scene}' not found.")



class Engine:

    @property
    def title_bar(self):
        """
         Title bar for this terminal.
         
         
         Returns: 
         	 The title of the game.
        """
        
        return self.name
    
    @title_bar.setter
    def title_bar(self, value: str=None):
        """
         Set the title bar. If no value is given a default will be used.
         
         Args:
         	 value: value to set (str)
        """
        
        if value is None:
            self.name = f"QuartzEngine"
        else:
            self.name = value
    
    def __init__(self):
        """
         Initialize the QuartzEngine. This is called by __init__ and should not be called directly.
        """
        
        self.name = f"QuartzEngine"

    def on_run(self):
        """
         Called when the process is started. A function should override this method to perform actions that need to be carried out on the run.
        """
        
        pass

    def FPS(self, target_fps):
        frame_start_time = time.time()
        desired_frame_duration = 1.0 / target_fps
        elapsed_time = time.time() - frame_start_time
    
        if elapsed_time < desired_frame_duration:
            time.sleep(desired_frame_duration - elapsed_time)
        
        # Calculate the actual elapsed time for the frame
        elapsed_time = time.time() - frame_start_time
        
        return elapsed_time

    def run(self, *args):
        """
         Called when the program is run. Args : args : Arguments passed to on_run
        """

        if os.name == "nt":
            os.system(f"title {self.name} - QuartzEngine")
        elif os.name == "posix":
            os.system(f"""echo -n -e "\033]0;{self.name} - QuartzEngine\007" """)
        else:
            pass

        self.on_run(*args)