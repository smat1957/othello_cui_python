from Game import Game

if __name__ == '__main__':
    sente = 'human'         # 'human, 'machine'
    senryaku = 'random'    # 'random', 'maxflip', 'minimax', 'alphabeta'
    game = Game( N=6, turn=sente, strategy=senryaku )      # board size -> N x N
    game.start()
