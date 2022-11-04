from string import ascii_lowercase
from collections import Counter
import sys

sys.stdin = open('blocks.in')
sys.stdout = open('blocks.out', 'w')

n = int(input())

letters = Counter()

for _ in range(n):
    a, b = input().split()
    letters += Counter(a) | Counter(b)

for s in ascii_lowercase:
    print(letters[s])
