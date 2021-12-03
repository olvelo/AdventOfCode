# Returns most common number in given array of arrays, at given index
def most_common(arrayofarrays, index):
    counter = 0
    for i, array in enumerate(arrayofarrays):
        counter += array[index]
    avg = counter / (i)
    return round(avg)

# These we want to calculate
oxygen, scrubber = 0, 0

# Open and read file
input = open('03_input.txt', 'r')

# Convert to array of arrays
inputarr = []
for line in input:
    line.strip()
    temparr = []
    for char in line.strip():
        temparr.append(int(char))
    inputarr.append(temparr)

# Close file
input.close()


# Sort in oxygen and scrubber candidates
oxygen_candidates, scrubber_candidates = [], []
common = most_common(inputarr, 0)
for input in inputarr:
    if input[0] == common:
        oxygen_candidates.append(input)
    else:
        scrubber_candidates.append(input)

# Apply search filter for rest of indexes
for i in range(1, len(inputarr[0])):
    if len(oxygen_candidates) > 1:
        common = most_common(oxygen_candidates, i)
        new_oxygen_candidates = []
        for candidate in oxygen_candidates:
            if candidate[i] == common:
                new_oxygen_candidates.append(candidate)
        oxygen_candidates = new_oxygen_candidates
    if len(scrubber_candidates) > 1:
        common = most_common(scrubber_candidates, i)
        new_scrubber_candidates = []
        for candidate in scrubber_candidates:
            if candidate[i] != common:
                new_scrubber_candidates.append(candidate)
        scrubber_candidates = new_scrubber_candidates

# Convert to numbers and calculate product
for i in range(len(oxygen_candidates[0])):
    oxygen += oxygen_candidates[0][i] << (len(oxygen_candidates[0]) - i - 1)
    scrubber += scrubber_candidates[0][i] << (len(oxygen_candidates[0]) - i - 1)

print(oxygen * scrubber)
