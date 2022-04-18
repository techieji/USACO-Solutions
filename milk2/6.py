"""
ID: drpradh1
LANG: PYTHON3
TASK: milk2
"""
import itertools as it

with open('milk2.in') as f:
    next(f)
    times = [range(*map(int, x.strip().split())) for x in f]

def incomplete(tf):
    try:
        if len(tf[-1]) == 1:
            return True
        else:
            return False
    except IndexError:
        return False

def a2tf(tf, x):
    if incomplete(tf):
        tf[-1] = (tf[-1][0], x)
    else:
        tf.append((x,))

maxtime = max(x.stop for x in times)
mintime = min(x.start for x in times)

alo_array = [(mintime,)]
none_array = []
atleastone = True
for x in range(mintime, maxtime + 1):
    if x % 200 == 0: print('.', end="", flush=True)
    _atleastone = any(x in n for n in times)
    if atleastone != _atleastone:
        a2tf(alo_array, x)
        a2tf(none_array, x)
        atleastone = _atleastone

if incomplete(alo_array):
    a2tf(alo_array, maxtime)
elif incomplete(none_array):
    a2tf(none_array, maxtime)

def gmr(tf):
    return max(b - a for a, b in tf)

print(gmr(alo_array), gmr(none_array))
