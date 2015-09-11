#! /usr/bin/python3
from xo import xo
from human import human
from randomPlayer import randomPlayer

def main():
	VERBOSE = False;
	N_GAMES = 1000
	print("\nTic Tac Toe Platform\nRandom Player vs Random Player\n______________________\n")
	
	player_random1 = randomPlayer(1,"Rand 1")
	player_random2 = randomPlayer(2,"Rand 2")
	
	rand1_win = 0
	rand1_win_turns = 0
	rand2_win = 0
	rand2_win_turns = 0
	draw = 0
	
	
	for i in range (0, N_GAMES):
		g=xo()
		while(g.game_over == False):
			move = player_random1.play(g.board)
			result = g.set_absolute(move,1)
			if (VERBOSE):
				print (str(result)+"\n")
			if (result == g.res.DRAW):
				print (g.getBoard())
				draw += 1
			if (result == g.res.WIN):
				print ("______________________")
				print (g.getBoard())
				print (player_random1.name+" has won")
				print ("______________________")
				rand1_win += 1
				rand1_win_turns += g.turn
			if (g.game_over == False):
				move = player_random2.play(g.board)
				result = g.set_absolute(move,2)
				if (VERBOSE):
					print (str(result)+"\n")
				if (result == g.res.DRAW):
					print (g.getBoard())
					draw += 1
				if (result == g.res.WIN):
					print ("______________________")
					print (g.getBoard())
					print (player_random2.name+" has won")
					print ("______________________")
					rand2_win += 1
					rand2_win_turns += g.turn
	print ("Random 1 Winner :"+str(rand1_win))
	print ("Average Moves to win :"+str(rand1_win_turns/rand1_win))
	print ("Random 2 Winner :"+str(rand2_win))
	print ("Average Moves to win :"+str(rand2_win_turns/rand2_win))
	print ("Draw :"+str(draw))

if __name__ == '__main__':
	main()