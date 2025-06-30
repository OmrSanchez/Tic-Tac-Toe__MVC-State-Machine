import guizero

class GameController:
    def __init__(self, model):
        self.model = model

    def handle_input(self, widget):
        widget.when_mouse_enters

        self.model.advance_state()
