#! /usr/bin/python3
from numpy import *
import math
from err import *


class board:
    def __init__(self, M, N, K, symbols):
        """
        Initilize a board of size m (rows) x n (columns), with k players playing in turn.
        Players use the symbols specified.
        """
        self.row = N
        self.col = M
        self.max_address = (M * N)
        self.num_players = K
        self.players = list(range(0, (K+1)))
        self.sym = [' ']+symbols
        self.reset()

    def reset(self):
        row = [0] * self.row
        self.board = zeros((self.col, self.row), 'int')
        self.free_positions = self.col * self.row

    def get_xy_from_pos(self, pos):
        x = int(math.floor(pos / self.row))
        y = pos % self.col
        return x, y

    def set_pos(self, pos, player):
        if(pos < self.max_address):
            # x = int (math.floor( pos / self.row ))
            # y = pos % self.col
            x, y = self.get_xy_from_pos(pos)
            if(self.board[x][y] == 0):
                self.board[x][y] = player
                returnVal = err.OK
                self.free_positions -= 1
            else:
                returnVal = err.INVALID_MOVE
            # dbg(1,"X:" + str(x) + "  Y:" +str(y)+" R:"+str(returnVal))
        else:
            returnVal = err.INVALID_MOVE
        return returnVal

    def get_board_str(self):
        board_string = '\n'
        for j, rows in enumerate(self.board):
            for i, e in enumerate(rows):
                board_string += ' ' + self.sym[e] + ' '
                if i < len(rows)-1:
                    board_string += '|'
            if(j < len(self.board)-1):
                board_string += '\n---+---+---\n'
        board_string += '\n'
        return board_string

    def count_empty_squares(self):
        self.free_positions = sum(sum(self.board == 0))
        return None


def dbg(level, message):
    if (level == 1):
        print(message)


def test():
    b = board(3, 3, 2, ['X', 'O'])
    b.set_pos(0, 1)
    b.set_pos(0, 1)

if __name__ == '__main__':
    test()
