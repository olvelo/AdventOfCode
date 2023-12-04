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

    sum = 0
    for card in cards:
        winning, mine = card
        cardsum = 0
        for number in mine:
            if number in winning:
                cardsum = cardsum * 2 if cardsum > 0 else 1
        sum += cardsum

    print(sum)







