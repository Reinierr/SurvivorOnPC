import pygame
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
BLACK = (0,0,0)

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

# game rules
REGELS =  Node("Select aantal spelers", 
          Node("Kies een kleur per gekozen speler",
          Node("Dobbel om aantal vakken te verplaatsen",
          Node("Kom je op een Fightvakje dan voer je een superfight uit.",
          Node("Kom je op een hoekvak van je tegenstander dan vecht je met die tegenstander",
          Node("Kom je op een vakje waar al een tegenstander staat dan vecht je met hem",
          Node("Per beurt wordt er maar 1 gevecht uitgevoerd Volgorde die wordt uitgevoerd",
          Node("Superfighter --> hoekfight --> vakfight",
          Node("Elke speler begint met 100 levenspunten en 15 conditiepunten",
          Node("De speler krijgt 10 levenspunten er bij als hij langs zijn eigen hoek komt (Max 100 levenspunten)",
          Node("De speler krijgt bij langs zijn eigen hoek komen zijn 15 conditiepunten terug (Max 15 conditiepunten)",
          Node("Als een speler 0 levenspunten heeft is hij verslagen",
          Node("Op de scorekaart staat de schade die je kan toebrengen bij een gegooide waarde",
          Node("Schade opties worden naar dobbelworp weergegeven en kosten conditiepunten",
          Node("Tussen 2 spelers word de schade hoog - laag = schade aan de speler met de laagste schade gedaan",
          Node("Have FUN ",Empty()))))))))))))))))

