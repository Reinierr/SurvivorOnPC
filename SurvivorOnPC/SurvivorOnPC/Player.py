import pygame
from Node import *
from Constants import *
from Tile import *

class Player:
  def __init__(self,position,texture):
    self.Position = position
    self.Texture = texture

  def Move(self,steps):
    




  def Draw(self, screen):
    pygame.image.load(self.Texture)