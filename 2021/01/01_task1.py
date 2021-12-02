# Open and read file
with open('input1.txt') as f:
    lines = f.readlines()

# Counter for depth-increases
c = 0

# Pop first element
depth_prev = int(lines.pop(0))

# Iterate through depths and count depth increases
for line in lines:
    depth_current = int(line)
    if depth_current > depth_prev:
        c += 1
    depth_prev = depth_current

# Print result
print(c)