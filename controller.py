class GameController:
    def __init__(self, model):
        self.model = model
        self.view = None

    def on_waffle_clicked(self, x, y):
        if not self.model.winner:
            # self.controller_debug_message.value = f"Player {self.model.current_player} selected ({x},{y})"
            self.model.make_move(y, x)
            for row in range(3):
                print(self.model.gameboard[row])

            if self.model.current_player == self.model.player1:
                self.model.current_player = self.model.player2
            else:
                self.model.current_player = self.model.player1
        self.model.advance_state()











