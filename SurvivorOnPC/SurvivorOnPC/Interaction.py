﻿import pygame
import sys

pygame.init()

scr_width = 1280
scr_height = 720 

class GameMenu():
    def __init__(self, screen):
        self.screen = screen
        self.scr_width = screen.get_rect().width
        self.scr_height = screen.get_rect().height
        self.bg_color = (0,0,0)

        self.font = pygame.font.SysFont(None, 30)
        self.font_color = (255, 255, 255)
        self.curpage = 'Menu'
        
        information = 'Hier komt de tekst van de how to play pagina'
        self.information = self.font.render(information, 1, self.font_color) 

        #buttons
        labels = self.font.render('Start', 1, self.font_color)
        labelc = self.font.render('Exit', 1, self.font_color)
        labelh = self.font.render('How to play', 1, self.font_color)
        labelb = self.font.render('Back', 1, self.font_color)
        
        self.start = [labels, self.scr_width / 2 - labels.get_rect().width / 2, self.scr_height / 2 - 60]
        self.close = [labelc, self.scr_width / 2 - labelc.get_rect().width / 2, self.scr_height / 2]
        self.help = [labelh, self.scr_width / 2 - labelh.get_rect().width / 2, self.scr_height / 2 - 30]
        self.back = [labelb, self.scr_width / 2 - labelb.get_rect().width / 2, self.scr_height - 50]

    def run(self):
        mainloop = True
        self.screen.fill(self.bg_color)

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
                    #Start actual game
                    print('start game')
                    mainloop = False
                    sys.exit()
                elif bh.collidepoint(pos) and self.curpage == 'Menu':
                    pygame.display.set_caption('How to play Menu')
                    self.curpage = 'HelpMenu'
                    self.screen.fill(self.bg_color)
                    bb = self.screen.blit(self.back[0], (self.back[1],self.back[2]))
                    print(self.scr_width, self.scr_height)
                    self.screen.blit(self.information,(self.scr_width / 10,self.scr_height / 10))
                elif bc.collidepoint(pos) and self.curpage == 'Menu':
                    mainloop = False
                    sys.exit()
                elif bb.collidepoint(pos) and self.curpage == 'HelpMenu':
                    pygame.display.set_caption('Game Menu')
                    self.curpage = 'Menu'
                    self.screen.fill(self.bg_color)
                    bs = self.screen.blit(self.start[0], (self.start[1],self.start[2]))
                    bh = self.screen.blit(self.help[0], (self.help[1],self.help[2]))
                    bc = self.screen.blit(self.close[0], (self.close[1],self.close[2]))
            

screen = pygame.display.set_mode((scr_width, scr_height))

pygame.display.set_caption('Game Menu')
gm = GameMenu(screen)
gm.run()