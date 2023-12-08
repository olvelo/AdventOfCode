if __name__ == "__main__":

    # Open and read file
    with open('input.txt') as f:
        lines = f.readlines()

    instructions = []
    line = lines.pop(0).strip()
    while len(line.strip()) > 0:
        for char in line:
            instructions.append(char)
        line = lines.pop(0)

    mymap = {}
    for line in lines:
        start, ends = line.strip().split("=")
        start = start[:3:]
        left, right = ends[2:5], ends[7:10]
        mymap[start] = (left, right)

    this = 'AAA'
    reached = False
    steps = 0
    while not reached:
        for instruction in instructions:
            if instruction == 'L':
                next = mymap[this][0]
            else:
                next = mymap[this][1]

            this = next
            steps += 1
            if this == 'ZZZ':
                reached = True

    print(steps)


