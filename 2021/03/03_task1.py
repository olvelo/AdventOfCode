# These we want to calculate
gamma_rate, epsilon_rate = 0, 0

# Open and read file
input = open('03_input.txt', 'r')

# Get first line to see length
firstline = input.readline().strip()

# Create array to store values and number of lines
counter_arr = [0] * (len(firstline))

# Update with first line
for i, char in enumerate(firstline):
    counter_arr[i] += int(char)

# Iterate through file and count in similar manner for the rest of the lines
line_counter = 1
for line in input:
    for i, char in enumerate(line.strip()):
        counter_arr[i] += int(char)
    line_counter += 1

# Build up gamma and epsilon rates based on what has been counted
for i, counter in enumerate(counter_arr):
    most_common = round(counter / line_counter)
    gamma_rate += most_common << (len(counter_arr) - i - 1)
    epsilon_rate += (1 - most_common) << (len(counter_arr) - i  - 1)

# Calculate product
print(gamma_rate * epsilon_rate)

input.close()
