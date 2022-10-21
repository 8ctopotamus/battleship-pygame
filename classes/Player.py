from random import choice
import constants
from classes.Cell import Cell
from pprint import pprint

class Player:
  shotsFired = []

  def __init__(self, isHuman=False):
    self.isHuman = isHuman
    self.grid = []
    self.generateGrid()    

  def generateGrid(self):
    grid = list( map(lambda _ : [0]*10, range(10)) )
    for size in [5,4,3,3,2]:
      processing = True
      # search for a space to put the ship
      while processing:
        # print("Working on ship size % s" % size)
        ship = [] # [[0, 0], [0, 1], [0, 2], [x, y]]
        attempts = 0
        # find an empty cell to start
        startRowIdx = choice(range(10))
        startColIdx = choice(range(10))
        vert = choice([True, False])
        # if start cell is available
        if grid[startRowIdx][startColIdx] == 0:
          ship.append([startRowIdx, startColIdx])
          while len(ship) < size and not attempts >= size:
            (prevX, prevY) = ship[len(ship) - 1] 
            # print("prevX: %s prevY: %s" % (prevX, prevY))
            if vert:
              if prevY - 1 > 0:
                ship.append([prevX, prevY - 1])
              # check below
              if (prevY + 1) < len(ship):
                ship.append([prevX, prevY + 1])
            else:
              # check left
              if prevX - 1 > 0:
                ship.append([prevX - 1, prevY])
              # check right
              if (prevX + 1) < len(grid[startRowIdx]):
                ship.append([prevX + 1, prevY])
            attempts += 1
        # draw ship
        for (x, y) in ship:
          grid[y][x] = 1
        processing = False
    # Create cells based on grid
    visible = True if self.isHuman else False
    offset = constants.HEIGHT / 2 if self.isHuman else 0
    for row in enumerate(grid):
      for col in enumerate(row[1]):
        self.grid.append(Cell(col[0]*constants.COL_SIZE + 1, (row[0]*constants.COL_SIZE)+offset+1, col[1], visible))