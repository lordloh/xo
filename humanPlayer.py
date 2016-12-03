#! /usr/bin/python3

class humanPlayer:
    def __init__(self,play_as,name,game):
        self.name = name
        self.play_as = play_as;
        self.title = "Human Player"
        self.game = game

    def reset(self):
        pass
        
    def play(self):
        boardString = "*********************\n";
        board = self.game.brd.board
        print (self.game.get_board(),end="")
        move = int(input(self.name+", enter the square number you want to mark with '"+self.game.brd.sym[self.play_as]+"' (0-8) :"))
        result = self.game.mark(move, self.play_as)
        return int(move), result
        
def main():
    player=humanPlayer(1);
    player.play([[0,0,0],[0,0,0],[0,0,0]])

if __name__ == '__main__':
	main()    