from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model import TicTacToe

class GameState(ABC):
    def __init__(self, game: TicTacToe):
        self.game = game

    @abstractmethod
    def handle_action(self):
        pass

class PlayersTurn(GameState):
    def handle_action(self):
        print("STATE ACTION: Playing a round...")
        print(f"Its {self.game.current_player}'s turn.")
        self.game.message = f"Its {self.game.current_player}'s turn."
        row = int(input('Select row: '))
        col = int(input('Select col: '))

        move_successful = self.game.make_move(row,col)
        if move_successful:
            print("STATE ACTION: Transitioning to TurnChange")
            self.game.transition_to(TurnChange(self.game))

class TurnChange(GameState):
    def handle_action(self):

        winner = self.game.check_winner()
        if winner:
            self.game.winner = winner
            print(f"STATE ACTION: Transitioning to GameOver")
            self.game.transition_to(GameOver(self.game))
            return
        elif not winner:
            self.game.check_draw()
            if self.game.board_state == 'full':
                print(f"No winner. This is a DRAW.")
                self.game.transition_to(GameOver(self.game))
                return

        print("STATE ACTION: Changing Turns...")
        if self.game.current_player == self.game.player1:
            self.game.current_player = self.game.player2
        else:
            self.game.current_player = self.game.player1
        self.game.transition_to(PlayersTurn(self.game))

class GameOver(GameState):
    def handle_action(self):
        print("Thank you for playing my game.")
        again = input('Would you like to play again?')
        if again == 'yes':
            print('STATE ACTION: Resetting game..')
            self.game.reset()
        else:
            print('STATE ACTION: Ending Game..')
            self.game.run = False



