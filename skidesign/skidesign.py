"""
ID: drpradh1
LANG: PYTHON3
TASK: skidesign
"""
import sys
sys.stdin = open('skidesign.in', 'r')
sys.stdout = open('skidesign.out', 'w')

n = int(input())
l = [int(input()) for _ in range(n)]

def cost(lb, hb):
    r = sum(0 if lb < x < hb else min([(lb - x)**2, (x - hb)**2]) for x in l)
    return r

print(min(map(cost, range(0, 84), range(17, 101))))
