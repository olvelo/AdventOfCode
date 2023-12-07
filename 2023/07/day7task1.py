"""
Create dict to store rank (enum) of each hand (1-7, five of a kind, four of a kind etc), create function to compare
classified hands, create function to classify each card. Insertion sort into list. Multiply list with rank times bid to get score.

"""
from enum import Enum

class HandType(Enum):
    HIGHCARD = 1
    ONEPAIR = 2
    TWOPAIR = 3
    THREEOFAKIND = 4
    FULLHOUSE = 5
    FOUROFAKIND = 6
    FIVEOFAKIND = 7

card_strength = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

hands_types = {}

def classify_hand(hand):
    hand_set = set(hand)
    hand_set_list = list(hand_set)
    if len(hand_set) == 1:
        return HandType.FIVEOFAKIND
    elif len(hand_set) == 2:
        if hand.count(hand_set_list[0]) == 4 or hand.count(hand_set_list[1]) == 4:
            return HandType.FOUROFAKIND
        else:
            return HandType.FULLHOUSE
    elif len(hand_set) == 3:
        if hand.count(hand_set_list[0]) == 3 or hand.count(hand_set_list[1]) == 3 or hand.count(hand_set_list[2]) == 3:
            return HandType.THREEOFAKIND
        else:
            return HandType.TWOPAIR
    elif len(hand_set) == 4:
        return HandType.ONEPAIR
    else:
        return HandType.HIGHCARD

def compare_classified_cards(card1, card2):
    if hands_types[card1].value > hands_types[card2].value:
        return 1
    elif hands_types[card2].value > hands_types[card1].value:
        return -1
    else:
        for i in range(len(card1)):
            if card_strength.index(card1[i]) < card_strength.index(card2[i]):
                return 1
            elif card_strength.index(card2[i]) < card_strength.index(card1[i]):
                return -1
    return 0


if __name__ == "__main__":

    # Open and read file
    with open('input.txt') as f:
        lines = f.readlines()

    # Get hands and bids
    hands = []
    bids = []
    for line in lines:
        hand, bid = line.strip().split()
        hands.append(hand)
        bids.append(int(bid))

    # Create hands_bid_map
    hands_bids = {}
    for i in range(len(hands)):
        hands_bids[hands[i]] = bids[i]

    # Classify the cards
    for hand in hands:
        handtype = classify_hand(hand)
        hands_types[hand] = handtype

    # Sort cards with insertion sort
    from functools import cmp_to_key
    sorted_hands = sorted(hands, key=cmp_to_key(compare_classified_cards))

    winnings = 0
    for i in range(len(sorted_hands)):
        winnings += (i+1) * hands_bids[sorted_hands[i]]

    print(winnings)
