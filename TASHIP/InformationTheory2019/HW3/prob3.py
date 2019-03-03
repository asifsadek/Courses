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
    x, y = b+c/2, 3*c/2
    return x, y

def plot(data):
    import matplotlib as mpl
    import scipy.interpolate
    import pandas as pd
    import matplotlib.pyplot as plt
    a, b, c, h = [np.array(x) for x in zip(*data)]
    x, y = a, b
    X, Y = np.meshgrid(np.linspace(min(x), max(x), 200)
            , np.linspace(min(y), max(y), 200)
            )
    Z = scipy.interpolate.griddata((x,y), h, (X, Y))
    ax = plt.subplot(111)
    c = ax.contour(X, Y, Z, levels=20, cmap='jet')
    levels = c.levels
    pts=[]
    for i, segs in enumerate(c.allsegs):
        z = levels[i]
        for seg in segs:
            for x, y in seg:
                pts.append((x,y,1-x-y,z))

    # now plot.
    a, b, c, z = [np.array(x) for x in zip(*pts)]
    x, y = ternary_trans(a, b, c)
    ax.clear()
    im = plt.scatter(x, y, c=z, s=1, cmap='jet')
    plt.colorbar(im, ax=ax)
    plt.title( '$H(a,b,c)$ where $a+b+c=1$')
    plt.savefig( f'{__file__}.png' )
    return pts
    

def main():
    print( "[INFO ] Solving problem 3" )
    dp = 3e-3
    aa = np.arange(0, 1, dp)
    ps = []
    allData = []
    for a in aa:
        for b in np.arange(0, 1-a, dp):
            for c in np.arange(0, 1-a-b, dp/2):
                h = a*math.log(2,2)+b*math.log(3,2)+c*math.log(6,2)
                allData.append((a,b,c,h))
    # plot the data.
    pts = plot(allData)
    with open('prob3.csv', 'w' ) as f:
        f.write( 'a b c h\n')
        for x, y, z, h in pts:
            f.write(f'{x} {y} {z} {h}\n')
    print( 'Done' )
    
if __name__ == '__main__':
    main()
