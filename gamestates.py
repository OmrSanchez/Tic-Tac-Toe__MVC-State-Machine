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
            self.game.context = "GAME CONTEXT: Winner decided."
            self.game.winner = winner
            self.game.message = f"Winner: Player {winner}"
            self.game.debug = f"STATE ACTION: Winner decided. Transitioning to GameOver"
            self.game.transition_to(GameOver(self.game))
        elif not winner:
            self.game.debug = "STATE ACTION: Checking Draw..."
            self.game.check_draw()

class GameOver(GameState):
    def handle_action(self):
        self.game.context = 'Tic-Tac-Toe...Game Over'