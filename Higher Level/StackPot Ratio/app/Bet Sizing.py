import numpy as np
import math
import pandas as pd
from pandas import *

def next_street_bet(pot, stack, streets_remaining, betpct):
    bet = pot*betpct
    if streets_remaining == 1:
        if abs(stack-bet) < 0.000001:
            return True,betpct
        else:
            return False,stack-bet
    else:
        return next_street_bet(pot+bet*2, stack-bet, streets_remaining-1, betpct)

def next_street_raise(pot, stack, streets_remaining, villbet, betpct):
    if villbet < 0: # it's not the first street
        bet = pot*betpct
    else:
        bet = (villbet*2+pot)*betpct+villbet
    if streets_remaining == 1:
        if abs(stack-bet) < 0.000001:
            return True,betpct
        else:
            return False,stack-bet
    else:
        return next_street_raise(pot+bet*2, stack-bet, streets_remaining-1, -1, betpct)
    

def binary_search(curr, betraise, params):    
    mini = 0
    maxi = 10
    prev = float('nan')
    while True:
        if betraise == 'bet':
            bet_size = next_street_bet(params[0],params[1],params[2],curr)
        else:
            bet_size = next_street_raise(params[0],params[1],params[2],params[3],curr)
            
        if bet_size[0] == True: # found it
            return bet_size[1]
        else: # keep going
            if math.isnan(prev): # first iteration
                prev = curr
                if bet_size[1] < 0: # bet size too big
                    curr /= 2 # halfway between 0 and curr
                else:
                    curr = (1+curr)/2 # halfway between 1 and curr
            else:
                if curr < prev: # if last attempt was too big
                    if bet_size[1] < 0: # still too big
                        prev = curr
                        curr = (curr+mini)/2
                    else: # now too small
                        maxi = prev # this is the highest possible value
                        tempprev = curr
                        curr = (curr + prev)/2
                        prev = tempprev
                else: # if last attempt was too small
                    if bet_size[1] < 0: # now too big
                        mini = prev # this is the lowest possible value
                        tempprev = curr
                        curr = (curr + prev)/2
                        prev = tempprev
                    else: # still too small
                        prev = curr
                        curr = (maxi+curr)/2
    return False # didn't work somehow

# testing
# bet needs: pot, stack, streets_remaining
print binary_search(0.5, 'bet', [40, 100, 3])
# raise needs: pot, stack, betraisepct, streets_remaining, vill_bet
print binary_search(0.5, 'raise', [10, 100, 2, 5])

#####################
# Print bet sizing data frame
def get_bet_sizes(pot, stack, betpct, streets_remaining, sizes):
    bet = betpct*pot
    sizes.append([pot,stack,bet,betpct])
    
    if streets_remaining == 1: # base case
        return sizes
    
    return get_bet_sizes(pot + 2*bet, stack-bet, betpct, streets_remaining-1, sizes)
    

pot = 40
stack = 100
streets_remaining = 3
bet_sizes = get_bet_sizes(pot, stack, binary_search(0.5, 'bet', [pot, stack, streets_remaining]),\
                          streets_remaining, [])

df = DataFrame(bet_sizes)
df.columns = 'Pot','Stack','Bet','%'
df.index.name = 'Street #'
print df

############
# print raise sizing dataframe

def get_raise_sizes(pot, stack, betpct, streets_remaining, villbet, sizes):
    
    if villbet == -1: # not the first street
        bet = betpct*pot
        sizes.append([pot,stack,float('nan'),bet,betpct])

    else:
        bet = (villbet*2 + pot)*betpct + villbet
        sizes.append([pot,stack,villbet,bet,betpct])

    if streets_remaining == 1: # base case
        return sizes
    
    return get_raise_sizes(pot + 2*bet, stack-bet, betpct, streets_remaining-1, -1, sizes)
    

pot = 10
villbet = 5
stack = 100
streets_remaining = 2
bet_sizes = get_raise_sizes(pot, stack, \
            binary_search(0.5, 'raise', [pot, stack, streets_remaining, villbet]),\
            streets_remaining, villbet, [])

df = DataFrame(bet_sizes)
df.columns = 'Pot','Stack','Bet/Raise','Villain Bet','%'
df.index.name = 'Street #'
print df