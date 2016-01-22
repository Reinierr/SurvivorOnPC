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
#from Dice import *

pygame.init()

def GameBoard(screen):
  screen.fill(BLACK)
  tilemap = Empty()
  tilemap = CreateMap()
  Iterate(tilemap, lambda x: x.Draw(screen))
  DrawImages(screen)

  pygame.display.set_caption('SurvivorOnPC')
  pygame.display.update()

class Game():          
    def __init__(self, screen):
        self.screen = screen
        self.scr_width = screen.get_rect().width
        self.scr_height = screen.get_rect().height
        self.bg_color = (BLACK)
        
        self.curpage = 'Menu'
        
        self.bg = pygame.image.load("Images\menubg.png")
        self.bgoffset = (self.scr_width - self.scr_height) / 2

        #Fix for name error on buttons
        self.dummy = FONT.render('Dummy', 1, (0,0,0))

    def run(self):
        mainloop = True
        self.screen.fill(self.bg_color)
        self.screen.blit(pygame.transform.scale(self.bg, (self.scr_height,self.scr_height)),(self.bgoffset,0))
        
        bs = Button(FONT.render('Start', 1, FONT_COLOR), self.screen, 0,-1)
        bh = Button(FONT.render('How to play', 1, FONT_COLOR), self.screen, 0,0)
        bc = Button(FONT.render('Exit', 1, FONT_COLOR), self.screen, 0,1)
        bbg = self.screen.blit(self.dummy, (0,0))
        bbh = self.screen.blit(self.dummy, (0,0))

        while mainloop:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

            pygame.display.flip()

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

                if bs.collidepoint(pos) and self.curpage == 'Menu':
                    #Start het spel
                    self.curpage = 'Game'
                    GameBoard(screen)
                    backButton = Button(FONT_TEXT.render('Back to menu', 1, FONT_COLOR), self.screen, (23*TILESIZE,0.2*TILESIZE))
                    bbg = self.screen.blit(backButton.Label,backButton.Pos)
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
                    sys.exit()
                elif bbh.collidepoint(pos) or bbg.collidepoint(pos):
                    if self.curpage == 'Game' or self.curpage == 'HelpMenu':
                        pygame.display.set_caption('Game Menu')
                        self.curpage = 'Menu'
                        self.screen.fill(self.bg_color)
                        self.screen.blit(pygame.transform.scale(self.bg, (self.scr_height,self.scr_height)),(self.bgoffset,0))
                        #Btns start/how to play/exit op het scherm plaatsen
                        bs = Button(FONT.render('Start', 1, FONT_COLOR), self.screen, 0,-1)
                        bh = Button(FONT.render('How to play', 1, FONT_COLOR), self.screen, 0,0)
                        bc = Button(FONT.render('Exit', 1, FONT_COLOR), self.screen, 0,1)

            

screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption('Game Menu')
gm = Game(screen)
gm.run()