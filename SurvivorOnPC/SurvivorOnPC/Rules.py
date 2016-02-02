import pygame
from Constants import *
from Node import *
from Player import *
from Board import *
            
REGELS =  Node("To pause the game press P",
          Node("To force exit the game press ESC",
          Node("Select amount of players", 
          Node("Pick a color per chosen player",
          Node("Throw dice to move tiles",
          Node("When you land on a fight tile you have to fight a superfighter",
          Node("When you land on a corner tile you have to fight the enemy",
          Node("When you land on the same tile as another player you have to fight him",
          Node("Every turn only 1 fight is executed, in the following order:",
          Node("Superfighter --> corner fight --> tile fight",
          Node("Every player has 100 lifepoints and 15 conditionpoints",
          Node("The player gets 10 lifepoints everytime he crosses it's own corner(Max 100 lifepoints)",
          Node("The player gets 10 conditionpoints everytime he crosses it's own corner(Max 15 conditionpoins)",
          Node("When a player has 0 lifepoints he is defeated",
          Node("On the scorecard you can select the amount of damage to cause to the enemy player",
          Node("Damage options cost conditionpoints",
          Node("The damage is dealt by the following: high-low, the player with the lowest damage gets hurt",
          Node("Have FUN ",Empty()))))))))))))))))))

class Rules():
    def __init__(self, screen):
      ls = LINE_OFFSET
      rules = REGELS
      while not rules.IsEmpty:
          ls = ls + LINE_OFFSET
          information = FONT_TEXT.render(rules.Value, 1, FONT_COLOR_TEXT) 
          screen.blit(information,(SIZE[0] / 10, SIZE[1] / 10 + ls - LINE_OFFSET))
          rules = rules.Tail