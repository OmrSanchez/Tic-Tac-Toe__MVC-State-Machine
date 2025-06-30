from guizero import Text, Waffle, App, Box

FONT_COLOR = 'white'
DEBUG_COLOR = 'yellow'
GAME_INTERNALS_COLOR = 'red'

PLAYER_O_COLOR = 'blue'
PLAYER_X_COLOR = 'red'
BACKGROUND_COLOR = 'black'
class GameViewGUI:
    def __init__(self, controller_callback):
        self.window = App(title='Tic-Tac-Toe', bg=BACKGROUND_COLOR, width=430, height=400)

        self.board_container = Box(self.window, layout="grid")

        self.widget = Waffle(self.board_container, height=3, width=3, pad=0, dim=100, grid=[0, 0], command=controller_callback)
        self.message_text = Text(self.window, text="", size=16, color=FONT_COLOR, grid=[0,1])

    def update_view(self, model):
        self.message_text.value = model.message

        for row in range(3):
            for col in range(3):
                if model.gameboard[row][col] == 'O':
                    self.widget.set_pixel(col, row, PLAYER_O_COLOR)
                elif model.gameboard[row][col] == 'X':
                    self.widget.set_pixel(col, row, PLAYER_X_COLOR)

    def start(self):
        self.window.display()
