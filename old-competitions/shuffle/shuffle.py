
with open('shuffle.in') as fin:
    fin.readline()
    order = map(int, fin.readline().split())
    cows = fin.readline().split()

def inverse(order):
    return [x + 1 for x, _ in sorted(enumerate(order), key=lambda x: x[1])]

def shuffle(cows, order):
    return [x for _, x in sorted(zip(order, cows))]

inv = inverse(order)

for x in range(3):
    cows = shuffle(cows, inv)

with open('shuffle.out', 'w') as fout:
    print('\n'.join(cows), file=fout)
