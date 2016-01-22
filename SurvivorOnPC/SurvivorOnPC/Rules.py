import pygame
from Constants import *
from Node import *

REGELS =  Node("Select aantal spelers", 
          Node("Kies een kleur per gekozen speler",
          Node("Dobbel om aantal vakken te verplaatsen",
          Node("Kom je op een Fightvakje dan voer je een superfight uit.",
          Node("Kom je op een hoekvak van je tegenstander dan vecht je met die tegenstander",
          Node("Kom je op een vakje waar al een tegenstander staat dan vecht je met hem",
          Node("Per beurt wordt er maar 1 gevecht uitgevoerd Volgorde die wordt uitgevoerd",
          Node("Superfighter --> hoekfight --> vakfight",
          Node("Elke speler begint met 100 levenspunten en 15 conditiepunten",
          Node("De speler krijgt 10 levenspunten er bij als hij op zijn eigen hoek komt (Max 100 levenspunten)",
          Node("De speler krijgt bij langs zijn eigen hoek komen zijn 15 conditiepunten terug (Max 15 conditiepunten)",
          Node("Als een speler 0 levenspunten heeft is hij verslagen",
          Node("Op de scorekaart staat de schade die je kan toebrengen bij een gegooide waarde",
          Node("Schade opties worden naar dobbelworp weergegeven en kosten conditiepunten",
          Node("Tussen 2 spelers word de schade hoog - laag = schade aan de speler met de laagste schade gedaan",
          Node("Have FUN ",Empty()))))))))))))))))

class Rules():
    def __init__(self, screen):
      Iterate
        ls = LINE_OFFSET
        rules = REGELS
        while not rules.IsEmpty:
            ls = ls + LINE_OFFSET
            information = FONT_TEXT.render(rules.Value, 1, FONT_COLOR_TEXT) 
            screen.blit(information,(SIZE[0] / 10, SIZE[1] / 10 + ls))
            rules = rules.Tail