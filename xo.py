#! /usr/bin/python3
from enum import Enum
from board import board, err
import math
from numpy import *

VERBOSE = 0


def transpose(board):
	transBoard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	c = 0
	for b in board:
		r = 2
		for e in b:
			transBoard[r][c] = e
			r -= 1
		c += 1
	return transBoard

"""
A generalized tic tac toe game class.
"""


class xo:
	def __init__(o, M, N, K, sym, order):
		"""
		Initilize a game with a board of size M x N with K players using the symbols in the list sym.
		The players play in the order specified by the list order.
		"""
		o.brd = board(M, N, K, sym)
		o.play_order = order
		o.num_players = K
		o.reset()

	def reset(o):
		o.brd.reset()
		o.game_turn = 0
		o.gameLog = ones((9, 2), int)*-1
		o.game_over = False
		o.turn = o.play_order[0]

	def mark(o, pos, player):
		"""
		Marks a position on the board with the symbol for the player.
		If the position is already marked, the function returns err.INVALID_MOVE
		If a player attempts to play out of turn, the function returns err.OUT_OF_TURN
		"""
		# Are we trying to play after the game is over?
		if(not o.game_over):
			# Is a player trying to play out of turn?
			if(player == o.play_order[(o.game_turn % o.num_players)]):
				returnVal = o.brd.set_pos(pos, player)
				# is the postion selected to mark is not invalid?
				if(returnVal == err.OK):
					o.gameLog[o.game_turn] = [player, pos]
					o.game_turn += 1
					# Do we have a winner?
					returnVal = o.has_won(player)
					if (returnVal == err.WIN):
						# Yes. We do have a winner
						o.game_over = True
			else:
				# Cheat! Did you think you could get away by playing out of turn? Well, you cant!
				console_log(1, "OUT OF TURN")
				returnVal = err.OUT_OF_TURN
		else:
			# yes. A player tried to play after the game was over... Droids !!!
			returnVal = err.INVALID_MOVE
		return returnVal

	def get_board(o):
		return o.brd.get_board_str()

	def has_won(o, player):
		"""
		Implemented for standard 3x3 tic tac toe game
		"""
		if (o.brd.free_positions == 0):
			o.game_over = True
		win_logic = (o.brd.board == player)
		# Check linear
		for i in range(0, 2):
			lin_sum = sum(sum(win_logic, i) == 3)
			if (lin_sum == 1):
				returnVal = err.WIN
				break
			else:
				returnVal = err.OK
		# check diagonals
		if (returnVal == err.OK):
			if (((sum(diagonal(win_logic))) == 3) |
					((sum(diagonal(transpose(win_logic)))) == 3)):
				returnVal = err.WIN
		if ((o.game_over) & (returnVal == err.OK)):
			returnVal = err.DRAW
		return returnVal

	def stateless_has_won(o, board, player):
		"""
		Implemented for standard 3x3 tic tac toe game
		"""
		game_over = False
		free_positions = sum(sum(board == 0))
		if (free_positions == 0):
			game_over = True
		win_logic = (board == player)
		# Check linear
		for i in range(0, 2):
			lin_sum = sum(sum(win_logic, i) == 3)
			if (lin_sum == 1):
				returnVal = err.WIN
				break
			else:
				returnVal = err.OK
		# check diagonals
		if (returnVal == err.OK):
			if (((sum(diagonal(win_logic))) == 3) | ((sum(diagonal(transpose(win_logic)))) == 3)):
				returnVal = err.WIN
		if ((game_over) & (returnVal == err.OK)):
			returnVal = err.DRAW
		return returnVal


def console_log(level, log_line):
	global VERBOSE
	if level <= VERBOSE:
		print(log_line)


def main():
	print("\nTic Tac Toe Platform Test\n_________________________")
	g = xo(3, 3, 2, ['X', 'O'], [2, 1])
	print(g.get_board())

	g.mark(0, 1)
	print(g.get_board())
	g.mark(0, 2)
	print(g.get_board())
	g.mark(2, 2)
	print(g.get_board())
	g.mark(3, 1)
	print(g.get_board())
	g.mark(4, 2)
	print(g.get_board())

	print("Game Log:" + str(g.gameLog))

if __name__ == '__main__':
	if __doc__:
		print('Module:')
		print(__doc__ + '\n')
	main()
