from gamestates import GameState, PlayersTurn, TurnChange
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
        self.winner = None
        self.message = ''
        self.debug = ''
        self.board_state = 'empty'

        self.state: GameState = None
        self.start_new_game()

    def decide_first_to_start(self):
        players = [self.player1, self.player2]
        random.shuffle(players)
        self.current_player =  players[0]

    def transition_to(self, new_state: GameState):
        self.state = new_state
        self.debug = f"GAME CONTEXT: Transitioned to '{self.state.__class__.__name__}'"
        print(f"GAME CONTEXT: Transitioned to '{self.state.__class__.__name__}'")

    def start_new_game(self):
        self.decide_first_to_start()
        self.message = f"Starting the game..."
        self.message = f"{self.current_player} goes first."
        self.transition_to(PlayersTurn(self))

    def advance_state(self):
        self.state.handle_action()

    def make_move(self, row, col):
        if self.gameboard[row][col] == '_':
            self.gameboard[row][col] = self.current_player
            return True
        else:
            print('Slot taken. Choose another.')
            return False

    def check_winner(self):
             # Horizontal wins
            print("GAME CONTEXT: Checking for winner...")
            for row in range(3):
                if self.gameboard[row][0] == self.gameboard[row][1] == self.gameboard[row][2] and self.gameboard[row][0] != '_':
                    print(f"Winner: Player {self.current_player}")
                    return self.gameboard[row][0]

            # Vertical wins
            for col in range(3):
                if self.gameboard[0][col] == self.gameboard[1][col] == self.gameboard[2][col] and self.gameboard[0][col] != '_':
                    print(f"Winner: Player {self.current_player}")
                    return self.gameboard[0][col]

            #Diagonal wins
            if self.gameboard[0][0] == self.gameboard[1][1] == self.gameboard[2][2] and self.gameboard[0][0] != '_':
                print(f"Winner: Player {self.current_player}")
                return self.gameboard[0][0]

            if self.gameboard[0][2] == self.gameboard[1][1] == self.gameboard[2][0] and self.gameboard[0][2] != '_':
                print(f"Winner: Player {self.current_player}")
                return self.gameboard[0][2]

            print("No winner... Continue.")
            return None

    def check_draw(self):
        full = 0
        count = 9
        for item in self.gameboard:
            for key in item:
                if key != '_':
                    count -= 1

        print(f"Available Tiles: {count}")
        if count == full:
            print('GAME CONTEXT: Board is full...')
            self.board_state = 'full'
            return self.board_state
        else:
            return None

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
        self.board_state = 'empty'
        self.state: GameState = None
        print('Game is now reset. Have Fun!')
        self.start_new_game()

















