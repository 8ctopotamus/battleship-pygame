import os
import pygame
import os
import time
import random

pygame.display.set_caption("Battleship")

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

square_size = WIDTH / 10

def main():
  run = True
  FPS = 60
  
  while run:
    clock.tick(FPS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    pygame.draw.rect(screen, (0,0,0), (100, 100, 100, 100))
    pygame.display.update()
  
  pygame.quit()

main()