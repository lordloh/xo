#! /usr/bin/python3

import numpy as np
import pickle
import math
from xo import xo

class MLDataStr:
	def __init__(self):
		self.policy = []
		self.train_cycles = 0
		self.row = 0
		self.col = 0
		self.num_states = 0
		self.num_players = 0
		self.turn_number = 0


class tdPlayer:
	"""
	The Temporal Difference Reinforcement learning player.
	"""
	def __init__(self, play_as, name, game):
		self.play_as = play_as
		self.name = name
		self.title = "Temporal Difference Player"
		self.game = game
		self.policy_update = False
		self.state_log = []
		# Load the policy if the file exist. 
		self.ml_data = MLDataStr()
		try:
			f = open(self.name + '_' + 'policy', 'rb')
			self.ml_data = pickle.load(f)
			f.close()
			if (self.ml_data.row == self.game.brd.row & self.ml_data.col == self.game.brd.col & self.ml_data.num_players == self.game.num_players):
				raise ValueError('The policy state space is not valid for this game.')
			self.train_cycles = self.ml_data.train_cycles
			self.policy = self.ml_data.policy
		except IOError:
			# Create a new policy
			self.ml_data.train_cycles = 0
			self.ml_data.num_states = pow((self.game.brd.num_players + 1), (self.game.brd.row * self.game.brd.col))
			print('players:'+str((self.game.brd.num_players + 1)))
			print('size:'+str((self.game.brd.row * self.game.brd.col)))
			self.ml_data.policy = np.random.randint(-5, 5, size=(self.ml_data.num_states, 1))
			self.ml_data.col = self.game.brd.col
			self.ml_data.num_players = self.game.num_players
			self.policy_update = True
		print(self.ml_data.num_states)
		print(self.ml_data.policy)

	def __del__(self):
		# Save the Policy - if any training has occured.
		if (self.policy_update):
			f = open(self.name + '_' + 'policy', 'wb')
			pickle.dump(self.ml_data, f)
			f.close()

	def reset(self):
		print(self.state_log)
		self.state_log = np.ones(((self.game.brd.row * self.game.brd.col), 2), int) * -1
		self.turn_number = 0

	def play(self):
		if (not self.game.game_over):
			possible_moves = []
			n = 0
			#board = self.game.brd.board
			#for b in board:
			#    for e in b:
			#        if (e == 0):
			#            possible_moves = possible_moves + [n]
			#        n += 1
			#move = possible_moves[np.random.randint(0, len(possible_moves))]
			game_state = self.compute_game_state()
			print('>'+str(self.game.game_turn) + ' : ' + str(self.turn_number))
			self.state_log[self.turn_number, 0] = game_state
			move = np.argmax(self.policy[game_state])
			self.turn_number += 1
			self.policy_update = True
		else:
			move = -1
		return int(move)

	def handle_results(self):
		pass

	def compute_game_state(self):
		state = 0
		i = 0
		board = self.game.brd.board
		for rows in board:
			for e in rows:
				x, y = self.game.brd.get_xy_from_pos(i)
				state += board[x][y] * (3 ^ (i))
				i += 1
		return state


def main():
	PLAY_ORDER = [1, 2]
	g = xo(3, 3, 2, ['X', 'O'], PLAY_ORDER)
	player = tdPlayer(1, 'tdTest', g)


if __name__ == '__main__':
    main()
