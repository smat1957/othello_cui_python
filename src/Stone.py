class Stone():
    EMPTY = 0
    BLACK = 1
    WHITE = 3 - BLACK
    MACHINE_ID = WHITE
    HUMAN_ID = BLACK
    def __init__(self, te, color):
        self.color = color
        self.locate = te

    def getLocate(self):
        return self.locate

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def flipColor(self):
        self.color = 3 - self.color

    def getFigure(self):
        if self.color==Stone.BLACK:
            return 'X'
        elif  self.color==Stone.WHITE:
            return 'O'
        return '.'

