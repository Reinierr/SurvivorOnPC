import pygame
from Constants import *
from Node import *
 
#VECTOR2 CLASS
class Vector2:
  def __init__(self, x, y):
    self.X = x
    self.Y = y

class Tile:
  def __init__(self, pos, color):
    self.Position = pos
    self.Color = color
    self.Up = None
    self.Down = None
    self.Right = None
    self.Left = None



  def Draw(self, screen):
    if self.Up == None:
      pygame.draw.rect(screen, self.Color, (self.Position.X , self.Position.Y, TILESIZE,TILESIZE))
    if self.Down == None:
      pygame.draw.rect(screen, self.Color, (self.Position.X , self.Position.Y, TILESIZE,TILESIZE))
    if self.Right == None:
      pygame.draw.rect(screen, self.Color, (self.Position.X , self.Position.Y, TILESIZE,TILESIZE))
    if self.Left == None:
      pygame.draw.rect(screen, self.Color, (self.Position.X , self.Position.Y, TILESIZE,TILESIZE))

    if self.Up != None:
      self.Up.Draw(screen)
    if self.Down != None:
      self.Down.Draw(screen)
    if self.Left != None:
      self.Left.Draw(screen)
    if self.Right != None:
      self.Right.Draw(screen)

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