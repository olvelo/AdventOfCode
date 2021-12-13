# Open and read file, split into list of dots and fold instructions
input = open('13_input.txt', 'r')
dots, folds = [], []
for line in input:
    if ',' in line:
        (x, y) = line.strip().split(',')
        dots.append((int(x), int(y)))
    elif 'fold' in line:
        text, number = line.strip().split('=')
        folds.append(text[-1] + '=' + number)
input.close()

print_dot_number = True
# Do folding instructions
for fold in folds:
    # Variable to know if we fold along x or y. If false, fold along x
    fold_axis, fold_number = fold.split('=')
    fold_number = int(fold_number)

    # If fold along y axis
    if fold_axis == 'y':

        # First fold dots over
        for dot in [dot for dot in dots if dot[1] > fold_number]:
            folded_dot = (dot[0], fold_number - (dot[1] - fold_number))
            dots.append(folded_dot)

        # Then remove dots that are folded
        dots = [dot for dot in dots if dot[1] < fold_number]

        # Convert to set and list again to only keep unique dots, removing overlapping
        dots = list(set(dots))

    # Same procedure for folds along x axis
    elif fold_axis == 'x':

        # First fold dots over
        for dot in [dot for dot in dots if dot[0] > fold_number]:
            folded_dot = (fold_number - (dot[0] - fold_number), dot[1])
            dots.append(folded_dot)

        # Then remove dots that are folded
        dots = [dot for dot in dots if dot[0] < fold_number]

        # Convert to set and list again to only keep unique dots, removing overlapping
        dots = list(set(dots))

    # Print number of dots only after first instruction
    if print_dot_number:
        print(f'Dots after first fold instruction = {len(dots)} \n')
        print_dot_number = False

# Decipher the code, first get max to create lists
max_x, max_y = 0, 0
for dot in dots:
    max_x = dot[0] if dot[0] > max_x else max_x
    max_y = dot[1] if dot[1] > max_y else max_y

print("Code after folding instructions complete:")

# Print the code so it can be read
for i in range(max_y + 1):
    str = ''
    for j in range(max_x + 1):
        str += '0 ' if (j, i) in dots else '. '
    print(str)
