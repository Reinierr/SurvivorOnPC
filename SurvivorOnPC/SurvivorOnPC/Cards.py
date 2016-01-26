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
    #playername = 'curtis'
    #color = 'red'
    #Dice_score = dicenumber
    playername = 'test123'
    playercolor = color
    damage = 11
    if playercolor == 'red':
        if Dice_score == 1:
            player = ScoreCard(playername, playercolor, 1, [10, 20, 30], [1, 2, 3])
            return (player.Name +' - '+ player.Color +' damage / condition '+damage)#+ DaCo(player.Damage,player.Condition))
            
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

##playercard('red')

def super(dicenumber):
    #Dice_score = dicenumber
    #sfc = str(fighters[random.randint(0,2)])
    
    Dice_score = 1
    D = random.randint(0,2)
    fighters = ['rocky belboa','manny pecquiao','Mike Tysen'] 
    sfc = 'rocky belboa'

    ##For Rocky Belboa superfightercard, damage, dicerolls ect
    if sfc == 'rocky belboa':
        if Dice_score == 1:
            superfighter = SuperFightCard( sfc, 1, [10, 20, 30])
            return int(superfighter.Damage[D])
        elif Dice_score == 2:
            superfighter = SuperFightCard( sfc, 2, [8, 13, 17])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

        elif Dice_score == 3:
            superfighter = SuperFightCard( sfc, 3, [3, 9, 19])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

        elif Dice_score == 4:
            superfighter = SuperFightCard( sfc, 4, [5, 11, 15])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

        elif Dice_score == 5:
            superfighter = SuperFightCard( sfc, 5, [7, 12, 16])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

        else:
            superfighter = SuperFightCard( sfc, 6, [2, 4, 6])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

    ##For manny pecquiao superfightercard, damage, dicerolls ect    
    elif sfc == 'manny pecquiao':
        if Dice_score == 1:
            superfighter = SuperFightCard( sfc, 1, [8, 13, 17])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

        elif Dice_score == 2:
            superfighter = SuperFightCard( sfc, 2, [10, 20, 30])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

        elif Dice_score == 3:
            superfighter = SuperFightCard( sfc, 3, [5, 11, 15])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

        elif Dice_score == 4:
            superfighter = SuperFightCard( sfc, 4, [3, 9, 19])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

        elif Dice_score == 5:
            superfighter = SuperFightCard( sfc, 5, [2, 4, 6])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

        else:
            superfighter = SuperFightCard( sfc, 6, [7, 12, 16])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

    ##For Mike Tysen superfightercard, damage, dicerolls ect
    else:
        if Dice_score == 1:
            superfighter = SuperFightCard( 'Mike Tysen', 1, [3, 9, 19])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

        elif Dice_score == 2:
            superfighter = SuperFightCard( 'Mike Tysen', 2, [5, 11, 15])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

        elif Dice_score == 3:
            superfighter = SuperFightCard( 'Mike Tysen', 3, [7, 12, 16])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

        elif Dice_score == 4:
            superfighter = SuperFightCard( 'Mike Tysen', 4, [2, 4, 6])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

        elif Dice_score == 5:
            superfighter = SuperFightCard( 'Mike Tysen', 5, [10, 20, 30])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))

        else:
            superfighter = SuperFightCard( 'Mike Tysen', 6, [8, 13, 17])
            return (superfighter.Name + " Rolled: " + str(superfighter.Dice_score) + " Damage given = " + str(superfighter.Damage[D]))