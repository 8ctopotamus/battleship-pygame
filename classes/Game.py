import pygame
from random import choice
from classes.Human import Human
from classes.Bot import Bot
import constants

class Game:
  def __init__(self, screen, clock):
    self.screen = screen
    self.clock = clock
    self.human = Human()
    self.bot = Bot()
    self.players = [self.human, self.bot]
    self.isHumansTurn = choice(True, False)
    self.running = False
  
  def run(self):
    running = True 
    while running:
      self.clock.tick(constants.FPS)

      # handle inputs
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and isHumansTurn:
          self.human.shoot(self.bot)
          isHumansTurn = False
        if event.type == pygame.QUIT:
          quit()
      
      self.drawUI()

      # bot shoot
      if not isHumansTurn:
        self.bot.shoot(self.human)
        isHumansTurn = True

      # check for game over
      if not self.human.isAlive() or not self.bot.isAlive():
        running = False

  def drawUI(self):
    self.screen.fill(constants.BLUE_DARK)
    for player in self.players:
      for cell in player.grid:
        cell.draw(self.screen)  
    pygame.display.flip()

  