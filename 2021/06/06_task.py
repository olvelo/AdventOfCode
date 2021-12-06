# Open and read file
input = open('06_input.txt', 'r')
lanternfish = [int(x) for x in input.readline().split(',')]
input.close()

# Bruteforce method below
"""
days = 256
for i in range(days):
    newfish = 0
    for j, fish in enumerate(lanternfish):
        if fish > 0:
            lanternfish[j] -= 1
        else:
            lanternfish[j] = 6
            newfish += 1
    lanternfish.extend([8] * newfish)
    print('Day {}: {} lanternfish'.format(i, len(lanternfish)))

print('Lanternfish after {} days: {}'.format(days, len(lanternfish)))
"""

# Method with one list to track number of days until birth instead
days = 256
fishdays = [0] * 9

# Initialize from input
for fish in lanternfish:
    fishdays[fish] += 1

# For each day
for i in range(days):
    # Count number of new fish created
    newfish = fishdays[0]
    # Decrement days until birth for each fish
    for j, fishday in enumerate(fishdays[:-1]):
        fishdays[j] = fishdays[j+1]
    # Add new fish with 8 days until birth
    fishdays[8] = newfish
    # Move birthing fishes back to 6 days again
    fishdays[6] += newfish

print('Number of lanternfish after {} days: {}'.format(days, sum(fishdays)))
