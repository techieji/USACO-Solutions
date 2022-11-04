"""
ID: drpradh1
LANG: PYTHON3
TASK: combo
"""

import itertools as it

with open('combo.in') as f:
    n = int(f.readline())
    c1 = tuple(map(int, f.readline().split()))
    c2 = tuple(map(int, f.readline().split()))

def sum_tuples(a):
    return tuple(x % n for x in map(sum, zip(*a)))

print(len(set(it.chain(
        map(sum_tuples, zip(it.repeat(c1), it.product([-2, -1, 0, 1, 2], repeat=3))),
        map(sum_tuples, zip(it.repeat(c2), it.product([-2, -1, 0, 1, 2], repeat=3)))
))), file=open('combo.out', 'w'))
