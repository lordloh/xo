#! /usr/bin/python3

from random import randint
from err import err

from copy import *
from numpy import *


class opportunityPlayer:
	"""
	A player that chooses to mark the squares where the probablity of winning is
	the highest.
	"""
	def __init__(o, play_as, name, game):
		o.play_as = play_as
		o.name = name
		o.title = "Opportuntiy player"
		o.game = game
		o.opportunity = [3, 2, 3, 2, 4, 2, 3, 2, 3]

	def reset(self):
		pass

	def play(o):
		# Compute possible moves
		possible_moves = []
		available_oportunity = []
		n = 0
		board = deepcopy(o.game.brd.board)
		for b in board:
			for e in b:
				if (e == 0):
					possible_moves = possible_moves + [n]
					available_oportunity += [o.opportunity[n]]
				n += 1
		move = -1
		# For each of the listed move, see if the player can win in the next move
		max_available_opportunity = max(available_oportunity)
		max_opportunity_pos = [possible_moves[i] for i, j in enumerate(available_oportunity) if j == max_available_opportunity]
		# print("Play List:"+str(max_opportunity_pos))
		move = max_opportunity_pos[randint(0, len(max_opportunity_pos)-1)]
		return int(move)


def main():
	pass

if __name__ == '__main__':
	main()
