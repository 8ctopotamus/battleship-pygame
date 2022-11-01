from pprint import pprint
import time
import random
from classes.Player import Player

class Bot(Player):
  shotsFired = []

  def __init__(self):
    super().__init__(False)

  def shoot(self, human):
    time.sleep(1)
    
    # print('Last shot')
    # pprint(self.shotsFired[len(self.shotsFired) - 1].value)
    
    cell = random.choice(human.grid)
    
    
    cell.takeDamage()
    self.shotsFired.append(cell)
