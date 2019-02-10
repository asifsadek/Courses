#!/usr/bin/env python
"""mean_dice.py: 
"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import random
import numpy as np

def main():
    D1, D2, S = [], [], []
    for i in range(10001):
        D1.append(random.randint(1,6))
        D2.append(random.randint(1,6))
        S.append(D1[-1]+D2[-1])
        if i < 100:
            continue
        if i % 20 == 0:
            print(i, np.mean(S), np.std(S) )

if __name__ == '__main__':
    main()

