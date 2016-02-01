import pygame, random, time
from Node import *
from Constants import *
 
def Dice(display): 
    size = TILESIZE*2        
    spot_size = size//10
    #Spots          
    middle_spot = int(size/2)
    top_spot =  int(size/4)             
    left_spot = int(size/4)               
    right_spot = size-left_spot
    bottom_spot = size-left_spot        
    rolling = 10 #Times that dice rolls             
    spot_colour = (BLACK)          
        
    for i in range(rolling):    
        random_int = random.randint(1,6)
        
        bgImage = pygame.image.load("Images\dice_bg.png")
        display.blit(pygame.transform.scale(bgImage, (2*TILESIZE,2*TILESIZE)),(1,1))                   
        
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