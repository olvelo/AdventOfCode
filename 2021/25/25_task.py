# Open and read file to set up map
map = []
input = open('25_input.txt', 'r')
for i, line in enumerate(input):
    map.append([])
    for char in line.strip():
        map[i].append(char)
input.close()

def moveright(map):
    """
    Take in map anc construct new map by moving right
    Args:
        map: The original map

    Returns: The new map after moving right
    """
    newmap = [['.' for x in map[0]] for x in map]

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '>':
                j_check = j + 1 if j < len(map[0]) - 1 else 0
                j_new = j_check if map[i][j_check] == '.' else j
                newmap[i][j_new] = '>'
            elif map[i][j] == 'v':
                newmap[i][j] = map[i][j]

    return newmap

def movedown(map):
    """
    Take in map anc construct new map by moving down
    Args:
        map: The original map

    Returns: The new map after moving down
    """
    newmap = [['.' for x in map[0]] for x in map]

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'v':
                i_check = i + 1 if i < len(map) - 1 else 0
                i_new = i_check if map[i_check][j] == '.' else i
                newmap[i_new][j] = 'v'
            elif map[i][j] == '>':
                newmap[i][j] = map[i][j]

    return newmap

# Variables to check if the map changed and count the number of steps with a changing map
mapchanged, steps = True, 0
while mapchanged:
    # Perform movement right and then down
    newmap = moveright(map)
    newmap = movedown(newmap)

    # Check if the map changed
    if map == newmap:
        mapchanged = False

    # Increment number of steps and update the map
    steps += 1
    map = newmap

print(steps)