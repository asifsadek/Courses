# -*- coding: utf-8 -*-
"""prob1.py: 

    Solution to the problem 1.

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import random
import math

codewords_ = dict(A='01', B='11', C='001', D='0000', E='0001'
        , F='1001', G='1010', H='1011')

def is_prefix_of_others(code, others):
    # check if the given string is prefix of other strings.
    for o in others:
        if code == o[:len(others)]:
            return o
    return None

def check_prefix_free(codewords):
    # A code is instantaneous is no code is prefix of any other code.
    sortedCodes = sorted( codewords.values(), key=lambda x: len(x))
    for i, c in enumerate(sortedCodes[:-1]):
        res = is_prefix_of_others(c, sortedCodes[i+1:])
        if res is not None:
            print(f'[WARN] {c} is prefix of {res}')
            return False
    return True

def parta():
    global codewords_
    print('=== (a)')
    if check_prefix_free(codewords_):
        print('Code is instantaneous')
    else:
        print('Code is not instantaneous')

def partb():
    global codewords_
    print( '=== (b)')
    # alphabet size is 2
    r = 2
    s = sum([r**-len(v) for k, v in codewords_.items()])
    assert s < 1.0, f'Does not satifies Kraft inequality since {s}>1.'
    print( f'Satifies Kraft inequality since {s}<1.')
    return True

def decode(s):
    # not very efficient way to decode.
    global codewords_
    replace = { v : k for k, v in codewords_.items() }
    maxL = 4
    decoded = True
    x, res = '', ''
    while s:
        x += s.pop(0)
        if x in replace:
            res += '%{}s'.format(len(x)) % replace[x]
            x = ''
        if len(x) > maxL:
            res += '%{}s'.format(maxL) % 'x'
            decoded = False
            break
    return res, decoded

def partc():
    # lets generate a random string and try to decode it.
    s = random.choices(['1','0'], k=random.randint(10,20))
    print(''.join(s))
    res, decoded = decode(s)
    print(res)
    if not decoded:
        print( 'Failed to decode')
        return False
    print( 'Successfully decoded')
    return True


def main():
    parta()
    partb()
    print( '=== (c)')
    res = True
    while res:
        res=partc()

if __name__ == '__main__':
    main()

