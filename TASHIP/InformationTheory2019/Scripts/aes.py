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
    ax1 = plt.subplot(121)
    ax1.set_xlabel( 'Scaled P')
    ax1.set_ylabel( '#Seq')

    ax2 = plt.subplot(122)
    ax2.set_xlabel('N')
    ax2.set_ylabel('#Seq at peak')
    plt.tight_layout()

    likely = []
    X2, Y2 = [], []
    for n in [2,4,6,8,10,12,14,16,18,20,22,24,26]:
        PS, NS = typical_for_n(n)
        # rescale PS
        PS = PS - PS.min()
        PS = PS / PS.max()
        ns = sorted(NS)
        likely.append((n,ns[-3:]))
        ax1.semilogx(PS, NS, label='N=%d'%n)
        ax1.legend()
        plt.show( block = False )

        xx, yy = zip(*likely)
        ax2.clear()
        ax2.plot(xx, yy)
        ax2.legend()
        plt.show( block=False )
        plt.pause(0.1)


if __name__ == '__main__':
    main()

