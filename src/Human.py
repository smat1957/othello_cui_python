from Board import Board
from Stone import Stone

class Human:
    def __init__(self, color=Stone.BLACK):
        self.color = color

    def Te(self, board):
        def puttable():
            elist =  board.empty_list()
            for v in elist:
                if board.can_put(v, self.color):
                    return True
            return False

        while True:
            instr = input('Your turn. [yx] or "pass": ')
            if 'pass' in instr:
                if puttable():
                    continue
                return Board.PASS
            if 1<len(instr) and self.numP( instr[0] ) and self.numP( instr[1] ):
                cy = self.serial_num( instr[0] )
                cx = self.serial_num( instr[1] )
                slot = cy * board.NW + cx
                if board.can_put(slot, self.color):
                    break
        print()
        return slot

    def numP(self, xy):
        if '0' <= xy <= '9':
            return True
        return False

    def serial_num(self, xy):
        def fromA(xy):
            return int(xy - 'a')

        if self.numP(xy):
            nxy = int( xy )
        else:
            nxy = fromA(xy)+10
        return nxy

