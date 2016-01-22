import pygame
from Node import *
from Constants import *

class Player:
  def __init__(self,position,texture):
    self.Tile = position
    self.Texture = texture
    self.Life = 100
    self.Condition = 15

  def Move(self,tilemap,steps):
    newIndex = self.Tile.Index + steps
    newTile = tilemap.Filter(lambda x: x.Index == newIndex)
    self.Tile = newTile.Value
  def Move(self,steps):
    




  def Draw(self, screen):
    pygame.image.load(self.Texture)
