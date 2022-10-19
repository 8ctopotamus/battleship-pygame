import time
import random
from classes.Player import Player

class Bot(Player):
  def __init__(self, grid):
    super().__init__(grid, False)
  
  def shoot(self, human):
    time.sleep(1)
    cell = random.choice(human.grid)
    cell.takeDamage()