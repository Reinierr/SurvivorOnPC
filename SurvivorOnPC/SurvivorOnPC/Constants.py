import pygame
from Node import *
pygame.init()

#screen size
SIZE = width, height = 1280, 720

#constants representing colors
BLUE = (71,106,165)
RED = (190,61,52)
GREEN = (119,182,60)
YELLOW = (244,234,61)
GREY = (200,200,200)
WHITE = (255,255,254)
BLACK = (0,0,0)

#boardsize and tilesize
TILESIZE = int (SIZE[0] / 26)
MAPWIDTH = 26
MAPHEIGHT = 14
OFFSET = ((MAPWIDTH - MAPHEIGHT) / 2) * TILESIZE

#text
FONT = pygame.font.SysFont(None, 50)
FONT_COLOR = RED
FONT_TEXT = pygame.font.SysFont(None, 30)
FONT_COLOR_TEXT = WHITE
LINE_OFFSET = 25

# game rules
REGELS =  Node("select aantal spelers", 
          Node("kies een kleur per gekozen speler",
          Node("de speler links boven begin",
          Node("4. ",Empty()))))

