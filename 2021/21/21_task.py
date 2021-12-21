# Open and read file with starting positions
positions_input = []
input = open('21_input.txt', 'r')
positions_input.append(int(input.readline().strip()[-1]))
positions_input.append(int(input.readline().strip()[-1]))
input.close()

"""
Task 1 below
"""
# Initialize scores, die and turn number
positions, scores, die, turn = [x for x in positions_input], [0, 0], 0, 0

# Repeat game while no player has 1000 points or above
while all(score < 1000 for score in scores):
    # Get new player based on turn
    player = turn % 2
    # Calculate moves from 3 die rolls
    moves = 0
    for i in range(3):
        die += 1
        moves += (die - 1) % 100 + 1
    # Update position and score, then increment turn
    positions[player] = (positions[player] + moves - 1) % 10 + 1
    scores[player] += positions[player]
    turn += 1

print(f'Task 1: We have a winner! Loosing score multiplied by number of die rolls is {scores[turn % 2] * die}')

"""
Task 2 below
"""
# Create dict of permutations giving each sum of three die throws
permutaitons_sum = {}
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1,4):
            if i + j + k in permutaitons_sum.keys():
                permutaitons_sum[i + j + k] += 1
            else:
                permutaitons_sum[i + j + k] = 1

# Create dict of new position based on position and die
newpos_posdie = {}
for i in range(1, 11):
    for j in range(3, 10):
        newpos_posdie[i, j] = (i + j - 1) % 10 + 1

win_count = [0,0]
def calculatevictories(pos0, pos1, score0, score1, target, win_count, times_here, round):
    """
        Calculate number of wins recursively, for all "parallell universes"
    Args:
        pos0: Position of player 0
        pos1: Position of player 1
        score0: Score of player 0
        score1: Score of player 1
        target: Target score
        win_count: Array counting wins per player
        times_here: Times we are reaching this code path, based on die statistics
        round: The playing round, to determine which player throws the die
    """
    if score0 >= target:
        win_count[0] += times_here
    elif score1 >= target:
        win_count[1] += times_here
    else:
        if round % 2 == 0:
            for i in range(3, 10):
                newpos0 = newpos_posdie[pos0, i]
                newscore0 = score0 + newpos0
                newpos1 = pos1
                newscore1 = score1
                calculatevictories(newpos0, newpos1, newscore0, newscore1, target, win_count, permutaitons_sum[i] * times_here, round + 1)
        else:
            for i in range(3, 10):
                newpos0 = pos0
                newscore0 = score0
                newpos1 = newpos_posdie[pos1, i]
                newscore1 = score1 + newpos1
                calculatevictories(newpos0, newpos1, newscore0, newscore1, target, win_count, permutaitons_sum[i] * times_here, round + 1)

calculatevictories(positions_input[0], positions_input[1], 0, 0, 21, win_count, 1, 0)
print(f'Task 2: Number of wins for the most-winning player is {max(win_count)}')
