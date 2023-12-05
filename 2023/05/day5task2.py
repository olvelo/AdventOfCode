import time


def process_input(lines):
    seeds = [int(number) for number in lines.pop(0).strip().split(" ")[1::]]

    seed_ranges = []
    while len(seeds) > 0:
        start, length = seeds.pop(0), seeds.pop(0)
        seed_ranges.append((start, start + length - 1))

    maps = []

    for i in range(7):

        lines.pop(0)
        lines.pop(0)

        map = {}
        while len(lines) > 0 and lines[0] != '\n':
            dest_start, source_start, length = [int(number) for number in lines.pop(0).strip().split(" ")]
            map[(source_start, source_start + length)] = dest_start

        maps.append(map)

    return seed_ranges, maps


if __name__ == "__main__":

    # Open and read file
    with open('input.txt') as f:
        lines = f.readlines()

    seed_ranges, maps = process_input(lines)

    lowest_location_number = 9999999999

    for seed_range in seed_ranges:

        old_ranges = [seed_range]

        for this_map in maps:

            new_ranges = []

            while len(old_ranges) > 0:

                this_range = old_ranges.pop(0)

                found_overlap = False

                for (source_start, source_end), dest_start in this_map.items():

                    overlapping_range = (max(this_range[0], source_start), min(this_range[1], source_end))
                    if overlapping_range[1] > overlapping_range[0]:
                        found_overlap = True

                        new_range = (dest_start + overlapping_range[0] - source_start, dest_start + overlapping_range[1] - source_start)
                        new_ranges.append(new_range)

                        # Need to check if any non-overlapping regions to break up into
                        left = (this_range[0], overlapping_range[0])
                        right = (this_range[1], overlapping_range[1])

                        if left[1] > left[0]:
                            old_ranges.append(left)
                        if right[1] > right[0]:
                            old_ranges.append(right)

                if not found_overlap:
                    new_ranges.append(this_range)

            old_ranges = new_ranges

        for range in new_ranges:
            if range[0] < lowest_location_number:
                lowest_location_number = range[0]
        print(lowest_location_number)
