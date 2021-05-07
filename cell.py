
class Cell:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.type = 0

        self.neighbors: [Cell] = []

    def p(self):
        pass