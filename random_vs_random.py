#! /usr/bin/python3
from xo import xo
from human import human
from randomPlayer import randomPlayer
from err import err

def main():
	VERBOSE = False;
	N_GAMES = 10000
	print("\nTic Tac Toe Platform\nRandom Player vs Random Player\n______________________\n")
	
	player_random1 = randomPlayer(1,"Rand 1")
	player_random2 = randomPlayer(2,"Rand 2")
	
	rand1_win = 0
	rand1_win_turns = 0
	rand2_win = 0
	rand2_win_turns = 0
	draw = 0
	
	f = open('gameLog.csv', 'w')
	for i in range (0, N_GAMES):
		csv_line = ''
		current_winner = 0
		g=xo(3,3,2,['X','O'],[1,2])
		while(g.game_over == False):
			move = player_random1.play(g.brd.board)
			result = g.mark(move,1)
			if (VERBOSE):
				print (str(result)+"\n")
			if (result == err.DRAW):
				#print (g.getBoard())
				current_winner = 0;
				draw += 1
			if (result == err.WIN):
				#print ("______________________")
				#print (g.getBoard())
				current_winner = 1
				print (player_random1.name+" has won")
				#print ("______________________")
				rand1_win += 1
				rand1_win_turns += g.turn
			if (g.game_over == False):
				move = player_random2.play(g.brd.board)
				result = g.mark(move,2)
				if (VERBOSE):
					print (str(result)+"\n")
				if (result == err.DRAW):
					#print (g.getBoard())
					current_winner = 0
					draw += 1
				if (result == err.WIN):
					#print ("______________________")
					#print (g.getBoard())
					current_winner = 2
					print (player_random2.name+" has won")
					#print ("______________________")
					rand2_win += 1
					rand2_win_turns += g.turn
		# Log game to CSV file
		for i, e in enumerate(g.play_order):
			csv_line += str(e)+','
		csv_line += str(current_winner)
		for e in g.gameLog[:,1]:
			csv_line += ', '+str(e)
		csv_line += '\n'
		f.write(csv_line)
	f.close()
	print ("Random 1 Winner :"+str(rand1_win))
	print ("Average Moves to win :"+str(rand1_win_turns/rand1_win))
	print ("Random 2 Winner :"+str(rand2_win))
	print ("Average Moves to win :"+str(rand2_win_turns/rand2_win))
	print ("Draw :"+str(draw))

if __name__ == '__main__':
	main()