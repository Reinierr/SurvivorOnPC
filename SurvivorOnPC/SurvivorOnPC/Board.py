﻿import pygame
from Constants import *
from Node import *
from Tile import *
from Button import *

def CreateMap():
  tilemap = Empty()
  for row in range(MAPHEIGHT):
    for column in range(MAPWIDTH):
      tilemap = Node(Tile(Vector2RC(column,row),Tile.Color(column,row)),tilemap)
  return tilemap

def DrawImages(screen):
  centerImage = pygame.image.load("Images\center.png")
  screen.blit(pygame.transform.scale(centerImage, (10*TILESIZE,10*TILESIZE)),(OFFSET + (2*TILESIZE),2*TILESIZE))

  #add fight images
  fightImage = pygame.transform.scale(pygame.image.load("Images\Fight.png"), (2*TILESIZE,1*TILESIZE))
  screen.blit(fightImage, (OFFSET + (6*TILESIZE),(TILESIZE*0.5))) #top
  screen.blit(fightImage, (OFFSET + (6*TILESIZE),12*TILESIZE + (TILESIZE*0.5))) #bottom
  screen.blit(pygame.transform.rotate(fightImage,90), (OFFSET + (12*TILESIZE) + 1*(TILESIZE*0.5),6*TILESIZE)) #left
  screen.blit(pygame.transform.rotate(fightImage,270), (OFFSET + (TILESIZE*0.5),6*TILESIZE)) #right

  #draw borders around corner tiles
  rectBorder = pygame.transform.scale(pygame.image.load("Images\hoek.png"), (2*TILESIZE,2*TILESIZE))
  screen.blit(rectBorder, (OFFSET,0)) #top-left
  screen.blit(rectBorder, (OFFSET+(12*TILESIZE),0)) #top-right
  screen.blit(rectBorder, (OFFSET,12*TILESIZE)) #bottom-left
  screen.blit(rectBorder, (OFFSET+(12*TILESIZE),12*TILESIZE)) #bottom-right

def EmptyScreen(color):
  screenmap = Empty()
  for row in range(MAPHEIGHT):
    for column in range(MAPWIDTH):
      screenmap = Node(Tile(Vector2RC(column,row),color),tilemap)
  return screenmap