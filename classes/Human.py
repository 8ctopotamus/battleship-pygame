import pygame
from classes.Player import Player

class Human(Player):
  def __init__(self):
    super().__init__(True)
  
  def shoot(self, bot):
    x, y = pygame.mouse.get_pos();
    targetCell = None
    for cell in bot.grid:
      if (cell.x + cell.width >= x and cell.y + cell.height >= y):
        targetCell = cell
        break
    if targetCell:
      targetCell.takeDamage()