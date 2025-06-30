from guizero import App, Text, PushButton, Drawing, Waffle

BACKGROUND_COLOR = 'black'
FONT_COLOR = 'white'
DEBUG_COLOR = 'yellow'

BUTTON_FONT = 'black'
BUTTON_BG_COLOR = 'white'
BUTTON_WIDTH = 35
BUTTON_HEIGHT = 10
BUTTON_TEXT_SIZE = 30

class GameViewGUI:
    def __init__(self):
        self.debug_message = "Debug: GameViewGUI object created."
        self.app_title = 'Tic-Tac-Toe'
        self.window = App(title=self.app_title, bg=BACKGROUND_COLOR, layout='grid', width=900, height=1000)
        self.debug_text = None
        self.game_message = None
        self.waffle = Waffle(self.window, height=3, pad=0, dim=300, grid=[0,0])
        self.input = None

    def draw(self, model):

        self.debug_text = Text(self.window, text=model.message, color=FONT_COLOR, bold=True, size=20, grid=[0,3])
        self.game_message = Text(self.window, text=model.debug, color=DEBUG_COLOR, size=8, grid=[0,4], align='bottom')











# self.button1 = PushButton(self.app, text='X', width=BUTTON_WIDTH, height=BUTTON_HEIGHT, grid=[0, 1])
        # self.button1.padding(10,10)
        # self.button1.text_color = BUTTON_FONT
        # self.button1.bg = BUTTON_BG_COLOR
        # self.button1.text_size = BUTTON_TEXT_SIZE
        # self.button1.resize(35,10)
        #
        # self.button4 = PushButton(self.app, text='4', width=BUTTON_WIDTH, height=BUTTON_HEIGHT, grid=[0, 2])
        # self.button4.text_color = BUTTON_FONT
        # self.button4.bg = BUTTON_BG_COLOR
        #
        # self.button7 = PushButton(self.app, text='7', width=BUTTON_WIDTH, height=BUTTON_HEIGHT, grid=[0, 3])
        # self.button7.text_color = BUTTON_FONT
        # self.button7.bg = BUTTON_BG_COLOR
        #
        # self.button2 = PushButton(self.app, text='2', width=BUTTON_WIDTH, height=BUTTON_HEIGHT, grid=[1, 1])
        # self.button2.text_color = BUTTON_FONT
        # self.button2.bg = BUTTON_BG_COLOR
        #
        # self.button5 = PushButton(self.app, text='5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT, grid=[1, 2])
        # self.button5.text_color = BUTTON_FONT
        # self.button5.bg = BUTTON_BG_COLOR
        #
        # self.button8 = PushButton(self.app, text='8', width=BUTTON_WIDTH, height=BUTTON_HEIGHT, grid=[1, 3])
        # self.button8.text_color = BUTTON_FONT
        # self.button8.bg = BUTTON_BG_COLOR
        #
        # self.button3 = PushButton(self.app, text='3', width=BUTTON_WIDTH, height=BUTTON_HEIGHT, grid=[2, 1])
        # self.button3.text_color = BUTTON_FONT
        # self.button3.bg = BUTTON_BG_COLOR
        #
        # self.button6 = PushButton(self.app, text='6', width=BUTTON_WIDTH, height=BUTTON_HEIGHT, grid=[2, 2])
        # self.button6.text_color = BUTTON_FONT
        # self.button6.bg = BUTTON_BG_COLOR
        #
        # self.button9 = PushButton(self.app, text='9', width=BUTTON_WIDTH, height=BUTTON_HEIGHT, grid=[2, 3])
        # self.button9.text_color = BUTTON_FONT
        # self.button9.bg = BUTTON_BG_COLOR
