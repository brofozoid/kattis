import sys

hands = []
amountOfHands, trumpSuit = sys.stdin.readline().split()
for line in sys.stdin:
    hands.append(line.strip())
trumpScores = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 20,
    "T": 10,
    "9": 14,
    "8": 0,
    "7": 0}
averageScores = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 2,
    "T": 10,
    "9": 0,
    "8": 0,
    "7": 0}


def get_card_type(card):
    return card[0]


def check_for_trump_suit(card):
    return card[1] == trumpSuit


def score_card(card):
    card_type = get_card_type(card)
    if check_for_trump_suit(card):
        return trumpScores[card_type]
    else:
        return averageScores[card_type]


def get_score(cards):
    mapped_cards = list(map(lambda card: (score_card(card)), cards))
    total_mapped_cards = 0
    for value in mapped_cards:
        total_mapped_cards += value
    return total_mapped_cards


print(get_score(hands))
