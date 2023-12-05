def process_input(lines):
    seeds = [int(number) for number in lines.pop(0).strip().split(" ")[1::]]

    maps = []

    for i in range(7):

        lines.pop(0)
        lines.pop(0)

        map = {}
        while len(lines) > 0 and lines[0] != '\n':
            dest_start, source_start, length = [int(number) for number in lines.pop(0).strip().split(" ")]
            map[(source_start, source_start + length)] = dest_start

        maps.append(map)

    return seeds, maps


if __name__ == "__main__":

    # Open and read file
    with open('input.txt') as f:
        lines = f.readlines()

    seeds, maps = process_input(lines)

    location_numbers = []
    for seed in seeds:
        this = seed
        for map in maps:
            in_map = False
            for (source_start, source_end), dest_start in map.items():
                if this >= source_start and this <= source_end:
                    in_map = True
                    this = dest_start + (this - source_start)
                    break
            if not in_map:
                this = this
        location_numbers.append(this)

    print(min(location_numbers))

    pass






