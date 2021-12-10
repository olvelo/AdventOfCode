# Dicts for points when calculating error and autocomplete scores
errorpoints = {')': 3, ']': 57, '}': 1197, '>': 25137}
autocompletepoints = {'(': 1, '[': 2, '{': 3, '<': 4}

# Open file
input = open('10_input.txt', 'r')

# Array for storing autocomplete scores, and variable to store error sum of faulty lines
autocompletescores = []
errorsum = 0
for line in input:
    # Create empty stack/string, and set initial errorscore to 0
    stack, errorscore = '', 0

    # Check each char in the line
    for char in line.strip():
        if char in '{[(<':
            # If opening, add to stack
            stack += char
        else:
            # If not, check if closing wrong bracket and calculate error score
            last = stack[-1]
            stack = stack[:-1]
            if (last == '{' and char != '}' or
                    last == '(' and char != ')' or
                    last == '[' and char != ']' or
                    last == '<' and char != '>'):
                errorscore += errorpoints[char]
                break

    if errorscore == 0:
        # No error found, calculate autocomplete score
        autocompletescore = 0
        for char in stack[::-1]:
            autocompletescore = autocompletescore * 5 + autocompletepoints[char]
        autocompletescores.append(autocompletescore)
    else:
        # Error found, add to total error sum
        errorsum += errorscore

# Close file and print results
input.close()
print('Error score = {}'.format(errorsum))
autocompletescores.sort()
print('Autocomplete score = {}'.format(autocompletescores[len(autocompletescores)//2]))
