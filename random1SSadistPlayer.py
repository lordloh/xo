#! /usr/bin/python3

from random import randint
from err import err

from copy import *
from numpy import *


class random1SSadistPlayer:
    """
    The random player with 1 step look ahead finds a list of valid moves, and
    chooses one among it such that it can win the next move, or prevent an
    adversary from winning in the next move.

    Essentially this is a 1 level min max algorithm.
    """
    def __init__(self, play_as, name, game):
        self.play_as = play_as
        self.name = name
        self.title = "Sadistic Player with one step look ahead"
        self.game = game

    def __del__(self):
        pass

    def reset(self):
        pass

    def play(self):
        # Compute possible moves
        possible_moves = []
        n = 0
        board = deepcopy(self.game.brd.board)
        for b in board:
            for e in b:
                if (e == 0):
                    possible_moves = possible_moves + [n]
                n += 1
        move = -1
        # See if our adversary can win if give a chance to play.
        # Compute the adversary's id
        temp = roll(self.game.play_order, 1)
        adversary = temp[self.play_as - 1]
        for m in possible_moves:
            new_board = deepcopy(board)
            x, y = self.game.brd.get_xy_from_pos(m)
            new_board[x][y] = adversary
            result = self.game.stateless_has_won(new_board, adversary)
            if (result == err.WIN):
                move = m
                break
        # The adversary cannot win in the next move.
        if (move == -1):
            # For each of the listed move, see if the player can win in the next move
            for m in possible_moves:
                new_board = deepcopy(board)
                x, y = self.game.brd.get_xy_from_pos(m)
                new_board[x][y] = self.play_as
                result = self.game.stateless_has_won(new_board, self.play_as)
                if (result == err.WIN):
                    move = m
                    break
        if (move == -1):
            # We cannot win in the next move.
            move = possible_moves[randint(0, len(possible_moves)-1)]
        else:
            # We can win in the next move.
            move = m
        result = self.game.mark(move, self.play_as)
        return int(move), result


def main():
    pass

if __name__ == '__main__':
	main()
