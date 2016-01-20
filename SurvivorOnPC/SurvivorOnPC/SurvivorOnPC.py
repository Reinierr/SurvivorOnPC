import pygame
import os
import time
from Node import *
from Tile import *
from Constants import * 
from Board import *

pygame.init()
screen = pygame.display.set_mode(SIZE)

tilemap = Empty()
tilemap = Board.CreateMap()
Iterate(tilemap, lambda x: x.Draw(screen))
Board.DrawImages(screen)

pygame.display.update()

time.sleep(5)

def Main():
  #game loop
  print("<3")

Main()  