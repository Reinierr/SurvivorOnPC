import pygame
import os
import time
from Node import *
from Tile import *
from Constants import * 

pygame.init()
screen = pygame.display.set_mode(SIZE)

tilemap = Empty()
tilemap = Tile.Board()
Iterate(tilemap, lambda x: x.Draw(screen))

centerImage = pygame.image.load("Images\center.png")
screen.blit(pygame.transform.scale(centerImage, (10*TILESIZE,10*TILESIZE)),(OFFSET + (2*TILESIZE),2*TILESIZE))

#add fight images
fightImage = pygame.transform.scale(pygame.image.load("Images\Fight.png"), (2*TILESIZE,1*TILESIZE))
screen.blit(fightImage, (OFFSET + (6*TILESIZE),1*(TILESIZE*0.5))) #top
#screen.blit(pygame.transform.rotate(fightImage,180), (OFFSET + (6*TILESIZE),1*(TILESIZE*0.5))) #top
screen.blit(fightImage, (OFFSET + (6*TILESIZE),12*TILESIZE + 1*(TILESIZE*0.5))) #bottom
screen.blit(pygame.transform.rotate(fightImage,90), (OFFSET + (12*TILESIZE) + 1*(TILESIZE*0.5),6*TILESIZE)) #left
screen.blit(pygame.transform.rotate(fightImage,270), (OFFSET + 1*(TILESIZE*0.5),6*TILESIZE)) #right

pygame.display.update()

time.sleep(5)

def Main():
  #game loop
  print("<3")

Main()  