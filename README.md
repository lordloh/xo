# XO

A python class for a game of X and O.

## To use the class,
```
import xo
game=xo.xo();
```

## `game.showBoard()`
This displays -

```
  | X |  
0 | 0 | X
0 |   | X
```

## `game.setX(<posx>,<posy>)`
This sets 'X' at a certain position. If successful, returns 0; else -1

## `game.setO(<posx>,<posy>)`
This sets 'O' at a certain position. If successful, returns 0; else -1

## `game.won`
After a move, this variable will be `True` if the last player who played has won. Else, it is `False`.