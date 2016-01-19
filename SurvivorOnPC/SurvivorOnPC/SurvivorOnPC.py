import pygame
import os
import time
from Node import *
from Tile import *
from Constants import * 

pygame.init()
screen = pygame.display.set_mode(SIZE)

def Color(column,row):
  grey = [3,5,8,10]
  white = [4,6,7,9]
  if(column in [0,1,2] and row in [0,1,2]):
    return BLUE
  elif(column in [11,12,13] and row in [0,1,2]):
    return RED
  elif(column in [0,1,2] and row in [11,12,13]):
    return YELLOW
  elif(column in [11,12,13] and row in [11,12,13]):
    return GREEN
  elif(column in grey or row in grey):
    return GREY
  elif(column in white or row in white):
    return WHITE
  else:
    return BLACK

tilemap = Empty()
#for row in range(MAPSIZE):
#  for column in range(MAPSIZE):
#    tilemap = Node(Tile(Vector2(OFFSET+(column*TILESIZE),row*TILESIZE),Color(column,row)),tilemap)
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