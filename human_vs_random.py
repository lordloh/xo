#! /usr/bin/python3
from xo import xo
from human import human
from randomPlayer import randomPlayer

def main():
	print("Tic Tac Toe Platform\nHuman vs Human\n")
	
	player1 = human(1)
	player2 = randomPlayer(2)
	
	
	g=xo()
	while(g.game_over == False):
		move = player1.play(g.board)
		result = g.set_absolute(move,1)
		print (str(g.game_over)+" >>>"+str(result))
		if (g.game_over == False):
			move = player2.play(g.board)
			result = g.set_absolute(move,2)
			print (str(g.game_over)+" *** "+str(result))
	

if __name__ == '__main__':
	main()