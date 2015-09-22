#! /usr/bin/python3

class humanPlayer:
    def __init__(o,play_as,name,game):
        o.name = name
        o.play_as = play_as;
        o.title = "Human Player"
        o.game = game

    def reset(self):
        pass
        
    def play(o):
        boardString = "*********************\n";
        board = o.game.brd.board
        print (o.game.get_board(),end="")
        move = input(o.name+", enter the square number you want to mark with '"+o.game.brd.sym[o.play_as]+"' (0-8) :")
        return int(move)
        
def main():
    player=humanPlayer(1);
    player.play([[0,0,0],[0,0,0],[0,0,0]])

if __name__ == '__main__':
	main()    