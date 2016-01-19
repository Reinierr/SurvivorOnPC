import pygame
import os
import time
from Node import *
from Tile import *
from Constants import * 

pygame.init()
screen = pygame.display.set_mode(SIZE)

tilemap = Empty()
tilemap = Tile.Board()
Iterate(tilemap, lambda x: x.Draw(screen))

centerImage = pygame.image.load("Images\center.png")
screen.blit(pygame.transform.scale(centerImage, (10*TILESIZE,10*TILESIZE)),(OFFSET + (2*TILESIZE),2*TILESIZE))

pygame.display.update()

time.sleep(5)

def Main():
  #game loop
  print("<3")

Main()  