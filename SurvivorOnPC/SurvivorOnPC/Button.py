import pygame
from Constants import *

class Button:
    def __init__(self,label,pos=0, buttoncount=0):
        self.Label = label
        if(pos == 0):
            pos = SIZE[0] / 2 - label.get_rect().width / 2, (SIZE[1] / 2 - label.get_rect().height / 2) + buttoncount*60
        self.Pos = pos