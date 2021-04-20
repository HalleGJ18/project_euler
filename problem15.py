#project euler #15
#lattice paths

x = 0
y = 0

grid = []
n = 2

for i in range(0,n):
    grid.append([])

for i in range(0,n):
    for j in range(0,n):
        grid[i].append(j)

for i in grid:
    print(i)
