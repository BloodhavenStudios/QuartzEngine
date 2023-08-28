from typing import Optional

import os
from sys import stdout
from time import sleep
import subprocess
import platform

from .error_handler import *

__all__: tuple[str, ...] = (
    "GraphicsEngine",
    "Color"
)

class GraphicsEngine:

    @staticmethod
    def clear():
        command = 'cls' if platform.system() == 'Windows' else 'clear'
        subprocess.call(command, shell=True)

    @staticmethod
    def type(string: type[str]=None, delay: type[int, float]=0.05):
        if string is None:
            raise ValueError("String Not Provided.")
        
        for char in string:
            stdout.write(char)
            stdout.flush()
            sleep(delay)
        print("")
    
class Color:
    """ The color class used for modifying the color of strings.
    
    Some colors:
        - red:       .fromRGB(255, 0, 0)
        - orange:    .fromRGB(255, 165, 0)
        - yellow:    .fromRGB(255, 255, 0)
        - green:     .fromRGB(0, 128, 0)
        - blue:      .fromRGB(0, 0, 255)
        - indigo:    .fromRGB(75, 0, 135)
        - violet:    .fromRGB(238, 130, 238)
        - cyan:      .fromRGB(0, 255, 255)
        - magenta:   .fromRGB(255, 0, 255)
    """

    class RGB:

        def __init__(self, r: int, g: int, b: int) -> 255:
            """
            Initializes the position of the Vector2 object. This is called by __init__ and should not be called directly.
            
            Args:
                r: The Red RGB Point
                g: The Green RGB Point
                b: The Blue RGB Point
            """

            if r > 255 or g > 255 or b > 255:
                raise ColorException("Invalid RGB values. Values must be between 0 and 255 inclusive.")

            self.r = r
            self.g = g
            self.b = b

        def __call__(self):
            """
            Returns the r, g and b points of the RGB object. This is useful for debugging the code that calls this method.
            
            
            Returns: 
                A tuple of ( r g b ) RGB Points of the RGB object
            """

            return (self.r, self.g, self.b)

        @staticmethod
        def new(r: int, g: int, b: int) -> 255:
            """
            Create a new instance of : class : ` RGB `.

            Args:
                r: The Red RGB Point
                g: The Green RGB Point
                b: The Blue RGB Point
            
            Returns: 
                A new instance of : class : ` RGB `
            """

            if r > 255 or g > 255 or b > 255:
                raise ColorException("Invalid RGB values. Values must be between 0 and 255 inclusive.")
            
            return Color.RGB(r, g, b)

    @staticmethod
    def set_foreground(rgb: type[RGB]):
        """
         Set the foreground color. This is a function that takes a tuple of RGB values and returns a string that can be used in a SETTHEGREET command
         
         Args:
         	 RGB: tuple of RGB values in the format ( r g b )
         
         Returns: 
         	 string of ANSI escape codes that can be used in a string
        """
        
        if isinstance(rgb, Color.RGB):
            return f"\033[38;2;{rgb()[0]};{rgb()[1]};{rgb()[2]}m"
        else:
            raise ColorException("Invalid RGB value. Expected a tuple of RGB values.")

    @staticmethod
    def set_background(rgb: type[RGB]):
        """
         Set the background color. This is a function that takes a tuple of RGB values and returns a string that can be used in a SET command
         
         Args:
         	 RGB: tuple of RGB values in the format ( r g b )
              
         Returns: 
         	 string of ANSI escape codes that can be used in a string
        """
        
        if isinstance(rgb, Color.RGB):
            return f"\033[48;2;{rgb()[0]};{rgb()[1]};{rgb()[2]}m"
        else:
            raise ColorException("Invalid RGB value. Expected a tuple of RGB values.")

    @staticmethod
    def fg(rgb: type[RGB]):
        Color.set_foreground(rgb)

    @staticmethod
    def bg(rgb: type[RGB]):
        Color.set_background(rgb)

    @staticmethod
    def reset():
        """
         Reset the screen to its initial state. This is useful for debugging and to make sure the screen doesn't hang indefinitely.
         
         
         Returns: 
         	 a string containing a ANSI escape code to reset the colors
        """
        
        return "\033[0m"

    @staticmethod
    def rainbowify(string: type[str]=None):
        """
         Converts a string to Rainbow text.
         
         Args:
         	 string: The string to convert. Must be a string of length 3.
         
         Returns: 
         	 A string with rainbow colors in the format.
        """

        if string is None:
            raise ColorException("Invalid input. Expected a non-empty string.")

        string_to_return = ""
        colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (238, 130, 238)]

        for i, character in enumerate(string):
            color = colors[i % len(colors)]
            string_to_return += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{character}"
        
        string_to_return += "\033[0m"
        return string_to_return

    @staticmethod
    def fromRGB(r: int, g: int, b: int) -> tuple[255, 255, 255]:
        """
         Convert RGB to string. This is a convenience function for color conversion. It will raise ColorException if r g or b are out of range.
            
         Args:
             r: Red component 0 - 255. Must be between 0 and 255 inclusive.
             g: Green component 0 - 255. Must be between 0 and 255 inclusive.
             b: Blue component 0 - 255. Must be between 0 and 255 inclusive.
             
         Returns: 
             Color string in R G B format e. g
        """

        if r > 255 or g > 255 or b > 255:
            raise ColorException("Invalid RGB values. Values must be between 0 and 255 inclusive.")
        else:
            return Color.RGB.new(r,g,b)

    @staticmethod
    def fromHEX(hex_code: str="#FFFFFF"):
        """
         Convert a hexadecimal color code to RGB. This is useful for color conversion from hex values such as #FFFFFF to a 3 - tuple of integers ( r g b )
             
         Args:
             hex_code: The hexadecimal color code to convert
             
         Returns: 
             A 3 - tuple of RGB values or an exception if the color code is
        """

        # Remove the "#" symbol if present
        hex_code = hex_code.lstrip("#")
        
        if len(hex_code) != 6:
            raise ColorException("Invalid hexadecimal color code. Expected format: #RRGGBB")

        try:
            r = int(hex_code[0:2], 16)
            g = int(hex_code[2:4], 16)
            b = int(hex_code[4:6], 16)
            return Color.RGB.new(r, g, b)
        except ValueError:
            raise ColorException("Invalid hexadecimal color code. Expected format: #RRGGBB")