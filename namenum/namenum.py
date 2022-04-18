"""
ID: drpradh1
LANG: PYTHON3
TASK: namenum
"""
import re

def get_letters(n):
    return {
        2: 'A,B,C', 5: 'J,K,L', 8: 'T,U,V',
        3: 'D,E,F', 6: 'M,N,O', 9: 'W,X,Y',
        4: 'G,H,I', 7: 'P,R,S',
    }[n].replace(',', '|')

def construct_regex(l):
    return '^' + ''.join(f'(?:{get_letters(x)})' for x in l) + '$'

def read_file(filename):
    with open(filename) as f:
        return f.read()

def write_file(filename, txt):
    with open(filename, 'w') as f:
        print(txt, file = f)

inp = map(int, read_file('namenum.in').strip())
regex = construct_regex(inp)
res = re.findall(regex, read_file('dict.txt'), re.MULTILINE)
if res:
    write_file('namenum.out', '\n'.join(res))
else:
    write_file('namenum.out', 'NONE')
