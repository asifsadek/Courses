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
from decimal import Decimal 

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
            l[i], h[i] = 'l', 'h'
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
        dist[''.join(x)] = 1.0/len(res)
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
    hx = entropy(xs)
    hy = entropy(ys)
    hxy = entropy(xys)
    print( f'hx={hx:.4f}, hy={hy:.4f}, hxy={hxy:.4f}' )
    return hx+hy-hxy

def prob_equal_ncoins(n):
    # This step is cruicial.
    # what is the probability of both side being equal? It is equal to
    # picking the 2*n normal coins i.e. 11/12*10/11*.... 
    # We pick a light, heavy or normal coin with the probability of 1/3. That is
    # there is 2/3 chance that there is counterfiet coins.
    e = (12-2*n)/12
    return 1/3+2*e/3

def save_df(df, n):
    df['Pr(Y)'] = df.sum(axis=1)
    xs = df.sum(axis=0)
    df.loc['P(X)'] = xs
    print(df)
    df.to_csv( f'{n}.csv', index=True)

def main( ):
    for n in range(1, 7):
        df = pd.DataFrame()
        print( f'[INFO] Coins to weigh {n}' )
        for outcome in ['LH', 'RH', 'EQ']:
            s = pd.Series(possibilities(n, outcome))
            pBalance = prob_equal_ncoins(n)
            pNotBalance = (1-pBalance)
            if outcome == 'EQ':
                s = s*pBalance
            else:
                s = s*pNotBalance/2.0
            df[outcome] = s
        mi = mutual_information(df)
        save_df(df, n)
        print(f'\t\tMUTUAL INFORMATION={mi:.4f}')

if __name__ == '__main__':
    main()
