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
    self.value = value
    self.visible = visible
    self.x = x 
    self.y = y

  def draw(self, screen, color=BLUE):
    if self.visible and self.value != 0:
      color = GREEN if self.value == 1 else RED
      pygame.draw.rect(screen, color, (self.x, self.y, COL_SIZE - 4, COL_SIZE - 4)) 

class Player:
  shotsFired = []
  
  def __init__(self, grid):
    self.grid = [] # list(map(lambda row : list(map(lambda col : Cell(row[0], col[0], col[1]), enumerate(row[1]))), enumerate(grid)))
    isHuman = isinstance(self, Human)
    offset = HEIGHT / 2 if isHuman else 0
    visible = True if isHuman else 0
    for row in enumerate(grid):
      for col in enumerate(row[1]):
        self.grid.append(Cell(col[0]*COL_SIZE + 1, (row[0]*COL_SIZE)+offset+1, col[1], visible))
    
class Human(Player):
  def __init__(self, grid):
    super().__init__(grid)

class Bot(Player):
  def __init__(self, grid):
    super().__init__(grid)

def handleInputs():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      x, y = pygame.mouse.get_pos();
      print(x)
      print(y)

def renderGUI(screen, players):
  screen.fill(BLUE)
  for player in players:
    for cell in player.grid:
      cell.draw(screen)  
  pygame.display.flip()

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
    renderGUI(screen, players)
    handleInputs()
    pygame.display.update()
  
  quit()

main()