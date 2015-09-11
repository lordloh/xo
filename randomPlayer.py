#! /usr/bin/python3

from random import randint

class randomPlayer:
    def __init__(self,play_as):
        self.sym = [ ' ', '0', 'X' ]
        self.play_as = play_as;
        self.name = "Random Player"
        
    def play(self,board):
        possible_moves=[];
        n = 0
        for b in board:
            for e in b:
                if (e == 0):
                    possible_moves=possible_moves+[n]
                n += 1
        move = possible_moves[randint(0, len(possible_moves)-1)]
        return int(move)
        
def main():
    player=randomPlayer(1);
    print( player.play([[0,0,0],[0,0,0],[0,0,0]]) )
    print( player.play([[0,1,0],[0,0,0],[0,0,0]]) )
    print( player.play([[0,1,2],[0,0,0],[0,0,0]]) )
    print( player.play([[0,1,2],[1,2,0],[0,0,0]]) )

if __name__ == '__main__':
	main()    