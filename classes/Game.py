import pygame
from random import choice
from random import choice
from classes.Cell import Cell
from classes.Human import Human
from classes.Bot import Bot
import constants

class Game:
  def __init__(self, screen, clock, onGameOver):
    self.screen = screen
    self.clock = clock
    self.isHumansTurn = choice([True, False])
    self.running = False
    self.onGameOver = onGameOver
    self.human = Human()
    self.bot = Bot()
    self.generateGrid(self.human)
    self.generateGrid(self.bot)
    self.players = [self.human, self.bot]
    self.run()
  
  def run(self):
    self.screen.fill(constants.BLUE_DARK)
    self.running = True 
    while self.running:
      self.clock.tick(constants.FPS)

      # handle inputs
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and self.isHumansTurn:
          self.human.shoot(self.bot)
          self.isHumansTurn = False
        if event.type == pygame.QUIT:
          self.running = False
          quit()
      
      self.drawUI()

      # bot shoot
      if not self.isHumansTurn:
        self.bot.shoot(self.human)
        self.isHumansTurn = True

      # check for game over
      if not self.human.isAlive() or not self.bot.isAlive():
        self.running = False
        self.onGameOver()

  def drawUI(self):
    for player in self.players:
      for cell in player.grid:
        # TODO: mouse hover
        # if player.isHuman
          # (x, y) = get mouse pos
          # if mouse is over cell
            # draw it darker shade
        cell.draw(self.screen)
    pygame.display.flip()

  def generateGrid(self, player):
    # print("Generating %s grid..." % ("Humans" if player.isHuman else "Bot's"))
    grid = list( map(lambda _ : [0]*10, range(10)) )
    for size in [5,4,3,3,2]:
      processing = True
      # search for a space to put the ship
      while processing:
        # print("Working on ship size % s" % size)
        ship = [] # [[0, 0], [0, 1], [0, 2], [x, y]]
        attempts = 0
        # find an empty cell to start
        startRowIdx = choice(range(10))
        startColIdx = choice(range(10))
        vert = choice([True, False])
        # if start cell is available
        if grid[startRowIdx][startColIdx] == 0:
          ship.append([startRowIdx, startColIdx])
          while len(ship) < size and not attempts >= size:
            (prevHeadX, prevHeadY) = ship[0]
            (prevTailX, prevTailY) = ship[len(ship) - 1] 
            # print("prevTailX: %s prevTailY: %s" % (prevTailX, prevTailY))
            if vert:
              if prevHeadY - 1 > 0:
                ship.insert(0, [prevTailX, prevTailY - 1])
              # check below
              if (prevTailY + 1) < len(ship):
                ship.append([prevTailX, prevTailY + 1])
            else:
              # check left
              if prevHeadX - 1 > 0:
                ship.insert(0, [prevTailX - 1, prevTailY])
              # check right
              if (prevTailX + 1) < len(grid[startRowIdx]):
                ship.append([prevTailX + 1, prevTailY])
            attempts += 1
            # pprint(ship)
        # draw ship
        for (x, y) in ship:
          grid[y][x] = 1
        processing = False
    # Create cells based on grid
    visible = True if player.isHuman else False
    offset = constants.HEIGHT / 2 if player.isHuman else 0
    for row in enumerate(grid):
      for col in enumerate(row[1]):
        player.grid.append(Cell(col[0]*constants.COL_SIZE + 1, (row[0]*constants.COL_SIZE)+offset+1, col[1], visible))
  