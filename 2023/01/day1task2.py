if __name__ == "__main__":

    # Open and read file
    with open('input1.txt') as f:
        lines = f.readlines()

    sum = 0
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for line in lines:

        # Find index of the words
        low_index, high_index = 99999999, 0
        first_digit, second_digit = 0, 0

        for word in words:
            if word in line:
                if line.index(word) < low_index:
                    low_index = line.index(word)
                    first_digit = words.index(word) + 1

                if line.rfind(word) > high_index:
                    high_index = line.rfind(word)
                    second_digit = words.index(word) + 1

        # Find lowest and highest index of numbers, if any
        for char in line:
            if char.isdigit():
                if line.index(char) < low_index:
                    low_index = line.index(char)
                    first_digit = char
                    break

        for char in line[::-1]:
            if char.isdigit():
                if line.rfind(char) >= high_index:
                    high_index = line.rfind(char)
                    second_digit = char
                    break

        digits = int(f'{first_digit}{second_digit}')
        sum += digits

    print(sum)
