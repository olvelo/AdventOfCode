# Open and read file
with open('input.txt') as file:
    lines = file.read().splitlines()
file.close()

x = 1
cycles = [20 + 40 * i for i in range(6)]
cycle_counter = 0
signal_strength = 0

for line in lines:
    operation = line.split(" ")
    if operation[0] == "noop":
        if cycle_counter + 1 >= cycles[0]:
            signal_strength += cycles.pop(0) * x
        cycle_counter += 1
    elif operation[0] == "addx":
        if cycle_counter + 2 >= cycles[0]:
            signal_strength += cycles.pop(0) * x
        cycle_counter += 2
        x = x + int(operation[1])

    if len(cycles) < 1:
        break

print("Task 1: " + str(signal_strength))

x = 1
cycle_counter = 0
lit_pixel_indexes = []

for line in lines:
    if cycle_counter % 40 in [x-1, x, x+1]:
        lit_pixel_indexes.append(cycle_counter)

    operation = line.split(" ")
    if operation[0] == "noop":
        cycle_counter += 1
    elif operation[0] == "addx":
        cycle_counter += 1
        if cycle_counter % 40 in [x - 1, x, x + 1]:
            lit_pixel_indexes.append(cycle_counter)
        cycle_counter += 1
        x = x + int(operation[1])

print("Task 2:")

for i in range(6):
    output = ""
    for j in range(40):
        if (i*40 + j) in lit_pixel_indexes:
            output += '* '
        else:
            output += '  '
    print(output)
