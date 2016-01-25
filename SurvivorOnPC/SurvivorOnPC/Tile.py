import pygame
from Constants import *
from Node import *
 
#VECTOR2 CLASS
class Vector2:
  def __init__(self, x, y):
    self.X = x
    self.Y = y

class Vector2RC:
  def __init__(self, col, row):
    self.Col = col
    self.Row = row

class Tile:
  def __init__(self, pos, color, index =None):
    self.Position = pos
    self.Color = color
    
#    rowBlue = 0
#    colRed = 11
#    rowGreen = 30
#    colYellow = 39

#    column = pos.Col
#    row = pos.Row

#    if not(column < 7) and not(column > 18) and not(column == 12) and not(row in [0,6,13]) and not((column in range(8,18)) and (row in range(2,12))):
#      if(row == 1):
#        index = rowBlue
#        rowBlue += 1
#      elif(column == 18):
#        index = colRed
#        colRed += 1
#      elif(row == 12):
#        index = rowGreen
#        rowGreen -= 1
#      elif(column == 7):
#        index = colYellow
#        colYellow -= 1
#    else:
#      index = None

    self.Index = index

#    print(self)

  def __str__(self):
    return "Col: " + str(self.Position.Col) + " Row: " + str(self.Position.Row) + " Index: " + str(self.Index)

  def Draw(self, screen):
    pygame.draw.rect(screen, self.Color, (self.Position.Col * TILESIZE, self.Position.Row * TILESIZE, TILESIZE,TILESIZE))

  def Color(column,row):
    if(column < 6 or column > 19):
      return BLACK
    elif(column in [6,7,8] and row in [0,1,2]):
      return BLUE
    elif(column in [17,18,19] and row in [0,1,2]):
      return RED
    elif(column in [6,7,8] and row in [11,12,13]):
      return YELLOW
    elif(column in [17,18,19] and row in [11,12,13]):
      return GREEN
    elif(column in [9,11,14,16] or row in [3,5,8,10]):
      return GREY
    elif(column in [10,12,13,15] or row in [4,6,7,9]):
      return WHITE
    else:
      return BLACK

#POSSIBLETILES = Empty()
#for row in range(MAPHEIGHT):
#  for column in range(MAPWIDTH):
#    if not(column < 7) and not(column > 18) and not(column == 12) and not(row in [0,6,13]) and not((column in range(8,18)) and (row in range(2,12))):
#      POSSIBLETILES = Node(Tile(Vector2RC(column,row),Tile.Color(column,row)),POSSIBLETILES)

def IndexFix(list):

  rowBlue = 0
  colRed = 11
  rowGreen = 30
  colYellow = 39
  newlist = Empty()
  while not list.IsEmpty:
      if not(list.Value.Position.Col < 7) and not(list.Value.Position.Col > 18) and not(list.Value.Position.Col == 12) and not(list.Value.Position.Row in [0,6,13]) and not((list.Value.Position.Col in range(8,18)) and (list.Value.Position.Row in range(2,12))):
        if(list.Value.Position.Row == 1):
          newlist = Node(Tile((list.Value.Position.Col, 1),list.Value.Color, rowBlue),newlist)
          rowBlue += 1
        elif(list.Value.Position.Col == 18):
          newlist = Node(Tile((list.Value.Position.Col, 1),list.Value.Color, colRed),newlist)
          colRed += 1
        elif(list.Value.Position.Row == 12):
          newlist = Node(Tile((list.Value.Position.Col, 1),list.Value.Color, rowGreen),newlist)
          rowGreen -= 1
        elif(list.Value.Position.Col == 7):
          newlist = Node(Tile((list.Value.Position.Col, 1),list.Value.Color, colYellow),newlist)
          colYellow -= 1
      else:
        index = None
      list = list.Tail
  return newlist