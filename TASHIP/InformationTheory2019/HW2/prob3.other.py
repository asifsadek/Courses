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

def enumerate_states():
    global N
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
    for k in dist:
        dist[k] = 1/len(dist)
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
    print(xs)
    print( f'hx={hx:.4f}, hy={hy:.4f}, hxy={hxy:.4f}' )
    return hx+hy-hxy

def prob_equal_ncoins(n):
    # This step is cruicial.
    # what is the probability of both side being equal? It is equal to
    # picking the 2*n normal coins i.e. 11/12*10/11*.... If there is a
    # counterfiet coin then probability is (11/12)^(2n). If the
    # probability that a counterfiet is in the heap is 0.5 then this
    # proability is (1-p) + p(11/12)^*2n . For simplicity let's
    # assume p=0.5
    e = 1.0
    for x in range(12, 12-2*n, -1):
        e *= (x-1)/x
    return 1/3 + 2*e/3


def save_df(df, n):
    df['Pr(Y)'] = df.sum(axis=1)
    xs = df.sum(axis=0)
    df.loc['P(X)'] = xs
    df.to_csv( f'{n}.csv', index=True)

def compute_probs(n, states):
    EQ, RH, LH = [], [], []
    for st in states:
        left, right=st[:n], st[n:2*n]
        if left == right:
            EQ.append(1)
            RH.append(0)
            LH.append(0)
        elif 'l' in left or 'h' in right:
            EQ.append(0)
            RH.append(1)
            LH.append(0)
        else:
            EQ.append(0)
            RH.append(0)
            LH.append(1)

    df = pd.DataFrame()
    df['EQ'] = EQ
    df['RH'] = RH
    df['LH'] = LH
    return df

def main( ):
    states = list(enumerate_states().keys())
    for n in range(2,7):
        print( f"[INFO ] Weighing {n} vs {n} coins." )
        df = compute_probs(n, states)
        print(df)
    print( states )

if __name__ == '__main__':
    main()
