# Open and read file to array
input = open('08_input.txt', 'r')
displays = []
for line in input:
    displays.append(line.strip())
input.close()

"""
Task 1, sum all 1, 4, 7 and 8
"""
# Sum all 2, 3, 4 and 7's
sum = 0
for display in displays:
    signal_pattern, output_values = display.split('|')
    for output_value in output_values.split(' '):
        if len(output_value) in [2, 3, 4, 7]:
            sum += 1

print('Number of 1, 4, 7 and 8: {}'.format(sum))

"""
Task 2, decode signal patterns
"""

# Function to check if something is contained in another
def contains(contained, container):
    for char in contained:
        if char not in container:
            return False
    return True

sum = 0
for display in displays:
    # Create dictionary to store decoded
    decoded = {}

    # Separate signal pattern and output values for the display, in arrays
    signal_pattern, output_values = display.split('|')
    signal_pattern = signal_pattern.strip().split(' ')
    output_values = output_values.strip().split(' ')

    # Look for 1, 4, 7 and 8
    for signal in signal_pattern:
        if len(signal) == 2:
            decoded[1] = signal
        elif len(signal) == 3:
            decoded[7] = signal
        elif len(signal) == 4:
            decoded[4] = signal
        elif len(signal) == 7:
            decoded[8] = signal

    # Remove numbers found from signal pattern, to avoid looping over again
    for value in decoded.values():
        signal_pattern.remove(value)

    # Decode the rest while not everything is decoded
    while(len(decoded) < 10):

        # Decode signals where possible
        for signal in signal_pattern:

            # 0, 6 and 9 all have 6 signals
            if len(signal) == 6:
                # Only 6 does not contain 1
                if not contains(decoded[1], signal):
                    decoded[6] = signal
                else:
                    # Must be 0 og 9
                    if not contains(decoded[4], signal):
                        # Signals to create 4 is not contained in 0, must be a 0
                        decoded[0] = signal
                    else:
                        # must be 9
                        decoded[9] = signal
            # The rest of the numbers (2, 3, 5) all have length of 5
            else:
                # Only 3 contains 1
                if contains(decoded[1], signal):
                    decoded[3] = signal
                # If not 3, must be 2 or 5
                elif (9 in decoded and contains(signal, decoded[9])) or (6 in decoded and contains(signal, decoded[6])):
                    # 5 is contained in 9 and 6, 2 is not
                    decoded[5] = signal
                else:
                    # Must be 2
                    decoded[2] = signal

    # Now we can decode the output value
    output = ''
    # For each value
    for value in output_values:
        # For each decoded
        for key in decoded:
            # Check if both contain each other
            if contains(decoded[key], value) and contains(value, decoded[key]):
                output += str(key)

    sum += int(output)

print('Sum of all decoded values = {}'.format(sum))
