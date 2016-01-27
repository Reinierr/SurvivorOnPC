﻿import pygame, math, time
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
    players = Node(Player( tilemap, colornumber[playeramount-1]),players)
    players
    playeramount -= 1
  return players

def ScoreMenu(screen, players):
    ls = LINE_OFFSET
    playlist = players
    playcount = 0
    pygame.draw.rect(screen, BLACK, (SIZE[0] / 10, SIZE[1] / 10,100,500))
    while not playlist.IsEmpty:
        playcount = playcount + 1
        ls = ls + (LINE_OFFSET*3)
        playcol = FONT_TEXT.render('Player '+str(playcount), 1, FONT_COLOR_TEXT) 
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
  pygame.draw.rect(screen, BLACK, (0,TILESIZE*14 , width,height-TILESIZE*14))

def playerturn(screen, players, dicenumber):
    newplayer = players
    cnt = 0
    colors = [BLUE, RED, GREEN, YELLOW]
    while not players.IsEmpty:
        cnt = cnt + 1
        if players.Value.Turn:
            #-Turn player starts-#
            players.Value.Move(CreateMap(), dicenumber)
            if players.Value.Tile.Index in [5, 15, 25, 35]:
                #player must roll dice again before this part continues
                timer = 30
                newdicenumber = 0
                while not timer == 0:
                    if timer == 20:
                        newdicenumber = Dice(screen)
                    if not newdicenumber == 0:
                        players.Value.Life = players.Value.Life - SuperFight(screen, players.Value.Life, newdicenumber)
                        ScoreMenu(screen, players)
                        timer = 0
                    else:
                        pygame.time.wait(1000)
                        timer = timer - 1

            players.Value.Turn = False
            #-Turn player ends-#
            if not players.Tail.IsEmpty:
                players.Tail.Value.Turn = True
                playerlabel = FONT_TEXT.render('Current turn: Player '+str(cnt), 1, colors[int(math.floor(players.Tail.Value.Home)/10)])
                screen.blit(playerlabel,(0, SIZE[1] - 25))
                return players
            else:
                newplayer.Value.Turn = True
                playerlabel = FONT_TEXT.render('Current turn: Player '+str(cnt), 1, colors[int(math.floor(newplayer.Value.Home)/10)])
                screen.blit(playerlabel,(0, SIZE[1] - 25))
                return newplayer
        players = players.Tail
 