"""prob2.py: 
Problem 2. Homework 2. Information Theory 2019. 
2019-02-26
"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import itertools
import functools
import math
from collections import defaultdict, Counter
import matplotlib as mpl
# mpl.use( 'pgf' )
import matplotlib.pyplot as plt
mpl.style.use( ['bmh', 'fivethirtyeight'] )


dist_ = dict(A=1/2,T=1/4,C=1/8,G=1/8)
assert sum(dist_.values()) == 1.0

def is_stringly_typical(seq):
    global dist_
    c = Counter(seq)
    for k, v in c.items():
        if not math.isclose(c[k]/len(seq), dist_[k]):
            return False
    return True

def do_prob(nSeq, ax=None):
    # First lets enumerate all possible sequences and write down their
    # proability. If you are smart, you can also do it by hand. Its trivial.
    alphabets = list(dist_.keys())
    res, stringlyTypical = [], []
    for s in itertools.product(alphabets, repeat=nSeq):
        p = functools.reduce(lambda x, y: x*y, [dist_[x] for x in s])
        res.append((p,''.join(s)))
        if is_stringly_typical(s):
            stringlyTypical.append(p)

    print(f'== Length of each sequence: {nSeq}')
    print(f'Total sequences: {len(res)}')
    print(f'Total stringently typical sequences: {len(stringlyTypical)}')
    print(f'Probability of all stringently sequences: {sum(stringlyTypical)}')
    r = defaultdict(int)
    for p, s in sorted(res):
        r[p] += 1
    print(r)

def main():
    do_prob(8)

if __name__ == '__main__':
    main()
