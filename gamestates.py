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
        winner = self.game.check_winner()
        if winner:
            self.game.winner = winner
            print(f"STATE ACTION: Transitioning to GameOver")
            self.game.transition_to(GameOver(self.game))
        elif not winner:
            self.game.check_draw()
            if self.game.board_state == 'full':
                print(f"No winner. This is a DRAW")
                self.game.transition_to(GameOver(self.game))

class GameOver(GameState):
    def handle_action(self):
        if self.game.winner == 'winner':
            self.game.message = "Thank you for playing my game."
        # if again == 'yes':
        #     print('STATE ACTION: Resetting game..')
        #     self.game.reset()
        # else:
        #     print('STATE ACTION: Ending Game..')
        #     self.game.run = False



