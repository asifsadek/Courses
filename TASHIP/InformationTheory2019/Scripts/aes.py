"""aes.py: 

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use('bmh')
import numpy as np
import random
import scipy.special

random.seed(10)
p = random.random()
print( p )

def typical_for_n(n):
    X, Y = [], []
    for k in range(n+1):
        numSeq = scipy.special.comb(n, k)
        probSeq = (p**k)*((1-p)**(n-k))
        X.append(probSeq)
        Y.append(numSeq)
    return np.array(X), np.array(Y)


def main():
    plt.figure(figsize=(8,4))
    ax = plt.subplot(121)
    maxNP = []
    X2, Y2 = [], []
    for n in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]:
        PS, NS = typical_for_n(n)
        # rescale PS
        PS = PS - PS.min()
        PS = PS / PS.max()
        maxNP.append((n,max(NS)))
        ax.semilogx(PS, NS, label='N=%d'%n)

        plt.legend()
    plt.xlabel( 'Normalized P')
    plt.ylabel( '#Seq')

    plt.subplot(122)
    xx, yy = zip(*maxNP)
    plt.plot(xx, yy)
    plt.xlabel('N')
    plt.ylabel('#Seq at peak')
    plt.tight_layout()
    plt.savefig( '%s.png' % __file__ )

if __name__ == '__main__':
    main()

