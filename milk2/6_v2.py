"""
ID: drpradh1
LANG: PYTHON3
TASK: milk2
"""
with open('milk2.in') as f:
    next(f)
    times = sorted((tuple(map(int, x.strip().split())) for x in f), key = lambda x: x[0])

starttime = times[0][0]
endtime = times[0][1]
maxrange = 0

lastendtime = times[0][1]
maxnorange = 0
for x, y in times:
    if endtime >= x:
        endtime = y if y > endtime else endtime
    else:
        range_len = endtime - starttime
        if range_len > maxrange:
            maxrange = range_len
        starttime = x
        endtime = y

    norange_len = x - lastendtime
    if norange_len > maxnorange:
        maxnorange = norange_len
    lastendtime = y if y > lastendtime else lastendtime

range_len = endtime - starttime
if range_len > maxrange:
    maxrange = range_len

print(maxrange, maxnorange)
print(maxrange, maxnorange, file=open('milk2.out', 'w'))
