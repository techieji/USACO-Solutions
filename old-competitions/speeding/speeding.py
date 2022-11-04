with open('speeding.in') as fin:
    cow_speeds = []
    road_speeds = []
    m, n = map(int, fin.readline().split())
    for x in range(m):
        length, speed = map(int, fin.readline().split())
        road_speeds += [speed] * length
    for x in range(n):
        length, speed = map(int, fin.readline().split())
        cow_speeds += [speed] * length

with open('speeding.out', 'w') as fout:
    print(max(0, max(map(lambda x, y: x - y, cow_speeds, road_speeds))), file=fout)
