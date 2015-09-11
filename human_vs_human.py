#! /usr/bin/python3
from xo import xo
from human import human

def main():
	print("\nTic Tac Toe Platform\nHuman vs Human Player\n______________________\n")
	
	name = input("Player 1 - Enter your name :")
	player1 = human(1,name)
	name = input("Player 2 - Enter your name :")
	player2 = human(2,name)
	
	
	g=xo()
	while(g.game_over == False):
		while True:
			move = player1.play(g.board)
			result = g.set_absolute(move,1)
			print (str(result)+"\n")
			if (not((result == g.res.INVALID_MOVE) | (result == g.res.OUT_OF_TURN))):
				break
		if (result == g.res.WIN):
			print ("______________________")
			print (g.getBoard())
			print (player1.name+" has won")
			print ("______________________")
		if (g.game_over == False):
			while True:
				move = player2.play(g.board)
				result = g.set_absolute(move,2)
				print (str(result)+"\n")
				if (not((result == g.res.INVALID_MOVE) | (result == g.res.OUT_OF_TURN))):
					break
			if (result == g.res.WIN):
				print ("______________________")
				print (g.getBoard())
				print (player2.name+" has won")
				print ("______________________")
	

if __name__ == '__main__':
	main()