import pygame
from Node import *
from Dice import *
from Constants import *

class ScoreCard:
  def __init__(self,name,color,dice_score,damage,condition):
    self.Name = name
    self.Color = color
    self.Dice_score = dice_score
    self.Damage = damage
    self.Condition = condition

class SuperFightCard:
  def __init__(self,name,dice_score,damage):
    self.Name = name
    self.Dice_score = dice_score
    self.Damage = damage
   
def ScoreCard(screen, player, dicenumber):
    
    return True

def SuperFight(screen, player, dicenumber):
    random_dice = random.randint(0,6)
    fighter_dmg = 0
    #handle scorecards with dicenumber< < <
    player_dmg = ScoreCard(screen, player, dicenumber)
    player_dmg = 0
    fighter_index = random.randrange(0,len(listfighters))
    fighter = listfighters[fighter_index]
    print(fighter_index)
    #fix voor iets... geen idee waaarom HAHAH!!
    superFighter1 = fighterlists[0]
    superFighter2 = fighterlists[1]
    superFighter3 = fighterlists[2]
    if fighter_index < 6:
        while not superFighter1.IsEmpty:
            if superFighter1.Value[2] == fighter_index:
                if superFighter1.Value[1] == random_dice:
                    fighter_dmg = superFighter1.Value[0]
            superFighter1 = superFighter1.Tail
    elif fighter_index in range(6,12):
        while not superFighter2.IsEmpty:
            if superFighter2.Value[2] == fighter_index:
                if superFighter2.Value[1] == random_dice:
                    fighter_dmg = superFighter2.Value[0]
            superFighter2 = superFighter2.Tail
    elif fighter_index > 12:
        while not superFighter3.IsEmpty:
            if superFighter3.Value[2] == fighter_index:
                if superFighter3.Value[1] == random_dice:
                    fighter_dmg = superFighter3.Value[0]
            superFighter3 = superFighter3.Tail
    resultdmg = fighter_dmg - player_dmg 
    if resultdmg > 0:
        superfight = FONT_TEXT.render('Superfight! '+str(fighter)+' hit you for '+str(fighter_dmg)+' damage!', 1, RED_BTN)
    else:
        superfight = FONT_TEXT.render('Superfight! You defended yourself from '+str(fighter), 1, RED_BTN)
    screen.blit(superfight,(SIZE[0]-superfight.get_rect().width, SIZE[1] - 25))
    return resultdmg if resultdmg > 0 else 0

#Player damage / condition outcome
def DaCo(damage,condition):
    print(damage)
    print(condition)

def playercard(dicenumber, color):
    Dice_score = 1   
    #Dice_score = dicenumber
    playername = 'test123'
    playercolor = color
    damage = 11
    if playercolor == 10:
        if Dice_score == 1:
            player = ScoreCard(playername, playercolor, 1, [10, 20, 30], [1, 2, 3])
            return int(player)
            
        elif Dice_score == 2:
            player = ScoreCard(playername, playercolor, 2, [10, 20, 30], [1, 2, 3])
        elif Dice_score == 3:
            player = ScoreCard(playername, playercolor, 3, [10, 20, 30], [1, 2, 3])
        elif Dice_score == 4:
            player = ScoreCard(playername, playercolor, 4, [10, 20, 30], [1, 2, 3])
        elif Dice_score == 5:
            player = ScoreCard(playername, playercolor, 5, [10, 20, 30], [1, 2, 3])
        else:
            player = ScoreCard(playername, playercolor, 6, [10, 20, 30], [1, 2, 3])

    elif playercolor == 'green':
        player = ScoreCard(playername, playercolor, 1, [10, 20, 30], [1, 2, 3])
    elif playercolor == 'blue':
        player = ScoreCard(playername, playercolor, 1, [10, 20, 30], [1, 2, 3])
    else:
        player = ScoreCard(playername, playercolor, 1, [10, 20, 30], [1, 2, 3])
    
