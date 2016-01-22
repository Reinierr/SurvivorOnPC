import pygame
from Constants import *

class Rules():
    def __init__(self, screen):
        ls = LINE_OFFSET
        rules = REGELS
        while not rules.IsEmpty:
            ls = ls + LINE_OFFSET
            information = FONT_TEXT.render(rules.Value, 1, FONT_COLOR_TEXT) 
            screen.blit(information,(SIZE[0] / 10, SIZE[1] / 10 + ls))
            rules = rules.Tail