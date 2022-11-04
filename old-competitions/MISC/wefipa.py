a, b, c, d = map(int, open('paint.in').read().split())
if a > c: a, b, c, d = c, d, a, b
print(max([b, d]) - min([a, c]) - (c - b if c > b else 0), file=open('paint.out', 'w'))
