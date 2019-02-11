#!/usr/bin/env python3
"""frisbee.py: 
"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import numpy as np
import random
import networkx as nx
import itertools
from collections import defaultdict

def init_game( g ):
    n1, n2 = 0, 1
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
        steps.append(len(f1))
    print( '============' )
    print( 'Polygon size %d' % N)
    print( 'Bad games: %d / Total %d' % (badGames, badGames+goodGames))
    u, s = np.mean(steps), np.std(steps)
    print( 'Mean steps: %.2f. var: %.2f' % (u,s**2))
    return u, s

def game(N):
    g = nx.cycle_graph(N)
    n1, n2 = init_game(g)
    f1, f2 = [n1], [n2]
    maxSteps = 500
    for i in itertools.count() :
        # n1 selects an edge
        n11 = random.choice(list(g.neighbors(n1)))
        n22 = random.choice(list(g.neighbors(n2)))
        #print( '%d->%d %d->%d | %d' % (n1, n2, n11, n22, abs(n11-n22)))
        n1, n2 = n11, n22
        f1.append(n1); f2.append(n2)
        if n1 == n2:
            break
        if 1+i == maxSteps:
            break
    return f1, f2

def simulate_game():
    n = 5
    u, s = simulate(N=n, n_games = 100000)
    print(u, s)

def simulate_state_machine(g, s, t, paths=[]):
    L = []
    N = 10000
    for i in range(N):
        path, p = s, 1.0
        while True:
            ns = list(g.successors(path[-1]))
            n = random.choices(ns, weights=[float(g[path[-1]][x]['p']) for x in ns], k=1)[0]
            p *= float( g[path[-1]][n]['p'] )
            path += n
            if n == t:
                break
        L.append(len(path))
    print( 'Mean and variance after %d runs' %N)
    print( np.mean(L), np.std(L))

def estimate( ):
    g = nx.DiGraph(nx.drawing.nx_agraph.read_dot('./frisbee.dot'))
    src, tgt = '1', '0'
    simulate_state_machine(g, src, tgt)

def main( ):
    estimate()
    simulate_game()

if __name__ == '__main__':
    main()
