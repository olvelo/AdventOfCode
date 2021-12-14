# Open and read file, getting polymer template and insertion rules
input = open('14_input.txt', 'r')
polymer_template = input.readline().strip()
insertion_rules = {}
for line in input:
    if '->' in line:
        pair, insertion = line.strip().split('->')
        insertion_rules[pair.strip()] = insertion.strip()
input.close()

# Initialize dict counting all polymer pairs
pair_count = {}
for i in range(len(polymer_template) - 1):
    pair = polymer_template[i] + polymer_template[i+1]
    if pair in pair_count.keys():
        pair_count[pair] += 1
    else:
        pair_count[pair] = 1

# Calculate number of each pair for a certain number of steps
steps = 40
for i in range(steps):

    # Create a dict for new pairs based on old pairs
    pair_count_new = {}

    # Figure out new pairs based on those we already have
    for pair in pair_count.keys():
        # Get insertion from insertion rules and generate new pairs
        insertion = insertion_rules[pair[0] + pair[1]]
        newpairs = (pair[0] + insertion, insertion + pair[1])
        for newpair in newpairs:
            if newpair in pair_count_new.keys():
                pair_count_new[newpair] += pair_count[pair]
            else:
                pair_count_new[newpair] = pair_count[pair]

    # Need to update the pairs to use as old pairs for next step
    pair_count = {}
    for pair in pair_count_new.keys():
        if pair in pair_count.keys():
            pair_count[pair] += pair_count_new[pair]
        else:
            pair_count[pair] = pair_count_new[pair]

# Sum up letters based on the pairs
letter_count = {}
for pair in pair_count:
    if pair[0] == pair[1]:
        # Equal letters in pair, add to sum
        if pair[0] in letter_count.keys():
            letter_count[pair[0]] += pair_count[pair]
        else:
            letter_count[pair[0]] = pair_count[pair]

    else:
        # Else, add half of it to avoid counting twice
        for letter in pair:
            if letter in letter_count.keys():
                letter_count[letter] += pair_count[pair] / 2
            else:
                letter_count[letter] = pair_count[pair] / 2

# Round numbers
for letter in letter_count.keys():
    letter_count[letter] = int(letter_count[letter] + 0.5)

print(f'Most common minus least common after {steps} steps: {max(letter_count.values()) - min(letter_count.values())}')
