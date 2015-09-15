#! /usr/bin/python3
from enum import Enum

class err(Enum):
	OK = 0
	WIN = 1
	DRAW = 2
	OUT_OF_TURN = -1
	INVALID_MOVE = -2
	
#	def __init__(o):
#		return None;