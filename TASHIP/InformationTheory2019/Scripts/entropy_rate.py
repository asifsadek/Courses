"""entropy_rate.py: 
"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import math
from collections import Counter
import random
import numpy as np
import matplotlib.pyplot as plt

def entropy(seq):
    ps, b = np.histogram(seq, range=(0, 2), bins=2, density=True)
    h = [ -p*math.log(p, 2) for p in ps if p > 0]
    return sum(h)

def main():
    seq = []
    for i in range(1000):
        seq.append(random.choice([0,1]))
        e = entropy(seq)
        print(i, e, e/i)


if __name__ == '__main__':
    main()
