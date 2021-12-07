# Open and read file
input = open('07_input.txt', 'r')
positions = [int(x) for x in input.readline().split(',')]
input.close()

# Find median
positions.sort()
median = positions[round(len(positions)/2)]

# Find average
average = sum(positions) // len(positions)

# Calculate fuel cost for one fuel per move
fuel_single, fuel_increasing = 0, 0
for position in positions:
    fuel_single += abs(position - median)
    fuel_increasing += sum([i for i in range(abs(position - average) + 1)])

print('Fuel cost with one fuel per move = {}'.format(fuel_single))
print('Fuel cost with increasing fuel per move = {}'.format(fuel_increasing))
