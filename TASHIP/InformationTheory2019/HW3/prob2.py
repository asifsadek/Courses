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
from collections import Counter
import numpy as np
import random

dist_ = dict(A=1/2, B=1/3, C=1/6)

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
    S = Seq(N)
    print(S)
    print(S.Q())

def main():
    solve(1000)

if __name__ == '__main__':
    main()

