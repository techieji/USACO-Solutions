f = open('milk2.in', 'w')

f.write('5000\n')
c = 0
for x in range(5000):
    f.write(f'{c} {c + 200}\n')
    c += 200
