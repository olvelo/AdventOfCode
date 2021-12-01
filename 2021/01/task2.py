# Open and read file
with open('input1.txt') as f:
    lines = f.readlines()

# Convert to list of ints
depths = [int(line) for line in lines]

# Counter for depth-increases
c = 0

# Get first window sum
window_sum_prev = sum(depths[0:3])

# Iterate through rest and compare, updating sliding windows. Could be optimized more
for i in range(3, len(lines)):
    window_sum = sum(int(line) for line in lines[i-2:i+1])
    if window_sum > window_sum_prev:
        c += 1
    window_sum_prev = window_sum

print(c)
