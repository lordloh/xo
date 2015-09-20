# XO
XO is written in Python 3 and is designed to be a general Tic Tac Toe game platform. It allows one to instantiate the game with a board of size M X N and K players.

The xo platform project consists of -
* **xo.py** - the game class
* **board.py** - the board class
* **err.py** - class to enumerate error codes.
* **Players** - these are a set of player classes.
* **2players.py** - an application to bind everything together.

Apart from these, one needs players to play on the platform. The current players are -
* **humanPlayer.py** - Asks a human what move to make and executes it.
* **randomPlayer.py** - chooses one of the empty squares at random as the next move.
* **random1SPlayer.py** - A 1step look ahead player. The player checks the board for positions where it may mark and win in the next move. If it cannot win in the next move, it plays such that it tried to prevent the adversary from winning in the next move. In the absence of either of these types of moves, the player marks a valid square at random.
* **random1SSadistPlayer.py** - A 1step look ahead player. The player checks the board for positions where it may mark and stop the adversary from winning. If no such position exist, it attempts to find a move by playing which it may win. In the absence of either of these types of moves, the player marks a valid square at random.
* **opportunityPlayer.py** - A player that marks the square where one has the maximum opportunity to win games. The positions are not re-evaluated after each mave.


## XO class
#### *Data*
* `brd` - board object
* `play_order` - The sequence in withch the players are expected to play.
* `num_players` - Number of players.
* `game_turn` - The sequence of turn.
* `gameLog` -  A log of each players moves.
* `game_over` - True if the game is over (`err.WIN`, `err.DRAW`)
* `turn` - The player to play next

### Instantiate

```
game = xo ( M_rows, N_columns, K_players, symbols, play_order )
```

example :

```
game = xo( 3, 3, 2, [ 'X', 'O' ], [ 1, 2 ] )
```
This creates a 3 x 3 board for a 2 player game who use the symbols `X` and `O`. The order of playing is `player 1` followed by `player 2`.

### Reset game
```
game.reset()
```

### Mark a position
```
result = game.mark( position, player )
```

position starts from 0 to 8 in a 3 x 3 board as

```
0 | 1 | 2
--+---+---
3 | 4 | 5
--+---+---
6 | 7 | 8
```

The player is a number form 1 to K.

The return value `result` may be one of the enumerated value of class `err` -
```
err.OK
err.WIN
err.DRAW
err.INVALID_MOVE
err.OUT_OF_TURN
```

### Get board
```
game.get_board()
```
this returns a format string that may be printed to the console to represent a board.

### Check for winner
```
result = game.has_won(player)
```
checks if a player has won. This function manipulates the game state. This function is only meant to be called form within the xo class.

```
result = game.stateless_has_won(board, player)
```
Checks if player has won given the board state. This does not manipulate the game state. This is useful for an external player to evaluate hypothetical game situations.

The return value my be one of the following -
```
err.OK
err.WIN
err.DRAW
```

## Board class.
#### *Data*
* `board` -  an array to save  board positions.
* `free_positions` - The total number of unmarked squares.

### Instantiate

The board class may be instantiated as -

```
board_object = board(M_rows, N_columns, K_players, symbols)
```

This needs to only be instantiated by the xo class. It creates a M x N board.

### Reset board

```
board_object.reset()
```

This resets the board state.

### Get board subscripts

```
x,y = board_object.get_xy_from_pos(pos)
```
`x` and `y` are the subscripts of the board variable of the board class. This is required to manipulate boards to make hypothetical moves and evaluate them.

### Get board string
```
result = board_object.get_board_str()
```

The return value `result` is a printable formatted string representing the board.

## *err* class
The `err` class has the following values.

```
err.OK = 0
err.WIN = 1
err.DRAW = 2
err.OUT_OF_TURN = -1
err.INVALID_MOVE = -2
```
