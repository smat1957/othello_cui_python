from random import randint
from Board import Board
from Stone import Stone
from Strategy import Strategy

class Machine( Strategy ):
    def __init__(self, color=Stone.WHITE, strategy = 'random'):
        self.color = color
        self.strategy = strategy

    def Te(self, board):
        telist, komalist = board.puttable_list( self.color )
        if not telist:
            return Board.PASS
        if len(telist)==1:
            return telist[0]
        if self.strategy == 'random':
            n = randint( 0, len(telist)-1 )
            return telist[n]
        elif self.strategy == 'maxflip':
            n = v = -1
            for i, k in enumerate(komalist):
                if n < k[-1]:
                    n = k[-1]
                    v = telist[i]
            return v
        elif self.strategy == 'minimax':
            print('thinking ...')
            n = self.bestMove(board, telist)
            print('Your turn.')
            return n
        elif self.strategy == 'alphabeta':
            n = self.bestMoveAB(board, telist)
            return n

