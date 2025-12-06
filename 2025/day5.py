ranges = []  # list of fresh ingredients ranges, inclusive
with open("day5_input.txt", 'r') as f:
    for line in f:
        split_line = line.strip().split('-')
        if len(split_line) == 2:
            ranges.append(list(map(int, split_line)))
        else:
            break
# sum the number of fresh ingredient ids that fall in the ranges

#combine the ranges
ranges.sort()
curr = ranges[0]
res = ranges[0][1] - ranges[0][0] + 1
for i in range(1, len(ranges)):
    interval = ranges[i]
    if curr[1] >= interval[0]:
        if interval[1] > curr[1]:
            res += interval[1] - curr[1]
            curr[1] = interval[1]
    else:
        curr = interval
        res += curr[1] - curr[0] + 1

print(res)