from model import TicTacToe
from cli_view import GameViewCLI
from gui_view import GameViewGUI
from controller import GameController
from guizero import App

def play_game():
    game = TicTacToe()
    cli_board = GameViewCLI()
    gui_board = GameViewGUI()
    controller = GameController()
    print("---Tic-Tac-Toe---")
    print(game.message)

    while True:
        controller.handle_input(gui_board.waffle)
        gui_board.draw(game)
        gui_board.window.display()

play_game()

