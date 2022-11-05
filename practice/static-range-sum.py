import itertools as it
n, q = map(int, input().split())
a = map(int, input().split())
prefix = list(it.accumulate(a))
for _ in range(q):
    lb, ub = map(int, input().split())
    e = prefix[ub - 1]
    l = prefix[lb - 1] if lb != 0 else 0
    print(e-l)