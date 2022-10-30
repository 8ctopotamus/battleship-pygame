import pygame
import constants

class Menu:
  def __init__(self, screen, clock):
    self.screen = screen
    self.clock = clock
    self.running = True
    self.largeFont = pygame.font.SysFont('impact', 65)
    self.smallFont = pygame.font.SysFont('impact', 45)
    self.run()
  
  def run(self):
    titleText = self.largeFont.render('BATTLESHIP', False, (255,255,255))
    quitText = self.smallFont.render("QUIT", False, (255,255,255))

    while self.running:
      self.clock.tick(constants.FPS)
      
      self.screen.blit(titleText, (constants.WIDTH // 2 - titleText.get_width() // 2, constants.HEIGHT // 2))
      self.screen.blit(quitText, (constants.WIDTH//2-quitText.get_width()//2, constants.HEIGHT//2 + titleText.get_height() + 50))
      
      (x, y) = pygame.mouse.get_pos()

      # for event in pygame.event.get():
      #   if event.type == pygame.MOUSEBUTTONDOWN:

          # self.running = False
        # if event.type == pygame.QUIT:
        #   quit()
      
      pygame.display.flip()
