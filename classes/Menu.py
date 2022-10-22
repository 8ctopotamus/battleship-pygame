import pygame
import constants

class Menu:
  running = True

  def __init__(self, screen, clock):
    self.screen = screen
    self.clock = clock

  def run(self):
    while self.running:
      self.clock.tick(constants.FPS)
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()