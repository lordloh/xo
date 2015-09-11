#! /usr/bin/python3

class human:
    def __init__(self,play_as):
        self.name = input("Enter your name :")
        self.sym = [ ' ', '0', 'X' ]
        self.play_as = play_as;
        
    def play(self,board):
        boardString = "*********************\n";
        for i in range(0, 3):
            for j in range (0,3):
                if j < 2:
                	boardString += self.sym[board[i][j]] + '| ';
                else:
                	boardString += self.sym[board[i][j]];
            boardString += "\n"
        print (boardString,end="")
        move = input(self.name+", enter the square number you want to mark with '"+self.sym[self.play_as]+"' (0-8) :")
        return int(move)
        
def main():
    player=human(1);
    player.play([[0,0,0],[0,0,0],[0,0,0]])

if __name__ == '__main__':
	main()    