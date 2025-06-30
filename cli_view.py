class GameViewCLI:
    def __init__(self):
        self.message = "Debug: GameViewCLI object created."

    def draw(self, model):
        for i in model.gameboard:
            print(i)



