import random
import pandas as pd

def initial_deal(num_players=1, deck_size=6):
    suits = ['♠', '♡', '♢', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # Create a deck with suits
    deck = [(rank, suit) for suit in suits for rank in ranks] * deck_size

    # Shuffle the deck
    shuffled_deck = deck.copy()
    random.shuffle(shuffled_deck)

    # Deal cards to each player and the dealer
    hands = {'Player {}'.format(i + 1): [shuffled_deck.pop(), shuffled_deck.pop()] for i in range(num_players)}
    hands['Dealer'] = [shuffled_deck.pop(), shuffled_deck.pop()]

    # Remaining cards in the deck
    remaining_cards = shuffled_deck

    # Create a DataFrame to record the initial deal
    df = pd.DataFrame(hands)
    return df, remaining_cards


def calculate_hand_value(hand):
    total_value = sum(11 if card[0] == 'A' else 10 if card[0] in ['J', 'Q', 'K'] else int(card[0]) for card in hand)

    for card in hand:
        if card[0] == 'A' and total_value > 21:
            total_value -= 10

    return total_value


def is_blackjack(hand):
    return any(card[0] == 'A' and any(c[0] in ['10', 'J', 'Q', 'K'] for c in hand) for card in hand)


def hit(remaining_cards):
    
    if remaining_cards:
        card = remaining_cards.pop()
        return card
    else:
        print("No more cards!")

def double_down(remaining_cards):
    
    if remaining_cards:
        card = remaining_cards.pop()
        return card
    else:
        print("No more cards!")