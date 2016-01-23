from Node import *
from Player import *
from Board import *
#from SurvivorOnPC import *

def PlayerList(playeramount, colornumber):
  players = Empty()
  while playeramount != 0:
    tilemap = CreateMap()
    tilemap
    players = Node(Player( tilemap, colornumber),players)
    playeramount -= 1

#  for c in colornumber:
#    players = Node(Player(tilemap,c),players)
  return players

def PlayerMove():
  return empty