"""prob3.py: 

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import random

N = 12

def possibilities(ncoins, outcome):
    global N
    normal = ["N" for i in range(N)]
    if outcome == "EQ":
        # Then there is no counterfiet in the given coins. 
        res = [ normal ]
    elif outcome == "LH":
        # Either left ncoins are heavy or right ncoins were light. All of these
        # are equally likely possibilities.
        res = []
        for i in range(ncoins):
            lc = normal.copy()
            rc = normal.copy()
            lc[i] = 'H'
            rc[ncoins+i] = 'L'
            res += [lc, rc]
    elif outcome == "RH":
        res = []
        for i in range(ncoins):
            lc = normal.copy()
            rc = normal.copy()
            lc[i] = 'L'
            rc[ncoins+i] = 'H'
            res += [lc, rc]
            
    return [''.join(x) for x in res]


def main( ):
    print(possibilities(3, 'LH'))

if __name__ == '__main__':
    main()
