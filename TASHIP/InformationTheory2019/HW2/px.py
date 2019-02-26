"""px.py: 

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import random
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

def init_coins():
    res = [1.0]*11 + [random.choice([0.9,1.0,1.1])]
    random.shuffle(res)
    return res

def weigh(n):
    res = defaultdict(int)
    N = 100000
    for i in range(N):
        cs = init_coins()
        left, right = cs[:n], cs[n:2*n]
        if sum(left) == sum(right):
            res['EQ'] += 1/N
        elif sum(left) < sum(right):
            res['RH'] += 1/N
        else:
            res['LH'] += 1/N
    res = { k : res[k] for k in sorted(res) }
    return res

def prob_equal(n):
    e = 1.0
    for x in range(12, 12-2*n, -1):
        e *= (x-1)/x
    return 1/3 + 2*e/3

def main():
    for x in range(1, 7):
        px = prob_equal(x)
        res = weigh(x)
        print(x, px, res)

if __name__ == '__main__':
    main()

