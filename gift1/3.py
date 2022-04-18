"""
ID: drpradh1
LANG: PYTHON3
TASK: gift1
"""

with open('gift1.in') as f:
    n = int(f.readline())
    people = [f.readline().strip() for x in range(n)]
    whom = {}
    money = {}
    for _ in range(n):
        name = f.readline().strip()
        money_, whom_n = map(int, f.readline().split())
        money[name] = money_
        whom[name] = [f.readline().strip() for x in range(whom_n)]

account = {a: 0 for a in people}

for x in people:
    recipients = whom[x]
    given = money[x]
    if len(recipients) != 0:
        account[x] -= given
        foreach, leftover = divmod(given, len(recipients))
        account[x] += leftover
        for y in recipients:
            account[y] += foreach

print('\n'.join(f'{x} {y}' for x, y in account.items()), file=open('gift1.out', 'w'))
