# Open and read file
with open('input.txt') as file:
    lines = file.read().splitlines()
file.close()

# Create dict of valves, and of non-zero valves
valve_dict = {}
non_zero_valve_list = []
for line in lines:
    linesplit = line.split(";")
    valvename, flowrate = linesplit[0].split(" ")[1], linesplit[0].split(" ")[4].split("=")[1]
    valves_connected = linesplit[1].split(" ")
    valves_list = []
    for i in range(5, len(valves_connected)):
        valves_list.append(valves_connected[i].strip(","))

    valve_dict[valvename] = (int(flowrate), valves_list)
    if int(flowrate) > 0:
        non_zero_valve_list.append(valvename)

# Create map of distance from all non-zero caves to all other non-zero caves, using BFS
non_zero_valve_distance_map = {}
for key_start in valve_dict:
    if valve_dict[key_start][0] > 0 or key_start == 'AA':

        for key_end in valve_dict:
            if (valve_dict[key_end][0] > 0 or key_end == 'AA') and key_end != key_start:

                # Find shortes distance to all other non-zero valves, with a BFS
                previous = (key_start, 0)
                visited = set()
                queue = [(key_start, 0)]
                visited.add(key_start)

                while len(queue) > 0:

                    node, distance = queue.pop(0)
                    if node == key_end:
                        non_zero_valve_distance_map[str(key_start) + str("-") + str(key_end)] = distance
                        pass

                    for neighbour in valve_dict[node][1]:
                        if neighbour not in visited:
                            queue.append((neighbour, distance + 1))
                            visited.add(neighbour)

# Create stack of states, and map list of visited to a pressure
stack = [('AA', 26, 0, 0, non_zero_valve_list, [])]
path_pressure = {}

while len(stack) > 0:

    # Get new new state
    stack_item = stack.pop(0)

    # For all possible moves
    for new_valve in stack_item[4]:

        # Get distance of move
        try:
            valve_distance = non_zero_valve_distance_map[stack_item[0] + str("-") + new_valve]
        except:
            pass

        # Check if time runs out before we reach and open it
        if stack_item[1] - valve_distance - 1 < 1:
            pass
        else:
            # If not, add new state to the stack
            new_unopened_valves = []
            for valve in stack_item[4]:
                if valve != new_valve:
                    new_unopened_valves.append(valve)

            visited_list = []
            for element in stack_item[5]:
                visited_list.append(element)
            visited_list.append(stack_item[0])

            stack.append((new_valve,
                          stack_item[1] - valve_distance - 1,
                          stack_item[2] + stack_item[3] * (valve_distance + 1),
                          stack_item[3] + valve_dict[new_valve][0],
                          new_unopened_valves,
                          visited_list))

    # Also evaluate just standing here
    visited_list = []
    for element in stack_item[5]:
        visited_list.append(element)
    visited_list.append(stack_item[0])
    path_pressure[str(visited_list)] = stack_item[2] + stack_item[3] * stack_item[1]

# Find two paths resulting in highest pressure
sorted_path_pressure_keys = sorted(path_pressure, key=path_pressure.get, reverse=True)
max_pressure = 0
for path_me in sorted_path_pressure_keys:
    for path_elephant in sorted_path_pressure_keys:
        if path_pressure[path_me] + path_pressure[path_elephant] > max_pressure:
            valid = True
            for point in eval(path_me):
                if point in eval(path_elephant) and point != 'AA':
                    valid = False
                    break
            if valid:
                max_pressure = path_pressure[path_me] + path_pressure[path_elephant]
        else:
            break

print("Task 2: Max pressure is " + str(max_pressure))
