# Open and read file
with open('input.txt') as file:
    lines = file.read().splitlines()
file.close()

# Create dict of sensors and their closest beacons
sensor_beacon_dict = {}
for line in lines:
    linesplit = line.split("Sensor at ")[1].split(": closest beacon is at ")
    sensor, beacon = linesplit[0].split(", "), linesplit[1].split(", ")
    sensor_x, sensor_y = int(sensor[0].split('x=')[1]), int(sensor[1].split('y=')[1])
    beacon_x, beacon_y = int(beacon[0].split('x=')[1]), int(beacon[1].split('y=')[1])
    sensor_beacon_dict[(sensor_x, sensor_y)] = (beacon_x, beacon_y)

# Inspect one row and find how many positions cannot contain a beacon
y_check = 2000000

# Create a set of points without beacons
points_without_beacons = set()
# For each sensor_beacon pair
for key in sensor_beacon_dict:

    # Find all points that cannot contain a beacon at row y_check, and add to the set
    sensor_x, sensor_y, beacon_x, beacon_y = key[0], key[1], sensor_beacon_dict[key][0], sensor_beacon_dict[key][1]
    distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    if not sensor_y - distance < y_check < sensor_y + distance:
        continue

    for x in range(sensor_x - distance, sensor_x + distance + 1):
        this_distance = abs(sensor_x - x) + abs(sensor_y - y_check)
        if this_distance <= distance and (x, y_check) not in sensor_beacon_dict.values():
            points_without_beacons.add((x, y_check))

counter = 0
for item in points_without_beacons:
    if item[1] == y_check:
        counter += 1
print(counter)
