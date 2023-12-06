def get_distance(time_charged, time_total):
    return time_charged * (time_total - time_charged)

if __name__ == "__main__":

    # Open and read file
    with open('input.txt') as f:
        lines = f.readlines()

    times = [int(number) for number in lines.pop(0).strip().split()[1::]]
    records = [int(number) for number in lines.pop(0).strip().split()[1::]]

    total_combinations = 1
    for i in range(len(times)):
        local_combinations = 0
        for t in range(times[i]):
            if get_distance(t, times[i]) > records[i]:
                local_combinations += 1
        total_combinations = total_combinations * local_combinations

    print(total_combinations)