from Node import *
from Player import *
from Board import *
#from SurvivorOnPC import *

def PlayerList(colornumber):
  players = Empty()
  tilemap = CreateMap()
  playeramount = len(colornumber)
  playeramount = len(colornumber)
  while playeramount != 0:
    players = Node(Player( tilemap, colornumber[playeramount-1]),players)
    players
    playeramount -= 1

#  for c in colornumber:
#    players = Node(Player(tilemap,c),players)
  return players

def PlayerMove():
  return empty

def SuperFighter(player):
    # ROW 6 / COL 12
    return player.Tile.Position.Row

def ScoreMenu(screen, players):
    ls = LINE_OFFSET
    playlist = players
    playcount = 0
    while not playlist.IsEmpty:
        playcount = playcount + 1
        ls = ls + (LINE_OFFSET*3)
        playcol = FONT_TEXT.render('Player '+str(playcount), 1, FONT_COLOR_TEXT) 
        hp = FONT_TEXT.render('HP: '+str(playlist.Value.Life), 1, FONT_COLOR_TEXT) 
        cp = FONT_TEXT.render('CP: '+str(playlist.Value.Condition), 1, FONT_COLOR_TEXT)
        items = [playcol, hp, cp]
        for v,i in enumerate(items):
            screen.blit(i,(SIZE[0] / 10, SIZE[1] / 10 + ls + v*20))
        playlist = playlist.Tail