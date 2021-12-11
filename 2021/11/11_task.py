def flash(octopi, x, y, flashes=0):
    """
    Recursive function to count octopi flashing

    Args:
        octopi: Map of octopi
        x: X coordinate
        y: Y coordinate
        flashes: Number of flashes
    """
    # Set energy level to 0 and append to flashmap
    flashes += 1
    octopi[x][y] = 0

    # Increase energy level of adjacent octopi
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            # Check that valid coordinate
            if 0 <= i < len(octopi) and 0 <= j < len(octopi[0]):
                # Increase energy level if it is above 0 and flash if it goes above 9
                if octopi[i][j] > 0:
                    octopi[i][j] += 1
                if octopi[i][j] > 9:
                    flashes += flash(octopi, i, j)
    return flashes

# Open and read file to array
input = open('11_input.txt', 'r')
octopi = []
for line in input:
    octopi.append([int(char) for char in line.strip()])
input.close()

# Need to know total number of octopi
total_octopi = len(octopi)*len(octopi[0])

# Variables to store if all octopi are in sync, number of steps and number of flashes
sync, step, flashes = False, 0, 0

while not sync:
    # Increase step counter and initialize new flashes counter
    step += 1
    newflashes = 0

    # Increase energy of all octopi
    octopi = [[x + 1 for x in column] for column in octopi]

    # Flash all octopi with high enough energy levels
    for j in range(len(octopi)):
        for k in range(len(octopi[0])):
            if octopi[j][k] > 9:
                newflashes += flash(octopi, j, k)

    # Print total flashes after 100 steps
    flashes += newflashes
    if step == 100:
        print(f'Flashes after {step} iterations: {flashes}')

    # If all octopi are flashing, they are in sync
    if newflashes == total_octopi:
        sync = True

print(f'Steps before all octopi flashing in sync: {step}')
