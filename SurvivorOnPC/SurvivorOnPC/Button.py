import pygame
from Constants import *

class Button:
    def __init__(self,label, screen, pos=0, buttoncount=0, value=0):
        self.Label = label
        self.Screen = screen
        self.Value = value
        if(pos == 0):
            pos = SIZE[0] / 2 - label.get_rect().width / 2, (SIZE[1] / 2 - label.get_rect().height / 2) + buttoncount*60
        self.Pos = pos
        self.collidepoint = self.Screen.blit(label, pos).collidepoint

def ButtonHover(screen,curpage,buttonname,curpage_name ,label,buttoncount,value):
     #Start button hover
    if buttonname.collidepoint(pygame.mouse.get_pos()) and curpage == curpage_name:
        buttonname = Button(FONT.render(label, 1, WHITE), screen, buttoncount,value)
    elif not buttonname.collidepoint(pygame.mouse.get_pos()) and curpage == curpage_name:
        buttonname = Button(FONT.render(label, 1, FONT_COLOR), screen, buttoncount,value)