# Open and read file
input = open('05_input.txt', 'r')

# Create dictionary to store which points have been covered by the vent lines
covered_points_dict = {}

# For each line
for line in input:

    # Get coordinates
    vent = [coordinate for coordinate in line.strip().split(' -> ')]
    x0, y0 = (int(number) for number in vent[0].split(','))
    x1, y1 = (int(number) for number in vent[1].split(','))

    # Check if horizontal, vertical or diagonal
    if y0 == y1:
        # Horizontal, update covered points by looping x
        for x in range(min(x0, x1), max(x0, x1) + 1):
            if (x, y0) in covered_points_dict:
                covered_points_dict[(x, y0)] += 1
            else:
                covered_points_dict[(x, y0)] = 1
    elif x0 == x1:
        # Vertical, update covered points by looping y
        for y in range(min(y0, y1), max(y0, y1) + 1):
            if (x0, y) in covered_points_dict:
                covered_points_dict[(x0, y)] += 1
            else:
                covered_points_dict[(x0, y)] = 1
    else:
        # Diagonal lines
        x_shift = -1 if x1 < x0 else 1
        y_shift = -1 if y1 < y0 else 1
        xvals = [x for x in range(x0, x1 + x_shift, x_shift)]
        yvals = [y for y in range(y0, y1 + y_shift, y_shift)]
        for i in range(len(xvals)):
            x, y = xvals[i], yvals[i]
            if (x, y) in covered_points_dict:
                covered_points_dict[(x, y)] += 1
            else:
                covered_points_dict[(x, y)] = 1

# Loop through dictionary and find points with more than one line overlapping
sum = 0
for key in covered_points_dict:
    if covered_points_dict[key] > 1:
        sum += 1

print(sum)

input.close()