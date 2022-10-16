import os
import pygame
import os
import time
import random

pygame.display.set_caption("Battleship")

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# square_size = WIDTH / 10

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
    for row in player.map:
      for col in row:
        pygame.draw.rect(screen, (255,0,0), (100, 100, 100, 100))

def main():
  run = True
  FPS = 60
  
  human = Human([
    [1,1,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,1],
    [0,0,1,0,1],
  ])

  bot = Bot([
    [0,1,0,0,0],
    [0,1,0,0,0],
    [0,1,0,1,1],
    [0,1,0,0,0],
    [0,0,1,1,1],
  ])

  players = [human, bot]

  while run:
    clock.tick(FPS)
    renderGUI(players)
    handleInputs()
    pygame.display.update()
  
  quit()

main()