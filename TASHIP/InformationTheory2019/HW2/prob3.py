"""prob3.py: 

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import math
import pandas as pd

N = 12

def possibilities(ncoins, outcome):
    global N
    assert 2*ncoins <= N
    # Initialize the probability table.
    normal = ["." for i in range(N)]
    dist = {''.join(normal) : 0.0}
    for i in range(N):
        s = normal.copy()
        s[i] = 'h'
        dist[''.join(s)] = 0.0
    for i in range(N):
        s = normal.copy()
        s[i] = 'l'
        dist[''.join(s)] = 0.0

    if outcome == "EQ":
        # Then there is no counterfiet in the given coins. They are in the rest.
        res = [normal]
        for i in range(2*ncoins, N):
            l = normal.copy()
            h = normal.copy()
            l[i], h[i] = 'h', 'l'
            res += [l, h]
    elif outcome == "LH":
        # Either left ncoins are heavy or right ncoins were light. All of these
        # are equally likely possibilities.
        res = []
        for i in range(ncoins):
            lc = normal.copy()
            rc = normal.copy()
            lc[i] = 'h'
            rc[ncoins+i] = 'l'
            res += [lc, rc]
    elif outcome == "RH":
        res = []
        for i in range(ncoins):
            lc = normal.copy()
            rc = normal.copy()
            lc[i] = 'l'
            rc[ncoins+i] = 'h'
            res += [lc, rc]
            
    for x in res:
        dist[''.join(x)] = 1 / len(res)
    return dist

def entropy(ps):
    e = 0.0
    assert math.isclose(sum(ps), 1.0)
    for p in ps:
        if p == 0.0:
            continue
        e += - p * math.log(p, 2)
    return e

def mutual_information(df):
    # assuming that LH, RH and EQ are equally likely.
    xs = df.sum(axis=0)
    ys = df.sum(axis=1)
    xys = df.values.ravel().tolist()
    assert math.isclose(sum(xs),1.0), sum(xs)
    assert math.isclose(sum(ys),1.0), sum(ys)
    #  print('xs', xs.values)
    #  print('ys', ys.values)
    #  print('xys', xys)
    hx = entropy(xs)
    hy = entropy(ys)
    hxy = entropy(xys)
    print(xs)
    print( f'hx={hx:.4f}, hy={hy:.4f}, hxy={hxy:.4f}' )
    return hx+hy-hxy

def prob_equal_ncoins(n):
    p = 1.0
    for l in range(12-n+1,12+1):
        p = p*(l-1)/l
    return p

def main( ):
    for n in range(1, 7):
        df = pd.DataFrame()
        print( f'[INFO] Coins to weigh {n}' )
        for outcome in ['LH', 'RH', 'EQ']:
            s = pd.Series(possibilities(n, outcome))
            # what is the probability of both side being equal is equal to
            # picking the 2*n coins of equal weight. If there is always a
            # counterfiet coin then probability is (11/12)^(2n). If the
            # probability that a counterfiet is in the heap is 0.5 then this
            # proability is (1-p) + p(11/12)^*2n . For simplicity let's
            # assume p=0.5
            pBalance = prob_equal_ncoins(n)
            pNotBalance = (1-pBalance)
            if outcome == 'EQ':
                s = s*pBalance
            else:
                s = s*pNotBalance/2.0
            df[outcome] = s
        mi = mutual_information(df)
        #  print(df)
        print(f'\t\tMUTUAL INFORMATION={mi:.4f}')

if __name__ == '__main__':
    main()
