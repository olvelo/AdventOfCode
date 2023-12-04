import copy

if __name__ == "__main__":

    # Open and read file
    with open('input.txt') as f:
        lines = f.readlines()


    cards = []
    for line in lines:
        winning, mine = line.strip().split("|")
        winning = winning.split(":")[1]
        winning = [x for x in winning.split(" ") if x != ""]
        mine = [x for x in mine.split(" ") if x != ""]
        cards.append((winning, mine))

    card_wins = {}
    card_instances = {}

    for i, card in enumerate(cards):
        winning, mine = card
        wins = 0
        for number in mine:
            if number in winning:
                wins += 1
        card_wins[i] = wins
        card_instances[i] = 1

    for i in range(len(cards)):
        for j in range(card_wins[i]):
            card_instances[i + j + 1] += card_instances[i]

    print(sum(card_instances.values()))
