from colorama import Fore
from sys import stdout
from time import sleep
import os
from .errorhandler import *
from typing import Union

from PIL import ImageFont
from fonts.ttf import (
  AmaticSC,
  Roboto,
  Caladea
)

class display(object):

  def __init__(self) -> None:
    self.fonts = {"AmaticSC": AmaticSC, "Roboto": Roboto, "Caladea": Caladea}
    
    self.colours = [self.red, self.yellow, self.green, self.blue, self.magenta, self.cyan, self.white, self.black,
                    self.lightred, self.lightyellow, self.lightgreen, self.lightblue, self.lightmagenta, self.lightcyan]

    self.red = self.red()
    self.yellow = self.yellow()
    self.green = self.green()
    self.blue = self.blue()
    self.magenta = self.magenta()
    self.cyan = self.cyan()
    self.white = self.white()
    self.black = self.black()

    self.lightred = self.lightred()
    self.lightyellow = self.lightyellow()
    self.lightgreen = self.lightgreen()
    self.lightblue = self.lightblue()
    self.lightmagenta = self.lightmagenta()
    self.lightcyan = self.lightcyan()
    self.lightblack = self.lightblack()
    
    self.reset = self.reset()

  def red(self):  return Fore.RED
  def yellow(self):  return Fore.YELLOW
  def green(self):  return Fore.GREEN
  def blue(self):  return Fore.BLUE
  def magenta(self):  return Fore.MAGENTA
  def cyan(self):  return Fore.CYAN
  def white(self):  return Fore.WHITE
  def black(self):  return Fore.BLACK

  def lightred(self):  return Fore.LIGHTRED_EX
  def lightyellow(self):  return Fore.LIGHTYELLOW_EX
  def lightgreen(self):  return Fore.LIGHTGREEN_EX
  def lightblue(self):  return Fore.LIGHTBLUE_EX
  def lightmagenta(self):  return Fore.LIGHTMAGENTA_EX
  def lightcyan(self):  return Fore.LIGHTCYAN_EX
  def lightblack(self):  return Fore.LIGHTBLACK_EX
    
  def reset(self):  return Fore.RESET

  def clear(self) -> None:
    if os.name == "nt":  os.system("cls")
    else:  os.system("clear")

  def set_font(self, font: str = None) -> None:

    if font == None:
      raise SetFontException(message="Failed to set font: None")
    if font not in self.fonts.keys():
      raise SetFontException(message="Font: {}, is not a valid font.".format(font))
    else:
      ImageFont.truetype(self.fonts[font])

  def write(self, string: str = None, delay: Union[int, float] = 0.05) -> None:
    for character in string:
      stdout.write(character)
      stdout.flush()
      sleep(delay)
    print("")
