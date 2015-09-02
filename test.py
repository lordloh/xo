#! /usr/bin/python3
import xo

def main():
	print("Hello");
	g=xo.xo();
	g.showBoard();
	print(g.setX(2,2));
	g.showBoard();
	print(g.won);
	
	print(g.setO(1,1));
	g.showBoard();
	print(g.won);
	
	print(g.setX(0,1));
	g.showBoard();
	print(g.won);
	
	print(g.setO(1,0));
	g.showBoard();
	print(g.won);
	
	print(g.setX(1,2));
	g.showBoard();
	print(g.won);
	
	print(g.setO(2,0));
	g.showBoard();
	print(g.won);
	
	print(g.setX(0,2));
	g.showBoard();
	print(g.won);



if __name__ == '__main__':
	main()