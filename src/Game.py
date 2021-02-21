from Board import Board
from Human import Human
from Machine import Machine
from Stone import Stone

class Game():
    def __init__(self, N=4, turn='human', strategy='random'):
        self.board = Board(NW=N)
        human = Human(color=Stone.BLACK)
        machine = Machine(color=Stone.WHITE, strategy=strategy)
        self.player = [human, machine]
        self.turn = 0
        if turn=='machine':
            self.turn = 1

    def start(self):
        turn = self.turn
        winner = Board.GAME
        while winner==Board.GAME:
            self.board.print()                    # ①

            te = self.player[turn].Te(self.board) # ②
            if te!=Board.PASS:                    # ③
                color = self.player[turn].color
                self.board.put_stone(te,color)    # ④

            turn = (turn+1)%2                     # ⑤
            winner = self.board.winner()          # ⑥

        self.board.print()
        print()
        if winner==Board.BLACK_WIN:
            print('Winner : BLACK')
        elif winner==Board.WHITE_WIN:
            print('Winner : WHITE')
        elif winner==Board.DRAW:
            print('DRAW')
