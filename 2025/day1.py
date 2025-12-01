curr = 50
res = 0
for line in open("day1_input.txt", 'r'):
    prev = curr
    direction, distance = line[0], int(line[1:])

    res += distance // 100
    distance %= 100
    if distance == 0:
        continue

    if direction == 'L':
        curr -= distance
    else:
        curr += distance
    curr %= 100

    if prev == 0:
        continue

    if curr == 0:
        res += 1
    elif direction == 'L' and curr > prev:
        res += 1
    elif direction == 'R' and curr < prev:
        res += 1
print(res)


