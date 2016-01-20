import pygame
import os
from Node import *
from Tile import *
from Constants import * 
from Board import *
from Button import *

pygame.init()

def GameBoard(screen):
  screen.fill(BLACK)
  tilemap = Empty()
  tilemap = Board.CreateMap()
  Iterate(tilemap, lambda x: x.Draw(screen))
  Board.DrawImages(screen)

  pygame.display.set_caption('SurvivorOnPC')
  pygame.display.update()

class GameMenu():
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
        information = 'How to play: Survivor'
        self.information = self.font_text.render(information, 2, self.font_color_text) 

        #Button labels
        self.start = Button(FONT.render('Start', 1, FONT_COLOR))
        self.close = Button(FONT.render('Exit', 1, FONT_COLOR))
        self.help = Button(FONT.render('How to play', 1, FONT_COLOR))
        self.back = Button(FONT.render('Back', 1, FONT_COLOR))

    def run(self):
        mainloop = True
        self.screen.fill(self.bg_color)
        self.screen.blit(pygame.transform.scale(self.bg, (self.scr_height,self.scr_height)),(self.bgoffset,0))
        
        bs = self.screen.blit(self.start[0], (self.start[1],self.start[2]))
        bh = self.screen.blit(self.help[0], (self.help[1],self.help[2]))
        bc = self.screen.blit(self.close[0], (self.close[1],self.close[2]))
        while mainloop:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

            pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if bs.collidepoint(pos) and self.curpage == 'Menu':
                    #Start het spel
                    GameBoard(screen)
                elif bh.collidepoint(pos) and self.curpage == 'Menu':
                    pygame.display.set_caption('How to play Menu')
                    self.curpage = 'HelpMenu'
                    self.screen.fill(self.bg_color)
                    #Back btn op het scherm plaatsen
                    bb = self.screen.blit(self.back.Label, self.back.Pos)
                    #Informatie op het scherm zetten | Margin van 10%
                    self.screen.blit(self.information,(self.scr_width / 10,self.scr_height / 10))
                elif bc.collidepoint(pos) and self.curpage == 'Menu':
                    #Exit game, stop loop en exit de console
                    mainloop = False
                    sys.exit()
                elif bb.collidepoint(pos) and self.curpage == 'HelpMenu':
                    pygame.display.set_caption('Game Menu')
                    self.curpage = 'Menu'
                    self.screen.fill(self.bg_color)
                    self.screen.blit(pygame.transform.scale(self.bg, (self.scr_height,self.scr_height)),(self.bgoffset,0))
                    #Btns start/how to play/exit op het scherm plaatsen
                    bs = self.screen.blit(self.start[0], (self.start[1],self.start[2]))
                    bh = self.screen.blit(self.help[0], (self.help[1],self.help[2]))
                    bc = self.screen.blit(self.close[0], (self.close[1],self.close[2]))
            

screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption('Game Menu')
gm = GameMenu(screen)
gm.run()