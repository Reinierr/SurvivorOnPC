from Node import *
from Player import *
#from SurvivorOnPC import *

def PlayerList(playeramount, colornumber):
  
  players = Empty()
#  while player != 0:
#    players = Node(Player( tilemap, colornumber),players)
#    playeramount -= 1

  for c in colornumber:
    players = Node(Player(tilemap,c),players)

  return players

def PlayerMove():
  return empty