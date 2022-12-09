# Open and read file
with open('input.txt') as file:
    lines = file.read().splitlines()
file.close()

# Move point according to instruction
def move_head(head, direction):
    if direction == "R":
        return (head[0] + 1, head[1])
    elif direction == "L":
        return (head[0] - 1, head[1])
    elif direction == "U":
        return (head[0], head[1] + 1)
    elif direction == "D":
        return (head[0], head[1] - 1)

# Move tail according to head
def follow_head(head, tail):
    # Check if touching
    if (head[0]-1 <= tail[0] <= head[0]+1) and (head[1]-1 <= tail[1] <= head[1]+1):
        return tail
    # Check if two points above, below, right or left
    elif (head[0] == tail[0] + 2 or head[0] == tail[0] - 2) and head[1] == tail[1]:
        return (int(tail[0] + (head[0] - tail[0]) / 2), tail[1])
    elif head[0] == tail[0] and (head[1] == tail[1] + 2 or head[1] == tail[1] - 2):
        return (tail[0], int(tail[1] + (head[1] - tail[1]) / 2))
    # Check if not in same row or column, then move diagonally
    elif head[0] != tail[0] and head[1] != tail[1]:
        x = tail[0] + 1 if tail[0] < head[0] else tail[0] - 1
        y = tail[1] + 1 if tail[1] < head[1] else tail[1] - 1
        return (x, y)
    else:
        print("Something gone wrong...")

# Instantiate rope
rope_length = 10
rope = [(0, 0) for i in range(rope_length)]

# Set to track visited positions
visited_set = set()

# Follow instructions
for line in lines:
    direction, steps = line.split(" ")
    for step in range(int(steps)):
        # First move head
        rope[0] = move_head(rope[0], direction)

        # Then move rope
        for i in range(1, rope_length):
            rope[i] = follow_head(rope[i-1], rope[i])

        visited_set.add(rope[i])

print("Number of visited points by tail: " + str(len(visited_set)))
