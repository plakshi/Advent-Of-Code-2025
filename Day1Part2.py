import sys
data = [line.strip() for line in sys.stdin if line.strip()]
dial = 50
zeros = 0
for step in data:
    d = step[0]
    N = int(step[1:])
    zeros += N // 100
    n = N % 100
    if d == 'L':
        new_pos = (dial - n) % 100
        if dial != 0 and new_pos > dial and new_pos != 0:
            zeros += 1
    else:
        new_pos = (dial + n) % 100
        if dial != 0 and new_pos < dial and new_pos != 0:
            zeros += 1
    if new_pos == 0:
        zeros += 1
    dial = new_pos
print(zeros)