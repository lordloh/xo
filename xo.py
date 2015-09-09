#! /usr/bin/python3
from enum import Enum

class res(Enum):
	OK = 0
	WIN = 1
	DRAW = 2
	OUT_OF_TURN = -1
	INVALID_MOVE = -2

class xo:
	def __init__(self):
		self.board = [ [0, 0, 0 ] , [ 0, 0, 0 ] , [ 0, 0, 0 ] ]
		self.sym = [ ' ', '0', 'X' ]
		self.turn = 0
		self.X_TURN_MODULUS = -1
		self.O_TURN_MODULUS = -1
		self.PLAYER_X = 2
		self.PLAYER_O = 1
		self.won = False
		self.game_over = False
		#self.res=enum(OK = 0, WIN = 1, DRAW = 2, OUT_OF_TURN = -1, INVALID_MOVE = -2)
		self.res=res;
		self.empty_positions = 9
		
	def set_pos(self,pos_x,pos_y,player):
		if (player >= 0 & player < 3):
			self.board[pos_x][pos_y]=player
		return 0
		
	def set_X(self, pos_x, pos_y):
		# check if X is playing first.
		if self.turn == 0:
			self.X_TURN_MODULUS = 0
			self.O_TURN_MODULUS = 1
		# check if X is not playing out of turn.
		if self.turn % 2 == self.X_TURN_MODULUS:
			# check if we are overwriting a position
			if (self.board[pos_x][pos_y] == 0):
				self.board[pos_x][pos_y] = self.PLAYER_X
				self.turn += 1
				# Check if the last move resulted in a victory
				return self.has_won(self.PLAYER_X)
			else:
				return self.res.INVALID_MOVE
		else:
			return self.res.OUT_OF_TURN
	
	def set_O(self,pos_x,pos_y):
		# check if O is playing first.
		if self.turn == 0:
			self.X_TURN_MODULUS = 1
			self.O_TURN_MODULUS = 0
		# check if O is not playing out of turn.
		if self.turn % 2 == self.O_TURN_MODULUS:
			# check if we are overwriting a position
			if ( self.board[pos_x][pos_y] == 0 ):
				self.board[pos_x][pos_y] = self.PLAYER_O
				self.turn += 1
				# Check if the last move resulted in a victory
				return self.has_won(self.PLAYER_O)
			else:
				return self.res.INVALID_MOVE
		else:
			return self.res.OUT_OF_TURN
	
	def has_won(self,player):
		self.count_empty_squares();
		transBoard = list(map(list, zip(*self.board)))
		result = self.check_board_for_winner( self.board, player ) | self.check_board_for_winner( transBoard, player )
		returnVal = self.res.OK
		# check for draw
		if (result == True):
			# We have a winner
			self.game_over = True
			self.won = True
			returnVal = self.res.WIN
		elif (result == False & self.game_over == True):
			# No winner and no moves left.
			returnVal = self.res.DRAW
		elif (result == False & self.game_over == False):
			# No winner and game not over. Play on.
			returnVal = self.res.OK
		self.won=result
		return returnVal
		
	def count_empty_squares(self):
		# Count the number of empty squares
		self.empty_positions = 0
		for i in self.board:
			for j in i:
				if j == 0:
					self.empty_positions += 1;
		if self.empty_positions == 0:
			# If there are no empty squares, then pronounce the game over.
			self.game_over = True;
	
	def check_board_for_winner(self,board,player):
		# Check 3 horizontal and 1 diagonal.
		win = False
		if board[0] == [player, player, player]:
			win = True
		if board[1] == [player, player, player]:
			win = True
		if board[2] == [player, player, player]:
			win = True
		if ( [board[0][0], board[1][1], board[2][2]] == [ player, player, player ] ):
			win = True
		return win
		
	
	def getBoard(self):
		boardString="";
		for i in range(0, 3):
			for j in range (0,3):
				if j < 2:
					boardString += self.sym[self.board[i][j]] + '| ';
				else:
					boardString += self.sym[self.board[i][j]];
			boardString += "\n"
		return boardString;	
		
def main():
	print("Tic Tac Toe Platform")
	g=xo()
	print(g.getBoard())
	
	print('Play :'+repr(g.set_X(2,2)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+repr(g.set_O(0,2)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_X(1,2)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_O(2,0)))
	print(g.getBoard())
	print('----------')

	print('Play :'+str(g.set_X(0,0)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_O(0,1)))
	print(g.getBoard())
	print('----------')
	
	# out of turn
	print('Play :'+str(g.set_O(0,1)))
	print(g.getBoard())
	print('----------')
	
	# invalid move
	print('Play :'+str(g.set_X(0,1)))
	print(g.getBoard())
	print('----------')
	
	
	print('Play :'+str((g.set_X(1,1))))
	print(g.getBoard())
	print('----------')

if __name__ == '__main__':
	main()