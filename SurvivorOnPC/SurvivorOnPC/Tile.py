import pygame


#VECTOR2 CLASS
class Vector2:
  def __init__(self, x, y):
    self.X = x
    self.Y = y

class Tile:
  def __init__(self, pos, color):
    self.Position = pos
    self.Color = color