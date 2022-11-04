with open('cowsignal.in') as fin, open('cowsignal.out', 'w') as fout:
    n, m, k = map(int, fin.readline().split())
    output = []
    for x in fin:
        print('\n'.join(k*[''.join(k*c for c in x.strip())]), file=fout)
