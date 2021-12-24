import heapq

def possiblestates(state, correct_room_dict, energy_per_move_dict):
    """
    Get all possible new states based on current state
    Args:
        state: The current state

    Returns: A list of all possible states, with the cost of moving to this state
    """
    # List of possible states
    possiblestates = []

    # Get hallway and rooms
    hallway, rooms = state[0], state[1]

    # Check moves for each char in each room, directly to correct room
    for roomnumber, room in enumerate(rooms):
        for roomposition, char in enumerate(room):
            if char != '.':

                # Make sure we don't move chars when they are blocked
                stop = False
                for i in range(roomposition):
                    if room[i] != '.':
                        stop = True
                if stop: continue

                # Get the correct room for this char, and the index in the hallway corresponding to that room
                target_room = rooms[correct_room_dict[char]]

                # Make sure we don't move into the same room as we are in
                if correct_room_dict[char] == roomnumber:
                    continue

                target_hallway_index = correct_room_dict[char] * 2 + 2
                room_hallway_index = roomnumber * 2 + 2

                # Need to check if valid path in the hallway to this room
                validpath = True
                moves = 0
                for path_index in range(min(target_hallway_index, room_hallway_index),
                                        max(target_hallway_index, room_hallway_index) + 1):
                    moves += 1
                    if hallway[path_index] != '.':
                        validpath = False
                        break

                # Can only move inside the room if it is available space and not any other chars in that room
                if target_room.count(char) + target_room.count('.') == 4 and validpath:

                    # Create new state. Move char into target room and find new state plus cost
                    updated_oldroom = []
                    for i in range(4):
                        if roomposition == i:
                            updated_oldroom.append('.')
                        else:
                            updated_oldroom.append(room[i])
                    updated_oldroom = tuple(updated_oldroom)

                    # Remembering to also add the cost of moving out of the room we came from
                    moves += roomposition + 1

                    # Update the target room and add moves
                    target_room_position = 0
                    for i in range(4):
                        if target_room[i] == '.':
                            target_room_position = i
                    moves += target_room_position + 1

                    updated_targetroom = []
                    for i in range(4):
                        if i == target_room_position:
                            updated_targetroom.append(char)
                        else:
                            updated_targetroom.append(target_room[i])
                    updated_targetroom = tuple(updated_targetroom)

                    updatedrooms = list(rooms)
                    updatedrooms[roomnumber] = updated_oldroom
                    updatedrooms[correct_room_dict[char]] = updated_targetroom
                    updatedrooms = tuple(updatedrooms)

                    possiblestates.append((hallway, updatedrooms, moves * energy_per_move_dict[char]))

    # If noe such moves found, search for moves from hallway to correct room
    if len(possiblestates) == 0:
        # Check moves for each char in the hallway
        for position, char in enumerate(hallway):
            if char != '.':

                # Get the correct room for this char, and the index in the hallway corresponding to that room
                target_room = rooms[correct_room_dict[char]]
                target_hallway_index = correct_room_dict[char] * 2 + 2

                # Can only move inside the room if it is available space and not any other chars in that room
                if target_room.count(char) + target_room.count('.') == 4:

                    # Need to check if valid path in the hallway to this room
                    validpath = True
                    moves = 0

                    # Figure out if we are moving right or left
                    end = target_hallway_index
                    start = position
                    firstmove = -1
                    if end > start:
                        firstmove = 1

                    for path_index in range(min(target_hallway_index, position + firstmove), max(target_hallway_index, position + firstmove) + 1):
                        moves += 1
                        if hallway[path_index] != '.':
                            validpath = False
                            break

                    if validpath:
                        # Create a new state. Move char into target room, and find new state plus cost
                        updatedhallway = list(hallway)
                        updatedhallway[position] = '.'

                        # Update the target room and add moves
                        target_room_position = 0
                        for i in range(4):
                            if target_room[i] == '.':
                                target_room_position = i
                        moves += target_room_position + 1

                        updatedroom = []
                        for i in range(4):
                            if i == target_room_position:
                                updatedroom.append(char)
                            else:
                                updatedroom.append(target_room[i])
                        updatedroom = tuple(updatedroom)

                        updatedrooms = list(rooms)
                        updatedrooms[correct_room_dict[char]] = updatedroom
                        updatedrooms = tuple(updatedrooms)

                        possiblestates.append((''.join(updatedhallway), updatedrooms, moves * energy_per_move_dict[char]))

    # One option left, moving char from room into the hallway
    if len(possiblestates) >= 0:
        for roomnumber, room in enumerate(rooms):
            for roomposition, char in enumerate(room):
                if char != '.':

                    # Make sure we don't move chars when they are blocked
                    stop = False
                    for i in range(roomposition):
                        if room[i] != '.':
                            stop = True
                    if stop: continue

                    # Also make sure we don't move out chars that have been placed correctly
                    if roomnumber == correct_room_dict[char] and (room.count(char) + room.count('.') == 4):
                        continue

                    # Get hallway index of the current room
                    room_hallway_index = roomnumber * 2 + 2

                    # Get modified room
                    updatedroom = []
                    for i in range(4):
                        if roomposition == i:
                            updatedroom.append('.')
                        else:
                            updatedroom.append(room[i])
                    updatedroom = tuple(updatedroom)

                    # Get modified room
                    updatedrooms = list(rooms)
                    updatedrooms[roomnumber] = updatedroom
                    updatedrooms = tuple(updatedrooms)

                    moves = 1 + roomposition

                    # Find all valid moves to the right
                    for hallwayindex in range(room_hallway_index, len(hallway)):

                        # Only repeat valid
                        if hallway[hallwayindex] == '.':
                            # Cannot stop in front of room
                            if hallwayindex not in [2, 4, 6, 8]:
                                updatedhallway = list(hallway)
                                updatedhallway[hallwayindex] = char
                                possiblestates.append((''.join(updatedhallway), updatedrooms, moves * energy_per_move_dict[char]))
                        else:
                            # Cannot jump over other chars
                            break
                        moves += 1

                    # Find all valid moves to the left
                    moves = 1 + roomposition
                    for hallwayindex in range(room_hallway_index, -1, -1):

                        # Only repeat valid
                        if hallway[hallwayindex] == '.':
                            # Cannot stop in front of room
                            if hallwayindex not in [2, 4, 6, 8]:
                                updatedhallway = list(hallway)
                                updatedhallway[hallwayindex] = char
                                possiblestates.append((''.join(updatedhallway), updatedrooms, moves * energy_per_move_dict[char]))
                        else:
                            # Cannot jump over other chars
                            break
                        moves += 1

    return possiblestates

