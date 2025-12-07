data = []
line = input().strip()
while line != "":
    data.append(line)
    line = input().strip()
dial = 50
zeros = 0
for step in data:
    d = step[0]
    n = int(step[1:]) % 100
    if d == 'R':
        dial = (dial + n) % 100
    else:
        dial = (dial - n) % 100
    if dial == 0:
        zeros += 1
print(zeros)
# Advent of Code 2025 Day 1 Part 1