#Superfighter cards, dicerolls = dicenumber and damage is random.
def super(dicenumber):
    Dice_score = dicenumber
    
    D = random.randint(0,2)
    fighters = ['terry crews','jason statham','jet ri'] 
    sfc = str(fighters[random.randint(0,2)])
    #sfc = 'rocky belboa'
    ##For Rocky Belboa superfightercard, damage, dicerolls ect
    if sfc == 'terry crews':
        if Dice_score == 1:
            superfighter = SuperFightCard( sfc, 1, 10)
            return int(superfighter.Damage)
        elif Dice_score == 2:
            superfighter = SuperFightCard( sfc, 2, 15)
            return int(superfighter.Damage)

        elif Dice_score == 3:
            superfighter = SuperFightCard( sfc, 3, 25)
            return int(superfighter.Damage)

        elif Dice_score == 4:
            superfighter = SuperFightCard( sfc, 4, 20)
            return int(superfighter.Damage)

        elif Dice_score == 5:
            superfighter = SuperFightCard( sfc, 5, 15)
            return int(superfighter.Damage)

        else:
            superfighter = SuperFightCard( sfc, 6, 10)
            return int(superfighter.Damage)

    ##For manny pecquiao superfightercard, damage, dicerolls ect    
    elif sfc == 'jason statham':
        if Dice_score == 1:
            superfighter = SuperFightCard( sfc, 1, 15)
            return int(superfighter.Damage)


        elif Dice_score == 2:
            superfighter = SuperFightCard( sfc, 2, 17)
            return int(superfighter.Damage)

        elif Dice_score == 3:
            superfighter = SuperFightCard( sfc, 3, 19)
            return int(superfighter.Damage)

        elif Dice_score == 4:
            superfighter = SuperFightCard( sfc, 4, 21)
            return int(superfighter.Damage)

        elif Dice_score == 5:
            superfighter = SuperFightCard( sfc, 5, 23)
            return int(superfighter.Damage)

        else:
            superfighter = SuperFightCard( sfc, 6, 26)
            return int(superfighter.Damage)

    ##For Mike Tysen superfightercard, damage, dicerolls ect
    else:
        if Dice_score == 1:
            superfighter = SuperFightCard( 'jet ri', 1, 10)
            return int(superfighter.Damage)

        elif Dice_score == 2:
            superfighter = SuperFightCard( 'jet ri', 2, 30)
            return int(superfighter.Damage)

        elif Dice_score == 3:
            superfighter = SuperFightCard( 'jet ri', 3, 12)
            return int(superfighter.Damage)

        elif Dice_score == 4:
            superfighter = SuperFightCard( 'jet ri', 4, 25)
            return int(superfighter.Damage)

        elif Dice_score == 5:
            superfighter = SuperFightCard( 'jet ri', 5,14)
            return int(superfighter.Damage)

        else:
            superfighter = SuperFightCard( 'jet ri', 6, 23)
            return int(superfighter.Damage)

#[Schade, Conditie, Dice, Color]
                            #-Rocky Belboa- 0/Blue#                                        
scorecardblue = Node([10,2,1,0],Node([20,5,1,0],Node([30,8,1,0],
             Node([8,3,2,0],Node([13,4,2,0],Node([17,5,2,0],
             Node([3,1,3,0],Node([9,2,3,0],Node([19,3,3,0],
             Node([5,2,4,0],Node([11,3,4,0],Node([15,5,4,0],
             Node([7,2,5,0],Node([12,3,5,0],Node([16,4,5,0],
             Node([2,1,6,0],Node([4,2,6,0],Node([6,3,6,0], Empty())))))))))))))))))) 
                            #-Mike Tysen- 1/Red#
scorecardred = Node([5,2,1,1],Node([11,3,1,1],Node([15,5,1,1], 
             Node([3,1,2,1],Node([9,2,2,1],Node([19,3,2,1],
             Node([2,1,3,1],Node([4,2,3,1],Node([6,3,3,1],
             Node([7,2,4,1],Node([12,3,4,1],Node([16,4,4,1],
             Node([8,3,5,1],Node([13,4,5,1],Node([17,5,5,1],
             Node([10,3,6,1],Node([20,3,6,1],Node([30,3,6,1], Empty())))))))))))))))))) 
                            #-Badr Heri- 2/Green#      
scorecardgreen = Node([1,1,1,2],Node([9,2,1,2],Node([19,3,1,2],
             Node([5,2,2,2],Node([11,3,2,2],Node([15,5,2,2],
             Node([7,2,3,2],Node([12,3,3,2],Node([16,4,3,2],
             Node([2,1,4,2],Node([4,2,4,2],Node([6,3,4,2],
             Node([10,2,5,2],Node([20,5,5,2],Node([30,8,5,2],
             Node([8,3,6,2],Node([13,4,6,2],Node([17,5,6,2], Empty())))))))))))))))))) 
                            #-Manny Pecquiao- 3/Yellow#   