# Dictionary with required energy per move for each letter
energy_per_move_dict = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
# Dicitonary with correct room for each letter
correct_room_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

# Set up hallway and rooms. Rooms with first element at the top, last element at the bottom. Then translate it to a state
hallway = '...........'
rooms = (('B', 'D', 'D', 'C'), ('B', 'C', 'B', 'A'), ('D', 'B', 'A', 'D'), ('A', 'A', 'C', 'C'))
targetrooms = (('A', 'A', 'A', 'A'), ('B', 'B', 'B', 'B'), ('C', 'C', 'C', 'C'), ('D', 'D', 'D', 'D'))
state = (hallway, rooms)
targetstate = (hallway, targetrooms)

# Create a state queue, list of sorted energies
statequeue = [(state, 0)]

"""
Need a neat way of calculating the cost. Dijkstra?
"""
# Create priority queue
visited = set()
costs = {state: 0}

heap = [(0, state)]

while heap:
    heapcost, heapstate = heapq.heappop(heap)

    if heapstate in visited:
        continue

    visited.add(heapstate)

    if heapstate == targetstate:
        print(f'Minimum energy to move to correct state is {costs[targetstate]}')
        print(costs[targetstate])
    for possible in possiblestates(heapstate, correct_room_dict, energy_per_move_dict):

        hallway, rooms, newcost = possible
        newstate = (hallway, rooms)
        if newstate in visited:
            continue
        old_cost = costs.get(newstate, float('inf'))
        new_cost = newcost + costs.get(heapstate)
        if new_cost < old_cost:
            costs[newstate] = new_cost
            heapq.heappush(heap, (new_cost, newstate))
