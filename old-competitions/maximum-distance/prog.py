from itertools import combinations

i = int(input())

xs = map(int, input().split())
ys = map(int, input().split())

def v(l):
    p1, p2 = l
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

print(max(map(v, combinations(zip(xs, ys), 2))))
