ranges = []  # list of fresh ingredients ranges, inclusive
ids = []  # list of ingredient ids
with open("day5_input.txt", 'r') as f:
    lines = f.read().splitlines()

for line in lines:
    split_line = line.strip().split('-')
    if len(split_line) == 2:
        ranges.append(list(map(int, split_line)))
    else:
        if split_line[0] == "":
            continue
        ids.append(int(split_line[0]))

#print(ranges)
#print(ids)
#print number of fresh ingredient ids
# first, combine the ranges
ranges.sort()
ranges_combined = []
for interval in ranges:
    if not ranges_combined:
        ranges_combined.append(interval)
        continue
    if ranges_combined[-1][1] >= interval[0]:
        ranges_combined[-1][1] = max(ranges_combined[-1][1], interval[1])
    else:
        ranges_combined.append(interval)
ranges = ranges_combined

# count how many ids fall into one of the ranges

# more efficiently you could binary search or
# sort ids beforehand so you wouldn't need to iterate
# through all ranges every time
fresh = 0
for id in ids:
    for l, r in ranges:
        if l <= id <= r:
            fresh += 1
            break
print(fresh)