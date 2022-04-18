"""
ID: drpradh1
LANG: PYTHON3
TASK: palsquare
"""
from string import printable

def highest_power(b, n):
    acc = b
    inc = 0
    while n >= acc:
        acc *= b
        inc += 1
    return inc

def to_base(b, n):
    digits = []
    for x in range(highest_power(b, n), -1, -1):
        q, rem = divmod(n, b**x)
        digits.append(q)
        n = rem
    return digits

def is_base_palindrome(b, n):
    d = to_base(b, n)
    return d == list(reversed(d))

def render(b, n):
    return ''.join(printable[x] for x in to_base(b, n)).upper()

with open('palsquare.in') as f:
    b = int(f.read())

with open('palsquare.out', 'w') as fw:
    for x in range(1, 301):
        if is_base_palindrome(b, x**2):
            print(render(b, x), render(b, x**2), file = fw)
