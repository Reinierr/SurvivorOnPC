import pygame, math
from Node import *
from Dice import *
from Constants import *

#DisplayScoreCard blits 3 choices a player can make on the screen depending on their diceroll
def DisplayScoreCard(screen, player_home, dicenumber):
    player_scorecard = scorecards[int(math.floor(player_home/10))]
    th = 5
    pygame.draw.rect(screen, BLACK, (21*TILESIZE,int(th-1)*TILESIZE , 250,250))
    sci = FONT_TEXT.render('Make a choice:', 1, RED_BTN)
    screen.blit(sci,(21*TILESIZE,int(th-1)*TILESIZE))
    while not player_scorecard.IsEmpty:
        if player_scorecard.Value[2] == dicenumber:
            sc = FONT_TEXT.render('DMG: '+str(player_scorecard.Value[0])+' CP: '+str(player_scorecard.Value[1]), 1, RED_BTN)
            screen.blit(sc,(21*TILESIZE,int(th)*TILESIZE))
            th = th + 1
        player_scorecard = player_scorecard.Tail

#ScoreCard function returns player dmg/cp/home of player
def ScoreCard(player_home, dicenumber, choice):
    player_scorecard = scorecards[int(math.floor(player_home/10))]
    while not player_scorecard.IsEmpty:
        if player_scorecard.Value[2] == dicenumber:
            if player_scorecard.Value[3] == choice:
                player_dmg = player_scorecard.Value[0]
                player_condition = player_scorecard.Value[1]
        player_scorecard = player_scorecard.Tail
    return [player_dmg, player_condition, player_home]

#Cornerfight returns the updated player list with their new hp/cp
def CornerFight(players, pstats1, pstats2):
    if pstats1[0] > pstats2[0]:
        dmg = pstats1[0] - pstats2[0]
        p1con = pstats1[1]
        p2con = pstats2[1]
        while not players.IsEmpty:
            if players.Value.Turn:
                players.Value.Condition = players.Value.Condition - p1con
            if players.Value.Home == pstats2[2]:
                players.Value.Life = players.Value.Life - dmg
                players.Value.Condition = players.Value.Condition - p2con
            players = players.Tail
        return players

    elif pstats1[0] < pstats2[0]:
        dmg = pstats2[0] - pstats1[0]
        p1con = pstats1[1]
        p2con = pstats2[1]
        while not players.IsEmpty:
            if players.Value.Turn:
                players.Value.Life = players.Value.Life - dmg
                players.Value.Condition = players.Value.Condition - p1con
            if players.Value.Home == pstats2[2]:
                players.Value.Condition = players.Value.Condition - p2con
            players = players.Tail
        return players
    else:
        return players

#superfight blits the fight data on screen
def SuperFight(screen, player_dmg, player_cp):
    random_dice = random.randint(1,6)
    resultdmg = 0
    fighter_dmg = 0
    fighter_index = random.randrange(0,len(listfighters))
    fighter = listfighters[fighter_index]
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
        superfight = FONT_TEXT.render('Superfight! '+str(fighter)+' hit you for '+str(resultdmg)+' damage!', 1, RED_BTN)
    else:
        superfight = FONT_TEXT.render('Superfight! You defended yourself from '+str(fighter), 1, RED_BTN)
    screen.blit(superfight,(SIZE[0]-superfight.get_rect().width, SIZE[1] - 25))
    return [resultdmg if resultdmg > 0 else 0, player_cp]

#[Schade, Conditie, Dice, Choice]
                            #-Rocky Belboa- 0/Blue#                                        
scorecardblue = Node([10,2,1,1],Node([20,5,1,2],Node([30,8,1,3],
             Node([8,3,2,1],Node([13,4,2,2],Node([17,5,2,3],
             Node([3,1,3,1],Node([9,2,3,2],Node([19,3,3,3],
             Node([5,2,4,1],Node([11,3,4,2],Node([15,5,4,3],
             Node([7,2,5,1],Node([12,3,5,2],Node([16,4,5,3],
             Node([2,1,6,1],Node([4,2,6,2],Node([6,3,6,3], Empty())))))))))))))))))) 
                            #-Mike Tysen- 1/Red#
scorecardred = Node([5,2,1,1],Node([11,3,1,2],Node([15,5,1,3], 
             Node([3,1,2,1],Node([9,2,2,2],Node([19,3,2,3],
             Node([2,1,3,1],Node([4,2,3,2],Node([6,3,3,3],
             Node([7,2,4,1],Node([12,3,4,2],Node([16,4,4,3],
             Node([8,3,5,1],Node([13,4,5,2],Node([17,5,5,3],
             Node([10,3,6,1],Node([20,3,6,2],Node([30,3,6,3], Empty())))))))))))))))))) 
                            #-Badr Heri- 2/Green#      
scorecardgreen = Node([1,1,1,1],Node([9,2,1,2],Node([19,3,1,3],
             Node([5,2,2,1],Node([11,3,2,2],Node([15,5,2,3],
             Node([7,2,3,1],Node([12,3,3,2],Node([16,4,3,3],
             Node([2,1,4,1],Node([4,2,4,2],Node([6,3,4,3],
             Node([10,2,5,1],Node([20,5,5,2],Node([30,8,5,3],
             Node([8,3,6,1],Node([13,4,6,2],Node([17,5,6,3], Empty())))))))))))))))))) 
                            #-Manny Pecquiao- 3/Yellow#   
scorecardyellow = Node([8,3,1,1],Node([13,4,1,2],Node([17,5,1,3], 
             Node([10,2,2,1],Node([20,5,2,2],Node([30,8,2,3],
             Node([5,2,3,1],Node([11,3,3,2],Node([15,5,3,3],
             Node([3,1,4,1],Node([9,2,4,2],Node([19,3,4,3],
             Node([2,1,5,1],Node([4,2,5,2],Node([6,3,5,3],
             Node([7,2,6,1],Node([12,3,6,2],Node([16,4,6,3], Empty()))))))))))))))))))  
#fix scorecards per color
scorecards = [scorecardblue,scorecardred,scorecardgreen,scorecardyellow]

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