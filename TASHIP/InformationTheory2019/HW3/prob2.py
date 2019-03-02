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
    X, Y, Z = [], [], []
    ps = np.arange(0, 0.5, 0.01)
    for p in ps:
        q = 1.0 - p
        for k in range(N):
            prn = nchoosek(N, k) * p**k * q**(N-k)
            hseq = - 1 / N * math.log(prn, 2) if prn > 0 else 0
            X.append(p)
            Y.append(k)
            Z.append(hseq)

    ax = plt.subplot(projection='3d')
    ax.plot_trisurf(X, Y, Z)
    xx, yy = np.meshgrid(ps, range(N))
    ax.plot_surface(xx, yy, np.ones_like(xx)*hp, alpha=0.5)
    ax.set_xlabel(r'$a$ s.t. $a+b=1$')
    ax.set_ylabel(r'$k$, $\binom{%d}{k}$'%N)
    ax.set_zlabel( r'$\frac{1}{N}\Pr(S)$' )

    plt.savefig( f'{__file__}.png' )

def main():
    solve(500)

if __name__ == '__main__':
    main()

