import pygame
from Node import *
from Constants import *

class Player:
  def __init__(self,position,texture):
    self.Tile = position
    self.Texture = pygame.transform.scale(pygame.image.load("Images\\" + texture + ".png"), (TILESIZE,TILESIZE))
    self.Life = 100
    self.Condition = 15

  def Move(self,tilemap,steps):
    newIndex = self.Tile.Index + steps
    newTile = tilemap.Filter(lambda x: x.Index == newIndex)
    self.Tile = newTile.Value
    
  def Draw(self, screen):
    screen.blit(self.Texture, (self.Tile.Position.Col*TILESIZE, self.Tile.Postion.Row*TILESIZE))
    