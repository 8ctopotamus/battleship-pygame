import constants
import classes.Human
import classes.Cell

class Player:
  shotsFired = []

  def __init__(self, grid):
    isHuman = isinstance(self, classes.Human)
    offset = constants.HEIGHT / 2 if isHuman else 0
    visible = True if isHuman else False
    self.grid = [] # list(map(lambda row : list(map(lambda col : Cell(row[0], col[0], col[1]), enumerate(row[1]))), enumerate(grid)))
    for row in enumerate(grid):
      for col in enumerate(row[1]):
        self.grid.append(classes.Cell(col[0]*constants.COL_SIZE + 1, (row[0]*constants.COL_SIZE)+offset+1, col[1], visible))