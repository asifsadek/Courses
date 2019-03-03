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

def ternary_trans(a, b, c):
    x, y = a/2+c, (3**0.5)*c/2
    return x, y

def plot(data):
    import matplotlib as mpl
    import scipy.interpolate
    import pandas as pd
    import matplotlib.pyplot as plt
    a, b, c, h = [np.array(x) for x in zip(*data)]
    x, y = ternary_trans(a, b, c)
    X, Y = np.meshgrid( np.linspace(min(x), max(x), 300)
            , np.linspace(min(y), max(y), 300)
            )
    H = scipy.interpolate.griddata((x,y), h, (X, Y))
    ax = plt.subplot(111)
    im = ax.contour(X, Y, H, levels=20, cmap='jet')

    pts = []
    for i, l in enumerate(im.levels):
        for segs in im.allsegs[i]:
            for x, y in segs:
                pts.append((x, y, l))
    plt.colorbar(im, ax=ax)
    plt.savefig( f'{__file__}.png' )
    return pts
    

def main():
    print( "[INFO ] Solving problem 3" )
    dp = 5e-3
    ps = []
    allData = []
    for a in np.arange(0, 1, dp):
        for b in np.arange(0, 1-a, dp):
            for c in np.arange(0, 1-a-b, dp):
                h = a*math.log(2,2)+b*math.log(3,2)+c*math.log(6,2)
                allData.append((a,b,c,h))
    # plot the data.
    pts = plot(allData)
    with open('prob3.csv', 'w' ) as f:
        f.write( 'a b c h\n')
        for x, y, h in pts:
            a = 2*(x-2*y/(3**0.5))
            c = 2 * y / (3**0.5)
            b = 1-a-c
            f.write(f'{a} {b} {c} {h}\n')
    print( 'Done' )
    
if __name__ == '__main__':
    main()
