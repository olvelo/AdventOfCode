# Open and read file
with open('input.txt') as file:
    lines = file.read().splitlines()
file.close()

# Populate tree matrix
tree_matrix = []
for i, line in enumerate(lines):
    tree_matrix.append([])
    for tree in line:
        tree_matrix[i].append(int(tree))

print(tree_matrix)

# Check each tree if it is visible from the outside
tree_count = 0

# First add all trees seen from immediate outside
tree_count += (len(tree_matrix) + len(tree_matrix[0])) * 2 - 4

for i in range(1, len(tree_matrix) - 1):
    for j in range(1, len(tree_matrix[0]) - 1):

        tree = tree_matrix[i][j]
        visible = False

        valid_path_up = True
        for k in range (0, i):
            if tree_matrix[k][j] >= tree:
                valid_path_up = False
                break

        valid_path_down = True
        for k in range(i + 1, len(tree_matrix)):
            if tree_matrix[k][j] >= tree:
                valid_path_down = False
                break

        valid_path_left = True
        for k in range(0, j):
            if tree_matrix[i][k] >= tree:
                valid_path_left = False
                break

        valid_path_right = True
        for k in range(j + 1, len(tree_matrix[0])):
            if tree_matrix[i][k] >= tree:
                valid_path_right = False

        if valid_path_right or valid_path_left or valid_path_up or valid_path_down:
            tree_count += 1

print("Part 1: " + str(tree_count))

max_scenic_score = 0

# Edges will have a 0 multiplier in one direction, so don't bother checking edges for scenic score
for i in range(1, len(tree_matrix) - 1):
    for j in range(1, len(tree_matrix[0]) - 1):

        # Can at least see one tree in each direction
        scenic_score = 1

        # How many trees can we see in each direction?
        multiplier = 1
        k = j+1
        while k < len(tree_matrix[0]) - 1 and tree_matrix[i][k] < tree_matrix[i][j]:
            multiplier += 1
            k += 1
        scenic_score *= multiplier

        multiplier = 1
        k = j-1
        while k > 0 and tree_matrix[i][k] < tree_matrix[i][j]:
            multiplier += 1
            k -= 1
        scenic_score *= multiplier

        multiplier = 1
        k = i+1
        while k < len(tree_matrix) - 1 and tree_matrix[k][j] < tree_matrix[i][j]:
            multiplier += 1
            k += 1
        scenic_score *= multiplier

        multiplier = 1
        k = i-1
        while k > 0 and tree_matrix[k][j] < tree_matrix[i][j]:
            multiplier += 1
            k -= 1
        scenic_score *= multiplier


        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print("Part 2: " + str(max_scenic_score))
