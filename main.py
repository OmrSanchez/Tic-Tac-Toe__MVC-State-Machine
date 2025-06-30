from model import TicTacToe
# from cli_view import GameViewCLI
from gui_view import GameViewGUI
from controller import GameController
from guizero import App

def play_game():
    game = TicTacToe()
    controller = GameController(game)
    gui_board = GameViewGUI(controller_callback=controller.on_waffle_clicked)
    controller.view = gui_board

    gui_board.update_view(game)

    gui_board.start()

if __name__ == '__main__':
    play_game()

