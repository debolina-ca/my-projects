# Picking a random playing card
from random import choice


def pick_card():
    card_type = ['Clubs', 'Diamonds', 'Hearts', 'Spades'];
    card_number = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    # choose a type at random
    t = choice(card_type)
    n = choice(card_number)

    return [n, t]


# Show the randomly picked card
print(pick_card())
