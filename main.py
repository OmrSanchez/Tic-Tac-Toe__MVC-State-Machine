import tkinter as tk
from model import TicTacToe
from view import GameView

# root = tk.Tk()
# root.title("TIC-TAC-TOE")
# w = tk.Label(root, text="Hello Tkinter!")
# w.pack()
#
# root.mainloop()

def play_game():
    game = TicTacToe()
    board = GameView()
    print("---Tic-Tac-Toe---")
    print(game.message)

    running = True
    while running:
        game.advance_state()
        board.draw(game)
        if not game.run:
            running = False



    print("Game Over")

play_game()

