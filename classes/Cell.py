import pygame
import constants

class Cell: 
  def __init__(self, x, y, value, visible=False):
    self.value = value # 0 = empty, 1 = ship, 2 = hit
    self.visible = visible
    self.hit = False
    self.x = x 
    self.y = y
    self.width = constants.COL_SIZE - 4
    self.height = constants.COL_SIZE - 4

  def drawHitMarker(self, screen):
    pygame.draw.circle(screen, constants.WHITE, (self.x+self.width/2, self.y+self.height/2), 6)

  def draw(self, screen, color=constants.BLUE):
    if self.hit:
      self.drawHitMarker(screen)
    else:
      pygame.draw.rect(screen, constants.BLUE, (self.x, self.y, self.width, self.height))
    if self.visible:
      if self.value != 0:
        color = constants.GREEN if self.value == 1 else constants.RED
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
      if self.hit:
        self.drawHitMarker(screen)

  def takeDamage(self):
    self.visible = True
    self.hit = True
    if (self.value == 1):
      self.value = 2