"""prob3.py: 
"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import numpy as np
import math
import random

def ternary_trans(a, b, c):
    x, y = c/2+b, np.sqrt(3)*c/2
    assert (x <= 1.0).all(), x.max()
    assert (y <= 1.0).all(), y.max()
    return x, y

def inv_tern(x, y):
    c = 2*y/math.sqrt(3)
    b = (x-c/2)
    return 1-b-c, b, c

def plot(data):
    import scipy.interpolate
    import matplotlib.pyplot as plt
    a, b, c, h = [np.array(x) for x in zip(*data)]
    x, y = ternary_trans(a, b, c)
    X, Y = np.meshgrid(np.linspace(min(x), max(x), 200)
            , np.linspace(min(y), max(y), 200)
            )
    H = scipy.interpolate.griddata((x,y), h, (X, Y))
    ax = plt.subplot(111)
    im = ax.contour(X, Y, H, levels=30, cmap='jet')
    plt.colorbar(im, ax=ax)
    plt.savefig( f'{__file__}.png' )

    pts = []
    for i, l in enumerate(im.levels):
        for segs in im.allsegs[i]:
            for x, y in segs:
                pts.append((x, y, l))
    return pts

def compute_h(a, b, c):
    return a*math.log(2,2)+b*math.log(3,2)+c*math.log(6,2)

def get_samples_uniform():
    # This does not do so well.
    allData = []
    dp = 0.5e-2
    for a in np.arange(0, 1, dp):
        for b in np.arange(0, 1-a, dp/2):
            for c in np.arange(0, 1-a-b, dp/3):
                allData.append((a,b,c,compute_h(a, b,c)))
    return allData

def get_samples_random():
    N = 1e6
    data = []
    for i in range(int(N)):
        a = random.uniform(0, 1)
        b = random.uniform(0, 1-a)
        c = 1-a-b
        data.append((a,b,c,compute_h(a, b,c)))
    return data

def main():
    print( "[INFO ] Solving problem 3" )
    # plot the data.
    algo = 'random'
    if algo == 'uniform':
        data = get_samples_uniform()
    else:
        data = get_samples_random()

    pts = plot(data)
    with open(f'prob3.{algo}.csv', 'w' ) as f:
        f.write( 'a b c h\n')
        oldh = 0
        for x, y, h in pts:
            a, b, c = inv_tern(x, y)
            if a * b * c < 0:
                print('E', a, b, c)
                continue
            if h != oldh:
                oldh = h
                f.write('\n')
            f.write(f'{a:.4f} {b:.4f} {c:.4f} {h:.4f}\n')
    print( 'Done' )
    
if __name__ == '__main__':
    main()
