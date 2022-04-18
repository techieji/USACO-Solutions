"""
ID: drpradh1
LANG: PYTHON3
TASK: beads
"""

from collections import deque
import itertools as it

with open('beads.in') as f:
    n = int(f.readline())
    _beads = f.readline().strip()

def get_colors(l):
    a = [x for x in l if x != 'w']
    if len(a) == 0:
        return 'r', 'r'
    else:
        return a[0], a[-1]

def paint(l):
    lc, rc = get_colors(l)
    ld, rd = False, False
    for x in range(len(l)):
        y = len(l) - x - 1
        if l[x] == 'w' and not ld: l[x] = lc
        if l[x] not in ['w', lc]: ld = True
        if l[y] == 'w' and not rd: l[y] = rc
        if l[y] not in ['w', rc]: rd = True

def count(l):
    lc, rc = l[0], l[-1]
    count = 0
    i = 0
    try:
        while l[0] == lc or l[-1] == rc:
            if l[0] == lc: 
                l.popleft()
                count += 1
            if l[-1] == rc: 
                l.pop()
                count += 1
    finally:
        return count

def rotate(l):
    l.append(l.popleft())

# beads = deque(input('> '))
beads = deque(_beads)
values = []
paint(beads)

for x in range(len(beads)):
    rotate(beads)
    l = beads.copy()
    paint(l)
    values.append(count(l))

# print(max(values))
print(max(values), file=open('beads.out', 'w'))
