class Player:
  def __init__(self, isHuman=False):
    self.isHuman = isHuman
    self.grid = []

  def isAlive(self):
    return any( list( map(lambda cell : cell.value == 1, self.grid) ) )