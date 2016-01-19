import pygame
from Constants import *
 
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