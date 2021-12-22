# Open and read file with reboot steps, appending to a list with coordinates and on or off
reboot_list = []
input = open('22_input.txt', 'r')
for line in input:
    xstring, ystring, zstring = line.strip().split(',')
    on = 1 if xstring.split(' ')[0] == 'on' else 0
    x0, x1 = xstring.split('..')
    x0 = x0.split('=')[-1]
    y0, y1 = ystring.split('..')
    y0 = y0.split('=')[-1]
    z0, z1 = zstring.split('..')
    z0 = z0.split('=')[-1]
    reboot_list.append((on, int(x0), int(x1), int(y0), int(y1), int(z0), int(z1)))
input.close()

"""
Task 1 below, bruteforcing
"""
# Now looop through in reverse order and only update cubes if not updated already, to always just use the last instruction
boundary = 50
cubes_state = {}
reboot_list.reverse()
for reboot_instruction in reboot_list:
    state, x0, x1, y0, y1, z0, z1 = reboot_instruction
    # Make sure we are within boundaries
    for x in range(max(-abs(boundary), x0), min(x1 + 1, abs(boundary + 1))):
        for y in range(max(-abs(boundary), y0), min(y1 + 1, abs(boundary + 1))):
            for z in range(max(-abs(boundary), z0), min(z1 + 1, abs(boundary + 1))):
                if (x, y, z) not in cubes_state.keys():
                    cubes_state[(x, y, z)] = state

# Now check number of cubes turned on in the dict
sum = 0
for key, val in cubes_state.items():
    sum += val
print(f'Task 1: Cubes turned on after applying all steps = {sum}')
reboot_list.reverse() # Reverse again for task 2

"""
Task 2 below, smarter way
"""
def check_overlap(cube0, cube1):
    """
    Check if overlap / intersection between two cubes

    Args:
        cube0: Coordinates of cube 0
        cube1: Coordinates of cube 1

    Returns: True if overlap / intersection, False if not
    """
    x0, x1, y0, y1, z0, z1 = cube0
    xx0, xx1, yy0, yy1, zz0, zz1 = cube1
    if (x1 >= xx0 and x0 <= xx1 and y1 >= yy0 and y0 <= yy1 and z1 >= zz0 and z0 <= zz1):
        return True
    return False

def splitcubes(cube0, cube1):
    """
    Split intersecting cubes into up to 6 different new cubes for each of them. Also separate out the intersection
    Args:
        cube0: Coordinates of cube 0
        cube1: Coordinates of cube 1

    Returns: The (max) 6 splitted cubes for both cube0 and cube1, plus the intersection
    """
    x0, x1, y0, y1, z0, z1 = cube0
    xx0, xx1, yy0, yy1, zz0, zz1 = cube1

    cube0split = [(x0, x1, y0, y1, max(z0, zz1 + 1), z1),
                  (x0, x1, y0, y1, z0, min(z1, zz0 - 1)),
                  (x0, x1, max(y0, yy1 + 1), y1, max(z0, zz0), min(z1, zz1)),
                  (x0, x1, y0, min(y1, yy0 - 1), max(z0, zz0), min(z1, zz1)),
                  (max(x0, xx1 + 1), x1, max(y0, yy0), min(y1, yy1), max(z0, zz0), min(z1, zz1)),
                  (x0, min(x1, xx0 - 1), max(y0, yy0), min(y1, yy1), max(z0, zz0), min(z1, zz1))]

    cube1split = [(xx0, xx1, yy0, yy1, max(zz0, z1 + 1), zz1),
                  (xx0, xx1, yy0, yy1, zz0, min(zz1, z0 - 1)),
                  (xx0, xx1, max(yy0, y1 + 1), yy1, max(zz0, z0), min(zz1, z1)),
                  (xx0, xx1, yy0, min(yy1, y0 - 1), max(zz0, z0), min(zz1, z1)),
                  (max(xx0, x1 + 1), xx1, max(yy0, y0), min(yy1, y1), max(zz0, z0), min(zz1, z1)),
                  (xx0, min(xx1, x0 - 1), max(yy0, y0), min(yy1, y1), max(zz0, z0), min(zz1, z1))]

    overlap = (max(x0, xx0), min(x1, xx1), max(y0, yy0), min(y1, yy1), max(z0, zz0), min(z1, zz1))


    # Only keep valid calculations
    cube0split_filtered, cube1split_filtered, overlap_filtered = [], [], None

    for cube in cube0split:
        x0, x1, y0, y1, z0, z1 = cube
        if x1 >= x0 and y1 >= y0 and z1 >= z0:
            cube0split_filtered.append(cube)

    for cube in cube1split:
        x0, x1, y0, y1, z0, z1 = cube
        if x1 >= x0 and y1 >= y0 and z1 >= z0:
            cube1split_filtered.append(cube)

    x0, x1, y0, y1, z0, z1 = overlap
    if x1 >= x0 and y1 >= y0 and z1 >= z0:
        overlap_filtered = overlap

    return cube0split_filtered, cube1split_filtered, overlap_filtered

# Create dictionary to store all cubes that are turning lights on
cubes = {}
# Loop over all reboot instructions
for instruction in reboot_list:

    # Get coordinates for the new cube
    state, x0, x1, y0, y1, z0, z1 = instruction
    newcube = (x0, x1, y0, y1, z0, z1)

    # Create list of cubes to add and remove
    toadd = []
    toremove = []

    # Loop over cubes already in the dictionary
    for oldcube in cubes.keys():

        # Check if any overlapping regions between the cubes
        overlap = check_overlap(newcube, oldcube)

        if overlap:

            # Split the old and new cubes, and get the overlapping region
            oldcubesplit, newcubesplit, overlap = splitcubes(oldcube, newcube)

            # Add the old cube splitted, remove the OG old cube
            if oldcube not in toremove:
                toremove.append(oldcube)
            toadd.extend(oldcubesplit)

            if state == 1 and newcube not in toadd:
                toadd.append(newcube)

    # Finally add the new cube, we have splitted all the old ones now
    if state == 1:
        toadd.append(newcube)

    for cubekey in toremove:
        del cubes[cubekey]

    for cubekey in toadd:
        cubes[cubekey] = 1


# Sum up cubes turned on
sum = 0
for key, val in cubes.items():
    x0, x1, y0, y1, z0, z1 = key
    if val == 1:
        sum += (x1+1-x0)*(y1+1-y0)*(z1+1-z0)

print(sum)
#1387966280636636


