# Open and read file
with open('input.txt') as file:
    lines = file.read().splitlines()
file.close()

folder_sizes = {}

path_stack = []
for line in lines:
    words = line.split(" ")
    if words[0] == "$" and words[1] == "cd":
        if words[2] == "..":
            path_stack.pop()
        else:
            path_stack.append(words[2])
    elif words[0] != "$" and words[0] != "dir":
        size = int(words[0])

        for i in range(len(path_stack)):

            if '/'.join(path_stack[:i+1]) in folder_sizes.keys():
                folder_sizes['/'.join(path_stack[:i+1])] += size
            else:
                folder_sizes['/'.join(path_stack[:i+1])] = size

sum = 0
for key in folder_sizes:
    if folder_sizes[key] < 100000:
        sum += folder_sizes[key]
print(sum)

space_total = 70000000
unused_needed = 30000000
space_available_now = space_total - folder_sizes['/']
space_needed_to_delete = unused_needed - space_available_now

# Find smallest directory to delete
to_delete = folder_sizes['/']
for key in folder_sizes:
    if space_needed_to_delete < folder_sizes[key] and to_delete > folder_sizes[key]:
        to_delete = folder_sizes[key]

print(to_delete)

