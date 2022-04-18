"""
ID: drpradh1
LANG: PYTHON3
TASK: dualpal
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

def check_n(n):
    count = 0
    for x in range(2, 11):
        count += is_base_palindrome(x, n)
    return count >= 2

def render(b, n):
    return ''.join(printable[x] for x in to_base(b, n)).upper()

with open('dualpal.in') as f:
    n, s = map(int, f.read().split())

with open('dualpal.out', 'w') as fw:
    count = 0
    s += 1
    while count != n:
        if check_n(s):
            count += 1
            print(s, file = fw)
        s += 1
