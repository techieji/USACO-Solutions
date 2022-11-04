from itertools import cycle

with open('mixmilk.in') as f:
    capacities, buckets = map(list, zip(*[tuple(map(int, x.split())) for x in f]))

for x in range(1, 101):
    prev, cur = (x - 1) % 3, x % 3
    pour_amt = min([buckets[prev], capacities[cur] - buckets[cur]])
    buckets[prev] -= pour_amt
    buckets[cur] += pour_amt

with open('mixmilk.out', 'w') as f:
    print('\n'.join(map(str, buckets)), file=f)
