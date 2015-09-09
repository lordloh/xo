#! /usr/bin/python3
from xo import xo

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