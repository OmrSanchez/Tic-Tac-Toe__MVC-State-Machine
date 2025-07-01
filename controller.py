class GameController:
    def __init__(self, model):
        self.model = model
        self.view = None

    def on_start_clicked(self):
        self.model.start_new_game()
        self.model.message = f"Its {self.model.current_player}'s turn."
        self.model.advance_state()
        self.view.draw_board(self.model)

    def on_waffle_clicked(self, x, y):
        if not self.model.winner and not self.model.board_space == 'full':
            self.model.make_move(y, x)
            self.view.update_view(self.model)
            self.model.turn_change()
            self.model.advance_state()
            self.view.update_view(self.model)
