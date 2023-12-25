import random
import os
import time


def main():
    total_shuffles = 0
    successful_shuffles = 0

    try:
        while True:
            _, is_solvable = solve(shuffle_deck(create_deck()))
            total_shuffles += 1
            if is_solvable:
                successful_shuffles += 1
    except KeyboardInterrupt:
        # Calculate and print the ratio when the program is terminated.
        ratio = successful_shuffles / total_shuffles if total_shuffles else 0
        print(
            f"\nRatio of successful shuffles ({successful_shuffles}) to total shuffles ({total_shuffles}): {ratio}"
        )


def create_deck():
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    # ranks = ["7", "8", "9", "T", "J", "Q", "K", "A"]

    # Hearts, Diamonds, Clubs, Spades.
    suits = ["H", "D", "C", "S"]
    deck = [[rank + suit] for rank in ranks for suit in suits]

    return deck


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def matches(card1, card2):
    return card1[0][0] == card2[0][0] or card1[0][1] == card2[0][1]


def append_cards(deck, index1, index2):
    deck[index2].extend(deck[index1])
    del deck[index1]
    return deck


def solve(deck):
    if len(deck) < 3:
        return (deck, True)

    # Index of the current card.
    i = 2

    while True:
        if matches(deck[i], deck[i - 2]):
            append_cards(deck, i - 2, i - 1)

            if i <= 3:
                i = 2
            else:
                i -= 2
        else:
            i += 1

        if i >= len(deck):
            return (deck, True if len(deck) == 2 else False)


def quick_check(deck):
    if len(deck) < 3:
        return (deck, True)

    for i in range(len(deck) - 3, -1, -1):
        if not any(matches(deck[i], card) for card in deck[i + 2 :]):
            return False

    return True


if __name__ == "__main__":
    main()
