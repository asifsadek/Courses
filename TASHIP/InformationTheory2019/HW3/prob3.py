"""prob3.py: 

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
import math
import numpy as np

def entropy(ps):
    e = 0.0
    for p in ps:
        if p > 0:
            e += -p * math.log(p, 2)
    return e

def main():
    X, Y, Z = [], [], []
    zz = np.arange(0, 1, 0.5e-2)
    for c in zz:
        bb = np.arange(0, 1-c, 0.5e-2)
        for b in bb:
            X.append(b+c/2)
            Y.append(1.5*c)
            Z.append(entropy([b+c/2,1.5*c,c]))

    plt.scatter(X, Y, c=Z)
    plt.colorbar()
    plt.savefig(f'{__file__}.png')


if __name__ == '__main__':
    main()
