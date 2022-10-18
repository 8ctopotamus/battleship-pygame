
from pprint import pprint
import pygame
import time
import random
import constants

icon = pygame.image.load('assets/images/icon.svg')
pygame.display.set_icon(icon)
pygame.display.set_caption("Battleship")
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
clock = pygame.time.Clock()

class Cell: 
  def __init__(self, x, y, value, visible=False):
    self.value = value # 0 = empty, 1 = ship, 2 = hit
    self.visible = visible
    self.hit = False
    self.x = x 
    self.y = y
    self.width = constants.COL_SIZE - 4
    self.height = constants.COL_SIZE - 4

  def drawHitMarker(self):
    pygame.draw.circle(screen, constants.WHITE, (self.x+self.width/2, self.y+self.height/2), 6)

  def draw(self, screen, color=constants.BLUE):
    if self.hit:
      self.drawHitMarker()
    else:
      pygame.draw.rect(screen, constants.BLUE, (self.x, self.y, self.width, self.height))
    if self.visible:
      if self.value != 0:
        color = constants.GREEN if self.value == 1 else constants.RED
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
      if self.hit:
        self.drawHitMarker()
  
  def takeDamage(self):
    self.visible = True
    self.hit = True
    if (self.value == 1):
      self.value = 2
      
class Player:
  shotsFired = []

  def __init__(self, grid):
    isHuman = isinstance(self, Human)
    offset = constants.HEIGHT / 2 if isHuman else 0
    visible = True if isHuman else False
    self.grid = [] # list(map(lambda row : list(map(lambda col : Cell(row[0], col[0], col[1]), enumerate(row[1]))), enumerate(grid)))
    for row in enumerate(grid):
      for col in enumerate(row[1]):
        self.grid.append(Cell(col[0]*constants.COL_SIZE + 1, (row[0]*constants.COL_SIZE)+offset+1, col[1], visible))
    
class Human(Player):
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

class Bot(Player):
  def __init__(self, grid):
    super().__init__(grid)
  
  def shoot(self, human):
    time.sleep(1)
    cell = random.choice(human.grid)
    cell.takeDamage()

def main():
  run = True
  FPS = 60
  human = Human([
    [1,1,1,0,0,0,0,0,0,1],
    [0,0,1,0,0,0,0,0,0,1],
    [0,0,1,0,0,0,0,0,0,1],
    [0,0,1,0,1,0,0,0,0,1],
    [0,0,1,0,1,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
  ])

  bot = Bot([
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,0,0,0],
  ])

  players = [human, bot]
  isHumansTurn = True    

  def drawUI():
    screen.fill(constants.BLUE_DARK)
    for player in players:
      for cell in player.grid:
        cell.draw(screen)  
    pygame.display.flip()

  while run:
    clock.tick(FPS)

    # handle inputs
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN and isHumansTurn:
        human.shoot(bot)
        isHumansTurn = False
      if event.type == pygame.QUIT:
        quit()
    
    drawUI()

    # bot shoot
    if not isHumansTurn:
      bot.shoot(human)
      isHumansTurn = True

  quit()

main()