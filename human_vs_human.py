#! /usr/bin/python3
from xo import xo
from human import human

def main():
	print("Tic Tac Toe Platform\nHuman vs Human\n")
	
	player1 = human(1)
	player2 = human(2)
	
	
	g=xo()
	while(g.game_over == False):
		while True:
			move = player1.play(g.board)
			result = g.set_absolute(move,1)
			print (str(result)+"\n")
			if (not((result == g.res.INVALID_MOVE) | (result == g.res.OUT_OF_TURN))):
				break
		if (result == g.res.WIN):
			print ("*********************")
			print (g.getBoard())
			print (player1.name+" has won")
		if (g.game_over == False):
			while True:
				move = player2.play(g.board)
				result = g.set_absolute(move,2)
				print (str(result)+"\n")
				if (not((result == g.res.INVALID_MOVE) | (result == g.res.OUT_OF_TURN))):
					break
			if (result == g.res.WIN):
				print ("*********************")
				print (g.getBoard())
				print(player1.name+" has won")
	

if __name__ == '__main__':
	main()