from sys import stdout

class Map(object):

  def __init__(self):

    self.map = [
      "#"
    ]

    self.char_map = {"wall": "#",
                     "navigatable": " ",
                     "misc_objects": ["🧰"]}
    self.spawn = 0
    self.width = 1
    self.height = 1

  def display_map(self):
    print("")
    current_key = 0
    for i in range(self.height):
      for i in range(self.width):
        stdout.flush
        stdout.write(self.map[current_key])
        current_key += 1
      print("")