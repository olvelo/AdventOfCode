def basinexplorer(map, x, y, basin):
    """
    Recursive function to explore a basin

    Args:
        map: Reference to map object with heights
        x: x coordinate
        y: y coordinate
        basin: Reference to array of basin coordinates
    """
    basin.append((x, y))
    if x != 0 and map[x][y] < map[x-1][y] < 9:
        basinexplorer(map, x-1, y, basin)
    if x != (len(map) - 1) and map[x][y] < map[x+1][y] < 9:
        basinexplorer(map, x+1, y, basin)
    if y != 0 and map[x][y] < map[x][y-1] < 9:
        basinexplorer(map, x, y-1, basin)
    if y != (len(map[0]) - 1) and map[x][y] < map[x][y+1] < 9:
        basinexplorer(map, x, y+1, basin)

# Open and read file to array
input = open('09_input.txt', 'r')
map = []
for line in input:
    map.append([int(char) for char in line.strip()])
input.close()

# Find low points
lows = []
for i in range(len(map)):
    for j in range(len(map[0])):

        candidate, low = map[i][j], True

        if i != 0 and map[i-1][j] <= candidate:
            continue
        if i != (len(map) - 1) and map[i+1][j] <= candidate:
            continue

        if j != 0 and map[i][j-1] <= candidate:
            continue
        if j != (len(map[0]) - 1) and map[i][j+1] <= candidate:
            continue

        lows.append((i, j))

# Sum risk level of low points
risk = 0
for low in lows:
    risk += map[low[0]][low[1]] + 1

print('Risk level = {}'.format(risk))

# Find all basins and store their size
basin_sizes = []
for low in lows:
    # Create new basin and use recursive function to store all coordinates
    basin = []
    basinexplorer(map, low[0], low[1], basin)

    # Sort and count without counting duplicates
    basin.sort()
    size = 1
    for i in range(1, len(basin)):
        if basin[i] != basin[i-1]:
            size += 1
    basin_sizes.append(size)

basin_sizes.sort(reverse=True)

print('Sum of three largest basins = {}'.format(basin_sizes[0] * basin_sizes[1] * basin_sizes[2]))
