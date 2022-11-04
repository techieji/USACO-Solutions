with open("lostcow.in") as fin:
    ox, y = map(int, fin.readline().split())

distance = 0
step = 1
x = ox
while True:
    newx = ox + step
    if min(x, newx) <= y <= max(x, newx):
        distance += abs(x - y)
        break
    else:
        distance += abs(newx - x)
    step *= -2
    x = newx

with open('lostcow.out', 'w') as fout:
    print(distance, file=fout)
