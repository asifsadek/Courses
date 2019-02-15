"""prefix_free_code.py: 
generate prefix free code.
"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

def generate_code(pis, nis):
    pass

def main():
    pis = [float(x) for x in sys.argv[0].split(',')]
    nis = [float(x) for x in sys.argv[1].split(',')]
    generate_code(pis, nis)

def test():
    pass

if __name__ == '__main__':
    test()