scorecardyellow = Node([8,3,1,3],Node([13,4,1,3],Node([17,5,1,3], 
             Node([10,2,2,3],Node([20,5,2,3],Node([30,8,2,3],
             Node([5,2,3,3],Node([11,3,3,3],Node([15,5,3,3],
             Node([3,1,4,3],Node([9,2,4,3],Node([19,3,4,3],
             Node([2,1,5,3],Node([4,2,5,3],Node([6,3,5,3],
             Node([7,2,6,3],Node([12,3,6,3],Node([16,4,6,3], Empty()))))))))))))))))))  
#fix scorecards per color

# [schade, dice, fighterid]
listfighters = ["Terry Crews","Jason Statham", "Wesley Sniper","Jet Ri","Steve Seagal", "Super Merio","Vin Dieser", "Chack Norris","The Roch","James Bend", "Ernold Schwarzenegger", "Steve Urkel", "Dexter", "Pariz Hilten", "John Cena","Agua Man", "Jackie Chen", "Bruce Hee"]
superFighter1 = Node([10,1,0],Node([15,2,0],Node([25,3,0],
              Node([20,4,0],Node([15,5,0],Node([10,6,0],
              Node([15,1,1],Node([17,2,1],Node([19,3,1],
              Node([21,4,1],Node([23,5,1],Node([26,6,1],
              Node([10,1,2],Node([12,2,2],Node([14,3,2],
              Node([16,4,2],Node([14,5,2],Node([12,6,2],
              Node([10,1,3],Node([30,2,3],Node([12,3,3],
              Node([25,4,3],Node([14,5,3],Node([23,6,3],
              Node([10,1,4],Node([15,2,4],Node([12,3,4],
              Node([11,4,4],Node([25,5,4],Node([20,6,4],
              Node([10,1,5],Node([10,2,5],Node([30,3,5],
              Node([30,4,5],Node([15,5,5],Node([15,6,5],Empty()))))))))))))))))))))))))))))))))))))
superFighter2 = Node([20,1,6],Node([25,2,6],Node([30,3,6],
              Node([25,4,6],Node([20,5,6],Node([15,6,6],
              Node([15,1,7],Node([28,2,7],Node([27,3,7],
              Node([25,4,7],Node([29,5,7],Node([30,6,7],
              Node([13,1,8],Node([28,2,8],Node([30,3,8],
              Node([17,4,8],Node([10,5,8],Node([7,6,8],
              Node([25,1,9],Node([15,2,9],Node([15,3,9],
              Node([7,4,9],Node([20,5,9],Node([25,6,9],
              Node([25,1,10],Node([25,2,10],Node([20,3,10],
              Node([15,4,10],Node([15,5,10],Node([10,6,10],
              Node([10,1,11],Node([5,2,11],Node([12,3,11],
              Node([11,4,11],Node([15,5,11],Node([8,6,11],Empty()))))))))))))))))))))))))))))))))))))
superFighter3 = Node([9,1,12],Node([8,2,12],Node([7,3,12],
              Node([15,4,12],Node([13,5,12],Node([9,6,12],
              Node([12,1,13],Node([8,2,13],Node([7,3,13],
              Node([15,4,13],Node([13,5,13],Node([9,6,13],
              Node([10,1,14],Node([6,2,14],Node([25,3,14],
              Node([7,4,14],Node([8,5,14],Node([11,6,14],
              Node([12,1,15],Node([15,2,15],Node([9,3,15],
              Node([7,4,15],Node([7,5,15],Node([13,6,15],
              Node([12,1,16],Node([10,2,16],Node([15,3,16],
              Node([9,4,16],Node([10,5,16],Node([25,6,16],
              Node([20,1,17],Node([15,2,17],Node([5,3,17],
              Node([7,4,17],Node([8,5,17],Node([26,6,17],Empty()))))))))))))))))))))))))))))))))))))
fighterlists = [superFighter1, superFighter2, superFighter3]

#print (listfighters[5])
#while not superFighter1.IsEmpty:
#    if superFighter1.Value[2] == 5 :
#        print (superFighter1.Value[0])
#        print (superFighter1.Value[1])
#    superFighter1 = superFighter1.Tail