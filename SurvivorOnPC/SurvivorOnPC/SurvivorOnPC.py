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
from Dice import *

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

        self.font = FONT
        self.font_color = FONT_COLOR
        self.font_text = FONT_TEXT
        self.font_color_text = FONT_COLOR_TEXT
        
        self.curpage = 'Menu'
        
        self.boxglove = pygame.image.load("Images\glove_red.png")
        self.bg = pygame.image.load("Images\menubg.png")
        self.bgoffset = (self.scr_width - self.scr_height) / 2

        #Button labels
        self.start = Button(FONT.render('Start', 1, FONT_COLOR),0,-1)
        self.help = Button(FONT.render('How to play', 1, FONT_COLOR),0,0)
        self.close = Button(FONT.render('Exit', 1, FONT_COLOR),0,1)
        self.back = Button(FONT.render('Back', 1, FONT_COLOR),0,3)
        self.dummy = FONT.render('Dummy', 1, (0,0,0))

    def run(self):
        mainloop = True
        self.screen.fill(self.bg_color)
        self.screen.blit(pygame.transform.scale(self.bg, (self.scr_height,self.scr_height)),(self.bgoffset,0))
        
        bs = self.screen.blit(self.start.Label, self.start.Pos)
        bh = self.screen.blit(self.help.Label, self.help.Pos)
        bc = self.screen.blit(self.close.Label, self.close.Pos)
        bbg = self.screen.blit(self.dummy, (0,0))
        bbh = self.screen.blit(self.dummy, (0,0))

        #Start button hover
        if bs.collidepoint(pygame.mouse.get_pos()) and self.curpage == 'Menu':
            self.start = Button(FONT.render('Start', 1, WHITE),0,-1)
            bs = self.screen.blit(self.start.Label, self.start.Pos)
        else:
            self.start = Button(FONT.render('Start', 1, RED),0,-1)
            bs = self.screen.blit(self.start.Label, self.start.Pos)

        #How to play hover
        if bh.collidepoint(pygame.mouse.get_pos()) :
            self.help = Button(FONT.render('How to play', 1, WHITE),0,0)
            bh = self.screen.blit(self.help.Label, self.help.Pos)
        else:
            self.help = Button(FONT.render('How to play', 1, RED),0,0)
            bh = self.screen.blit(self.help.Label, self.help.Pos)

        #Back button
        if bc.collidepoint(pygame.mouse.get_pos()) :
            self.close = Button(FONT.render('Exit', 1, WHITE),0,1)
            bc = self.screen.blit(self.close.Label, self.close.Pos)
        else:
            self.close = Button(FONT.render('Exit', 1, RED),0,1)
            bc = self.screen.blit(self.close.Label, self.close.Pos)

        while mainloop:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

            pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if bs.collidepoint(pos) and self.curpage == 'Menu':
                    #Start het spel
                    self.curpage = 'Game'
                    GameBoard(screen)
                    backButton = Button(FONT_TEXT.render('Back to menu', 1, FONT_COLOR),(23*TILESIZE,0.2*TILESIZE))
                    bbg = self.screen.blit(backButton.Label,backButton.Pos)
                elif bh.collidepoint(pos) and self.curpage == 'Menu':
                    pygame.display.set_caption('How to play Menu')
                    self.curpage = 'HelpMenu'
                    self.screen.fill(self.bg_color)
                    #Back btn op het scherm plaatsen
                    bbh = self.screen.blit(self.back.Label, self.back.Pos)
                    #Informatie op het scherm zetten | Margin van 10%
                    ls = LINE_OFFSET
                    rules = REGELS
                    while not rules.IsEmpty:
                        ls = ls + LINE_OFFSET
                        information = self.font_text.render(rules.Value, 1, self.font_color_text) 
                        self.screen.blit(information,(self.scr_width / 10,self.scr_height / 10 + ls))
                        rules = rules.Tail
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
                        bs = self.screen.blit(self.start.Label, self.start.Pos)
                        bh = self.screen.blit(self.help.Label, self.help.Pos)
                        bc = self.screen.blit(self.close.Label, self.close.Pos)

            

screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption('Game Menu')
gm = Game(screen)
gm.run()