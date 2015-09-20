#! /usr/bin/python3

from random import randint


class randomPlayer:
    """
    The random player finds a list of valid moves, and chooses one among it.
    """
    def __init__(o, play_as, name, game):
        o.play_as = play_as
        o.name = name
        o.title = "Random Player"
        o.game = game

    def play(o):
        possible_moves = []
        n = 0
        board = o.game.brd.board
        for b in board:
            for e in b:
                if (e == 0):
                    possible_moves = possible_moves + [n]
                n += 1
        move = possible_moves[randint(0, len(possible_moves)-1)]
        return int(move)


def main():
    player = randomPlayer(1)
    print(player.play([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(player.play([[0, 1, 0], [0, 0, 0], [0, 0, 0]]))
    print(player.play([[0, 1, 2], [0, 0, 0], [0, 0, 0]]))
    print(player.play([[0, 1, 2], [1, 2, 0], [0, 0, 0]]))

if __name__ == '__main__':
    main()
