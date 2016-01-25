from Node import *
from Player import *
from Board import *
#from SurvivorOnPC import *

def PlayerList(colornumber):
  players = Empty()
  tilemap = CreateMap()
  playeramount = len(colornumber)
  newtile = IndexFix(tilemap)
  playeramount = len(colornumber)
  newtile
  while playeramount != 0:
    players = Node(Player( tilemap, colornumber[playeramount-1]),players)
    playeramount -= 1

#  for c in colornumber:
#    players = Node(Player(tilemap,c),players)
  return players

def PlayerMove():
  return empty