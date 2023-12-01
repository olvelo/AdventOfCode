if __name__ == "__main__":

    # Open and read file
    with open('input1.txt') as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        digits = ''
        for char in line:
            if char.isdigit():
                digits += char
                break

        for char in line[::-1]:
            if char.isdigit():
                digits += char
                break
        sum += int(digits)
    print(sum)
