#!/usr/bin/env python3
"""strategy.py: 

This strategy is due to following students of Information theory class 2019 and
2016.

- Pushkar Khandar (2019)
- Pavan Kaushik (2016)

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import random

nWeigh_     = 0
strategy_   = []

class Coin():
    def __init__(self, index, w):
        self.weight = w
        self.index = index
        self.type = 'n'
        if self.weight > 1.0:
            self.type = 'h'
        elif self.weight < 1.0:
            self.type = 'l'

    def __repr__(self):
        return f'{self.index:X}{self.type}'

def init_coins(where=-1, whichType=''):
    N = 12
    cs = [Coin(i,1.0) for i in range(N)]
    if where < 0:
        where = random.choice(range(N))
    if not whichType:
        whichType = random.choice(['h', 'l'])
    cs[where] = Coin(where, 1.1) if whichType == 'h' else Coin(where, 0.9)
    return cs

def answer(what, coin):
    global nWeigh_
    global strategy_
    if what == 'LIGHT':
        assert coin.weight < 1.0, strategy_
    else:
        assert coin.weight > 1.0, strategy_
    print( f'[ANS] Found counterfiet count. It is {what}. {coin}' )
    print( f'\tTotal {nWeigh_} weighings. Strategy is below.' )

    # Print strategy
    for i, (a, b, res) in enumerate(strategy_):
        left = ','.join(map(str,a))
        right = ','.join(map(str,b))
        print( f'\tWeigh {i}: Weight {left} vs {right} => {res}' )

def weigh(left, right):
    global nWeigh_
    global strategy_
    nWeigh_ += 1
    wLeft = sum([x.weight for x in left])
    wRight = sum([x.weight for x in right])
    if wLeft > wRight:
        res = 'LH'
    elif wRight > wLeft:
        res = 'RH'
    else:
        res = 'EQ'
    strategy_.append((left, right, res))
    return res

def first_equal(withCounterfiet, normal):
    # We are here because previous weighing of 4 vs 4 was equal. That means that
    # the counterfiet coin is in the withCounterfiet group. Now we take 3 coins
    # from the first group and 3 from the second and weigh them.
    res = weigh(withCounterfiet[:3], normal[:3])
    if res == 'EQ':
        # 4th coin in withCounterfiet is counterfiet. 
        badCoin = withCounterfiet[3]
        r = weigh([badCoin], [normal[3]])
        if r == 'EQ':
            raise RuntimeError( "Algorithm failed or there was no "
                    "counterfiet coin. Suckers!" )
        elif r == 'LH':
            answer('HEAVY', badCoin)
        else:
            answer('LIGHT', badCoin)
        return nWeigh_ 
    
    # if left group was heavy then counterfiet coin is in the left group and it
    # is heavy.
    if res == 'LH':
        res1 = weigh([withCounterfiet[0]], [withCounterfiet[1]])
        if "EQ" == res1:
            answer('HEAVY', withCounterfiet[2])
        elif 'LH' == res1:
            answer('HEAVY', withCounterfiet[0])
        else:
            answer('HEAVY', withCounterfiet[1])
        return nWeigh_

    if res == 'RH':
        res1 = weigh([withCounterfiet[0]], [withCounterfiet[1]])
        if "EQ" == res1:
            answer('LIGHT', withCounterfiet[2])
        elif 'LH' == res1:
            answer('LIGHT', withCounterfiet[1])
        else:
            answer('LIGHT', withCounterfiet[0])
        return nWeigh_

def findCounterfietIn3Coins(coins, counterfietIs):
    # Find counterfiet coin when type is known among three coins. This structure
    # appears again and again in the problem so I've turned it into a function.

    # First check that we are not made fool by caller.
    assert len(coins) == 3, "Only three coins."
    totalSum = sum([x.weight for x in coins])
    if counterfietIs == 'LIGHT':
        assert totalSum < 3.0
    else:
        assert totalSum > 3.0

    first, second, third = coins
    res = weigh([first], [second])
    if res == 'RH':
        return (second if counterfietIs=='HEAVY' else first)
    elif res == 'LH':
        return (first if counterfietIs=='HEAVY' else second)
    else:
        return third

def rightSideHeady(left, right, good):
    # Right side was heavy.
    # Take 3 coins from right and create a group
    aside = right[:3]
    # Take fourth coin from the right and add two coins to it from the left.
    group1 = [right[3]] + left[:2]
    # Add a good coin to rest of the left group.
    group2 = left[2:] + [good[0]]
    # all these groups are of size three
    assert len(group1) == 3
    assert len(group2) == 3
    assert len(aside) == 3

    # we now weigh group1 and group2. Keep the group1 on the right. Not
    # essential but make argument easy.
    res = weigh(group2, group1)
    if res == 'RH':
        # if right side is still heavy then we have following options.
        # 1. Assume that counterfiet coin is heavy then it is definately  first
        # coin in the group1 (which is fourth coin in the 'right').
        # 2. Assuming that counterfiet coun is light then it is one of first two
        # coins in group2. 
        # In either case, we have to weigh the first two coins of the group2.
        res1 = weigh([group2[0]], [group2[1]])
        if res1 == 'EQ':
            # then coin is heavy and it is first coin of group1.
            answer('HEAVY', group1[0])
            return 
        else:
            # definately coin is light it is one the first 2 in group2.
            answer('LIGHT', group2[0]) if res1 == 'RH' else answer('LIGHT', group2[1])
            return 
    elif res == 'EQ':
        # Then the aside group has the counterfiet coin and it is heavy. Weigh
        # any two.
        coin = findCounterfietIn3Coins(aside, "HEAVY")
        answer("HEAVY", coin)
    else:
        # Ok. Now balance has flipped the side. Last two coins in group1 are the
        # light coins. Weigh them.
        coin = findCounterfietIn3Coins(group1, 'LIGHT')
        answer('LIGHT', coin)

def find_counterfeit(coins):
    global nWeigh_
    nWeigh_ = 0
    # step 1. Split into 3 groups of 4 coins each and weigh first two.
    groups = [coins[i*4:(i+1)*4] for i in range(3)]
    res = weigh(groups[0], groups[1])
    if res == 'EQ':
        # First weigh was equal. That is we have counterfiet in the rest of the
        # coins. 
        first_equal(groups[2], groups[1])
    elif res == 'RH':
        # right side is heavy
        rightSideHeady(groups[0], groups[1], groups[2])
    elif res == 'LH':
        # Left grup is heavy i.e, either the counterfiet coin is heavy and is in
        # the left group or it is light and is in the right group. We use the
        # same function rightSideHeady after swap the group.
        rightSideHeady(groups[1], groups[0], groups[2])
    else:
        raise RuntimeError( "Are you kidding me!" )

def play(coins):
    print( '== Finding coin.' )
    print( 'Initial configuration', coins )
    find_counterfeit(coins)

def test( N = 1000 ):
    global nWeigh_, strategy_
    for i in range(1000):
        nWeigh_ = 0
        strategy_ = []
        coins = init_coins()
        play(coins)

def main(**kwargs):
    coins = init_coins(kwargs['where'], kwargs['type'])
    play(coins)

if __name__ == '__main__':
    import argparse
    # Argument parser.
    description = '''Find the counterfiet coin.'''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--where', '-w'
        , required = True, type=int
        , help = 'Location of the counterfiet coin. Between 0 and 11.'
        )
    parser.add_argument('--type', '-t'
        , required = True, choices=['h', 'l']
        , help = 'Heavy (h) or Light (l).'
        )
    class Args: pass 
    args = Args()
    parser.parse_args(namespace=args)
    main(**vars(args))
