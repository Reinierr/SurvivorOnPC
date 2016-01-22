﻿import pygame
from Node import *
from Constants import *

class Player:
  def __init__(self,tilemap,color):
    self.Texture = pygame.transform.scale(pygame.image.load("Images\glove_" + color + ".png"), (TILESIZE,TILESIZE))
    self.Life = 100
    self.Condition = 15
    self.Home = any(h['color'] == color for h in HOMETILES)
    self.Tile = tilemap.Filter(lambda x: x.Index == newIndex).Value

  def Move(self,tilemap,steps):
    newIndex = (self.Tile.Index + steps)
    if self.Home in range(self.Tile.Index + 1, newIndex + 1): #if player passes own corner, replenish condition to 15
      self.Condition = 15
    
    newIndex %= 40
      
    if newIndex == self.Home: #if player lands on own corner, increment life by 10
      self.Life = self.Life + 10
      if self.Life > 100:
        self.Life = 100
    
    newTile = Empty()
    newTile = tilemap.Filter(lambda x: x.Index == newIndex)
    self.Tile = newTile.Value
    
  def Draw(self, screen):
    screen.blit(self.Texture, (self.Tile.Position.Col*TILESIZE, self.Tile.Postion.Row*TILESIZE))
    