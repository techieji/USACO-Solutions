"""
ID: drpradh1
LANG: PYTHON3
TASK: barn1
"""

with open('barn1.in') as f:
    max_board, stall_num, _occupied_stall_num = map(int, next(f).split())
    spots = [0] * (stall_num + 10)    # Bitlist
    for line in f:
        spots[int(line)] = 1

first_index, *_, last_index = [i for i, x in enumerate(spots) if x == 1]
spots = spots[first_index:last_index + 1]
print(spots)

spots += [0]

occupied_blocks = []
inter_blocks = []

last_state = 0
block_len = 0
for x in spots:
    if last_state == 0 and x == 1:
        inter_blocks.append(block_len)
        block_len = 0
    if last_state == 1 and x == 0:
        occupied_blocks.append(block_len)
        block_len = 0
    block_len += 1
    last_state = x

boards = len(occupied_blocks)
covered_stalls = sum(occupied_blocks)
while not boards < max_board:
    boards -= 1
    covered_stalls += min(inter_blocks)
    inter_blocks.remove(min(inter_blocks))

print(covered_stalls, file=open('barn1.out', 'w'))
