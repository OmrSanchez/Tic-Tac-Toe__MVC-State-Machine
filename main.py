from model import TicTacToe
# from cli_view import GameViewCLI
from gui_view import GameViewGUI
from controller import GameController

def play_game():
    game = TicTacToe()
    controller = GameController(game)
    gui_board = GameViewGUI(controller_waffle=controller.on_waffle_clicked, controller_start_button=controller.on_start_clicked)
    controller.view = gui_board

    gui_board.start()

if __name__ == '__main__':
    play_game()