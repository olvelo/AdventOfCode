def explore_once(waypoint, alternatives, currentpath, paths):
    """
    Recursive function to explore cave
    Args:
        waypoint: The new waypoint
        alternatives: Alternatives for all waypoints
        currentpath: Current path being explored, string as it must be immutable
        paths: Paths found so far
    """
    # Append new waypoint to current path and get alternatives from here
    currentpath += (',' + waypoint) if currentpath != '' else waypoint
    alternatives_here = alternatives[waypoint]

    for alternative in alternatives_here:
        if alternative.isupper():
            # Can explore all uppercase caves as many times we want
            explore_once(alternative, alternatives, currentpath, paths)
        elif alternative == 'end':
            # If end reached, we have a full path
            paths.append(currentpath + ',' + alternative)
        elif alternative not in currentpath:
            # Make sure lowercase caves are only visited once
            explore_once(alternative, alternatives, currentpath, paths)

def explore_twice(waypoint, alternatives, currentpath, paths):
    """
    Recursive function to explore cave, can visit a single small cave twice
    Args:
        waypoint: The new waypoint
        alternatives: Alternatives for all waypoints
        currentpath: Current path being explored, string as it must be immutable
        paths: Paths found so far
    """
    # Append new waypoint to current path and get alternatives from here
    currentpath += (',' + waypoint) if currentpath != '' else waypoint
    alternatives_here = alternatives[waypoint]

    for alternative in alternatives_here:
        if alternative.isupper():
            # Can explore all uppercase caves as many times we want
            explore_twice(alternative, alternatives, currentpath, paths)
        elif alternative == 'end':
            # If end reached, we have a full path
            paths.append(currentpath + ',' + alternative)
        elif alternative != 'start':
            # Create list of all visited small caves so far
            small_visited = []
            for cave in currentpath.split(','):
                if not cave.isupper():
                    small_visited.append(cave)

            # Convert to a set to have only unique small caves visited
            small_visited_set = set(small_visited)

            # If lengths are equal, or if this small cave has not been explored yet, we can proceed
            if len(small_visited_set) == len(small_visited) or alternative not in small_visited:
                explore_twice(alternative, alternatives, currentpath, paths)


# Open and read file to list of tuples
input = open('12_input.txt', 'r')
connections = []
for line in input:
    (a, b) = line.strip().split('-')
    connections.append((a, b))
input.close()

# Create dictionary of alternatives per cave
alternatives = {}
for connection in connections:
    if connection[0] not in alternatives:
        alternatives[connection[0]] = [connection[1]]
    elif connection[1] not in alternatives[connection[0]]:
        alternatives[connection[0]].append(connection[1])
    if connection[1] not in alternatives:
        alternatives[connection[1]] = [connection[0]]
    elif connection[0] not in alternatives[connection[1]]:
        alternatives[connection[1]].append(connection[0])

paths_once = []
explore_once('start', alternatives, '', paths_once)

print(f'Number of paths visiting small caves max once: {len(paths_once)}')

paths_twice = []
explore_twice('start', alternatives, '', paths_twice)

print(f'Number of paths visiting one small cave max twice: {len(paths_twice)}')
