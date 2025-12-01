curr = 50
res = 0
for line in open("day1_input.txt", 'r'):
    direction, distance = line[0], int(line[1:])
    if direction == 'L':
        curr -= distance
    else:
        curr += distance

    curr %= 100
    if curr == 0:
        res += 1
print(res)


