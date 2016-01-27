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

        self.pc1 = '-1'
        self.pc2 = '-2'
        self.pc3 = '-3'
        self.pc4 = '-4'

        self.players = []
    def run(self):
        mainloop = True
        self.screen.fill(self.bg_color)
        self.screen.blit(pygame.transform.scale(self.bg, (self.scr_height,self.scr_height)),(self.bgoffset,0))
        
        bs = Button(FONT.render('Start', 1, FONT_COLOR), self.screen, 0,-1)
        bh = Button(FONT.render('How to play', 1, FONT_COLOR), self.screen, 0,0)
        bc = Button(FONT.render('Exit', 1, FONT_COLOR), self.screen, 0,1)

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

        while mainloop:
            self.clock.tick(9)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

            #Start button hover
            if bs.collidepoint(pygame.mouse.get_pos()) and self.curpage == 'Menu':
                bs = Button(FONT.render('Start', 1, WHITE), self.screen, 0,-1)
            elif not bs.collidepoint(pygame.mouse.get_pos()) and self.curpage == 'Menu':
                bs = Button(FONT.render('Start', 1, FONT_COLOR), self.screen, 0,-1)

            #How to play hover
            if bh.collidepoint(pygame.mouse.get_pos()) and self.curpage == 'Menu':
                bh = Button(FONT.render('How to play', 1, WHITE), self.screen ,0,0)
            elif not bh.collidepoint(pygame.mouse.get_pos()) and self.curpage == 'Menu':
                bh = Button(FONT.render('How to play', 1, FONT_COLOR), self.screen ,0,0)

            #Back button
            if bc.collidepoint(pygame.mouse.get_pos()) and self.curpage == 'Menu':
                bc = Button(FONT.render('Exit', 1, WHITE), self.screen ,0,1)
            elif not bc.collidepoint(pygame.mouse.get_pos()) and self.curpage == 'Menu':
                bc = Button(FONT.render('Exit', 1, FONT_COLOR), self.screen, 0,1)

            if bbg.collidepoint(pygame.mouse.get_pos()) and self.curpage == 'Game':
                bbg = Button(FONT_TEXT.render('Back to menu', 1, WHITE), self.screen, (23*TILESIZE,0.2*TILESIZE))
            elif not bbg.collidepoint(pygame.mouse.get_pos()) and self.curpage == 'Game':
                bbg = Button(FONT_TEXT.render('Back to menu', 1, FONT_COLOR), self.screen, (23*TILESIZE,0.2*TILESIZE))

            if bbh.collidepoint(pygame.mouse.get_pos()) and self.curpage == 'HelpMenu':
                bbh = Button(FONT.render('Back', 1, WHITE), self.screen, 0,3)
            elif not bbh.collidepoint(pygame.mouse.get_pos()) and self.curpage == 'HelpMenu':
                bbh = Button(FONT.render('Back', 1, FONT_COLOR), self.screen, 0,3)
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                if self.curpage == 'Turn2':
                    if sc1.collidepoint(pos):
                        ScoreCard(self.screen, players.Value, dicenumber2, sc1.Value)
                        #endplayerturn(self.screen, players)
                    elif sc2.collidepoint(pos):
                        ScoreCard(self.screen, players.Value, dicenumber2, sc2.Value)
                    elif sc3.collidepoint(pos):
                        ScoreCard(self.screen, players.Value, dicenumber2, sc3.Value)

                if self.curpage == 'PlayerSelect':
                    if len(self.players) == 2:
                        if self.pc1 == '-1' and self.pc2 == '-2' and self.pc3 == '-3' and self.pc4 == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = bpr.Value
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = bpb.Value
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = bpg.Value
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = bpy.Value
                        elif self.pc2 == '-2' and not self.pc1 == '-1' and self.pc3 == '-3' and self.pc4 == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpr.Value:
                                self.pc2 = bpr.Value
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpb.Value:
                                self.pc2 = bpb.Value
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpg.Value:
                                self.pc2 = bpg.Value
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpy.Value:
                                self.pc2 = bpy.Value 
                        CheckPlayers(self.screen, [self.pc1, self.pc2])
                        if not self.pc1 == '-1' and not self.pc2 == '-2':
                            self.players = [self.pc1,self.pc2]
                            bst = Button(FONT.render('Play', 1, FONT_COLOR), self.screen, 0,2)
                    elif len(self.players) == 3:
                        if self.pc1 == '-1' and self.pc2 == '-2' and self.pc3 == '-3' and self.pc4 == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = bpr.Value
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = bpb.Value
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = bpg.Value
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = bpy.Value
                        elif self.pc2 == '-2' and not self.pc1 == '-1' and self.pc3 == '-3' and self.pc4 == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpr.Value:
                                self.pc2 = bpr.Value
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpb.Value:
                                self.pc2 = bpb.Value
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpg.Value:
                                self.pc2 = bpg.Value
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpy.Value:
                                self.pc2 = bpy.Value
                        elif self.pc3 == '-3' and not self.pc1 == '-1' and not self.pc2 == '-2' and self.pc4 == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpr.Value and not self.pc2 == bpr.Value:
                                self.pc3 = bpr.Value
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpb.Value and not self.pc2 == bpb.Value:
                                self.pc3 = bpb.Value
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpg.Value and not self.pc2 == bpg.Value:
                                self.pc3 = bpg.Value
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpy.Value and not self.pc2 == bpy.Value:
                                self.pc3 = bpy.Value
                        CheckPlayers(self.screen, [self.pc1, self.pc2, self.pc3])
                        if not self.pc1 == '-1' and not self.pc2 == '-2' and not self.pc3 == '-3':
                            self.players = [self.pc1,self.pc2, self.pc3]
                            bst = Button(FONT.render('Play', 1, FONT_COLOR), self.screen, 0,2)
                    elif len(self.players) == 4:
                        if self.pc1 == '-1' and self.pc2 == '-2' and self.pc3 == '-3' and self.pc4 == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = bpr.Value
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = bpb.Value
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = bpg.Value
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect':
                                self.pc1 = bpy.Value
                        elif self.pc2 == '-2' and not self.pc1 == '-1' and self.pc3 == '-3' and self.pc4 == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpr.Value:
                                self.pc2 = bpr.Value
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpb.Value:
                                self.pc2 = bpb.Value
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpg.Value:
                                self.pc2 = bpg.Value
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpy.Value:
                                self.pc2 = bpy.Value
                        elif self.pc3 == '-3' and not self.pc1 == '-1' and not self.pc2 == '-2' and self.pc4 == '-4':
                            if bpr.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpr.Value and not self.pc2 == bpr.Value:
                                self.pc3 = bpr.Value
                            elif bpb.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpb.Value and not self.pc2 == bpb.Value:
                                self.pc3 = bpb.Value
                            elif bpg.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpg.Value and not self.pc2 == bpg.Value:
                                self.pc3 = bpg.Value
                            elif bpy.collidepoint(pos) and self.curpage == 'PlayerSelect' and not self.pc1 == bpy.Value and not self.pc2 == bpy.Value:
                                self.pc3 = bpy.Value
                        elif self.pc4 == '-4' and not self.pc1 == '-1' and not self.pc2 == '-2' and not self.pc3 == '-3':
                            if not self.pc1 == bpr.Value and not self.pc2 == bpr.Value and not self.pc3 == bpr.Value:
                                self.pc4 = bpr.Value
                            elif not self.pc1 == bpb.Value and not self.pc2 == bpb.Value and not self.pc3 == bpb.Value:
                                self.pc4 = bpb.Value
                            elif not self.pc1 == bpg.Value and not self.pc2 == bpg.Value and not self.pc3 == bpg.Value:
                                self.pc4 = bpg.Value
                            elif not self.pc1 == bpy.Value and not self.pc2 == bpy.Value and not self.pc3 == bpy.Value:
                                self.pc4 = bpy.Value
                        CheckPlayers(self.screen, [self.pc1, self.pc2, self.pc3, self.pc4])
                        if not self.pc1 == '-1' and not self.pc2 == '-2' and not self.pc3 == '-3' and not self.pc4 == '-4':
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

                    self.pc1 = '-1'
                    self.pc2 = '-2'
                    self.pc3 = '-3'
                    self.pc4 = '-4'

                    self.players = [self.pc1, self.pc2]

                elif bp3.collidepoint(pos) and self.curpage == 'PlayerSelect':
                    bp2 = Button(FONT.render('2', 1, FONT_COLOR), self.screen, 0,-2,2)
                    bp3 = Button(FONT.render('3', 1, WHITE), self.screen, 0,-1,3)
                    bp4 = Button(FONT.render('4', 1, FONT_COLOR), self.screen, 0,0,4)

                    bpr = Button(FONT.render('Red', 1, RED_BTN), self.screen, ((self.scr_width/6)*1, 1.7*OFFSET),0,1)
                    bpb = Button(FONT.render('Blue', 1, BLUE), self.screen, ((self.scr_width/6)*2, 1.7*OFFSET),0,0)
                    bpg = Button(FONT.render('Green', 1, GREEN), self.screen, ((self.scr_width/6)*4, 1.7*OFFSET),0,2)
                    bpy = Button(FONT.render('Yellow', 1, YELLOW), self.screen, ((self.scr_width/6)*5, 1.7*OFFSET),0,3)

                    self.pc1 = '-1'
                    self.pc2 = '-2'
                    self.pc3 = '-3'
                    self.pc4 = '-4'
                    self.players = [self.pc1, self.pc2, self.pc3]

                elif bp4.collidepoint(pos) and self.curpage == 'PlayerSelect':
                    bp2 = Button(FONT.render('2', 1, FONT_COLOR), self.screen, 0,-2,2)
                    bp3 = Button(FONT.render('3', 1, FONT_COLOR), self.screen, 0,-1,3)
                    bp4 = Button(FONT.render('4', 1, WHITE), self.screen, 0,0,4)

                    bpr = Button(FONT.render('Red', 1, RED_BTN), self.screen, ((self.scr_width/6)*1, 1.7*OFFSET),0,1)
                    bpb = Button(FONT.render('Blue', 1, BLUE), self.screen, ((self.scr_width/6)*2, 1.7*OFFSET),0,0)
                    bpg = Button(FONT.render('Green', 1, GREEN), self.screen, ((self.scr_width/6)*4, 1.7*OFFSET),0,2)
                    bpy = Button(FONT.render('Yellow', 1, YELLOW), self.screen, ((self.scr_width/6)*5, 1.7*OFFSET),0,3)

                    self.pc1 = '-1'
                    self.pc2 = '-2'
                    self.pc3 = '-3'
                    self.pc4 = '-4'
                    self.players = [self.pc1, self.pc2, self.pc3, self.pc4]

                if bst.collidepoint(pos):
                    if self.curpage == 'PlayerSelect' or self.curpage == 'Menu':
                        if len(self.players) >= 2:
                            start = False
                            for v in self.players:
                                if int(v) > -1:
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
                                td = Button(FONT_TEXT.render('Throw Dice', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
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
                elif bh.collidepoint(pos) and self.curpage == 'Menu':
                    #How to play page
                    pygame.display.set_caption('How to play Menu')
                    self.curpage = 'HelpMenu'
                    self.screen.fill(self.bg_color)
                    #Back btn op het scherm plaatsen
                    bbh = Button(FONT.render('Back', 1, FONT_COLOR), self.screen, 0,3)
                    #Informatie op het scherm zetten | Margin van 10%
                    Rules(screen)
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
                        bc = Button(FONT.render('Exit', 1, FONT_COLOR), self.screen, 0,1)
                elif throw_dice.collidepoint(pos) and self.curpage == 'Game':
                    dicenumber = Dice(self.screen)
                    pygame.time.delay(1000)             
                    ResetMap(self.screen, players)
   
                    throw_dice = Button(FONT_TEXT.render('Throw Dice', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                    sc1 = Button(FONT_TEXT.render('Clicklabel', 1, BLACK), self.screen, (21*TILESIZE,5*TILESIZE),0,1)
                    sc2 = Button(FONT_TEXT.render('Clicklabel', 1, BLACK), self.screen, (21*TILESIZE,6*TILESIZE),0,2)
                    sc3 = Button(FONT_TEXT.render('Clicklabel', 1, BLACK), self.screen, (21*TILESIZE,7*TILESIZE),0,3)   
                       
                    playerturn(self.screen, players, dicenumber)
                    players.Iterate(lambda x: x.Draw(self.screen,players))
                    x = players
                    while not x.IsEmpty:
                        if x.Value.Turn:
                            if x.Value.Tile.Index in [5, 15, 25, 35]:
                                pygame.draw.rect(screen, BLACK, (0, 0 , 250,30))
                                throw_dice_fight = Button(FONT_TEXT.render('Fight', 1, FONT_COLOR), self.screen, (2*TILESIZE,0.2*TILESIZE))
                                self.curpage = 'Turn2'
                        x = x.Tail
                elif throw_dice_fight.collidepoint(pos) and self.curpage == 'Turn2':
                    dicenumber2 = Dice(self.screen)
                    pygame.time.delay(1000)

            if mainloop:
                pygame.display.flip()
            else:
                pygame.quit()
                sys.exit()
            

screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption('Game Menu')
gm = Game(screen)
gm.run()