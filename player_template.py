from xo import xo
from err import err

class player_template:
    """
	A generic player template.
	
	To implement a player with a new stratey, code the following functions.
	"""
	def __init__(self, play_as, name, game):
	    self.play_as = play_as
		self.name = name
		self.title = "Generic Player Template"
		self.game = game

    def __del__(self):
        pass

    def reset(self):
        pass

    def play(self):
        # figure out what square to mark.
        [move, result] = self.game.mark(move, self.play_as)

def main():
    pass

if __name__ == '__main__':
    main()