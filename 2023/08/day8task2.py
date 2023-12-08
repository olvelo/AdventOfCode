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

    # Figure out starting nodes
    starting_nodes = []
    for key in mymap.keys():
        if 'A' in key:
            starting_nodes.append(key)

    # For all starting nodes, find when they first reach Z
    startnode_step_map = {}
    for starting_node in starting_nodes:
        this = starting_node
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
                if 'Z' in this:
                    reached = True
                    startnode_step_map[starting_node] = steps

    # Find least common multiple
    import math
    print(math.lcm(*startnode_step_map.values()))


