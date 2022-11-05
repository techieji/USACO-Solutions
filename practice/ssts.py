import sys

sys.stdin = open('div7.in')
#sys.stdout = open('div7.out', 'w')

n = int(input())
l = []   # Make tuple?

maxlen = 0

for i in range(n):
    a = int(input())
    l.append(0)
    for f, x in enumerate(l):
        l[f] += a   # Perf
        if (a + x) % 7 == 0 and f - i > maxlen:
            maxlen = f - i

print(l)
print(maxlen)