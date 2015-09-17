#! /usr/bin/python3

from random import randint
from err import err

from copy import *
from numpy import *

class randomPlayer1S:
    """
    The random player with 1 step look ahead finds a list of valid moves, and 
    chooses one among it such that it can win the next move, or prevent an 
    adversary from winning in the next move.
    
    Essentially this is a 1 level min max algorithm.
    
    """
    def __init__(o,play_as,name,game):
        o.play_as = play_as;
        o.name = name
        o.title = "Random Player with one step look ahead"
        o.game = game
        
    def play(o):
        # Compute possible moves
        possible_moves=[];
        n = 0
        board = deepcopy(o.game.brd.board)
        for b in board:
            for e in b:
                if (e == 0):
                    possible_moves=possible_moves+[n]
                n += 1
        move = -1
        # For each of the listed move, see if the player can win in the next move
        for m in possible_moves:
            new_board = deepcopy(board)
            x,y=o.game.brd.get_xy_from_pos(m)
            new_board[x][y]=o.play_as;
            result = o.game.stateless_has_won(new_board,o.play_as)
            if (result == err.WIN):
                move = m;
                break
        # We cannot win in the next move.
        if (move == -1):
            # See if our adversary can win if give a chance to play.
            temp = roll(o.game.play_order,1)
            adversary=temp[o.play_as-1]
            for m in possible_moves:
                new_board = deepcopy(board)
                x,y=o.game.brd.get_xy_from_pos(m)
                new_board[x][y]=adversary;
                result = o.game.stateless_has_won(new_board,adversary)
                if (result == err.WIN):
                    move = m;
                    break
        if (move == -1):
            move = possible_moves[randint(0, len(possible_moves)-1)]
        else:
            move = m
        return int(move)
        
def main():
    player=randomPlayer(1);
    print( player.play([[0,0,0],[0,0,0],[0,0,0]]) )
    print( player.play([[0,1,0],[0,0,0],[0,0,0]]) )
    print( player.play([[0,1,2],[0,0,0],[0,0,0]]) )
    print( player.play([[0,1,2],[1,2,0],[0,0,0]]) )

if __name__ == '__main__':
	main()    