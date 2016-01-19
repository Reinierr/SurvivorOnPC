import pygame
import os
import time
from Node import *
from Tile import *
from Constants import * 

pygame.init()
screen = pygame.display.set_mode(SIZE)

tilemap = Empty()
tilemap = Tile.Board(screen)
Iterate(tilemap, lambda x: x.Draw(screen))

pygame.display.update()

time.sleep(5)

def Main():
  #game loop
  print("<3")

Main()  