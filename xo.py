#! /usr/bin/python3
class xo:
	def __init__(self):
		self.board=[[0,0,0],[0,0,0],[0,0,0]];
		self.sym=[' ','0','X'];
		self.turn=0;
		self.modResX=-1;
		self.modResO=-1;
		self.won=False;
		
	def setPos(self,posx,posy,who):
		if (who>=0 & who<3):
			self.board[posx][posy]=who;
		return 0;
		
	def setX(self,posx,posy):
		if self.turn==0:
			self.modResX=0;
			self.modResO=1;
		if self.turn%2==self.modResX:
			self.board[posx][posy]=2;
			self.turn+=1;
			self.win(2);
			return 0;
		else:
			return -1;
	
	def setO(self,posx,posy):
		if self.turn==0:
			self.modResX=1;
			self.modResO=0;
		if self.turn%2==self.modResO:
			self.board[posx][posy]=1;
			self.turn+=1;
			self.win(1);
			return 0;
		else:
			return -1;
	
	def win(self,who):
		win=False;
		if self.board[0]==[who, who, who]:
			win=True;
		if self.board[1]==[who, who, who]:
			win=True;
		if self.board[2]==[who, who, who]:
			win=True;
		if ([self.board[0][0], self.board[1][1], self.board[2][2]]==[who,who,who]):
			win=True;
			
		transList=list(map(list, zip(*self.board)))
		if transList[0]==[who, who, who]:
			win=True;
		if transList[1]==[who, who, who]:
			win=True;
		if transList[2]==[who, who, who]:
			win=True;
		if ([transList[0][0], transList[1][1], transList[2][2]]==[who,who,who]):
			win=True;
		self.won=win;
		return win;
		
	def showBoard(self):
		for i in range(0, 3):
			for j in range (0,3):
				if j<2:
					print (self.sym[self.board[i][j]],'| ',end="",flush=True)
				else:
					print (self.sym[self.board[i][j]],end="",flush=True)
			print(end="\n")
		print(end="\n")
		return 0;
		
def main():
	print("Hello");
	g=xo();
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