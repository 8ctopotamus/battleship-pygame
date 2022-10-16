import os
import pygame
import os
import time
import random

WIDTH, HEIGHT = 500, 1000
COL_SIZE = WIDTH / 10
BLUE = (18, 11, 139)
RED = (155, 29, 43)
WHITE = (255,255,255)
GREY = (200,200,200)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Battleship")

class Player:
  def __init__(self, map):
    # TODO: randomly generate map if none passed in
    self.map = map
    self.shotsFired = []

class Human(Player):
  def __init__(self, map):
    super().__init__(map)

class Bot(Player):
  def __init__(self, map):
    super().__init__(map)

def handleInputs():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()

def renderGUI(players):
  for player in players:
    for i in range(len(player.map)):
      row = player.map[i]
      for j in range(len(row)):
        offset = 0
        col = row[j] 
        color = BLUE
        if col == 1:
          color = GREY          
        if col == 2:
          color = RED
        if isinstance(player, Human):
          offset = HEIGHT / 2
        
        pygame.draw.rect(screen, color, (j*COL_SIZE, (i*COL_SIZE)+offset, COL_SIZE, COL_SIZE))

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

  while run:
    clock.tick(FPS)
    renderGUI(players)
    handleInputs()
    pygame.display.update()
  
  quit()

main()