# Open and read file
input = open('04_input.txt', 'r')

# Get first line with random numbers
firstline = input.readline().strip()
randoms = [int(random) for random in firstline.split(',')]

# Get boards as array of arrays
boards, newboard = [], []
for line in input:
    if len(newboard) == 25:
        boards.append(newboard)
    if line == '\n':
        newboard = []
    else:
        numberstring = ''
        for char in line:
            if char != ' ' and char != '\n':
                numberstring += char
            elif len(numberstring) > 0:
                newboard.append(int(numberstring))
                numberstring = ''

# Append last number and board
newboard.append(int(numberstring))
boards.append(newboard)

# Play bingo, iterating over random drawn numbers
boardwinners = []
for drawn in randoms:

    # For all boards
    for board in boards:

        # Mark drawn numbers
        for i, number in enumerate(board):
            if number == drawn:
                board[i] = -1

                # Check for winner
                rowstart = i - i % 5
                columnstart = i % 5
                rowwinner, columnwinner = True, True
                for i in range(rowstart, rowstart + 5):
                    if board[i] != -1:
                        rowwinner = False

                for i in range(columnstart, columnstart + 25, 5):
                    if board[i] != -1:
                        columnwinner = False

                if columnwinner or rowwinner:

                    # Calculate winner score
                    sum = 0
                    for number in board:
                        if number != -1:
                            sum += number
                    sum = sum * drawn
                    if boards.index(board) not in boardwinners:
                        print("Board {}, Score {}".format(sum, boards.index(board)))
                        boardwinners.append(boards.index(board))


input.close()
