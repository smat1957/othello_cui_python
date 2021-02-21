from Board import Board
from Stone import Stone

class Strategy:
    INFINITY = 100000
    def __init__(self):
        pass

    # MiniMax
    def bestMove(self, board, telist):
        bestEval = -Strategy.INFINITY
        bestMove = -1
        for n, v in enumerate(telist):
            flist = board.put_stone(v, self.color)
            eval = self.minimax(board, 0, False)
            if bestEval<eval:
                bestEval = eval
                bestMove = v
            board.reset_stones(v, flist, self.color)
        return bestMove

    def minimax(self, board, depth, isMaximizingPlayer):
        def evaluate(depth):
            if board.state == Board.MACHINE_WIN:
                board.state = Board.GAME
                return board.NxN-depth     #return NxN
            elif board.state == Board.HUMAN_WIN:
                board.state = Board.GAME
                return depth-board.NxN     #return -NxN
            else:
                self.state = Board.GAME
                return 0

        board.winner()
        if board.state != Board.GAME:
            return evaluate(depth)

        color = Stone.MACHINE_ID if isMaximizingPlayer else Stone.HUMAN_ID
        telist, _ = board.puttable_list(color)
        bestVal = -Strategy.INFINITY if isMaximizingPlayer else +Strategy.INFINITY
        for n, v in enumerate(telist):
            flist = board.put_stone(v, color)
            value = self.minimax(board, depth + 1, not isMaximizingPlayer)
            bestVal = max(value, bestVal) if isMaximizingPlayer else min(value, bestVal)
            board.reset_stones(v, flist, color)
        return bestVal

    # Alpha-Beta
    def bestMoveAB(self, board, telist):
        bestEval = -Strategy.INFINITY
        bestMove = -1
        for n, v in enumerate(telist):
            flist = board.put_stone(v, self.color)
            eval = self.minimaxab(board, 8, 0, False, -Strategy.INFINITY, +Strategy.INFINITY)
            if bestEval<eval:
                bestEval = eval
                bestMove = v
            board.reset_stones(v, flist, self.color)
        return bestMove

    def minimaxab(self, board, node, depth, isMaximizingPlayer, alpha, beta):
        def evaluate(depth):
            if board.state == Board.MACHINE_WIN:
                board.state = Board.GAME
                return board.NxN-depth     #return NxN
            elif board.state == Board.HUMAN_WIN:
                board.state = Board.GAME
                return depth-board.NxN     #return -NxN
            else:
                self.state = Board.GAME
                return 0

        board.winner()
        if board.state != Board.GAME:
            return evaluate(depth)
        elif node==0:
            n = board.nBlack - board.nWhite
            return n if isMaximizingPlayer else -n

        color = Stone.MACHINE_ID if isMaximizingPlayer else Stone.HUMAN_ID
        telist, _ = board.puttable_list(color)
        bestVal = -Strategy.INFINITY if isMaximizingPlayer else +Strategy.INFINITY
        for n, v in enumerate(telist):
            flist = board.put_stone(v, color)
            value = self.minimaxab(board, node-1, depth+1, not isMaximizingPlayer, alpha, beta)
            board.reset_stones(v, flist, color)
            if isMaximizingPlayer:
                bestVal = max(value, bestVal)
                alpha = max(alpha, bestVal)
            else:
                bestVal = min(value, bestVal)
                beta = min(beta, bestVal)
            if beta<=alpha:
                break
        return bestVal
