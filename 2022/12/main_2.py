# Open and read file
with open('input.txt') as file:
    lines = file.read().splitlines()
file.close()

# Create map as array of arrays, and find starting point and end point
map = []
startingpoints = []
i_end, j_end = 0, 0
for i, line in enumerate(lines):
    map.append([])
    for j, char in enumerate(line):
        map[i].append(char)
        if char == 'a':
            startingpoints.append((i, j))
        elif char == 'S':
            startingpoints.append((i, j))
            map[i][j] = 'a'
        elif char == 'E':
            i_end, j_end = i, j
            map[i][j] = 'z'

shortes_path_start = (-1, -1)
shortest_path_cost = float('inf')

for startingpoint in startingpoints:

    # Use Dijkstra to find path. Create dict of visited points and initialize costs to inf. Costs track number of steps
    visited = {}
    costs = []
    for row in map:
        costs.append([float('inf') for point in row])

    # First node has cost of 0, initialize starting indices and create a queue for nodes to search next
    i, j = startingpoint[0], startingpoint[1]
    costs[i][j] = 0
    queue = {(i, j): 0}

    # While we have not visited the end node
    while (i_end, j_end) not in visited:

        # Iterate through all adjacent nodes, not including diagonal points
        for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:

            # Make sure it's a valid point and has not been visited yet
            if 0 <= x < len(map) and 0 <= y < len(map[0]) and (x, y) not in visited.keys():

                # Continue if not allowed move
                if ord(map[x][y]) - ord(map[i][j]) > 1:
                    continue

                # Update costs
                if costs[i][j] + 1 < costs[x][y]:
                    costs[x][y] = costs[i][j] + 1
                    # Also update the queue, we already check above that it is not visited
                    queue[(x, y)] = costs[x][y]

        # Find point in queue with least cost, to get indexes for next iteration
        try:
            i, j = min(queue, key=queue.get)
        except:
            break

        # Add point to visited, using the cost calculated. Remove that point from the queue since we have visiting it
        visited[(i, j)] = costs[i][j]
        queue.pop((i, j))

    if costs[i_end][j_end] < shortest_path_cost:
        shortest_path_cost = costs[i_end][j_end]
        shortes_path_start = (startingpoint[0], startingpoint[1])

print("Task 2: Fewest steps from startingpoint " + str(shortes_path_start) + " with cost = " + str(shortest_path_cost))
