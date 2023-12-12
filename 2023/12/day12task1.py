import itertools
import time

if __name__ == "__main__":

    # Open and read file
    with open('input.txt') as f:
        lines = f.readlines()

    spring_rows, row_group_sizes = [], []
    for line in lines:
        springs, group = line.strip().split(" ")
        springs = [char for char in springs]
        group_sizes = [int(char) for char in group.split(",")]
        spring_rows.append(springs)
        row_group_sizes.append(group_sizes)

    # Store how many valid combinations we have
    counts = 0

    # For each row in the input
    for row_index in range(len(spring_rows)):

        # Get the springs and groups for this row
        springs = spring_rows[row_index]
        groups = row_group_sizes[row_index]

        # Generate all permutations of indexes to start the groups at
        group_start_combinations = itertools.combinations([x for x in range(len(springs))], len(groups))

        # For each permutation
        for group_starts in group_start_combinations:

            # Groups cannot start right after one another
            skip = False
            for i in range(len(group_starts) - 1):
                if group_starts[i+1] - group_starts[i] < 2:
                    skip = True
                    break
            if skip:
                continue

            # Check that the groups don't overlap
            for i in range(len(groups) - 1):
                if groups[i] + group_starts[i] >= group_starts[i+1]:
                    skip = True
                    break
            if skip:
                continue

            # And that the last one does not go beyond the end
            if groups[len(groups) - 1] + group_starts[len(groups) - 1] > len(springs):
                continue

            # Create spring candidate and check it against the springs we see
            springs_candidate = ['.' for spring in springs]
            for i in range(len(group_starts)):
                springs_candidate[group_starts[i]:group_starts[i] + groups[i]] = '#' * groups[i]

            for i in range(len(springs)):
                if springs[i] == '.' and springs_candidate[i] == '#':
                    skip = True
                    break
                elif springs[i] == '#' and springs_candidate[i] == '.':
                    skip = True
                    break
            if skip:
                continue

            counts += 1

    print(counts)
