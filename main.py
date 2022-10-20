import pygame
import constants
from classes.Human import Human
from classes.Bot import Bot

icon = pygame.image.load('assets/images/icon.svg')
pygame.display.set_icon(icon)
pygame.display.set_caption("Battleship")
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
clock = pygame.time.Clock()
    
def main():
  run = True
  FPS = 60

  human = Human([
    [0,0,0,0,0,0,0,0,0,1],
    [0,0,1,1,1,1,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,1,0,0,1],
    [0,0,0,0,0,0,1,0,0,1],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
  ])

  bot = Bot([
    [0,1,0,0,0,0,1,1,1,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,0,0,0],
  ])

  players = [human, bot]
  isHumansTurn = True    

  def drawUI():
    screen.fill(constants.BLUE_DARK)
    for player in players:
      for cell in player.grid:
        cell.draw(screen)  
    pygame.display.flip()

  while run:
    clock.tick(FPS)

    # handle inputs
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN and isHumansTurn:
        human.shoot(bot)
        isHumansTurn = False
      if event.type == pygame.QUIT:
        quit()
    
    drawUI()

    # bot shoot
    if not isHumansTurn:
      bot.shoot(human)
      isHumansTurn = True

    # TODO: check for game over

  quit()

main()