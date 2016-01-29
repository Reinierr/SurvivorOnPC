import random
from Cards import *
from Node import *
import math

def AI(player, dice):
  home = player.Home
  index = player.Tile.Index
  condition = player.Condition
  
  if index > home:
    distance = home + 40 - index
  elif index <= home:
    distance = home - index

