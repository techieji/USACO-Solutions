"""
ID: drpradh1
LANG: PYTHON3
TASK: milk
"""
from pprint import pprint
with open('milk.in') as f:
    n, _ = map(int, next(f).split())
    farmers = sorted([tuple(map(int, x.split())) for x in f])

costs = 0
for cost, units in farmers:
    if n == 0:
        break
    if units < n:
        n -= units
        costs += cost * units
    else:
        costs += cost * n
        n = 0

with open('milk.out', 'w') as f:
    print(costs, file=f)
