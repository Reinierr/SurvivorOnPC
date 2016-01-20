﻿class Player:
    def __init__(self,position,texture):
        self.position = position
        self.texture = texture

class ScoreCard:
    def __init__(self,name,color,dice_score,damage,condition):
        self.name = name
        self.color = color
        self.dice_score = dice_score
        self.damage = damage
        self.condition = condition

class SuperFightCard:
    def __init__(self,name,dice_score,damage):
        self.name = name
        self.dice_score = dice_score
        self.damage = damage


import pygame, random, time
def Dice():
    size = 256         
    spot_size = size//10            
    middle_spot = int(size/2)
    top_spot =  int(size/4)             
    left_spot = int(size/4)               
    right_spot = size-left_spot
    bottom_spot = size-left_spot        
    rolling = 10  # times that dice rolls before stopping
    background_color = (0,0,0)              
    spot_colour = (0,127,127)          
 
    display = pygame.display.set_mode((size, size))
    display.fill(background_color)
    pygame.display.set_caption("Dice Simulator")
    for i in range(rolling):    
        random_int = random.randint(1,6)                   
        display.fill(background_color)                          
    
        if random_int % 2 == 1:
            pygame.draw.circle(display,spot_colour,(middle_spot,middle_spot),spot_size)# middle spot

        if random_int == 2 or random_int == 3 or random_int == 4 or random_int == 5 or random_int == 6:
            pygame.draw.circle(display,spot_colour,(left_spot,bottom_spot),spot_size)# left bottom
            pygame.draw.circle(display,spot_colour,(right_spot,top_spot),spot_size)# right top

        if random_int == 4 or random_int == 5 or random_int == 6:
            pygame.draw.circle(display,spot_colour,(left_spot,top_spot),spot_size)# left top
            pygame.draw.circle(display,spot_colour,(right_spot,bottom_spot),spot_size)# right bottom

        if random_int == 6:
            pygame.draw.circle(display,spot_colour,(middle_spot,bottom_spot),spot_size)# middle bottom
            pygame.draw.circle(display,spot_colour,(middle_spot,top_spot),spot_size)# middle top
     
        pygame.display.flip()
        time.sleep(0.2)
    

    return random_int

dicenumber = Dice()   
print (dicenumber)


