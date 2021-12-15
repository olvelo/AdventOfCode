# Open and read file, getting map of risks
map = []
input = open('15_input.txt', 'r')
for line in input:
    map.append([int(risk) for risk in line.strip()])
input.close()

# How many times we should expand the map. Use 5 to run task 2 and 1 to run task 1
map_multiplier = 5

# Create expanded map, can be done more smoothly..
map_expanded = [[0 for i in range(len(map)*map_multiplier)] for j in range(len(map[0])*map_multiplier)]
for i in range(map_multiplier):
    for j in range(map_multiplier):
        for k in range(len(map)):
            for n in range(len(map[0])):
                # Calculate value in expanded map, making sure numbers are wrapping correctly
                map_expanded[i * len(map) + k][j * len(map[0]) + n] = ((map[k][n] + i + j) - 1) % (9) + 1

# Use Dijkstra to find path with min risk. Create dict of visited points and initialize costs to inf
visited = {}
costs = []
for row in map_expanded:
    costs.append([float('inf') for risk in row])

# First node has cost of 0, initialize starting indices and create a queue for nodes to search next
i, j = 0, 0
costs[i][j] = 0
queue = {(0,0):0}

# While we have not visited the end node
while (len(map_expanded) - 1, len(map_expanded[0]) - 1) not in visited:

    # Iterate through all adjacent nodes, not including diagonal points
    for (x, y) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        # Make sure it's a valid point and has not been visited yet
        if 0 <= x < len(map_expanded) and 0 <= y < len(map_expanded[0]) and (x, y) not in visited.keys():
            # Update costs
            if costs[i][j] + map_expanded[x][y] < costs[x][y]:
                costs[x][y] = costs[i][j] + map_expanded[x][y]
                # Also update the queue, we already check above that it is not visited
                queue[(x,y)] = costs[x][y]

    # Find point in queue with least cost, to get indexes for next iteration
    i, j = min(queue, key=queue.get)

    # Add point to visited, using the cost calculated. Remove that point from the queue since we have visiting it
    visited[(i, j)] = costs[i][j]
    queue.pop((i, j))

print(f'Lowest total risk of any path = {visited[(len(map_expanded) - 1, len(map_expanded[0]) - 1)]}')
