from random import choice
from pprint import pprint

grid = list( map(lambda _ : [0]*10, range(10)) )
for size in [5,4,3,3,2]:
  processing = True
  vert = choice([True, False])
  # search for a space to put the ship
  while processing:
    # find an empty cell to start
    startRowIdx = choice(range(10))
    startColIdx = choice(range(10))
    if grid[startRowIdx][startColIdx] == 0:
      grid[startRowIdx][startColIdx] = 1
      processing = False

pprint(grid)