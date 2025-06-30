class GameView:
    def __init__(self):
        self.message = "Debug: GameView object created."

    def draw(self, model):
        for i in model.gameboard:
            print(i)



