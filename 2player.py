#! /usr/bin/python3
from xo import xo
from humanPlayer import humanPlayer
from randomPlayer import randomPlayer
from random1SPlayer import random1SPlayer
from random1SSadistPlayer import random1SSadistPlayer
from opportunityPlayer import opportunityPlayer
from tdPlayer import tdPlayer
from err import err

from random import randint
from numpy import *

VERBOSE = 0
N_GAMES = 10000
ROLL = False
LINE = "-----------------------------------------"


def main():
	global LINE
	PLAY_ORDER = [2,1]
	g = xo(3, 3, 2, ['X', 'O'], PLAY_ORDER)
	player1 = random1SSadistPlayer(1, "Rand1SSaddist", g)
	player2 = random1SPlayer(2, "Rnd1SPlayer", g)
	print('\nThe XO - Tic Tac Toe Platform\n' + player1.title + ' vs ' + player2.title)
	console_log(0, LINE)

	player1_win = 0
	player1_win_turns = 0
	player2_win = 0
	player2_win_turns = 0
	draw = 0

	# Play N Games
	csv_line = ''
	for i in range(0, N_GAMES):
		g.reset()
		player1.reset()
		player2.reset()
		current_winner = 0
		# create a game instance
		if ROLL:
			PLAY_ORDER = roll(PLAY_ORDER, 1)
		# Keep playing till the game in not over.
		while(not g.game_over):
			move, result = player1.play()
			#result = g.mark(move, 1)
			console_log(3, 'Result: ' + str(result) + '\n')
			if (result == err.DRAW):
				console_log(2, '______________________')
				console_log(2, g.get_board())
				console_log(1, 'Game Drawn')
				console_log(2, '______________________')
				current_winner = 0
				draw += 1
			if (result == err.WIN):
				console_log(2, '______________________')
				console_log(2, g.get_board())
				console_log(1, player1.name + ' has won')
				console_log(2, '______________________')
				current_winner = 1
				player1_win += 1
				player1_win_turns += g.game_turn
			if (not g.game_over):
				move, result = player2.play()
				#result = g.mark(move, 2)
				console_log(3, 'Result: ' + str(result) + '\n')
				if (result == err.DRAW):
					console_log(2, '______________________')
					console_log(2, g.get_board())
					console_log(1, 'Game Drawn')
					console_log(2, '______________________')
					draw += 1
					current_winner = 0
					draw += 1
				if (result == err.WIN):
					console_log(2, "______________________")
					console_log(2, g.get_board())
					console_log(1, player2.name+" has won")
					console_log(2, "______________________")
					current_winner = 2
					player2_win += 1
					player2_win_turns += g.game_turn
		# Log game to CSV file
		for i, e in enumerate(g.play_order):
			csv_line += str(e)+','
		csv_line += str(current_winner)
		for e in g.gameLog[:, 1]:
			csv_line += ', ' + str(e)
		csv_line += '\n'
	f = open('game_log_' + player1.name + '-vs-' + player2.name + '.csv', 'w')
	f.write(csv_line)
	f.close()
	console_log(1, '\n' + LINE)
	print(player1.name + ' Winner :' + str(player1_win))
	if(player1_win > 0):
		print('Average Moves to win :' + str(player1_win_turns / player1_win))
	print(player2.name + ' Winner :' + str(player2_win))
	if(player2_win > 0):
		print("Average Moves to win :" + str(player2_win_turns / player2_win))
	print('Draw :' + str(draw))


def console_log(level, log_line):
	global VERBOSE
	if level <= VERBOSE:
		print(log_line)

if __name__ == '__main__':
	main()
