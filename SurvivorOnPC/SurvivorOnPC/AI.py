import random
from Cards import *
from Node import *
import math

#[Schade, Conditie, Dice, Choice]

def AI(player, dice):
  if player.AI == 1:
    return EasyAI(player,dice)
  elif player.AI == 2:
    return HardAI(player,dice)

def HardAI(player, dice):
  home = player.Home
  index = player.Tile.Index
  condition = player.Condition
  
  #calculate distance to home tile
  if index > home:
    distance = home + 40 - index
  elif index <= home:
    distance = home - index
  
  #create list with possible actions
  scorecard = Empty()
  scorecard = scorecards[int(math.floor(home/10))]
  possibleActions = Empty()
  possibleActions = scorecard.Filter(lambda x: x[2] == dice).Filter(lambda x: not (x[1] > condition))

  #return 0 dmg if no possible actions
  if possibleActions.IsEmpty:
    return [0, 0, home]

  #create list with dmg/cond ratio
  x = possibleActions
  dmgCost = [] #(dmg / cond)
  while not x.IsEmpty:
    #[dmgCost, dmg, cond]
    dmgCost.append([(x.Value[0]/x.Value[1]), x.Value[0], x.Value[1]])
    x = x.Tail

  if distance > 20:
    dmgCost = sorted(dmgCost, key=lambda x: x[0], reverse=True)
  else:
    dmgCost = sorted(dmgCost, key=lambda x: x[1], reverse=True)

  choice = dmgCost[0]

  return [choice[1],choice[2], home]

def EasyAI(player,dice):
  home = player.Home
  condition = player.Condition

  #create list with possible actions
  scorecard = Empty()
  scorecard = scorecards[int(math.floor(home/10))]
  possibleActions = Empty()
  possibleActions = scorecard.Filter(lambda x: x[2] == dice).Filter(lambda x: not (x[1] > condition))

  #return 0 dmg if no possible actions
  if possibleActions.IsEmpty:
    return [0, 0, home]

  #create list
  x = possibleActions
  actions = []
  while not x.IsEmpty:
    actions.append(x.Value)
    x = x.Tail

  choice = actions[random.randint(0,len(actions)-1)]

  return [choice[0], choice[1], home]