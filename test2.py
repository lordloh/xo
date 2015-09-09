#! /usr/bin/python3
from xo import xo

# Test for inedxed addressing game

def main():
	print("Tic Tac Toe Platform")
	g=xo()
	print(g.getBoard())
	
	print('Play :'+repr(g.set_absolute(0,2)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+repr(g.set_absolute(1,1)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_absolute(2,2)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_absolute(3,1)))
	print(g.getBoard())
	print('----------')

	print('Play :'+str(g.set_absolute(4,2)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_absolute(5,1)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_absolute(6,2)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_absolute(7,1)))
	print(g.getBoard())
	print('----------')
	
	print('Play :'+str(g.set_absolute(8,2)))
	print(g.getBoard())
	print('----------')

if __name__ == '__main__':
	main()