with open('traffic.in') as f:
    n = int(f.readline())
    l = [f.readline().split() for _ in range(n)]

def intersection(i1, i2):
    return [max(i1[0], i2[0]), min(i1[1], i2[1])]

def sub(i1, i2):
    return [i1[0] - i2[1], i1[1] - i2[0]]

def add(i1, i2):
    return [i1[0] + i2[0], i1[1] + i2[1]]

in_ = [0, 1000]
for name, *_i in reversed(l):
    i = list(map(int, _i))
    if name == 'on':
        in_ = sub(in_, i)
    elif name == 'none':
        in_ = intersection(in_, i)
    elif name == 'off':
        in_ = add(in_, i)

# Could probably factor out one of these
out = [0, 1000]
for name, *_i in l:
    i = list(map(int, _i))
    if name == 'on':
        out = add(out, i)
    elif name == 'none':
        out = intersection(out, i)
    elif name == 'off':
        out = sub(out, i)

with open('traffic.out', 'w') as fout:
    print('{} {}'.format(*in_), file=fout)
    print('{} {}'.format(*out), file=fout)
