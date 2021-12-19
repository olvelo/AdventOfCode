import numpy as np

def rotations():
    """
    Generate all 24 possible 3D rotation matrices based on rotations 90 degrees around X and Y axes

    Returns: All possible 3D rotation matrices as a list
    """
    X = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
    Y = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]
    rotation_matrices = []

    rotation_matrices.append([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    rotation_matrices.append(X)
    rotation_matrices.append(Y)

    rotation_matrices.append(np.matmul(X, X).tolist())
    rotation_matrices.append(np.matmul(X, Y).tolist())
    rotation_matrices.append(np.matmul(Y, X).tolist())
    rotation_matrices.append(np.matmul(Y, Y).tolist())

    rotation_matrices.append(np.matmul(np.matmul(X, X), X).tolist())
    rotation_matrices.append(np.matmul(np.matmul(X, X), Y).tolist())
    rotation_matrices.append(np.matmul(np.matmul(X, Y), X).tolist())
    rotation_matrices.append(np.matmul(np.matmul(Y, X), X).tolist())
    rotation_matrices.append(np.matmul(np.matmul(Y, Y), X).tolist())
    rotation_matrices.append(np.matmul(np.matmul(X, Y), Y).tolist())
    rotation_matrices.append(np.matmul(np.matmul(Y, Y), Y).tolist())

    rotation_matrices.append(np.matmul(np.matmul(np.matmul(X, X), X), Y).tolist())
    rotation_matrices.append(np.matmul(np.matmul(np.matmul(X, X), Y), X).tolist())
    rotation_matrices.append(np.matmul(np.matmul(np.matmul(X, X), Y), Y).tolist())
    rotation_matrices.append(np.matmul(np.matmul(np.matmul(X, Y), X), X).tolist())
    rotation_matrices.append(np.matmul(np.matmul(np.matmul(X, Y), Y), Y).tolist())
    rotation_matrices.append(np.matmul(np.matmul(np.matmul(Y, X), X), X).tolist())
    rotation_matrices.append(np.matmul(np.matmul(np.matmul(Y, Y), Y), X).tolist())

    rotation_matrices.append(np.matmul(np.matmul(np.matmul(np.matmul(X, X), X), Y), X).tolist())
    rotation_matrices.append(np.matmul(np.matmul(np.matmul(np.matmul(X, Y), X), X), X).tolist())
    rotation_matrices.append(np.matmul(np.matmul(np.matmul(np.matmul(X, Y), Y), Y), X).tolist())

    return rotation_matrices

# Open and read file to a list of beacons scanned by each scanner
all_beacons = []
input = open('19_input.txt', 'r')
scanner_index = 0
for line in input:
    if 'scanner' in line:
        all_beacons.append([])
        continue
    elif line.strip() == '':
        scanner_index += 1
    else:
        all_beacons[scanner_index].append([int(x) for x in line.strip().split(',')])
input.close()

# Obtain all 24 rotation matrices
rotation_matrices = rotations()

# Create a list of lists, where first index denotes the scanner, second index denotes the rotation-permutation and
# third index denotes the beacon (rotated)
scanner_permutation_beacon_list = []
for scanner_beacons in all_beacons:
    beacon_permutations = []
    permutation_index = 0
    for rotation_matrix in rotation_matrices:
        beacon_permutations.append([])
        for beacon in scanner_beacons:
            beacon_permutations[permutation_index].append(np.matmul(rotation_matrix, beacon).tolist())
        permutation_index += 1
    scanner_permutation_beacon_list.append(beacon_permutations)

# Dict containing located scanners and their positions
located_scanner_positions = {0: [0, 0, 0]}

# Dict containing located scanners and their beacons, oriented same way as scanner 1
located_scanner_beacons = {0: scanner_permutation_beacon_list[0][0]}

# Store total number of scanners for easier indexing
scanners_amount = len(scanner_permutation_beacon_list)

# Locate scanners while not all are located
while(len(located_scanner_positions) < len(scanner_permutation_beacon_list)):

    # Update unlocated and located scanner indexes
    unlocated_scanner_indexes = [x for x in range(scanners_amount) if x not in located_scanner_positions.keys()]
    located_scanner_indexes = [x for x in range(scanners_amount) if x in located_scanner_positions.keys()]

    # Get a list of beacons from a located scanner
    for located_index in located_scanner_indexes:
        known_beacons = located_scanner_beacons[located_index]

        # Check all possible unlocated scanners
        for unlocated_index in unlocated_scanner_indexes:

            # Get a list of beacons from an unlocated scanner:
            scanner_was_located = False
            for unknown_beacons in scanner_permutation_beacon_list[unlocated_index]:

                # Initialize dictionary to track relative differences between beacons. Key is relative difference and value is count
                diff_count = {}

                # Iterate over beacons
                for known_beacon in known_beacons:
                    for unknown_beacon in unknown_beacons:

                        # Find relative distance and update dictionary
                        diff = (known_beacon[0] - unknown_beacon[0], known_beacon[1] - unknown_beacon[1], known_beacon[2] - unknown_beacon[2])
                        if diff in diff_count.keys():
                            diff_count[diff] += 1
                        else:
                            diff_count[diff] = 1

                # Check if 12 or more points have same relative difference
                for key in diff_count:
                    if diff_count[key] >= 12:
                        # We have 12 or more points covered by the same scanners, now in same orientation. Update located scanner beacons and positions
                        located_scanner_beacons[unlocated_index] = unknown_beacons
                        located_scanner_positions[unlocated_index] = [a + b for a, b in zip(list(key), located_scanner_positions[located_index])]
                        scanner_was_located = True
                        break

                if scanner_was_located:
                    # No need to try other permutations
                    break

# Now we need to calculate all unique beacons
unique_beacons = []
for i in range(len(located_scanner_positions)):
    position = located_scanner_positions[i]
    beacons = located_scanner_beacons[i]
    for beacon in beacons:
        absolutebeacon = [a + b for a, b in zip(beacon, position)]
        if absolutebeacon not in unique_beacons:
            unique_beacons.append(absolutebeacon)

print(f'Number of unique beacons is {len(unique_beacons)}')

# Find largest manhattan distance between any two scanners
max_manhattan_dist = 0
for key1 in located_scanner_positions:
    for key2 in located_scanner_positions:
        candidate = (abs(located_scanner_positions[key1][0] - located_scanner_positions[key2][0]) +
                     abs(located_scanner_positions[key1][1] - located_scanner_positions[key2][1]) +
                     abs(located_scanner_positions[key1][2] - located_scanner_positions[key2][2]))

        max_manhattan_dist = max(max_manhattan_dist, candidate)

print(f'Max Manhattan distance is {max_manhattan_dist}')
