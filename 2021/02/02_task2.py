# Starting coordinates
x, y, aim = 0, 0, 0

# Open and read file
input = open('02_input.txt', 'r')

# Iterate through lines
for line in input:
    direction, amount = line.split()
    if direction == "forward":
        x += int(amount)
        y += aim * int(amount)
    elif direction == "up":
        aim -= int(amount)
    elif direction == "down":
        aim += int(amount)
    else:
        raise ValueError("Wrong string format")

input.close()

print(x * y)
