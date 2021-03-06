﻿import pygame
from Node import *
pygame.init()

#screen size
SIZE = width, height = 1280, 720

#constants representing colors
BLUE = (71,106,165)
RED = (190,61,52)
RED_BTN = (255,34,33)
GREEN = (119,182,60)
YELLOW = (244,234,61)
GREY = (200,200,200)
WHITE = (255,255,254)
ORANGE = (255,165,0)
GREEN_BTN = (0,204,0)
BLACK = (0,0,0)
COLORLIST = [BLUE, RED, GREEN, YELLOW]
COLORLIST2 = ['BLUE', 'RED', 'GREEN', 'YELLOW']
#boardsize and tilesize
TILESIZE = int (SIZE[0] / 26)
MAPWIDTH = 26
MAPHEIGHT = 14
OFFSET = ((MAPWIDTH - MAPHEIGHT) / 2) * TILESIZE

#text
FONT = pygame.font.SysFont(None, 50)
FONT_COLOR = RED_BTN
FONT_TEXT = pygame.font.SysFont(None, 30)
FONT_COLOR_TEXT = WHITE
LINE_OFFSET = 25

#HOMETILES = [
#    {'color': 'blue', 'home': 0, 'number': 0},
#    {'color': 'red', 'home': 10, 'number': 1},
#    {'color': 'green', 'home': 20, 'number': 2},
#    {'color': 'yellow', 'home': 30, 'number': 3}
#  ]

CORNERTILES = [0,10,20,30]

#sounds
punch = pygame.mixer.Sound('Sounds/Punch_Sound.wav')
winning = pygame.mixer.Sound('Sounds/Winning_Applause.wav')                                        