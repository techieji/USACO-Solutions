"""
ID: drpradh1
LANG: PYTHON3
TASK: transform
"""
import itertools as it

def p(a):
    print(a)
    return a

with open('transform.in') as _f:
    f = list(_f)
    n = int(f[0])
    square = [list(x.strip()) for x in f[1:n+1]]
    result = [list(x.strip()) for x in f[n+1:]]

num = 1
def mark(fn, n=None):
    global num
    if n is None:
        fn.n = num
        num += 1
    else:
        fn.n = n
    return fn

@mark
def rotate90(n, s):
    res = []
    for x in range(n):
        interm = []
        for y in s:
            interm.append(y[x])
        res.append(list(reversed(interm)))
    return res
@mark
def rotate180(n, s): return rotate90(n, rotate90(n, s))
@mark
def rotate270(n, s): return rotate90(n, rotate180(n, s))
@mark
def reflect(_, s): return [list(reversed(x)) for x in s]
@mark
def combine(n, s, fn): return fn(n, reflect(n, s))
@mark
def nochange(_, s): return s

nochange.n = 6

def find(n, s, sf):
    rots = [rotate90, rotate180, rotate270]
    for fn in [*rots, reflect, *map(lambda f: mark(lambda n, s: combine(n, s, f), n=5), rots), nochange]:
        res = fn(n, s)
        # print(fn, len(res), len(res[0]), res)
        if fn(n, s) == sf:
            return fn.n
    return 7

# print(rotate90(n, square))
print(find(n, square, result), file=open('transform.out', 'w'))
