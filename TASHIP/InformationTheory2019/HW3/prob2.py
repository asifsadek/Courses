"""prob2.py: 
"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d 
from collections import Counter
import numpy as np
import random
import math
import scipy.special

dist_ = dict(A=1/2, B=1/3, C=1/6)

def nchoosek_math(n, k):
    f = math.factorial
    return f(n)/f(k)/f(n-k)

def nchoosek(n, k):
    return scipy.special.comb(n, k)

def entropy(ps):
    assert math.isclose(sum(ps), 1.0), sum(ps)
    return sum([-p*math.log(p,2) for p in ps if p > 0])

def solve1():
    hp = entropy([1/2, 1/3, 1/6])
    return hp

def solve2(hp):
    p, q = 1/2, 1/3
    print('(b) Followings are the numerical solutions.' )
    for a in np.arange(0, 0.5, 1e-5):
        pr = a*math.log(1/p, 2)+(1-a)*math.log(1/q,2)
        if math.isclose(pr, hp, rel_tol=1e-5):
            print(f"H(p)={hp:.6f}, pr={pr:.6f}, a={a:.6f}")

def solve():
    hp = solve1()
    print( f'(a) Entropy is {hp} bit.' )
    b = solve2(hp)

def main():
    solve()

if __name__ == '__main__':
    main()

