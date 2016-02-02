import pygame
import os
import sys
from Node import *
from Tile import *
from Constants import * 
from Board import *
from Button import *
from Cards import *
from Player import *
from Rules import *
from Dice import *
from Gameplay import *
from AI import *
 
pygame.init()

def GameBoard(screen):
  screen.fill(BLACK)
  tilemap = Empty()
  tilemap = CreateMap()
  tilemap.Iterate(lambda x: x.Draw(screen))
  DrawImages(screen)

  pygame.display.set_caption('SurvivorOnPC')
  pygame.display.update()

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.scr_width = screen.get_rect().width
        self.scr_height = screen.get_rect().height
        self.bg_color = (BLACK)
        
        self.clock = pygame.time.Clock()

        self.curpage = 'Menu'
        self.superfight = False
        
        self.bg = pygame.image.load("Images\menubg.png")
        self.bgoffset = (self.scr_width - self.scr_height) / 2

        #Fix for name error on buttons
        self.dummy = FONT.render('Dummy', 1, (0,0,0))

        self.pc1 = ['-1']
        self.pc2 = ['-2']
        self.pc3 = ['-3']
        self.pc4 = ['-4']

        self.players = []
    def run(self):
        mainloop = True
        
        on = self.screen.blit(self.dummy, (-1,0))
        off = self.screen.blit(self.dummy, (-1,0))
        bbg = self.screen.blit(self.dummy, (-1,0))
        bbh = self.screen.blit(self.dummy, (-1,0))
        bp2 = self.screen.blit(self.dummy, (-1,0))
        bp3 = self.screen.blit(self.dummy, (-1,0))
        bp4 = self.screen.blit(self.dummy, (-1,0))
        bpr = self.screen.blit(self.dummy, (-1,0))
        bpb = self.screen.blit(self.dummy, (-1,0))
        bpg = self.screen.blit(self.dummy, (-1,0))
        bpy = self.screen.blit(self.dummy, (-1,0))
        bst = self.screen.blit(self.dummy, (-1,0))
        throw_dice = self.screen.blit(self.dummy, (-1,0))
        throw_dice_fight = self.screen.blit(self.dummy, (-1,0))
        sc1 = self.screen.blit(self.dummy, (-1,0))
        sc2 = self.screen.blit(self.dummy, (-1,0))
        sc3 = self.screen.blit(self.dummy, (-1,0))
        bsg = self.screen.blit(self.dummy, (-1,0))
        bai = self.screen.blit(self.dummy, (-1,0))
        bsb = self.screen.blit(self.dummy, (-1,0))
        ai1 = Button(FONT_TEXT.render('Easy', 1, BLACK), self.screen, (SIZE[0] / 10 + 120, SIZE[1] / 10 + (LINE_OFFSET * 2)),0,1)
        ai2 = Button(FONT_TEXT.render('Easy', 1, BLACK), self.screen, (SIZE[0] / 10 + 120, SIZE[1] / 10 + (LINE_OFFSET * 3)),0,1)
        ai3 = Button(FONT_TEXT.render('Easy', 1, BLACK), self.screen, (SIZE[0] / 10 + 120, SIZE[1] / 10 + (LINE_OFFSET * 4)),0,1)
        ai4 = Button(FONT_TEXT.render('Easy', 1, BLACK), self.screen, (SIZE[0] / 10 + 120, SIZE[1] / 10 + (LINE_OFFSET * 5)),0,1)
        ai1h = Button(FONT_TEXT.render('Hard', 1, BLACK), self.screen, (SIZE[0] / 10 + 185, SIZE[1] / 10 + (LINE_OFFSET * 2)),0,2)
        ai2h = Button(FONT_TEXT.render('Hard', 1, BLACK), self.screen, (SIZE[0] / 10 + 185, SIZE[1] / 10 + (LINE_OFFSET * 3)),0,2)
        ai3h = Button(FONT_TEXT.render('Hard', 1, BLACK), self.screen, (SIZE[0] / 10 + 185, SIZE[1] / 10 + (LINE_OFFSET * 4)),0,2)
        ai4h = Button(FONT_TEXT.render('Hard', 1, BLACK), self.screen, (SIZE[0] / 10 + 185, SIZE[1] / 10 + (LINE_OFFSET * 5)),0,2)
        players = Empty()

        self.screen.fill(self.bg_color)
        self.screen.blit(pygame.transform.scale(self.bg, (self.scr_height,self.scr_height)),(self.bgoffset,0))
        
        bs = Button(FONT.render('Start', 1, FONT_COLOR), self.screen, 0,-1)
        bh = Button(FONT.render('How to play', 1, FONT_COLOR), self.screen, 0,0)
        bss = Button(FONT.render('Settings', 1, FONT_COLOR), self.screen, 0,1)
        bc = Button(FONT.render('Exit', 1, FONT_COLOR), self.screen, 0,2)

        while mainloop:
            self.clock.tick(9)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
            #Back to menu button
            ButtonHover(self.screen,self.curpage,bbg,'Game','Back to menu',FONT_TEXT,(23*TILESIZE,0.2*TILESIZE))
            #Back buttons hover
            ButtonHover(self.screen,self.curpage,bbh,'HelpMenu','Back',FONT,0,3)
            ButtonHover(self.screen,self.curpage,bbh,'PlayerSelect','Back',FONT,0,5)
            #Start button hover
            ButtonHover(self.screen,self.curpage,bs,'Menu','Start',FONT,0,-1)
            #How to play hover
            ButtonHover(self.screen,self.curpage,bh,'Menu','How to play',FONT,0,0)
            #Exit button
            ButtonHover(self.screen,self.curpage,bc,'Menu','Exit',FONT,0,2)
            #Play again button hover
            ButtonHover(self.screen,self.curpage,bsg,'Winning_screen','Play again',FONT,0,3)
            #Settings Hover
            ButtonHover(self.screen,self.curpage,bss,'Menu','Settings',FONT,0,1)
            #Settings Hover
            ButtonHover(self.screen,self.curpage,bsb,'Settings','Back',FONT,0,3)

            aiPlayerCheckList = players

            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or (not aiPlayerCheckList.Filter(lambda x : x.Turn and x.AI > 0).IsEmpty):
                pos = pygame.mouse.get_pos()

                if self.curpage == 'Turn2':
                    if sc1.collidepoint(pos):
                        newlist = players
                        status = False
                        #Check if player_stats exists
                        try:
                            player_stats1
                        except NameError:
                            player_stats1 = False
                        try:
                            player_stats2
                        except NameError:
                            player_stats2 = False
                        while not newlist.IsEmpty:
                            if newlist.Value.Turn:
                                #check if current player is on a superfighter tile
                                if newlist.Value.Tile.Index in [5, 15, 25, 35]:
                                    player_stats = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Home, dicenumber2, sc1.Value)
                                    stats = SuperFight(self.screen, player_stats[0], player_stats[1])
                                    #update list where players have taken damage or used condition points
                                    players = UpdatePlayers(players, stats)
                                    ScoreMenu(self.screen, players)
                                    status = True
                                #check if current player is on a corner tile
                                elif newlist.Value.Tile.Index in [0, 10, 20, 30]:
                                    #fill attacking player stats = 1
                                    if not player_stats1:
                                        player_stats1 = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Home, dicenumber2, sc1.Value)
                                        print(player_stats1)
                                        pygame.draw.rect(screen, BLACK, (0, 0 , 250,150))
                                        throw_dice = Button(FONT_TEXT.render('Defend', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                                    #fill defending player stats = 2
                                    else:
                                        player_stats2 = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Tile.Index, dicenumber2, sc1.Value)
                                        print(player_stats2)
                                    #start actual corner fight when both the players have made their choice
                                    if player_stats1 and player_stats2:
                                        CornerFight(screen,players, player_stats1, player_stats2)
                                        status = True
                                        player_stats1 = False
                                        player_stats2 = False 
        #marcels test for pvp on tiles
        #current minnor bug where player turn gets moved on before this event happens and second player values are wrong
                                elif newlist.Value.Tile.Index in [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24,26,27,28,29,31,32,33,34,36,37,38,39]:
                                     if not player_stats1:
                                         player_stats1 = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Home, dicenumber2, sc1.Value)
                                         print(player_stats1)
                                         pygame.draw.rect(screen,BLACK, (0,0, 250,150))
                                         throw_dice = Button(FONT_TEXT.render('Defend', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                                         player_stats1
                                     else:
                                        y = newlist
                                        tempPlayers = y.Filter(lambda x: x.Home == p2)
                                        player_stats2 = AI(tempPlayers.Value,dicenumber2) if CheckAI(tempPlayers.Value) else ScoreCard(tempPlayers.Value.Home, dicenumber2, sc1.Value)
                                        print(player_stats2)
                                        player_stats2
                                    #start actual Tile fight when both the players have made their choice
                                     if player_stats1 and player_stats2:
                                        CornerFight(screen,players, player_stats1, player_stats2)
                                        status = True
                                        player_stats1 = False
                                        player_stats2 = False
    #end of Marcels test for pvp on tiles                                      
                            newlist = newlist.Tail
                        #continue gameloop and allow next player to play their turn
                        if status:
                            ResetMap(self.screen, players)
                            endplayerturn(self.screen, players)
                            players.Iterate(lambda x: x.Draw(self.screen,players))
                            throw_dice = Button(FONT_TEXT.render('Throw Dice', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                            self.curpage = 'Game'
                    elif sc2.collidepoint(pos):
                        newlist = players
                        status = False
                        #Check if player_stats exists
                        try:
                            player_stats1
                        except NameError:
                            player_stats1 = False
                        try:
                            player_stats2
                        except NameError:
                            player_stats2 = False
                        while not newlist.IsEmpty:
                            if newlist.Value.Turn:
                                #check if current player is on a superfighter tile
                                if newlist.Value.Tile.Index in [5, 15, 25, 35]:
                                    player_stats = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Home, dicenumber2, sc2.Value)
                                    stats = SuperFight(self.screen, player_stats[0], player_stats[1])
                                    #update list where players have taken damage or used condition points
                                    players = UpdatePlayers(players, stats)
                                    ScoreMenu(self.screen, players)
                                    status = True
                                #check if current player is on a corner tile
                                elif newlist.Value.Tile.Index in [0, 10, 20, 30]:
                                    #fill attacking player stats = 1
                                    if not player_stats1:
                                        player_stats1 = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Home, dicenumber2, sc2.Value)
                                        pygame.draw.rect(screen, BLACK, (0, 0 , 250,150))
                                        throw_dice = Button(FONT_TEXT.render('Defend', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                                    #fill defending player stats = 2
                                    else:
                                        player_stats2 = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Home, dicenumber2, sc2.Value)
                                        print(player_stats2)
                                    #start actual corner fight when both the players have made their choice
                                    if player_stats1 and player_stats2:
                                        CornerFight(screen,players, player_stats1, player_stats2)
                                        status = True
                                        player_stats1 = False
                                        player_stats2 = False

                                elif newlist.Value.Tile.Index in [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24,26,27,28,29,31,32,33,34,36,37,38,39]:
                                     if not player_stats1:
                                         player_stats1 = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Home, dicenumber2, sc1.Value)
                                         print(player_stats1)
                                         pygame.draw.rect(screen,BLACK, (0,0, 250,150))
                                         throw_dice = Button(FONT_TEXT.render('Defend', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                                         player_stats1
                                     else:
                                        y = newlist
                                        tempPlayers = y.Filter(lambda x: x.Home == p2)
                                        player_stats2 = AI(tempPlayers.Value,dicenumber2) if CheckAI(tempPlayers.Value) else ScoreCard(tempPlayers.Value.Home, dicenumber2, sc1.Value)
                                        print(player_stats2)
                                        player_stats2
                                    #start actual Tile fight when both the players have made their choice
                                     if player_stats1 and player_stats2:
                                        CornerFight(screen,players, player_stats1, player_stats2)
                                        status = True
                                        player_stats1 = False
                                        player_stats2 = False
                            newlist = newlist.Tail
                        #continue gameloop and allow next player to play their turn
                        if status:
                            ResetMap(self.screen, players)
                            endplayerturn(self.screen, players)
                            players.Iterate(lambda x: x.Draw(self.screen,players))
                            throw_dice = Button(FONT_TEXT.render('Throw Dice', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                            self.curpage = 'Game'
                    elif sc3.collidepoint(pos):
                        newlist = players
                        status = False
                        #Check if player_stats exists
                        try:
                            player_stats1
                        except NameError:
                            player_stats1 = False
                        try:
                            player_stats2
                        except NameError:
                            player_stats2 = False
                        while not newlist.IsEmpty:
                            if newlist.Value.Turn:
                                #check if current player is on a superfighter tile
                                if newlist.Value.Tile.Index in [5, 15, 25, 35]:
                                    player_stats = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Home, dicenumber2, sc3.Value)
                                    stats = SuperFight(self.screen, player_stats[0], player_stats[1])
                                    #update list where players have taken damage or used condition points
                                    players = UpdatePlayers(players, stats)
                                    ScoreMenu(self.screen, players)
                                    status = True
                                #check if current player is on a corner tile
                                elif newlist.Value.Tile.Index in [0, 10, 20, 30]:
                                    #fill attacking player stats = 1
                                    if not player_stats1:
                                        player_stats1 = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Home, dicenumber2, sc3.Value)
                                        pygame.draw.rect(screen, BLACK, (0, 0 , 250,150))
                                        throw_dice = Button(FONT_TEXT.render('Defend', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                                    #fill defending player stats = 2
                                    else:
                                        player_stats2 = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Home, dicenumber2, sc3.Value)
                                        print(player_stats2)
                                    #start actual corner fight when both the players have made their choice
                                    if player_stats1 and player_stats2:
                                        CornerFight(screen,players, player_stats1, player_stats2)
                                        status = True
                                        player_stats1 = False
                                        player_stats2 = False

                                elif newlist.Value.Tile.Index in [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24,26,27,28,29,31,32,33,34,36,37,38,39]:
                                     if not player_stats1:
                                         player_stats1 = AI(newlist.Value,dicenumber2) if CheckAI(newlist.Value) else ScoreCard(newlist.Value.Home, dicenumber2, sc1.Value)
                                         print(player_stats1)
                                         pygame.draw.rect(screen,BLACK, (0,0, 250,150))
                                         throw_dice = Button(FONT_TEXT.render('Defend', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                                         player_stats1
                                     else:
                                        y = newlist
                                        tempPlayers = y.Filter(lambda x: x.Home == p2)
                                        player_stats2 = AI(tempPlayers.Value,dicenumber2) if CheckAI(tempPlayers.Value) else ScoreCard(tempPlayers.Value.Home, dicenumber2, sc1.Value)
                                        print(player_stats2)
                                        player_stats2
                                    #start actual Tile fight when both the players have made their choice
                                     if player_stats1 and player_stats2:
                                        CornerFight(screen,players, player_stats1, player_stats2)
                                        status = True
                                        player_stats1 = False
                                        player_stats2 = False
                            newlist = newlist.Tail
                        #continue gameloop and allow next player to play their turn
                        if status:
                            ResetMap(self.screen, players)
                            endplayerturn(self.screen, players)
                            players.Iterate(lambda x: x.Draw(self.screen,players))
                            throw_dice = Button(FONT_TEXT.render('Throw Dice', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                            self.curpage = 'Game'
                if self.curpage == 'PlayerSelect':
                    if ai1.collidepoint(pos):
                        if not len(self.pc1) == 2:
                            self.pc1.append(1)
                    if ai2.collidepoint(pos):
                        if not len(self.pc2) == 2:
                            self.pc2.append(1)
                    if ai3.collidepoint(pos):
                        if not len(self.pc3) == 2:
                            self.pc3.append(1)
                    if ai4.collidepoint(pos):
                        if not len(self.pc4) == 2:
                            self.pc4.append(1)
                    if ai1h.collidepoint(pos):
                        if not len(self.pc1) == 2:
                            self.pc1.append(2)
                    if ai2h.collidepoint(pos):
                        if not len(self.pc2) == 2:
                            self.pc2.append(2)
                    if ai3h.collidepoint(pos):
                        if not len(self.pc3) == 2:    
                            self.pc3.append(2)
                    if ai4h.collidepoint(pos):
                        if not len(self.pc4) == 2:
                            self.pc4.append(2)
                    if len(self.players) == 2:
                        if self.pc1[0] == '-1' and self.pc2[0] == '-2' and self.pc3[0] == '-3' and self.pc4[0] == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = [bpr.Value]
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = [bpb.Value]
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = [bpg.Value]
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = [bpy.Value]
                        elif self.pc2[0] == '-2' and not self.pc1[0] == '-1' and self.pc3[0] == '-3' and self.pc4[0] == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpr.Value:
                                self.pc2 = [bpr.Value]
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpb.Value:
                                self.pc2 = [bpb.Value]
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpg.Value:
                                self.pc2 = [bpg.Value]
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpy.Value:
                                self.pc2 = [bpy.Value]
                        CheckPlayers(self.screen, [self.pc1, self.pc2])
                        if not self.pc1[0] == '-1' and not self.pc2[0] == '-2':
                            self.players = [self.pc1,self.pc2]
                            bst = Button(FONT.render('Play', 1, FONT_COLOR), self.screen, 0,2)
                    elif len(self.players) == 3:
                        if self.pc1[0] == '-1' and self.pc2[0] == '-2' and self.pc3[0] == '-3' and self.pc4[0] == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = [bpr.Value]
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = [bpb.Value]
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = [bpg.Value]
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = [bpy.Value]
                        elif self.pc2[0] == '-2' and not self.pc1[0] == '-1' and self.pc3[0] == '-3' and self.pc4[0] == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpr.Value:
                                self.pc2 = [bpr.Value]
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpb.Value:
                                self.pc2 = [bpb.Value]
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpg.Value:
                                self.pc2 = [bpg.Value]
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpy.Value:
                                self.pc2 = [bpy.Value]
                        elif self.pc3[0] == '-3' and not self.pc1[0] == '-1' and not self.pc2[0] == '-2' and self.pc4[0] == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpr.Value and not self.pc2[0] == bpr.Value:
                                self.pc3 = [bpr.Value]
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpb.Value and not self.pc2[0] == bpb.Value:
                                self.pc3 = [bpb.Value]
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpg.Value and not self.pc2[0] == bpg.Value:
                                self.pc3 = [bpg.Value]
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpy.Value and not self.pc2[0] == bpy.Value:
                                self.pc3 = [bpy.Value]
                        CheckPlayers(self.screen, [self.pc1, self.pc2, self.pc3])
                        if not self.pc1[0] == '-1' and not self.pc2[0] == '-2' and not self.pc3[0] == '-3':
                            self.players = [self.pc1,self.pc2, self.pc3]
                            bst = Button(FONT.render('Play', 1, FONT_COLOR), self.screen, 0,2)
                    elif len(self.players) == 4:
                        if self.pc1[0] == '-1' and self.pc2[0] == '-2' and self.pc3[0] == '-3' and self.pc4[0] == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = [bpr.Value]
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = [bpb.Value]
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = [bpg.Value]
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = [bpy.Value]
                        elif self.pc2[0] == '-2' and not self.pc1[0] == '-1' and self.pc3[0] == '-3' and self.pc4[0] == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpr.Value:
                                self.pc2 = [bpr.Value]
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpb.Value:
                                self.pc2 = [bpb.Value]
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpg.Value:
                                self.pc2 = [bpg.Value]
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpy.Value:
                                self.pc2 = [bpy.Value]
                        elif self.pc3[0] == '-3' and not self.pc1[0] == '-1' and not self.pc2[0] == '-2' and self.pc4[0] == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpr.Value and not self.pc2[0] == bpr.Value:
                                self.pc3 = [bpr.Value]
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpb.Value and not self.pc2[0] == bpb.Value:
                                self.pc3 = [bpb.Value]
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpg.Value and not self.pc2[0] == bpg.Value:
                                self.pc3 = [bpg.Value]
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1[0] == bpy.Value and not self.pc2[0] == bpy.Value:
                                self.pc3 = [bpy.Value]
                        elif self.pc4[0] == '-4' and not self.pc1[0] == '-1' and not self.pc2[0] == '-2' and not self.pc3[0] == '-3':
                            if not self.pc1[0] == bpr.Value and not self.pc2[0] == bpr.Value and not self.pc3[0] == bpr.Value:
                                self.pc4 = [bpr.Value]
                            elif not self.pc1[0] == bpb.Value and not self.pc2[0] == bpb.Value and not self.pc3[0] == bpb.Value:
                                self.pc4 = [bpb.Value]
                            elif not self.pc1[0] == bpg.Value and not self.pc2[0] == bpg.Value and not self.pc3[0] == bpg.Value:
                                self.pc4 = [bpg.Value]
                            elif not self.pc1[0] == bpy.Value and not self.pc2[0] == bpy.Value and not self.pc3[0] == bpy.Value:
                                self.pc4 = [bpy.Value]
                        CheckPlayers(self.screen, [self.pc1, self.pc2, self.pc3, self.pc4])
                        if not self.pc1[0] == '-1' and not self.pc2[0] == '-2' and not self.pc3[0] == '-3' and not self.pc4[0] == '-4':
                            self.players = [self.pc1,self.pc2, self.pc3, self.pc4]
                            bst = Button(FONT.render('Play', 1, FONT_COLOR), self.screen, 0,2)
                
                if bp2.collidepoint(pos) and self.curpage == 'PlayerSelect':
                    bp2 = Button(FONT.render('2', 1, WHITE), self.screen, 0,-2,2)
                    bp3 = Button(FONT.render('3', 1, FONT_COLOR), self.screen, 0,-1,3)
                    bp4 = Button(FONT.render('4', 1, FONT_COLOR), self.screen, 0,0,4)

                    bpr = Button(FONT.render('Red', 1, RED_BTN), self.screen, ((self.scr_width/6)*1, 1.7*OFFSET),0,1)
                    bpb = Button(FONT.render('Blue', 1, BLUE), self.screen, ((self.scr_width/6)*2, 1.7*OFFSET),0,0)
                    bpg = Button(FONT.render('Green', 1, GREEN), self.screen, ((self.scr_width/6)*4, 1.7*OFFSET),0,2)
                    bpy = Button(FONT.render('Yellow', 1, YELLOW), self.screen, ((self.scr_width/6)*5, 1.7*OFFSET),0,3)

                    self.pc1 = ['-1']
                    self.pc2 = ['-2']
                    self.pc3 = ['-3']
                    self.pc4 = ['-4']

                    self.players = [self.pc1, self.pc2]

                elif bp3.collidepoint(pos) and self.curpage == 'PlayerSelect':
                    bp2 = Button(FONT.render('2', 1, FONT_COLOR), self.screen, 0,-2,2)
                    bp3 = Button(FONT.render('3', 1, WHITE), self.screen, 0,-1,3)
                    bp4 = Button(FONT.render('4', 1, FONT_COLOR), self.screen, 0,0,4)

                    bpr = Button(FONT.render('Red', 1, RED_BTN), self.screen, ((self.scr_width/6)*1, 1.7*OFFSET),0,1)
                    bpb = Button(FONT.render('Blue', 1, BLUE), self.screen, ((self.scr_width/6)*2, 1.7*OFFSET),0,0)
                    bpg = Button(FONT.render('Green', 1, GREEN), self.screen, ((self.scr_width/6)*4, 1.7*OFFSET),0,2)
                    bpy = Button(FONT.render('Yellow', 1, YELLOW), self.screen, ((self.scr_width/6)*5, 1.7*OFFSET),0,3)

                    self.pc1 = ['-1']
                    self.pc2 = ['-2']
                    self.pc3 = ['-3']
                    self.pc4 = ['-4']
                    self.players = [self.pc1, self.pc2, self.pc3]

                elif bp4.collidepoint(pos) and self.curpage == 'PlayerSelect':
                    bp2 = Button(FONT.render('2', 1, FONT_COLOR), self.screen, 0,-2,2)
                    bp3 = Button(FONT.render('3', 1, FONT_COLOR), self.screen, 0,-1,3)
                    bp4 = Button(FONT.render('4', 1, WHITE), self.screen, 0,0,4)

                    bpr = Button(FONT.render('Red', 1, RED_BTN), self.screen, ((self.scr_width/6)*1, 1.7*OFFSET),0,1)
                    bpb = Button(FONT.render('Blue', 1, BLUE), self.screen, ((self.scr_width/6)*2, 1.7*OFFSET),0,0)
                    bpg = Button(FONT.render('Green', 1, GREEN), self.screen, ((self.scr_width/6)*4, 1.7*OFFSET),0,2)
                    bpy = Button(FONT.render('Yellow', 1, YELLOW), self.screen, ((self.scr_width/6)*5, 1.7*OFFSET),0,3)

                    self.pc1 = ['-1']
                    self.pc2 = ['-2']
                    self.pc3 = ['-3']
                    self.pc4 = ['-4']
                    self.players = [self.pc1, self.pc2, self.pc3, self.pc4]
                
                if bst.collidepoint(pos):
                    if sound == True:
                        bell = pygame.mixer.Sound('Sounds/boxing_bell.wav')
                        bell.play()
                    if self.curpage == 'PlayerSelect' or self.curpage == 'Menu':
                        if len(self.players) >= 2:
                            start = False
                            for v in self.players:
                                if int(v[0]) > -1:
                                    start = True
                                else:
                                    start = False
                            if start:
                                #Start het spel
                                self.curpage = 'Game'
                                self.screen.fill(self.bg_color)
                                #Display gameboard
                                GameBoard(screen)
                                #Display players on board
                                players = PlayerList(self.players)
                                players.Iterate(lambda x: x.Draw(self.screen,players))
                                ScoreMenu(self.screen, players)

                                playerturn(self.screen, players, 0)

                                bbg = Button(FONT_TEXT.render('Back to menu', 1, FONT_COLOR), self.screen, (23*TILESIZE,0.2*TILESIZE))
                                throw_dice = Button(FONT_TEXT.render('Throw Dice', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))

                                sc1 = Button(FONT_TEXT.render('Clicklabel', 1, BLACK), self.screen, (21*TILESIZE,5*TILESIZE),0,1)
                                sc2 = Button(FONT_TEXT.render('Clicklabel', 1, BLACK), self.screen, (21*TILESIZE,6*TILESIZE),0,2)
                                sc3 = Button(FONT_TEXT.render('Clicklabel', 1, BLACK), self.screen, (21*TILESIZE,7*TILESIZE),0,3)
                            else:
                                print('Niet genoeg spelers geselecteerd.')
                                #label op scherm toevoegen
                elif bs.collidepoint(pos) and self.curpage == 'Menu':
                    self.screen.fill(self.bg_color)
                    self.curpage = 'PlayerSelect'
                    label = FONT.render('Choose amount of players', 1, FONT_COLOR)
                    screen.blit(label, (SIZE[0] / 2 - label.get_rect().width / 2, (SIZE[1] / 3.8 - label.get_rect().height / 2)))

                    bp2 = Button(FONT.render('2', 1, FONT_COLOR), self.screen, 0,-2,2)
                    bp3 = Button(FONT.render('3', 1, FONT_COLOR), self.screen, 0,-1,3)
                    bp4 = Button(FONT.render('4', 1, FONT_COLOR), self.screen, 0,0,4)

                    bbh = Button(FONT.render('Back', 1, FONT_COLOR), self.screen, 0,5)
                elif bai.collidepoint(pos) and self.curpage == 'PlayerSelect':
                    print ('AI')
                elif bh.collidepoint(pos) and self.curpage == 'Menu':
                    #How to play page
                    pygame.display.set_caption('How to play Menu')
                    self.curpage = 'HelpMenu'
                    self.screen.fill(self.bg_color)
                    #Back btn op het scherm plaatsen
                    bbh = Button(FONT.render('Back', 1, FONT_COLOR), self.screen, 0,3)
                    #Informatie op het scherm zetten | Margin van 10%
                    Rules(screen)
                elif bss.collidepoint(pos) and self.curpage == 'Menu':
                     self.curpage = 'Settings'
                     self.screen.fill(self.bg_color)
                     bsb = Button(FONT.render('Back', 1, FONT_COLOR), self.screen, 0,3)
                     on = Button(FONT.render('On', 1, FONT_COLOR), self.screen, 0,-2)
                     label = FONT.render('Sound:', 1, WHITE)
                     screen.blit(label, (SIZE[0] / 2 - label.get_rect().width / 2, (SIZE[1] / 3.8 - label.get_rect().height / 2)))

                elif on.collidepoint(pos) and self.curpage == 'Settings':
                    sound = True
                    self.curpage = 'Settings'
                    self.screen.fill(self.bg_color)
                    bsb = Button(FONT.render('Back', 1, FONT_COLOR), self.screen, 0,3)
                    off = Button(FONT.render('Off', 1, FONT_COLOR), self.screen, 0,-2)
                    label = FONT.render('Sound:', 1, WHITE)
                    screen.blit(label, (SIZE[0] / 2 - label.get_rect().width / 2, (SIZE[1] / 3.8 - label.get_rect().height / 2)))
                
                elif off.collidepoint(pos) and self.curpage == 'Settings':
                    print('test')
                    #Broken
                
                elif bsb.collidepoint(pos) and self.curpage == 'Settings':
                    self.curpage = 'Menu'
                    self.screen.fill(self.bg_color)
                    self.screen.blit(pygame.transform.scale(self.bg, (self.scr_height,self.scr_height)),(self.bgoffset,0))
                    #Btns start/how to play/exit op het scherm plaatsen
                    bs = Button(FONT.render('Start', 1, FONT_COLOR), self.screen, 0,-1)
                    bh = Button(FONT.render('How to play', 1, FONT_COLOR), self.screen, 0,0)
                    bss = Button(FONT.render('Settings', 1, FONT_COLOR), self.screen, 0,1)
                    bc = Button(FONT.render('Exit', 1, FONT_COLOR), self.screen, 0,2)
                elif bc.collidepoint(pos) and self.curpage == 'Menu':
                    #Exit game, stop loop en exit de console
                    mainloop = False
                    pygame.quit()
                    sys.exit()
                elif bbh.collidepoint(pos) or bbg.collidepoint(pos):
                    if self.curpage == 'Game' or self.curpage == 'HelpMenu' or self.curpage == 'PlayerSelect':
                        pygame.display.set_caption('Game Menu')
                        self.curpage = 'Menu'
                        self.screen.fill(self.bg_color)
                        self.screen.blit(pygame.transform.scale(self.bg, (self.scr_height,self.scr_height)),(self.bgoffset,0))
                        #Btns start/how to play/exit op het scherm plaatsen
                        bs = Button(FONT.render('Start', 1, FONT_COLOR), self.screen, 0,-1)
                        bh = Button(FONT.render('How to play', 1, FONT_COLOR), self.screen, 0,0)
                        bss = Button(FONT.render('Settings', 1, FONT_COLOR), self.screen, 0,1)
                        bc = Button(FONT.render('Exit', 1, FONT_COLOR), self.screen, 0,2)
                elif bsg.collidepoint(pos) and self.curpage == 'Winning_screen':
                        print('klik')
                        pygame.display.set_caption('Game Menu')
                        self.curpage = 'Menu'
                        self.screen.fill(self.bg_color)
                        self.screen.blit(pygame.transform.scale(self.bg, (self.scr_height,self.scr_height)),(self.bgoffset,0))
                        #Btns start/how to play/exit op het scherm plaatsen
                        bs = Button(FONT.render('Start', 1, FONT_COLOR), self.screen, 0,-1)
                        bh = Button(FONT.render('How to play', 1, FONT_COLOR), self.screen, 0,0)
                        bc = Button(FONT.render('Exit', 1, FONT_COLOR), self.screen, 0,1)
                elif (throw_dice.collidepoint(pos) or not aiPlayerCheckList.Filter(lambda x : x.Turn and x.AI > 0).IsEmpty) and self.curpage == 'Game':
                    dicenumber = Dice(self.screen)
                    pygame.time.delay(1000)             
                    ResetMap(self.screen, players)

                    throw_dice = Button(FONT_TEXT.render('Throw Dice', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                    sc1 = Button(FONT_TEXT.render('Clicklabel', 1, BLACK), self.screen, (21*TILESIZE,5*TILESIZE),0,1)
                    sc2 = Button(FONT_TEXT.render('Clicklabel', 1, BLACK), self.screen, (21*TILESIZE,6*TILESIZE),0,2)
                    sc3 = Button(FONT_TEXT.render('Clicklabel', 1, BLACK), self.screen, (21*TILESIZE,7*TILESIZE),0,3)      
                    players = RemoveDeathPlayers(players)
                    playerturn(self.screen, players, 10)#dicenumber)
                    players.Iterate(lambda x: x.Draw(self.screen,players))
                    temp = players
                    x = players
                    y = players
                    while not x.IsEmpty:
                        if x.Value.Turn:
                            if x.Value.Tile.Index in [5, 15, 25, 35]:
                                pygame.draw.rect(screen, BLACK, (0, 0 , 250,30))
                                throw_dice_fight = Button(FONT_TEXT.render('Fight', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                                self.curpage = 'Turn2'
                            elif x.Value.Tile.Index in [0, 10, 20, 30]:
                                if not temp.Filter(lambda z:z.Home == x.Value.Tile.Index and not x.Value.Home == z.Home).IsEmpty:
                                    pygame.draw.rect(screen, BLACK, (0, 0 , 250,30))
                                    throw_dice_fight = Button(FONT_TEXT.render('Fight', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                                    self.curpage = 'Turn2'
                                    player1 = True
                                else:
                                    endplayerturn(self.screen, players)
                                    break
        #marcels custom loop for PVP on tiles
        #I'm Kinda stuck
                            elif x.Value.Tile.Index in range (0,39):
                                while not y.IsEmpty:
                                    if not x.Value.Home == y.Value.Home and x.Value.Tile.Index == y.Value.Tile.Index:
                                        pygame.draw.rect(screen, BLACK, (0, 0 , 250,30))
                                        throw_dice_fight = Button(FONT_TEXT.render('Fight', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                                        self.curpage = 'Turn2'
                                        p2 = y.Value.Home
                                        p1 = x.Value.Home
                                    y = y.Tail
                                if y.IsEmpty:
                                    endplayerturn(self.screen, players)
                                    break
                            else:
                                endplayerturn(self.screen, players)
                                break
                        x = x.Tail
                elif (throw_dice_fight.collidepoint(pos) or not aiPlayerCheckList.Filter(lambda x : x.Turn and x.AI > 0).IsEmpty) and self.curpage == 'Turn2':
                    dicenumber2 = Dice(self.screen)

                    x = players
                    while not x.IsEmpty:
                        if x.Value.Turn:
                            try:
                                p1
                            except NameError:
                                p1 = -2
                            try:
                                p2
                            except NameError:
                                p2 = -2
                            if p1 > -1:
                                DisplayScoreCard(screen, x.Value.Home, dicenumber2, x.Value.Condition)
                                p1 = -2
                            elif p2 > -1 and not p1 > -1:
                                z = x
                                tempPlayers = z.Filter(lambda x: x.Home == p2)
                                DisplayScoreCard(screen, p2, dicenumber2, tempPlayers.Value.Condition)
                            elif x.Value.Tile.Index in [0, 10, 20, 30]:
                                if player1:
                                    DisplayScoreCard(screen, x.Value.Home, dicenumber2, x.Value.Condition)
                                    player1 = False
                                else:
                                    DisplayScoreCard(screen, x.Value.Tile.Index, dicenumber2, x.Value.Condition)
                            else:
                                DisplayScoreCard(screen, x.Value.Home, dicenumber2, x.Value.Condition)
                        x = x.Tail
                    pygame.time.delay(1000)

            #Winning screen , verander countcurrent players naar == 2 om te testen!
            if CountCurrentPlayers(players) == 1:
                colors = [BLUE, RED, GREEN, YELLOW]
                self.curpage = 'Winning_screen'
                self.screen.fill(self.bg_color)
                label = FONT.render('Player '+str(players.Value.Number)+ ' Wins', 1, colors[int(math.floor(players.Value.Home)/10)])
                screen.blit(label, (SIZE[0] / 2 - label.get_rect().width / 2, (SIZE[1] / 3.8 - label.get_rect().height / 2)))
                bsg = Button(FONT.render('Play again', 1, FONT_COLOR), self.screen, 0,3)
                players = Empty()
                self.players = []
                if bsg.collidepoint(pos) and self.curpage == 'Winning_screen': 
                    pygame.display.set_caption('Game Menu')
                    self.curpage = 'Menu'
                    self.screen.fill(self.bg_color)
                    self.screen.blit(pygame.transform.scale(self.bg, (self.scr_height,self.scr_height)),(self.bgoffset,0))
                    #Btns start/how to play/exit op het scherm plaatsen
                    bs = Button(FONT.render('Start', 1, FONT_COLOR), self.screen, 0,-1)
                    bh = Button(FONT.render('How to play', 1, FONT_COLOR), self.screen, 0,0)
                    bc = Button(FONT.render('Exit', 1, FONT_COLOR), self.screen, 0,1)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if mainloop:
                pygame.display.flip()
            else:
                pygame.quit()
                sys.exit()
            
screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption('Game Menu')
gm = Game(screen)
gm.run()