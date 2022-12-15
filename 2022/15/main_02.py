import time
start = time.time()

# Open and read file
with open('input.txt') as file:
    lines = file.read().splitlines()
file.close()

# Create dict of sensors and their closest beacons
sensor_distance_dict = {}
for line in lines:
    linesplit = line.split("Sensor at ")[1].split(": closest beacon is at ")
    sensor, beacon = linesplit[0].split(", "), linesplit[1].split(", ")
    sensor_x, sensor_y = int(sensor[0].split('x=')[1]), int(sensor[1].split('y=')[1])
    beacon_x, beacon_y = int(beacon[0].split('x=')[1]), int(beacon[1].split('y=')[1])
    distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    sensor_distance_dict[(sensor_x, sensor_y)] = distance

# Distress beacon must be within these limits
x_min_map, y_min_map, x_max_map, y_max_map = 0, 0, 4000000, 4000000

found = False
for x in range(x_min_map, x_max_map + 1):

    range_list = []
    for key in sensor_distance_dict:

        y_min = key[1] - sensor_distance_dict[key] + abs(key[0] - x)
        if y_min > key[1]:
            continue
        y_max = key[1] + sensor_distance_dict[key] - abs(key[0] - x)
        if y_max < key[1]:
            continue

        range_list.append((y_min, y_max + 1))

    range_list.sort(key=lambda element: (element[1], element[0]))

    # Find number not covered
    while len(range_list) > 1:
        last = range_list.pop(len(range_list) - 1)
        next_last = range_list.pop(len(range_list) - 1)
        if last[0] > next_last[1] and x_min_map <= last[0] <= x_max_map and x_min_map <= next_last[1] <= x_max_map:
            print(x)
            print(x * 4000000 + last[0] - 1)
            found = True
        range_list.append((min(last[0], next_last[0]), max(last[1], next_last[1])))
    if found:
        break

end = time.time()
print(end - start)
