"""prob1.py: 

    Problem 1. HW2. Information Theory : 2019.

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import numpy as np
import math

mat = np.matrix( '0.25 0.25; 0 0.5' )

def getPX( x ):
    global mat
    return np.sum(mat[:,x])

def getPY( y ):
    global mat
    return np.sum(mat[y,:])

def entropy(ps, normalize=False):
    if isinstance(ps, np.ndarray):
        ps = ps.ravel().tolist()[0]

    if normalize:
        ps = [p/sum(ps) for p in ps]

    assert sum(ps) == 1.0, ps
    entropy = 0
    for p in ps:
        if p == 0:
            continue
        entropy += - p * math.log(p,2)
    return entropy

def main():
    res = {}
    assert np.isclose(np.sum(mat),1.0), "probablities must add upto 1.0"
    res[ 'H(X,Y)' ] = entropy(mat.ravel())
    # h(x)
    px = np.sum(mat, axis=0)
    res['H(X)'] = entropy(px)
    # h(y)
    py = np.sum(mat, axis=1)
    res['H(Y)'] = entropy(py)

    # h(x|y)
    pY0, pY1 = [getPY(y) for y in [0,1]]
    hxy = pY0 * entropy(mat[0,:], True) + pY0 * entropy(mat[1,:], True)
    res['H(X|Y)'] = hxy

    # h(y|x)
    pX0, pX1 = [getPX(x) for x in [0,1]]
    hyx = pX0 * entropy(mat[:,0], True) + pX1 * entropy(mat[:,1], True)
    res['H(Y|X)'] = hyx

    # rest
    res['H(X)+H(Y)-H(X,Y)'] = res['H(X)'] + res['H(Y)'] - res['H(X,Y)']
    res['H(X)-H(X|Y)'] = res['H(X)'] + - res['H(X|Y)']
    res['H(Y)-H(Y|X)'] = res['H(Y)'] + - res['H(Y|X)']
    
    with open('sol1.tsv', 'w' ) as f:
        f.write("Entropy\t Value\n")
        for k, v in res.items():
            print(f'{k:20s} {v:g} bits')
            f.write(f'{k}\t{v}\n')

if __name__ == '__main__':
    main()

