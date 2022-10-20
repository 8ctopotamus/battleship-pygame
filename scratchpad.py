from random import choice
from pprint import pprint

grid = list( map(lambda _ : [0]*10, range(10)) )

pprint(grid)

for size in [5,4,3,3,2]:
  print(choice(grid))
