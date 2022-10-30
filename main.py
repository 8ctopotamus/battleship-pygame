from pprint import pprint
import pygame
import constants
from classes.Game import Game
from classes.Menu import Menu

icon = pygame.image.load('assets/images/icon.svg')
pygame.display.set_icon(icon)
pygame.display.set_caption("Battleship")
pygame.font.init()

screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
clock = pygame.time.Clock()

screen.fill(constants.BLUE_DARK)

def main():
  Menu(screen, clock)
  Game(screen, clock)

  quit()

main()