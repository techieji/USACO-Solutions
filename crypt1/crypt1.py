"""
ID: drpradh1
LANG: PYTHON3
TASK: crypt1
"""
import itertools as it

with open('crypt1.in') as f:
    f.readline()
    digits = f.readline().split()    # Strings

def valid_num(n: str):
    return all(x in digits for x in n)

def validate_direct(a):
    n1, n2 = a
    res = str(int(n1) * int(n2))
    return valid_num(res) and len(res) == 4

def validate_partial_product(a):
    n1, n2 = a
    p1 = str(int(n1) * int(n2[1]))
    p2 = str(int(n1) * int(n2[0]))
    r = valid_num(p1) and valid_num(p2) and len(p1) == 3 and len(p2) == 3
    if r:
        print(n1, n2)
    return r

def all_c():
    for ns in it.product(*[digits]*5):
        n1 = ''.join(ns[:3])
        n2 = ''.join(ns[3:])
        yield (n1, n2)

ans = sum(1 for _ in filter(validate_partial_product, filter(validate_direct, all_c())))
print(ans, file=open('crypt1.out', 'w'))
