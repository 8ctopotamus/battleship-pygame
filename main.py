from pprint import pprint
import pygame
import time
import random

WIDTH, HEIGHT = 400, 800
COL_SIZE = WIDTH / 10
BLUE = (44, 73, 127)
BLUE_LIGHT = (188, 210, 238)
RED = (219, 48, 105)
WHITE = (251,252,255)
GREEN = (106, 141, 115)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Battleship")

class Cell: 
  def __init__(self, x, y, value, visible=False):
    self.value = value # 0 = empty, 1 = ship, 2 = hit
    self.visible = visible
    self.hit = False
    self.x = x 
    self.y = y
    self.width = COL_SIZE - 4
    self.height = COL_SIZE - 4

  def draw(self, screen, color=BLUE):
    if self.visible:
      if self.value != 0:
        color = GREEN if self.value == 1 else RED
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
      if self.hit:
        pygame.draw.circle(screen, WHITE, (self.x+self.width/2, self.y+self.height/2), 10)

class Player:
  shotsFired = []
  
  def __init__(self, grid):
    isHuman = isinstance(self, Human)
    offset = HEIGHT / 2 if isHuman else 0
    visible = True if isHuman else False
    self.grid = [] # list(map(lambda row : list(map(lambda col : Cell(row[0], col[0], col[1]), enumerate(row[1]))), enumerate(grid)))
    for row in enumerate(grid):
      for col in enumerate(row[1]):
        self.grid.append(Cell(col[0]*COL_SIZE + 1, (row[0]*COL_SIZE)+offset+1, col[1], visible))
    
class Human(Player):
  def __init__(self, grid):
    super().__init__(grid)
  
  def shoot(self, bot):
    x, y = pygame.mouse.get_pos();
    print(x)
    print(y)
    for cell in bot.grid:
      if (cell.x >= x and cell.y >= y):
        pprint(vars(cell))
        cell.visible = True
        cell.hit = True
        if (cell.value == 1):
          cell.value = 2
        break

class Bot(Player):
  def __init__(self, grid):
    super().__init__(grid)

def handleInputs(human, bot):
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      human.shoot(bot)
    if event.type == pygame.QUIT:
      quit()

def renderGUI(screen, players):
  screen.fill(BLUE)
  for player in players:
    for cell in player.grid:
      cell.draw(screen)  
  # pygame.display.flip()
  pygame.display.update()

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

  while run:
    clock.tick(FPS)
    handleInputs(human, bot)
    renderGUI(screen, players)
  
  quit()

main()