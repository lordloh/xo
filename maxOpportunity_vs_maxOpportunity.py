#! /usr/bin/python3
from xo import xo
from human import human
from maxOpportunityPlayer import maxOpportunityPlayer

def main():
	VERBOSE = False;
	N_GAMES = 10000
	print("\nTic Tac Toe Platform\nMaximum Opportunity Player vs Maximum Opportunity Player\n______________________\n")
	
	player_maxO1 = maxOpportunityPlayer(1,"Max Opportunity Player1")
	player_maxO2 = maxOpportunityPlayer(2,"Max Opportunity Player2")
	
	maxO1_win = 0
	maxO1_win_turns = 0
	maxO2_win = 0
	maxO2_win_turns = 0
	draw = 0
	
	
	for i in range (0, N_GAMES):
		g=xo()
		while(g.game_over == False):
			move = player_maxO1.play(g.board)
			result = g.set_absolute(move,1)
			if (VERBOSE):
				print (str(result)+"\n")
			if (result == g.res.DRAW):
				print (g.getBoard())
				draw += 1
			if (result == g.res.WIN):
				print ("______________________")
				print (g.getBoard())
				print (player_maxO1.name+" has won")
				print ("______________________")
				maxO1_win += 1
				maxO1_win_turns += g.turn
			if (g.game_over == False):
				move = player_maxO2.play(g.board)
				result = g.set_absolute(move,2)
				if (VERBOSE):
					print (str(result)+"\n")
				if (result == g.res.DRAW):
					print (g.getBoard())
					draw += 1
				if (result == g.res.WIN):
					print ("______________________")
					print (g.getBoard())
					print (player_maxO2.name+" has won")
					print ("______________________")
					maxO2_win += 1
					maxO2_win_turns += g.turn
	print ("Maximum Opportunity Player 1 Winner Winner :"+str(maxO1_win))
	print ("Average Moves to win :"+str(maxO1_win_turns/maxO1_win))
	print ("Maximum Opportunity Player 2 Winner :"+str(maxO2_win))
	print ("Average Moves to win :"+str(maxO2_win_turns/maxO2_win))
	print ("Draw :"+str(draw))

if __name__ == '__main__':
	main()