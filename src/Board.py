from random import randint
from Stone import Stone

class Board:
    PASS = -10
    GAME =  -1
    DRAW =   0
    HUMAN_WIN = BLACK_WIN = Stone.BLACK * 100
    MACHINE_WIN = WHITE_WIN = Stone.WHITE * 100
    UNITV = ((0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1))

    def __init__(self, NW=4):
        self.nKoma = [0 for _ in range(9)]
        self.NW = NW
        self.NxN = NW * NW
        self.stones = [ Stone(i, Stone.EMPTY) for i in range(self.NxN) ]
        m = NW//2
        n = m - 1
        self.stones[NW*n+n].setColor( Stone.WHITE )
        self.stones[NW*n+m].setColor( Stone.BLACK )
        self.stones[NW*m+n].setColor( Stone.BLACK )
        self.stones[NW*m+m].setColor( Stone.WHITE )
        nrnd = randint(0,1)
        if nrnd==0:
            self.stones[NW * n + n].flipColor()
            self.stones[NW * n + m].flipColor()
            self.stones[NW * m + n].flipColor()
            self.stones[NW * m + m].flipColor()
        self.nBlack = self.nWhite = 2
        self.nEmpty = self.NxN - (self.nBlack + self.nWhite)
        self.state = Board.GAME

    def winner(self):
        self.nBlack = self.nWhite = self.nEmpty = 0
        for i in range(self.NxN):
            if self.stones[i].getColor() == Stone.HUMAN_ID:
                self.nBlack += 1
            elif self.stones[i].getColor() == Stone.MACHINE_ID:
                self.nWhite += 1
            else:
                self.nEmpty += 1
        if self.nBlack+self.nWhite == self.NxN:
            if self.nBlack < self.nWhite:
                return Board.MACHINE_WIN
            elif self.nBlack > self.nWhite:
                return Board.HUMAN_WIN
            else:
                return Board.DRAW
        return Board.GAME

    def print(self):
        print(f"WHITE:{self.nWhite}, BLACK:{self.nBlack}")
        print(' ',end=' ')
        for x in range(self.NW):
            print(f"{x}", end=' ')
        print("→x")
        for y in range(self.NW):
            print(f"{y:}", end=' ')
            for x in range(self.NW):
                print(f"{self.stones[ y*self.NW+x ].getFigure()}", end=' ')
            print()
        print("↓\ny")

    def check_flip(self, stone):
        y = stone.getLocate()//self.NW
        x = stone.getLocate()%self.NW
        self.nKoma[8] = 0
        if self.stones[y*self.NW+x].getColor() == Stone.EMPTY:
            for i1 in range( len(self.nKoma)-1 ):   # 0,1,2,3,4,5,6,7
                m1, m2 = x, y
                self.nKoma[i1] = s = ct = 0
                while s<2:
                    m1 += Board.UNITV[i1][0]
                    m2 += Board.UNITV[i1][1]
                    if (0<=m1<self.NW) and (0<=m2<self.NW):
                        color = self.stones[m2*self.NW+m1].getColor()
                        if color==Stone.EMPTY:
                            s = 3
                        elif color==stone.getColor():
                            s=2 if s==1 else 3
                        else:
                            s=1
                            ct += 1
                    else:
                        s=3
                if s==2:
                    self.nKoma[8] += ct
                    self.nKoma[i1] = ct
        return self.nKoma[8]

    def flip_list(self, stone):
        self.check_flip(stone)
        y = stone.getLocate()//self.NW
        x = stone.getLocate()%self.NW
        flipped = []
        for i1 in range( len(self.nKoma)-1 ):   # 0,1,2,3,4,5,6,7
            m1, m2 = x, y
            for i2 in range( self.nKoma[i1] ):
                m1 += Board.UNITV[i1][0]
                m2 += Board.UNITV[i1][1]
                if (0 <= m1 < self.NW) and (0 <= m2 < self.NW):
                    z = m2*self.NW+m1
                    self.stones[z].setColor( stone.getColor() )
                    flipped.append( z )
        z = y*self.NW+x
        self.stones[z].setColor( stone.getColor() )
        flipped.append(z)
        return flipped

    def empty_list(self):
        list = [v for v in range(self.NxN) if self.is_empty(v)]
        return list

    def is_empty(self, te):
        return True if self.stones[te].getColor()==Stone.EMPTY else False

    def can_put(self, te, color):
        if 0<=te<self.NxN:
            if 0<self.check_flip( Stone(te, color) ):
                return True
        return False

    def puttable(self, te, color):
        if self.can_put(te, color):
            return self.nKoma

    def puttable_list(self, color):
        emptyl = self.empty_list()
        komal = []
        telist = []
        for n in emptyl:
            w = self.puttable(n, color)
            if w:
                telist.append(n)
                komal.append(w)
        return telist, komal

    def put_stone(self, te, color):
        stone = Stone(te, color)
        flist = self.flip_list( stone )
        self.set_stones(flist, color)
        self.stones[te] = stone
        if color==Stone.BLACK:
            self.nBlack = len(flist) + 1
        else:
            self.nWhite = len(flist) + 1
        return flist

    def set_stones(self, flist, color):
        for z in flist:
            self.stones[z] = Stone(z, color)
        self.stones[z] = Stone(z, Stone.EMPTY)

    def reset_stones(self, te, flist, color):
        if color==Stone.WHITE:
            c = Stone.BLACK
        elif color==Stone.BLACK:
            c = Stone.WHITE
        self.stones[te] = Stone(te,c)
        for z in flist:
            self.stones[z] = Stone(z, c)
        self.stones[z] = Stone(z, Stone.EMPTY)

    def debug_print(self):
        for y in range(self.NW):
            for x in range(self.NW):
                n = y*self.NW + x
                print(self.stones[n].color, end=' ')
            print()
        print('\n')

