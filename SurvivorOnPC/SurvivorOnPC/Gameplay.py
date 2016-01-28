import pygame, math, time
from Node import *
from Player import *
from Board import *
from Cards import *
#from SurvivorOnPC import *

pygame.init()

def PlayerList(colornumber):
  players = Empty()
  tilemap = CreateMap()
  playeramount = len(colornumber)
  while playeramount != 0:
      if playeramount -1 == 0:  #len(colornumber):
         players = Node(Player( tilemap, colornumber[playeramount-1]),players)
         players.Value.Turn = True
         players.Value.Number = playeramount
      else:
         players = Node(Player( tilemap, colornumber[playeramount-1]),players)
         players.Value.Number = playeramount 
      players
      playeramount -= 1
  return players

def ScoreMenu(screen, players):
    ls = LINE_OFFSET
    playlist = players
    pygame.draw.rect(screen, BLACK, (SIZE[0] / 10, SIZE[1] / 10,100,500))
    while not playlist.IsEmpty:
        ls = ls + (LINE_OFFSET*3)
        if playlist.Value.Life < 0:
            playlist.Value.Life = 0
            
        playcol = FONT_TEXT.render('Player '+str(playlist.Value.Number), 1, FONT_COLOR_TEXT) 
        hp = FONT_TEXT.render('LP: '+str(playlist.Value.Life), 1, FONT_COLOR_TEXT) 
        cp = FONT_TEXT.render('CP: '+str(playlist.Value.Condition), 1, FONT_COLOR_TEXT)
        items = [playcol, hp, cp]
        for v,i in enumerate(items):
            screen.blit(i,(SIZE[0] / 10, SIZE[1] / 10 + ls + v*20))
        playlist = playlist.Tail

def CheckPlayers(screen, players):
    ls = LINE_OFFSET
    playlist = players
    pygame.draw.rect(screen, BLACK, (SIZE[0] / 10, SIZE[1] / 10,100,200))
    for i,v in enumerate(playlist):
        ls = ls + LINE_OFFSET
        if int(v) == 0:
            playcol = FONT_TEXT.render('Player '+str(i + 1), 1, BLUE) 
        elif int(v) == 1:
            playcol = FONT_TEXT.render('Player '+str(i + 1), 1, RED) 
        elif int(v) == 2:
            playcol = FONT_TEXT.render('Player '+str(i + 1), 1, GREEN) 
        elif int(v) == 3:
            playcol = FONT_TEXT.render('Player '+str(i + 1), 1, YELLOW)
        if int(v) > -1:
            screen.blit(playcol,(SIZE[0] / 10, SIZE[1] / 10 + ls))

def ResetMap(screen, players):
  resetmap = CreateMap()
  resetmap.Iterate(lambda x: x.Draw(screen))
  DrawImages(screen)
  ScoreMenu(screen, players)
  pygame.draw.rect(screen, BLACK, (0,TILESIZE*14 , TILESIZE*6,height-TILESIZE*14))

def playerturn(screen, players, dicenumber):
    newplayer = players
    colors = [BLUE, RED, GREEN, YELLOW]
    while not players.IsEmpty:
        if players.Value.Life != 0:
            if players.Value.Turn:
                playerlabel = FONT_TEXT.render('Current turn: Player '+str(players.Value.Number), 1, colors[int(math.floor(players.Value.Home)/10)])
                screen.blit(playerlabel,(0, SIZE[1] - 25))
                #-Turn player starts-#
                players.Value.Move(CreateMap(),dicenumber)
        else:
            endplayerturn(screen, newplayer)
        players = players.Tail
def endplayerturn(screen, players):
    newplayer = players
    colors = [BLUE, RED, GREEN, YELLOW]
    while not players.IsEmpty:
        if players.Value.Turn:
            players.Value.Turn = False
            #-Turn player ends-#
            if not players.Tail.IsEmpty:
                players.Tail.Value.Turn = True
                playerlabel = FONT_TEXT.render('Current turn: Player '+str(players.Tail.Value.Number), 1, colors[int(math.floor(players.Tail.Value.Home)/10)])
                tempwidth = playerlabel.get_rect().width
                pygame.draw.rect(screen, BLACK, (0, SIZE[1] - 25 , tempwidth,SIZE[1]- 25))
                screen.blit(playerlabel,(0, SIZE[1] - 25))
                return players
            else:
                newplayer.Value.Turn = True
                playerlabel = FONT_TEXT.render('Current turn: Player '+str(newplayer.Value.Number), 1, colors[int(math.floor(newplayer.Value.Home)/10)])
                tempwidth = playerlabel.get_rect().width
                pygame.draw.rect(screen, BLACK, (0, SIZE[1] - 25 , tempwidth,SIZE[1]- 25))
                screen.blit(playerlabel,(0, SIZE[1] - 25,))
                return newplayer
            
        players = players.Tail
def UpdatePlayers(list, stats):
    players = Empty()
    while not list.IsEmpty:
        if list.Value.Turn:
            list.Value.Life = list.Value.Life - stats[0]
            list.Value.Condition = list.Value.Condition - stats[1]
            players = Node(list.Value, players)
        else:
            players = Node(list.Value, players)
        list = list.Tail
    return players

# filtert op een lijst op  levende spelers
def RemoveDeathPlayers(players):
    return players.Filter(lambda x: x.Life!=0)
# neemt een lijst van players en return de hoeveelheid spelers in de lijst
def CountCurrentPlayers(players):
    cnt = 0 
    while not players.IsEmpty:
            cnt +=1
            players = players.Tail
    return cnt
