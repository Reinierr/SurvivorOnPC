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

scorecards = Node([10,2,1,0],Node([20,5,1,0],Node([30,8,1,0],
             Node([8,3,2,0],Node([13,4,2,0],Node([17,5,2,0],
             Node([3,1,3,0],Node([9,2,3,0],Node([19,3,3,0],
             Node([5,2,4,0],Node([11,3,4,0],Node([15,5,4,0],
             Node([7,2,5,0],Node([12,3,5,0],Node([16,4,5,0],
             Node([2,1,6,0],Node([4,2,6,0],Node([6,3,6,0], Empty()))))))))))))))))))

while not scorecards.IsEmpty:
    if scorecards.Value[3] == 0:
        if scorecards.Value[2] == 4:
            print(scorecards.Value[0], scorecards.Value[1])
    scorecards = scorecards.Tail