# Starting coordinates
x, y = 0, 0

# Open and read file
input = open('02_input.txt', 'r')

# Iterate through lines
for line in input:
    direction, amount = line.split()
    if direction == "forward":
        x += int(amount)
    elif direction == "up":
        y -= int(amount)
    elif direction == "down":
        y += int(amount)
    else:
        raise ValueError("Wrong string format")

input.close()

print(x * y)
