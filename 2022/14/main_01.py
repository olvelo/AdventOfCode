# Open and read file
with open('input.txt') as file:
    lines = file.read().splitlines()
file.close()

# Create dictionary to track our map, and an y_max variable
map = {}
y_max = -float('inf')

# Process input to create map of the rock
for line in lines:
    points = line.split("->")
    for i in range(len(points) - 1):
        x0, y0 = [int(c) for c in points[i].split(",")]
        x1, y1 = [int(c) for c in points[i+1].split(",")]

        y_max = max(y0, y1, y_max)

        for x in range(min(x0, x1), max(x0, x1) + 1):
            for y in range(min(y0, y1), max(y0, y1) + 1):
                map[(x, y)] = '#'

# Start to let sand fall
endless_fall = False
while not endless_fall:
    sand = (500, 0)
    can_move = True
    while can_move and not endless_fall:
        if (sand[0], sand[1] + 1) in map.keys():
            if (sand[0] - 1, sand[1] + 1) in map.keys():
                if (sand[0] + 1, sand[1] + 1) in map.keys():
                    can_move = False
                    map[(sand[0], sand[1])] = 'o'
                else:
                    sand = (sand[0] + 1, sand[1] + 1)
            else:
                sand = (sand[0] - 1, sand[1] + 1)
        else:
            sand = sand[0], sand[1] + 1
        if sand[1] > y_max:
            endless_fall = True

units = 0
for key in map:
    if map[key] == 'o':
        units += 1

print("Task 1: " + str(units))
