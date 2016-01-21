import pygame
from Node import *
from Constants import *

class ScoreCard:
  def __init__(self,name,color,dice_score,damage,condition):
    self.Name = name
    self.Color = color
    self.Dice_score = dice_score
    self.Damage = damage
    self.Condition = condition

class SuperFightCard:
  def __init__(self,name,dice_score,damage):
    self.Name = name
    self.Dice_score = dice_score
    self.Damage = damage