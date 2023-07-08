from typing import Optional

from sys import stdout
from time import sleep
from threading import Thread
import copy
from multiprocessing import Pool

from .error_handler import *

__all__: tuple[str, ...] = (
    "Map",
)

class World(object):

    def __init__(self, array: list=None):
        """
         Initialize the world. This is called by __init__ and should not be called directly.
         
         Args:
         	 array: The array to use for the world. If None a error will be returned
        """
        
        if array is None:
            raise ValueError("No array provided")

        self.test = "yes"
        self.world_clone = copy.deepcopy(array)
        self.world = copy.deepcopy(array)

    def tick(self):
        # Go through the array backwards
        for y in reversed(range(len(self.world))):
            for x in range(len(self.world[y])):
                current_pixel = self.world[y][x]
                current_pixel.World = self
                current_pixel.update_Vector2(x, y)

                # Check if the current pixel has DynamicBody.has_gravity is True
                if current_pixel.DynamicBody.has_gravity:
                    # Check if there is an element below the current one
                    if y < len(self.world) - 1:
                        below_pixel = self.world[y+1][x]

                        if current_pixel.DynamicBody.has_collision and below_pixel.DynamicBody.has_collision:
                            pass
                        else:
                            self.world[y][x] = self.world_clone[y][x]
                            self.world[y+1][x] = current_pixel
                            current_pixel.update_Vector2(x, y+1)

    def tick_process(self, fps: int):
        while True:
            self.tick()
            sleep(fps)
            
    def start_threaded_ticking(self, fps: int):
        """
        fps arg is basically for a shitty VSYNC
        (Frames and Refresh rate same)
        (keep frames and world aligned so it doesnt look laggy)
        """
        Thread(target=self.tick_process, daemon=True, args=(fps,)).start()
    
    def draw_world(self):
        """
        Draws the world.
        """
        
        output = "\n".join("\033[0m" + "".join(tile.Texture for tile in line) for line in self.world)
        stdout.write(output + "\n")
        stdout.flush()
    