from Quartz import *
from getkey import getkey, keys
import time

connect_blue = Pixel(Color.set_background(Color.fromRGB(255, 255, 0)) + "🔵" + Color.reset(), DynamicBody(True, True))
connect_red = Pixel(Color.set_background(Color.fromRGB(255, 255, 0)) + "🔴" + Color.reset(), DynamicBody(True, True))
b = Pixel(Color.set_background(Color.fromRGB(255, 255, 0)) + "ㅤ" + Color.reset(), DynamicBody(False, False))
i = Pixel("ㅤ", DynamicBody(True, False))

board = [
    [b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b],
    [b,b,b,b,b,b,b],
    [i,i,i,i,i,i,i],
]
world = World(board)

SceneManager = SceneController()
game = Engine()
fps_cap = game.FPS(5)

sel = 1
turn = connect_blue

def check_win(player):
    rows, cols = len(world.world), len(world.world[0])

    def get_line(x, y, dx, dy):
        if 0 <= x + 3*dx < rows and 0 <= y + 3*dy < cols:
            return [world.world[x + i*dx][y + i*dy] for i in range(4)]
        return []

    def consecutive_tiles(line):
        return any(all(cell == player for cell in line[i:i+4]) for i in range(len(line) - 3))

    return any(
        consecutive_tiles(get_line(x, y, dx, dy))
        for x in range(rows)
        for y in range(cols)
        for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1)]
    )

def alternate():
    global turn
    turn = connect_red if turn == connect_blue else connect_blue

def get_last_turn():
    return connect_red if turn == connect_blue else connect_blue

@SceneManager.new_scene
def connect4():
    global sel, turn

    won = False
    while not won:
        GraphicsEngine.clear()
        world.draw_world()

        min, max = 0, 8
        print("ㅤ" * int(sel-1) + "⬆️")

        key = getkey(False)

        if key in ["a", "A", keys.LEFT]:
            if int(sel - 1) != min:
                sel -= 1
        if key in ["d", "D", keys.RIGHT]:
            if int(sel + 1) != max:
                sel += 1
        elif key in [keys.SPACE, keys.ENTER]:
            piece = world.world[0][sel-1] = turn
            alternate()

        try:
            if piece.had_collision("below"):
                res = check_win(get_last_turn())
                if res == True:
                    won = True
                    input(f"{get_last_turn().Texture} WON!")
        except:
            pass

        time.sleep(fps_cap)

world.start_threaded_ticking(fps_cap)

game.on_run = lambda: SceneManager.load_scene(0)
game.run()