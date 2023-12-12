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

        final_springs = []
        for spring in springs:
            final_springs.append(spring)
        for i in range(4):
            final_springs.append('?')
            for spring in springs:
                final_springs.append(spring)

        final_group_sizes = []
        for i in range(5):
            for group_size in group_sizes:
                final_group_sizes.append(group_size)

        spring_rows.append(final_springs)
        row_group_sizes.append(final_group_sizes)

    pass
