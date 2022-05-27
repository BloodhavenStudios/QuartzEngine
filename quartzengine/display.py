from colorama import Fore
from sys import stdout
from time import sleep
import os

__all__ = ("display", "Display")

class display(object):

  def __init__(self):
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

  def clear(self):
    if os.name == "nt":  os.system("cls")
    else:  os.system("clear")

  def write(self, string, delay=0.05):
    for character in string:
      stdout.write(character)
      stdout.flush()
      sleep(delay)
    print("")

Display = display()