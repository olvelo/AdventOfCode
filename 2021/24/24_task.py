# Open and read file and split into instruction blocks
instruction_blocks = []
input = open('24_input.txt', 'r')
block = []
for line in input:
    if 'inp' in line.strip():
        instruction_blocks.append(block)
        block = [line.strip()]
    else:
        block.append(line.strip())
instruction_blocks.append(block)
del instruction_blocks[0]
input.close()

# Dictionary for index of each variable in the ALO
variable_index = {'w': 0, 'x': 1, 'y': 2, 'z': 3}

def find_highest_possible_numbers(instruction_blocks):

    # Dict with z val as key and number as value
    unique_options = {0: 0}

    # From left to right index
    for index in range(14):
        # For each possible number at this digit
        new_options = {}

        possible_numbers = [9] if index == 0 else [9,8,7,6,5,4,3,2,1]
        for possible_number in possible_numbers:
            # For each of the previous possibilities
            for key, val in unique_options.items():
                # Key is numbers and val is z value
                wxyz = [0, 0, 0, key]

                for instr in instruction_blocks[index]:

                    # Split instruction into a list
                    instr_list = instr.split(' ')

                    # The only instruction with two items is the input instruction
                    if len(instr_list) == 2:

                        # Read input to variable and increment model number index
                        wxyz[variable_index[instr_list[1]]] = possible_number

                    else:

                        # Get variable index to store result in
                        wxyz_index = variable_index[instr_list[1]]

                        # Get the variables for the operation
                        var1 = wxyz[variable_index[instr_list[1]]]
                        var2 = wxyz[variable_index[instr_list[2]]] if instr_list[2] in 'wxyz' else int(instr_list[2])

                        # Figure out operation and do it
                        operation = instr_list[0]
                        if operation == 'add':
                            wxyz[wxyz_index] = var1 + var2
                        elif operation == 'mul':
                            wxyz[wxyz_index] = var1 * var2
                        elif operation == 'div':
                            wxyz[wxyz_index] = var1 // var2
                        elif operation == 'mod':
                            wxyz[wxyz_index] = var1 % var2
                        elif operation == 'eql':
                            wxyz[wxyz_index] = 1 if var1 == var2 else 0

                # Have calulated new z value for new number combination of numbers. Only keep largest number giving that z
                newnumber = val * 10 + possible_number
                if wxyz[3] not in new_options.keys():
                    new_options[wxyz[3]] = newnumber
                elif newnumber > new_options[wxyz[3]]:
                    new_options[wxyz[3]] = newnumber

        unique_options = new_options
        print(len(unique_options))


    mylist = []
    for key,val in unique_options.items():
        if key == 0:
            mylist.append(val)
    return mylist

def find_smallest_possible_numbers(instruction_blocks):

    # Dict with z val as key and number as value
    unique_options = {0: 0}

    # From left to right index
    for index in range(14):
        # For each possible number at this digit
        new_options = {}

        possible_numbers = [5] if index == 0 else [9,8,7,6,5,4,3,2,1]
        for possible_number in possible_numbers:
            # For each of the previous possibilities
            for key, val in unique_options.items():
                # Key is numbers and val is z value
                wxyz = [0, 0, 0, key]

                for instr in instruction_blocks[index]:

                    # Split instruction into a list
                    instr_list = instr.split(' ')

                    # The only instruction with two items is the input instruction
                    if len(instr_list) == 2:

                        # Read input to variable and increment model number index
                        wxyz[variable_index[instr_list[1]]] = possible_number

                    else:

                        # Get variable index to store result in
                        wxyz_index = variable_index[instr_list[1]]

                        # Get the variables for the operation
                        var1 = wxyz[variable_index[instr_list[1]]]
                        var2 = wxyz[variable_index[instr_list[2]]] if instr_list[2] in 'wxyz' else int(instr_list[2])

                        # Figure out operation and do it
                        operation = instr_list[0]
                        if operation == 'add':
                            wxyz[wxyz_index] = var1 + var2
                        elif operation == 'mul':
                            wxyz[wxyz_index] = var1 * var2
                        elif operation == 'div':
                            wxyz[wxyz_index] = var1 // var2
                        elif operation == 'mod':
                            wxyz[wxyz_index] = var1 % var2
                        elif operation == 'eql':
                            wxyz[wxyz_index] = 1 if var1 == var2 else 0

                # Have calulated new z value for new number combination of numbers. Only keep largest number giving that z
                newnumber = val * 10 + possible_number
                if wxyz[3] not in new_options.keys():
                    new_options[wxyz[3]] = newnumber
                elif newnumber < new_options[wxyz[3]]:
                    new_options[wxyz[3]] = newnumber

        unique_options = new_options
        print(len(unique_options))


    mylist = []
    for key,val in unique_options.items():
        if key == 0:
            mylist.append(val)
    return mylist

"""
Not the best solution, but it works (takes some time

- Reverse-engineered ALU to determine only state kept from one instruction set to the next is variable z
- For each digit, find largest/smallest possible number for each unique z value
- Move on to next digit and repeat
- Return all numbers resulting in a z value of 0 at the end
- The two functions contain a qualified guess for the first digit (found after trial and error) to speed up the calculation
"""

numbers = find_highest_possible_numbers(instruction_blocks)
print(max(numbers))

numbers = find_smallest_possible_numbers(instruction_blocks)
print(min(numbers))
