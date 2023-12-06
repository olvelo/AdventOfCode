import math


def get_distance(time_charged, time_total):
    return time_charged * (time_total - time_charged)

if __name__ == "__main__":

    # Open and read file
    with open('input.txt') as f:
        lines = f.readlines()

    time = int("".join(lines.pop(0).strip().split()[1::]))
    record = int("".join(lines.pop(0).strip().split()[1::]))

    time_one = time + math.sqrt(time*time - 4*record) / 2
    time_two = time - math.sqrt(time*time - 4*record) / 2

    print(int(time_one - time_two))

    wins = 0
    for t in range(time):
        if get_distance(t, time) > record:
            wins += 1

    print(wins)
