#! /usr/bin/python3

#from game.board import *
from board import board
from err import err


def main():
    b = board(3, 3, 2, ['X','O'],[1,2])
    print (str(b.set_pos(0,1)==err.OK))
    print(b.get_board_str())
    b.set_pos(1,2)
    print(b.get_board_str())
    
if __name__ == '__main__':
	main()