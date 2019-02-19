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
p = 0.7

def typical_for_n(n):
    X, Y = [], []
    for k in range(n+1):
        numSeq = scipy.special.comb(n, k)
        probSeq = (p**k)*((1-p)**(n-k))
        X.append(probSeq)
        Y.append(numSeq)
    return np.array(X), np.array(Y)


def main():
    ax = plt.subplot(121)
    maxNP = []
    for n in [10,20,30,40,50]:
        PS, NS = typical_for_n(n)
        # rescale PS
        PS = PS - PS.min()
        PS = PS / PS.max()
        print(n, len(NS))
        maxNP.append((n,max(NS)))
        ax.semilogy(PS, NS, label='N=%d'%n)
        plt.legend()
    plt.xlabel( 'Normalized P')
    plt.ylabel( '#Seq')

    plt.subplot(122)
    plt.plot(maxNP[0], maxNP[1])

    plt.savefig( '%s.png' % __file__ )

if __name__ == '__main__':
    main()

