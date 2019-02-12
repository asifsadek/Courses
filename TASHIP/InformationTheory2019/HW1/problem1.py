"""problem1.py: 
"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import math
import itertools

def subsets(n, m):
    ss = [ ]
    for x in range( m ):
        s = [ ]
        ss.append( s )
    return ss

def prob_of_ith_class(i):
    return 2**(-i)

def sum_prod(hs, ps):
    return sum([h*p for (h,p) in zip(hs,ps)])

def distribute_horses(N, pis):
    p = 0.0
    dist = []
    for hs in itertools.product(range(N+1), repeat=len(pis)):
        if sum(hs) != N:
            continue
        if 1.0 == sum_prod(hs,pis):
            print( end='.')
            sys.stdout.flush()
            dist.append(hs)
    print()
    print( '[INFO] Total %d distributions found' % len(dist))
    return dist

def entropy(xi, pi):
    return - sum([x*p*math.log(p,2) for (x,p) in zip(xi,pi)])

def main( ):
    nH = 8
    pis = [prob_of_ith_class(i) for i in range(1,6)]
    print( pis )
    dist = distribute_horses(8, pis)
    print('\n\n=== Distributions of horse ===')
    print('%s  Entropy' % ' '.join(['%.5f'%p for p in pis]))
    for i, d in enumerate(dist):
        print('%s  %.3f'%(' '.join(['%7d'%x for x in d]), entropy(d,pis)))

if __name__ == '__main__':
    main()
