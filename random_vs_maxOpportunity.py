#! /usr/bin/python3
from xo import xo
from human import human
from randomPlayer import randomPlayer
from maxOpportunityPlayer import maxOpportunityPlayer

def main():
	VERBOSE = False;
	N_GAMES = 10000
	print("\nTic Tac Toe Platform\nRandom Player vs Maximum Opportunity Player\n______________________\n")
	
	#player_maxO= maxOpportunityPlayer(1,"Max Opportunity Player")
	#player_random = randomPlayer(2,"Random Player")
	player_random= maxOpportunityPlayer(1,"Max Opportunity Player")
	player_maxO = randomPlayer(2,"Random Player")
	
	rand_win = 0
	rand_win_turns = 0
	maxO_win = 0
	maxO_win_turns = 0
	draw = 0
	
	
	for i in range (0, N_GAMES):
		g=xo()
		while(g.game_over == False):
			move = player_random.play(g.board)
			result = g.set_absolute(move,1)
			if (VERBOSE):
				print (str(result)+"\n")
			if (result == g.res.DRAW):
				print (g.getBoard())
				draw += 1
			if (result == g.res.WIN):
				print ("______________________")
				print (g.getBoard())
				print (player_random.name+" has won")
				print ("______________________")
				rand_win += 1
				rand_win_turns += g.turn
			if (g.game_over == False):
				move = player_maxO.play(g.board)
				result = g.set_absolute(move,2)
				if (VERBOSE):
					print (str(result)+"\n")
				if (result == g.res.DRAW):
					print (g.getBoard())
					draw += 1
				if (result == g.res.WIN):
					print ("______________________")
					print (g.getBoard())
					print (player_maxO.name+" has won")
					print ("______________________")
					maxO_win += 1
					maxO_win_turns += g.turn
	print ("Random Winner :"+str(rand_win))
	print ("Average Moves to win :"+str(rand_win_turns/rand_win))
	print ("Maximum Opportunity Player Winner :"+str(maxO_win))
	print ("Average Moves to win :"+str(maxO_win_turns/maxO_win))
	print ("Draw :"+str(draw))

if __name__ == '__main__':
	main()