#! /usr/bin/python3
from xo import xo

# Test for X Y addressing game

def main():
	print("Tic Tac Toe Platform")
	g=xo()
	print(g.getBoard())
	
	print('Play :'+repr(g.set_X(0,0)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+repr(g.set_O(0,1)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_X(0,2)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_O(1,0)))
	print(g.getBoard())
	print('----------')

	print('Play :'+str(g.set_X(1,1)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_O(1,2)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_X(2,0)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_O(2,1)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_X(2,2)))
	print(g.getBoard())
	print('----------')

if __name__ == '__main__':
	main()