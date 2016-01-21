import pygame
from Node import *
from Constants import *

class Player:
  def __init__(self,position,texture):
    self.Position = position
    self.Texture = texture