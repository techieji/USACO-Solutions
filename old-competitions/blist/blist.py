from operator import add
from functools import reduce, partial

def mklist(start, stop, val):
    return [val if start <= i <= stop else 0 for i in range(0, 1001)]

def addlists(ls):
    return reduce(partial(map, add), ls)

with open('blist.in') as f, open('blist.out', 'w') as fout:
    n = int(f.readline())
    print(max(addlists(mklist(*map(int, line.split())) for line in f)), file=fout)
