from guizero import Text, Waffle, App, Box, PushButton

FONT_COLOR = 'white'
DEBUG_COLOR = 'yellow'
GAME_INTERNALS_COLOR = 'red'

PLAYER_O_COLOR = 'blue'
PLAYER_X_COLOR = 'red'
BACKGROUND_COLOR = 'black'
class GameViewGUI:
    def __init__(self, controller_waffle, controller_start_button):
        self.window = App(title='Tic-Tac-Toe', bg=BACKGROUND_COLOR, width=500, height=450)

        self.empty_label = Text(self.window, text="", size=20)

        self.start_button_container = Box(self.window, layout='auto')
        self.start_button = PushButton(self.start_button_container, text='START', command=controller_start_button)
        self.start_button.bg = 'grey'
        self.start_button.text_size = 25
        self.start_button.text_color = 'white'

        self.board_container = Box(self.window, layout="grid", visible=False)
        self.widget = Waffle(self.board_container, height=3, width=3, pad=0, dim=100, grid=[0, 0], command=controller_waffle)

        self.game_message_text = Text(self.window, text="", size=16, color=FONT_COLOR)
        self.game_space_count = Text(self.window, text="", size=10, color=FONT_COLOR)

        self.game_context_text = Text(self.window, text="", size=10, color=FONT_COLOR)
        self.game_debug_text = Text(self.window, text="", size=10, color=DEBUG_COLOR)

    def update_view(self, model):
        self.game_message_text.value = model.message
        self.game_debug_text.value = model.debug
        self.game_context_text.value = model.context
        self.game_space_count.value = model.space_message

        for row in range(3):
            for col in range(3):
                if model.gameboard[row][col] == 'O':
                    self.widget.set_pixel(col, row, PLAYER_O_COLOR)
                elif model.gameboard[row][col] == 'X':
                    self.widget.set_pixel(col, row, PLAYER_X_COLOR)

    def start(self):
        self.window.display()

    def draw_board(self, model):
        self.game_message_text.value = model.message
        self.game_debug_text.value = model.debug
        self.start_button_container.visible = False
        self.board_container.visible = True

