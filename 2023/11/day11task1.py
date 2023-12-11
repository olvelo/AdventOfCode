if __name__ == "__main__":

    # Open and read file
    with open('input.txt') as f:
        lines = f.readlines()

    # Map out galaxies
    galaxies = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char == '#':
                galaxies.append((x, y))
            pass

    # Find empty rows and columns
    galaxies_x_set = set(galaxy[0] for galaxy in galaxies)
    galaxies_y_set = set(galaxy[1] for galaxy in galaxies)
    empty_x = [i for i in range(x) if i not in galaxies_x_set]
    empty_y = [i for i in range(y) if i not in galaxies_y_set]

    # Find distance between all pairs
    pair_distances = {}
    for this_galaxy in galaxies:
        for other_galaxy in galaxies:
            if ((this_galaxy, other_galaxy) not in pair_distances.keys() and
                    (other_galaxy, this_galaxy) not in pair_distances.keys() and this_galaxy != other_galaxy):
                # Calculate distance and add steps for expanding rows/columns
                distance = abs(this_galaxy[0] - other_galaxy[0]) + abs(this_galaxy[1] - other_galaxy[1])
                for x in empty_x:
                    if this_galaxy[0] < x < other_galaxy[0] or other_galaxy[0] < x < this_galaxy[0]:
                        distance += 1
                for y in empty_y:
                    if this_galaxy[1] < y < other_galaxy[1] or other_galaxy[1] < y < this_galaxy[1]:
                        distance += 1

                pair_distances[(this_galaxy, other_galaxy)] = distance

    # Sum all of them
    print(sum(pair_distances.values()))
