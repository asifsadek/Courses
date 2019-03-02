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

class Seq():
    def __init__(self, N):
        global dist_
        alph = list(dist_.keys())
        ws = list(dist_.values())
        self.s = random.choices(alph, weights=ws, k=N)

    def __repr__(self):
        return ''.join(self.s)

    def Q(self):
        c = Counter(self.s)
        return {k:v/len(self.s) for k, v in c.items()}

def solve(N):
    hp = 1.459148
    aa = np.arange(0, 0.5, 1e-5)
    H = []
    for a in aa:
        b = 1-a
        hq = a*math.log(2,2) + b*math.log(3,2) 
        H.append(hq)
        if abs(hp-hq)/hp < 1e-6:
            print( f"{a:.5f}, {b:.5f}, {hq:.5f}")

def main():
    solve(1000)

if __name__ == '__main__':
    main()

