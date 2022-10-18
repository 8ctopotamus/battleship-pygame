from pprint import pprint
import pygame
import time
import random

WIDTH, HEIGHT = 300, 800
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
  def __init__(self, rowIdx, colIdx, value):
    self.value = value
    self.visible = False
    self.coords = { 
      "x": colIdx*COL_SIZE + 1, 
      "y": rowIdx*COL_SIZE 
    }
  
  def draw(self, screen, color, coords):
    if self.visible:
      pygame.draw.rect(screen, color, (coords.x, coords.y, COL_SIZE - 4, COL_SIZE - 4)) 

class Player:
  def __init__(self, grid):
    # TODO: randomly generate grid if none passed in
    self.grid = list(map(lambda row : list(map(lambda col : Cell(row[0], col[0], col[1]), enumerate(row[1]))), enumerate(grid)))
    self.shotsFired = []
    
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
  # for player in players:
  #   for i in range(len(player.grid)):
  #     row = player.grid[i]
  #     for j in range(len(row)):
  #       screenOffset = 0
  #       col = row[j] 
  #       if (col != 0):
  #         if isinstance(player, Human):
  #           screenOffset = HEIGHT / 2
  #         color = GREEN if col == 1 else RED
  #         pygame.draw.rect(screen, color, (j*COL_SIZE + 1, (i*COL_SIZE)+screenOffset+1, COL_SIZE - 4, COL_SIZE - 4))    
  pygame.display.flip()

def main():
  run = True
  FPS = 60
  human = Human([
    [1,1,1,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0],
    [0,0,1,0,1,0,0,0,0,0],
    [0,0,1,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
  ])

  bot = Bot([
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
  ])

  players = [human, bot]
  pprint(vars(human))
  # pprint(vars(bot))
  # pprint(players)

  # while run:
  #   clock.tick(FPS)
  #   renderGUI(screen, players)
  #   handleInputs()
  #   pygame.display.update()
  
  quit()

main()