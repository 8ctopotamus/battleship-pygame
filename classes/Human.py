import pygame
import classes.Player

class Human(classes.Player):
  def __init__(self, grid):
    super().__init__(grid)
  
  def shoot(self, bot):
    x, y = pygame.mouse.get_pos();
    targetCell = None
    for cell in bot.grid:
      if (cell.x + cell.width >= x and cell.y + cell.height >= y):
        targetCell = cell
        break
    if targetCell:
      targetCell.takeDamage()