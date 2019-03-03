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

def main():
    print( "[INFO ] Solving problem 3" )
    dp = 1e-2
    aa = np.arange(0, 1, dp)
    ps = []
    for a in aa:
        for b in np.arange(0, 1-a, dp):
            for c in np.arange(0, 1-a-b, dp):
                ps.append((a, b, c))

    with open('prob3.csv', 'w' ) as f:
        f.write("a b c h\n")
        for a, b, c in ps:
            h = a*math.log(2,2)+b*math.log(3,2)+c*math.log(6,2)
            print(a, b, c, h)
            f.write(f"{a} {b} {c} {h}\n")
    
if __name__ == '__main__':
    main()
