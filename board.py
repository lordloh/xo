#! /usr/bin/python3
from numpy import *
import math
from err import *


class board:
    def __init__(o, M, N, K, symbols):
        """
        Initilize a board of size m (rows) x n (columns), with k players playing in turn.
        Players use the symbols specified.
        """
        o.row = N
        o.col = M
        o.max_address = (M * N)
        o.num_players = K
        o.players = list(range(0, (K+1)))
        o.sym = [' ']+symbols
        o.reset()

    def reset(o):
        row = [0] * o.row
        o.board = zeros((o.col, o.row), 'int')
        o.free_positions = o.col * o.row

    def get_xy_from_pos(o, pos):
        x = int(math.floor(pos / o.row))
        y = pos % o.col
        return x, y

    def set_pos(o, pos, player):
        if(pos < o.max_address):
            # x = int (math.floor( pos / o.row ))
            # y = pos % o.col
            x, y = o.get_xy_from_pos(pos)
            if(o.board[x][y] == 0):
                o.board[x][y] = player
                returnVal = err.OK
                o.free_positions -= 1
            else:
                returnVal = err.INVALID_MOVE
            # dbg(1,"X:" + str(x) + "  Y:" +str(y)+" R:"+str(returnVal))
        else:
            returnVal = err.INVALID_MOVE
        return returnVal

    def get_board_str(o):
        board_string = '\n'
        for j, rows in enumerate(o.board):
            for i, e in enumerate(rows):
                board_string += ' ' + o.sym[e] + ' '
                if i < len(rows)-1:
                    board_string += '|'
            if(j < len(o.board)-1):
                board_string += '\n---+---+---\n'
        board_string += '\n'
        return board_string

    def count_empty_squares(o):
        o.free_positions = sum(sum(o.board == 0))
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
