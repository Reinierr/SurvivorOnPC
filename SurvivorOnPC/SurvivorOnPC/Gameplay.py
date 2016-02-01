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
            if len(colornumber[playeramount-1]) == 2:
                players = Node(Player( tilemap, colornumber[playeramount-1][0], colornumber[playeramount-1][1]),players)
            else:
                players = Node(Player( tilemap, colornumber[playeramount-1][0]),players)
            players.Value.Turn = True
            players.Value.Number = playeramount
        else:
            if len(colornumber[playeramount-1]) == 2:
                players = Node(Player( tilemap, colornumber[playeramount-1][0], colornumber[playeramount-1][1]),players)
            else:
                players = Node(Player( tilemap, colornumber[playeramount-1][0]),players)
            players.Value.Number = playeramount
        playeramount -= 1
    return players

def ScoreMenu(screen, players):
    ls = LINE_OFFSET
    playlist = players
    pygame.draw.rect(screen, BLACK, (SIZE[0] / 10, SIZE[1] / 10,100,500))
    colors = [BLUE, RED, GREEN, YELLOW]
    hpcolors = [GREEN_BTN, ORANGE, RED_BTN]
    while not playlist.IsEmpty:
        ls = ls + (LINE_OFFSET*3)
        if playlist.Value.Life < 0:
            playlist.Value.Life = 0
        
        
        lplabel = FONT_TEXT.render('LP: ', 1, FONT_COLOR_TEXT) 
        playcol = FONT_TEXT.render('Player '+str(playlist.Value.Number), 1, colors[int(math.floor(playlist.Value.Home/10))]) 
        if playlist.Value.Life >= 75:
            lp = FONT_TEXT.render(str(playlist.Value.Life), 1, hpcolors[0])
        elif playlist.Value.Life < 75 and playlist.Value.Life >= 25:
            lp = FONT_TEXT.render(str(playlist.Value.Life), 1, hpcolors[1])
        elif playlist.Value.Life < 25:
            lp = FONT_TEXT.render(str(playlist.Value.Life), 1, hpcolors[2])
        cp = FONT_TEXT.render('CP: '+str(playlist.Value.Condition), 1, FONT_COLOR_TEXT)
        items = [playcol, lp, cp]
        for v,i in enumerate(items):
            if v == 1:
                screen.blit(i,(SIZE[0] / 10 + 40, SIZE[1] / 10 + ls + v*20))
            else:
                screen.blit(i,(SIZE[0] / 10, SIZE[1] / 10 + ls + v*20))
        screen.blit(lplabel, (SIZE[0] / 10, SIZE[1] / 10 + ls + v*20-20))
        playlist = playlist.Tail

def CheckPlayers(screen, players):
    ls = LINE_OFFSET
    playlist = players
    pygame.draw.rect(screen, BLACK, (SIZE[0] / 10, SIZE[1] / 10,250,200))
    for i,v in enumerate(playlist):
        ls = ls + LINE_OFFSET
        if int(v[0]) == 0:
            playcol = FONT_TEXT.render('Player '+str(i + 1), 1, BLUE) 
        elif int(v[0]) == 1:
            playcol = FONT_TEXT.render('Player '+str(i + 1), 1, RED) 
        elif int(v[0]) == 2:
            playcol = FONT_TEXT.render('Player '+str(i + 1), 1, GREEN) 
        elif int(v[0]) == 3:
            playcol = FONT_TEXT.render('Player '+str(i + 1), 1, YELLOW)
        if int(v[0]) > -1:
            AIlabel = FONT_TEXT.render('AI: Easy | Hard ', 1, WHITE)
            screen.blit(playcol,(SIZE[0] / 10, SIZE[1] / 10 + ls))
            screen.blit(AIlabel,(SIZE[0] / 10 + playcol.get_rect().width+5, SIZE [1] / 10 + ls))

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
    players2 = Empty()
    while not list.IsEmpty:
        if list.Value.Turn:
            list.Value.Life = list.Value.Life - stats[0]
            list.Value.Condition = list.Value.Condition - stats[1]
            players = Node(list.Value, players)
        else:
            players = Node(list.Value, players)
        list = list.Tail
    while not players.IsEmpty:
        players2 = Node(players.Value, players2)
        players = players.Tail
    return players2

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
