#! /usr/bin/python3
from xo import xo
from human import human
from randomPlayer import randomPlayer

def main():
	print("\nTic Tac Toe Platform\nHuman vs Random Player\n______________________\n")
	
	name = input("Human Player, enter your name :")
	player1 = human(1,name)
	player_random = randomPlayer(2,"Random Player")
	
	
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
			move = player_random.play(g.board)
			result = g.set_absolute(move,2)
			print (str(result)+"\n")
			if (result == g.res.WIN):
				print ("______________________")
				print (g.getBoard())
				print (player_random.name+" has won")
				print ("______________________")
	

if __name__ == '__main__':
	main()