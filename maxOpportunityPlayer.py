#! /usr/bin/python3

from random import randint

class maxOpportunityPlayer:
    def __init__(self,play_as,name):
        self.sym = [ ' ', '0', 'X' ]
        self.play_as = play_as;
        self.name = name
        self.opportunity = [3, 2, 3, 2, 4, 2, 3, 2, 3]
        
    def play(self,board):
        possible_moves = []
        available_oportunity = []
        n = 0
        for b in board:
            for e in b:
                if (e == 0):
                    possible_moves += [n]
                    available_oportunity += [self.opportunity[n]]
                n += 1
        max_available_opportunity = max(available_oportunity)
        max_opportunity_pos = [possible_moves[i] for i, j in enumerate(available_oportunity) if j == max_available_opportunity]
        #print("Play List:"+str(max_opportunity_pos))
        move = max_opportunity_pos[randint(0, len(max_opportunity_pos)-1)]
        return int(move)
        
def main():
    player=randomPlayer(1);
    print( player.play([[0,0,0],[0,0,0],[0,0,0]]) )
    print( player.play([[0,1,0],[0,0,0],[0,0,0]]) )
    print( player.play([[0,1,2],[0,0,0],[0,0,0]]) )
    print( player.play([[0,1,2],[1,2,0],[0,0,0]]) )

if __name__ == '__main__':
	main()    