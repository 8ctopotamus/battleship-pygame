import pygame
import constants

class Menu:
  def __init__(self, screen, clock, onClose):
    self.screen = screen
    self.clock = clock
    self.running = True
    self.onClose = onClose
    self.largeFont = pygame.font.SysFont('impact', 65)
    self.smallFont = pygame.font.SysFont('impact', 45)
    self.run()
  
  def run(self):
    titleText = self.largeFont.render('BATTLESHIP', False, (255,255,255))
    
    while self.running:
      self.clock.tick(constants.FPS)
      
      self.screen.blit(titleText, (constants.WIDTH // 2 - titleText.get_width() // 2, constants.HEIGHT // 2 - titleText.get_height() // 2))
      
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
          self.running = False
          self.onClose()
        if event.type == pygame.QUIT:
          quit()
      
      pygame.display.flip()
