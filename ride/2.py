"""
ID: drpradh1
LANG: PYTHON3
PROG: ride
"""
from functools import reduce
from operator import mul
import string

get_n = lambda st: reduce(mul, map(lambda x: string.ascii_uppercase.index(x) + 1, st)) % 47

with open('ride.out', 'w') as fout, open('ride.in') as fin:
    if get_n(fin.readline().strip()) == get_n(fin.readline().strip()):
        print('GO', file=fout)
    else:
        print('STAY', file=fout)
