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
    aa = np.arange(0, 1+dp, dp)
    ps = []
    for a in aa:
        for b in np.arange(0, 1-a+dp, dp):
            for c in np.arange(0, 1-a-b+dp, dp):
                h = a*math.log(2,2)+b*math.log(3,2)+c*math.log(6,2)
                if math.isclose(h, 1.459, rel_tol=1e-3):
                    ps.append((a, b, c, float(f"{h:.3f}")))

    ps = sorted(ps, key=lambda x: x[-1])
    with open('prob3.csv', 'w' ) as f:
        f.write("a b c h\n")
        oldh = ps[0][-1]
        for a, b, c, h in ps:
            line = f"{a} {b:.2f} {c:.2f} {h}"
            if h != oldh:
                line = '\n' + line
                oldh = h
            f.write(line + '\n')
            print(line)
    
if __name__ == '__main__':
    main()
