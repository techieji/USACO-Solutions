"""
ID: drpradh1
LANG: PYTHON3
TASK: friday
"""

days = ['sa', 'su', 'm', 'tu', 'w', 'th', 'f']

class Date:
    def __init__(self, d, m, y, dow):
        self.day = d
        self.month = m
        self.year = y
        self.dow = dow

    @property
    def is_leap(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                return not self.year % 400
            return True
        return False

    def adjust_month(self):
        if ((self.day > 31 and self.month in [1, 3, 5, 7, 8, 10, 12]) or 
            (self.day > 30 and self.month in [4, 6, 9, 11]) or 
            (self.day > 29 and self.month == 2 and self.is_leap) or
            (self.day > 28 and self.month == 2 and not self.is_leap)):
            self.day = 1
            self.month += 1

    def adjust_year(self):
        if self.month > 12:
            self.month = 1
            self.year += 1

    def inc(self):
        self.day += 1
        self.adjust_month()
        self.adjust_year()
        self.dow = days[(days.index(self.dow) + 1) % 7]

with open('friday.in') as f:
    n = int(f.read())

freq = {a: 0 for a in days}
d = Date(1, 1, 1900, 'm')

while d.year < 1900 + n:
    if d.day == 13:
        freq[d.dow] += 1
    d.inc()

print(' '.join(map(str, freq.values())), file=open('friday.out', 'w'))
