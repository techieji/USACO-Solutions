from operator import itemgetter

with open('wormhole.in') as f:
    n = int(next(f))
    l = [tuple(map(int, line.split(' '))) for line in f]

x_limit = max(map(itemgetter(0), l))
y_limit = max(map(itemgetter(1), l))

def run(y, l, d):
    pos = (0, y)
    seen = set()
    while True:
        if t in d:
            pos = d[t]
            seen.add(t)
        else:
            pos = (pos[0] + 1, pos[1])
        if pos[0] > x_limit:
            return 1
        if pos in seen:
            return 0

def test_pairing(l, p):
    d = {**dict(p), **dict(map(tuple, map(reversed, p)))}
