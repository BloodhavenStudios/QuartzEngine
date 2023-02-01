from .errorHandler import *

import os
from sys import stdout
from time import sleep
from colorama import Fore
import string

__all__ = ["GraphicsEngine"]

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
            
class GraphicsEngine:

    def __init__(self):
        self.fg = Fore

    def clear(self):
        print(self.fg.RESET)
        clear()

    def write(self, string: str=None, delay=0.05):
        for char in string:
            stdout.write(char)
            stdout.flush()
            sleep(delay)
        print("")

    def ascii(self, text: str, font_size: int):
        length = len(text)
        fontsize = font_size
        while fontsize*length < (fontsize+1)*length:
            fontsize += 1
        for i in range(length):
            ASCII = string.ascii_uppercase[ord(text[i])-65] * (fontsize//length)
            print(''.join(ASCI))

    class FrameAnimator(object):

        def __init__(self, engine=None, animation=None):
            self.animation = animation
            self.engine = engine
  
        def process_errors(self):
            if self.engine is None:
                raise AnimationException(message="Engine is NoneType.")
            if self.animation is None:
                raise AnimationException(message="Animation is NoneType.")
            if not self.animation:
                raise AnimationException(message="Animation: {}, does not have any animatiable frames.".format(self.animation))

        def Render(self, delay_between_frames=1, loop=1):
            self.process_errors()
        
            for i in range(loop):
                for frame in self.animation:
                    clear()
                    print(f"{frame}")
                    sleep(delay_between_frames)
                clear()
