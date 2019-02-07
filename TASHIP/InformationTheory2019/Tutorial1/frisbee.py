#!/usr/bin/env python3
"""frisbee.py: 

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import numpy as np
import random
import cv2 
import networkx as nx
import itertools
import matplotlib.pyplot as plt

def init_game( g ):
    n1, n2 = random.sample(g.nodes(), k=2)
    return n1, n2

def simulate(N, n_games):
    steps = []
    badGames, goodGames = 0, 0
    for i in range(n_games):
        f1, f2 = game(N)
        if len(f1) > 100:
            badGames += 1
            continue
        goodGames += 1
        #  print('Game%3d,' % i, end = '' )
        #  print(' Steps %3d ' % len(f1), end='')
        steps.append(len(f1))
    print( '============' )
    print( 'Polygon size %d' % N)
    print( 'Bad games: %d / Total %d' % (badGames, badGames+goodGames))
    u, s = np.mean(steps), np.std(steps)
    print( 'Mean steps: %.2f. std: %.2f' % (u,s))
    return u, s

def game(N):
    g = nx.cycle_graph(N)
    n1, n2 = init_game(g)
    f1, f2 = [n1], [n2]
    maxSteps = 200
    for i in itertools.count() :
        # n1 selects an edge
        n11 = random.choice(list(g.neighbors(n1)))
        n22 = random.choice(list(g.neighbors(n2)))
        #print( '%d->%d %d->%d | %d' % (n1, n2, n11, n22, abs(n11-n22)))
        n1, n2 = n11, n22
        f1.append(n1); f2.append(n2)
        if n1 == n2:
            break
        if i == maxSteps:
            break
    return f1, f2

def main():
    X, Y, Yerr = [], [], []
    for n in range(4, 15):
        X.append(n)
        u, s = simulate(N=n, n_games = n*5000)
        Y.append(u)
        Yerr.append(s)
    plt.errorbar(X, Y, Yerr)
    plt.xlabel( 'Polygon size')
    plt.ylabel( r'#Games')
    plt.savefig( '%s.png' % __file__ )


if __name__ == '__main__':
    main()
