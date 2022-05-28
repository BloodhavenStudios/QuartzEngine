import sys
sys.path.append("..")

from quartzengine import engine
from quartzengine import display as quartz

red = quartz.Display.red
blue = quartz.Display.blue
reset = quartz.Display.reset

class TicTacToe(engine.Engine):

  def setup(self):
    self.scenes = [self.testscene, self.game]
    self.player1 = "❎"
    self.player2 = "🅾️"
    turn = engine.Switch(self.player1, self.player2)
    self.game_over = engine.Switch(True, False)

    self.board = [
      "⬜", "⬜", "⬜",
      "⬜", "⬜", "⬜",
      "⬜", "⬜", "⬜"
    ]
    
    self.conditions = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
    ]

  def testscene(self):
    print("before 15 secs")
    self.rest("15s")
    print("after 15 secs o.o")
  
  def game(self):

    quartz.Display.clear()

    print(self.getBoard())

    print(self.game_over.get())
    
    while not self.game_over.get():
      input(f"{self.turn.get()} its your move: ")
  
  def getBoard(self):
    char = 0
    output = ""
    for i in range(3):
      for i in range(3):
        output += str(self.board[char])
        char += 1
      output += "\n"
    return output

TicTacToe.title = "Tic-Tac-Toe"
TicTacToe().start()