from gamestates import GameState, PlayersTurn, GameOver
import random

PLAYER_SYMBOL_X = 'X'
PLAYER_SYMBOL_O = 'O'

class TicTacToe:
    def __init__(self):
        self.run = True
        self.player1 = PLAYER_SYMBOL_O
        self.player2 = PLAYER_SYMBOL_X
        self.current_player = None
        self.gameboard = [
           #(0,0)(0,1)(0,2)
            ['_', '_', '_'],
           #(1,0)(1,1)(1,2)
            ['_', '_', '_'],
           #(2,0)(2,1)(2,2)
            ['_', '_', '_']
        ]
        self.spaces = 9
        self.winner = None
        self.draw = None

        self.message = ''
        self.debug = ''
        self.context = ''
        self.space_message = ''

        self.board_space = 'empty'

        self.state: GameState = None

    def decide_first_to_start(self):
        players = [self.player1, self.player2]
        random.shuffle(players)
        self.current_player =  players[0]

    def transition_to(self, new_state: GameState):
        self.state = new_state
        self.debug = f"DEBUG: Transitioned to '{self.state.__class__.__name__}'"

    def start_new_game(self):
        self.decide_first_to_start()
        self.context = "GAME CONTEXT: Game Start"
        self.transition_to(PlayersTurn(self))

    def advance_state(self):
            self.state.handle_action()

    def make_move(self, x, y):
        if self.gameboard[x][y] == '_':
            self.gameboard[x][y] = self.current_player
            self.spaces -= 1
            self.space_message = f"{self.spaces} spaces available."
            return True
        else:
            self.context = 'GAME CONTEXT: Slot taken. Choose another.'
            return False

    def turn_change(self):
        # self.message = f"Its {self.current_player}'s turn."
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
        self.message = f"Its {self.current_player}'s turn."

    def check_winner(self):
         # Horizontal wins
        self.context = 'GAME CONTEXT: Checking for winner...'
        for row in range(3):
            if self.gameboard[row][0] == self.gameboard[row][1] == self.gameboard[row][2] and self.gameboard[row][0] != '_':
                return self.gameboard[row][0]
        # Vertical wins
        for col in range(3):
            if self.gameboard[0][col] == self.gameboard[1][col] == self.gameboard[2][col] and self.gameboard[0][col] != '_':
                return self.gameboard[0][col]

        #Diagonal wins
        if self.gameboard[0][0] == self.gameboard[1][1] == self.gameboard[2][2] and self.gameboard[0][0] != '_':
            return self.gameboard[0][0]

        if self.gameboard[0][2] == self.gameboard[1][1] == self.gameboard[2][0] and self.gameboard[0][2] != '_':
            return self.gameboard[0][2]
        return None

    def check_draw(self):
        self.context = "GAME CONTEXT: Checking for draw"
        if self.spaces == 0:
            self.context = "GAME CONTEXT: Board is full..."
            self.board_space = 'full'
        if self.winner is None and self.board_space == 'full':
            self.message = "DRAW..."
            self.transition_to(GameOver(self))

    def reset(self):
        self.run = True
        self.player1 = PLAYER_SYMBOL_O
        self.player2 = PLAYER_SYMBOL_X
        self.current_player = None
        self.gameboard = [
            # (0,0)(0,1)(0,2)
            ['_', '_', '_'],
            # (1,0)(1,1)(1,2)
            ['_', '_', '_'],
            # (2,0)(2,1)(2,2)
            ['_', '_', '_']
        ]
        self.winner = None
        self.message = ''
        self.board_space = 'empty'
        self.state: GameState = None

        self.start_new_game()