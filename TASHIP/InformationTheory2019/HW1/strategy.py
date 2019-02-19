#!/usr/bin/env python3
"""strategy.py: 
"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import random
import networkx as nx

nWeigh_ = 0

class Coin():
    def __init__(self, index, w):
        self.weight = w
        self.index = index

    def __repr__(self):
        return 'C%d=%.1f'%(self.index,self.weight)

def init_coins(N):
    cs = [Coin(i,1.0) for i in range(N)]
    i = random.choice(range(N))
    cs[i] = random.choice([Coin(i,1.1), Coin(i,0.9)])
    return cs

def weigh(left, right):
    global nWeigh_
    nWeigh_ += 1
    wLeft = sum([x.weight for x in left])
    wRight = sum([x.weight for x in right])
    if wLeft > wRight:
        return 'LH'
    elif wRight > wLeft:
        return 'RH'
    else:
        return 'EQ'

def first_equal(withCounterfiet, normal):
    # We are here because previous weighing of 4 vs 4 was equal. That means that
    # the counterfiet coin is in the withCounterfiet group. Now we take 3 coins
    # from the first group and 3 from the second and weigh them.
    res = weigh(withCounterfiet[:3], normal[:3])
    # if res is EQ then the 4th coin in withCounterfiet is counterfiet. 
    if res == 'EQ':
        badCoin = withCounterfiet[3]
        r = weigh([badCoin], normal[3])
        if r == 'EQ':
            raise RuntimeError( "Algorithm failed or there was no "
                    "counterfiet suckers." )
        elif r == 'LH':
            print( 'Found counterfiet. It is heavy.')
        else:
            print( 'Found counterfiet. It is light.')
        print( badCoin )
        print( 'Total weighings %d' % nWeigh_)
        return nWeigh_ 
    
    # if left group was heavy then counterfiet coin is in the left group and it
    # is heavy.
    if res == 'LH':
        print( 'Found Conterfiet. It is heavy.')
        res1 = weigh([withCounterfiet[0]], [withCounterfiet[1]])
        if "EQ" == res1:
            print( withCounterfiet[2] )
        elif 'LH' == res1:
            print(withCounterfiet[0])
        else:
            print(withCounterfiet[1])
        print( 'Total weighings %d' % nWeigh_)
        return nWeigh_

    if res == 'RH':
        print( 'Found counterfiet. It is light')
        res1 = weigh([withCounterfiet[0]], [withCounterfiet[1]])
        if "EQ" == res1:
            print( withCounterfiet[2] )
        elif 'LH' == res1:
            print(withCounterfiet[1])
        else:
            print(withCounterfiet[0])
        print( 'Total weighings %d' % nWeigh_)
        return nWeigh_

def find_counterfeit(coins, g):
    global nWeigh_
    nWeigh_ = 0
    # step 1. Split into 3 groups of 4 coins each and weigh first two.
    groups = [coins[i*4:(i+1)*4] for i in range(3)]
    res = weigh(groups[0], groups[1])
    if res == 'EQ':
        # First weigh was equal. That is we have counterfiet in the rest of the
        # coins. 
        first_equal(groups[2], groups[1])
    elif res == 'LH':
        # Left grup is heavy i.e, either the counterfiet coin is heavy and is in
        # the left group or it is light and is in the right group.
        coins = (groups[0], groups[1])
    print( res, coins, 'Num weighs %d' % nWeigh_ )


def play(i):
    coins = init_coins(12)
    g = nx.DiGraph()
    find_counterfeit(coins, g)

def main():
    for i in range(1):
        play(i)

if __name__ == '__main__':
    main()
