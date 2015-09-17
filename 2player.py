#! /usr/bin/python3
from xo import xo
from humanPlayer import humanPlayer
from randomPlayer import randomPlayer
from randomPlayer1S import randomPlayer1S
from err import err

from random import randint
from numpy import *

VERBOSE = 2
N_GAMES = 1000
ROLL = False
LINE = "-----------------------------------------"

def main():
	global LINE
	PLAY_ORDER = [1,2]
	g=xo(3,3,2,['X','O'],PLAY_ORDER)
	player1 = randomPlayer1S(1,"Rand 1",g)
	player2 = randomPlayer1S(2,"Rand 2",g)	
	print('\nTic Tac Toe Platform\n'+player1.title+' vs '+player2.title)
	console_log(0,LINE)
	
	rand1_win = 0
	rand1_win_turns = 0
	rand2_win = 0
	rand2_win_turns = 0
	draw = 0
	
	f = open('game_log_rand_rand1.csv', 'w')
	# Play N Games
	for i in range (0, N_GAMES):
		csv_line = ''
		g.reset()
		current_winner = 0
		# create a game instance
		if ROLL :
			PLAY_ORDER = roll (PLAY_ORDER,1)
		# Keep playing till the game in not over.
		while(g.game_over == False):
			move = player1.play()
			result = g.mark(move,1)
			console_log (3,'Result: '+str(result)+"\n")
			if (result == err.DRAW):
				console_log (2, g.get_board())
				current_winner = 0;
				draw += 1
			if (result == err.WIN):
				console_log (2, '______________________')
				console_log (2, g.get_board())
				console_log (1, player1.name+' has won')
				current_winner = 1
				console_log (2, '______________________')
				rand1_win += 1
				rand1_win_turns += g.game_turn
			if (g.game_over == False):
				move = player2.play()
				result = g.mark(move,2)
				console_log (3,'Result: '+str(result)+"\n")
				if (result == err.DRAW):
					console_log (2,g.get_board())
					current_winner = 0
					draw += 1
				if (result == err.WIN):
					console_log (2, "______________________")
					console_log (2, g.get_board())
					console_log (1, player2.name+" has won")
					console_log (2, "______________________")
					current_winner = 2
					rand2_win += 1
					rand2_win_turns += g.game_turn;
		# Log game to CSV file
		for i, e in enumerate(g.play_order):
			csv_line += str(e)+','
		csv_line += str(current_winner)
		for e in g.gameLog[:,1]:
			csv_line += ', '+str(e)
		csv_line += '\n'
		f.write(csv_line)
	f.close()
	console_log(1,LINE)
	print (player1.name+" Winner :"+str(rand1_win))
	if (rand1_win>0):
		print ("Average Moves to win :"+str(rand1_win_turns/rand1_win))
	print (player2.name+" Winner :"+str(rand2_win))
	if (rand2_win>0):
		print ("Average Moves to win :"+str(rand2_win_turns/rand2_win))
	print ("Draw :"+str(draw))

def console_log(level,log_line):
	global VERBOSE
	if level <= VERBOSE:
		print (log_line)

if __name__ == '__main__':
	main()