import pygame
import constants
from classes.Game import Game
from classes.Menu import Menu

icon = pygame.image.load('assets/images/icon.svg')
pygame.display.set_icon(icon)
pygame.display.set_caption("Battleship")

screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
clock = pygame.time.Clock()

def main():
  menu = Menu(screen, clock)  
  game = Game(screen, clock)

  quit()

main()