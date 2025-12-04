grid = []
for line in open('day4_input.txt', 'r'):
    grid.append(list(line.strip()))
#print(grid)
# @ - roll of paper
# count rolls of paper that have less than 4 surrounding rolls

def step():
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '@':
                continue
            # count surrounding rolls at any given index
            surrounding = 0
            for i1 in range(i - 1, i + 2):
                for j1 in range(j - 1, j + 2):
                    if i1 == i and j1 == j:
                        continue
                    if i1 < 0 or i1 >= len(grid) or j1 < 0 or j1 >= len(grid):
                        continue
                    if grid[i1][j1] == '@':
                        surrounding += 1
            if surrounding < 4:
                # print(i, j)
                count += 1
                grid[i][j] = 'x'
    return count

res = 0
more = step()
while more:
    res += more
    more = step()
print(res)