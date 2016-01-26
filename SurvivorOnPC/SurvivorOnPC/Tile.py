import pygame
from Constants import *
from Node import *
 
#VECTOR2 CLASS
class Vector2:
  def __init__(self, x, y):
    self.X = x
    self.Y = y

class Vector2RC:
  def __init__(self, col, row):
    self.Col = col
    self.Row = row

class Tile:
  def __init__(self, pos, color, index =None):
    self.Position = pos
    self.Color = color
    self.Index = index

  def Draw(self, screen):
    pygame.draw.rect(screen, self.Color, (self.Position.Col * TILESIZE, self.Position.Row * TILESIZE, TILESIZE,TILESIZE))

  def Color(column,row):
    if(column < 6 or column > 19):
      return BLACK
    elif(column in [6,7,8] and row in [0,1,2]):
      return BLUE
    elif(column in [17,18,19] and row in [0,1,2]):
      return RED
    elif(column in [6,7,8] and row in [11,12,13]):
      return YELLOW
    elif(column in [17,18,19] and row in [11,12,13]):
      return GREEN
    elif(column in [9,11,14,16] or row in [3,5,8,10]):
      return GREY
    elif(column in [10,12,13,15] or row in [4,6,7,9]):
      return WHITE
    else:
      return BLACK