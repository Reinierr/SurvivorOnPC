import pygame, math, time
from Node import *
from Player import *
from Board import *
from Cards import *
from AI import *
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
        if playlist.Value.AI == 1:
            playcol = FONT_TEXT.render('Player '+str(playlist.Value.Number)+' Easy', 1, colors[int(math.floor(playlist.Value.Home/10))])
        elif playlist.Value.AI == 2:
            playcol = FONT_TEXT.render('Player '+str(playlist.Value.Number)+' Hard', 1, colors[int(math.floor(playlist.Value.Home/10))])
        else:
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
  screen.blit(FONT_TEXT.render('P to pause the game', 1, RED_BTN), (21*TILESIZE,9*TILESIZE))
  screen.blit(FONT_TEXT.render('R to view the rules', 1, RED_BTN), (21*TILESIZE,10*TILESIZE))
  screen.blit(FONT_TEXT.render('ESC to exit the game', 1, RED_BTN), (21*TILESIZE,11*TILESIZE))

def playerturn(screen, players, dicenumber):
    tempMap = CreateMap()
    newplayer = x = players
    colors = [BLUE, RED, GREEN, YELLOW]
    while not players.IsEmpty:
        if players.Value.Life != 0:
            if players.Value.Turn:
                playerlabel = FONT_TEXT.render('Current turn: Player '+str(players.Value.Number), 1, colors[int(math.floor(players.Value.Home)/10)])
                screen.blit(playerlabel,(0, SIZE[1] - 25))
                #-Turn player starts-#
                #players.Value.Move(CreateMap(),dicenumber)
                playermove(screen,tempMap,players,x,dicenumber)
        else:
            endplayerturn(screen, newplayer)
        players = players.Tail

def playermove(screen,tempMap,players,x,dicenumber):
  if dicenumber > 0:
    players.Value.Move(tempMap,1)
    tempMap.Filter(lambda i: i.Position.Col in range(6,20)).Iterate(lambda t: t.Draw(screen))
    x.Iterate(lambda p: p.Draw(screen,x))
    DrawImages(screen)
    dicenumber = dicenumber - 1
    pygame.display.flip()
    time.sleep(0.4)
    return playermove(screen,tempMap,players,x,dicenumber)
  else:
    return 0

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

def ScoreBtn(btn, screen, dicenumber2, players, player_stats1=False):
    newlist = players
    status = False
    #Check if player_stats exists
    try:
        player_stats2
    except NameError:
        player_stats2 = False
    while not newlist.IsEmpty:
        if newlist.Value.Turn:
            #check if current player is on a superfighter tile
            if newlist.Value.Tile.Index in [5, 15, 25, 35]:
                player_stats = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Home, dicenumber2, btn.Value)
                stats = SuperFight(screen, player_stats[0], player_stats[1])
                #update list where players have taken damage or used condition points
                players = UpdatePlayers(players, stats)
                ScoreMenu(screen, players)
                status = True
            #check if current player is on a corner tile
            elif newlist.Value.Tile.Index in [0, 10, 20, 30]:
                #fill attacking player stats = 1
                if not player_stats1:
                    player_stats1 = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Home, dicenumber2, btn.Value)
                    pygame.draw.rect(screen, BLACK, (0, 0 , 250,150))
                    throw_dice = Button(FONT_TEXT.render('Defend', 1, FONT_COLOR), screen, (2*TILESIZE,0.2*TILESIZE))
                    return player_stats1
                #fill defending player stats = 2
                else:
                    player_stats2 = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Tile.Index, dicenumber2, btn.Value)
                #start actual corner fight when both the players have made their choice
                if player_stats1 and player_stats2:
                    CornerFight(screen,players, player_stats1, player_stats2)
                    status = True
                    player_stats1 = False
                    player_stats2 = False 
            elif newlist.Value.Tile.Index in [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24,26,27,28,29,31,32,33,34,36,37,38,39]:
                    if not player_stats1:
                        player_stats1 = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Home, dicenumber2, btn.Value)
                        pygame.draw.rect(screen,BLACK, (0,0, 250,150))
                        throw_dice = Button(FONT_TEXT.render('Defend', 1, FONT_COLOR), screen, (2*TILESIZE,0.2*TILESIZE))
                        return player_stats1
                    else:
                        y = newlist
                        tempPlayers = y.Filter(lambda x: x.Home == p2)
                        player_stats2 = AI(tempPlayers.Value,dicenumber2) if CheckAI(tempPlayers.Value) else ScoreCard(tempPlayers.Value.Home, dicenumber2, btn.Value)
                        player_stats2
                #start actual Tile fight when both the players have made their choice
                    if player_stats1 and player_stats2:
                        CornerFight(screen,players, player_stats1, player_stats2)
                        status = True
                        player_stats1 = False
                        player_stats2 = False                                    
        newlist = newlist.Tail
    if status:
        ResetMap(screen, players)
        endplayerturn(screen, players)
        players.Iterate(lambda x: x.Draw(screen,players))
        throw_dice = Button(FONT_TEXT.render('Throw Dice', 1, FONT_COLOR), screen, (2*TILESIZE,0.2*TILESIZE))
        curpage = 'Game'
        return curpage
