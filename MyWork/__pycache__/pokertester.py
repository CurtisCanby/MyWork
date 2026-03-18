# Making a poker hand tester
# allow user to pick their hand
# then randomly generate a hand for computer
# then deal cards and determine who wins
# do that 1000 times and see the win rate for the user
# the game is texas hold em so the user and computer get 2 cards each then deal 5
# the best 5 card hand wins
# use the standard poker hand rankings to determine the winner
import random
from collections import Counter
from itertools import combinations
# Define the ranks and suits
RANKS = '23456789TJQKA'
SUITS = 'CDHS'
# Create a deck of cards
DECK = [rank + suit for rank in RANKS for suit in SUITS]
# Function to evaluate the hand strength
def evaluate_hand(hand):
    ranks = sorted([RANKS.index(card[0]) for card in hand], reverse=True)
    suits = [card[1] for card in hand]
    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)
    is_flush = max(suit_counts.values()) == 5
    is_straight = (max(ranks) - min(ranks) == 4) and len(rank_counts) == 5
    if is_straight and is_flush:
        return (8, max(ranks))  # Straight flush
    elif 4 in rank_counts.values():
        return (7, [rank for rank, count in rank_counts.items() if count == 4][0])  # Four of a kind
    elif 3 in rank_counts.values() and 2 in rank_counts.values():
        return (6, [rank for rank, count in rank_counts.items() if count == 3][0])  # Full house
    elif is_flush:
        return (5, ranks)  # Flush
    elif is_straight:
        return (4, max(ranks))  # Straight
    elif 3 in rank_counts.values():
        return (3, [rank for rank, count in rank_counts.items() if count == 3][0])  # Three of a kind
    elif list(rank_counts.values()).count(2) == 2:
        return (2, sorted([rank for rank, count in rank_counts.items() if count == 2], reverse=True))  # Two pair
    elif 2 in rank_counts.values():
        return (1, [rank for rank, count in rank_counts.items() if count == 2][0])  # One pair
    else:
        return (0, ranks)  # High card

# Function to compare two hands
def compare_hands(hand1, hand2):
    eval1 = evaluate_hand(hand1)
    eval2 = evaluate_hand(hand2)
    if eval1 > eval2:
        return 1  # hand1 wins
    elif eval1 < eval2:
        return 2  # hand2 wins
    else:
        return 0  # tie

# Function to simulate a game
def simulate_game(user_hand):
    # Randomly generate a hand for the computer
    computer_hand = random.sample(DECK, 2)
    # Deal 5 community cards
    community_cards = random.sample([card for card in DECK if card not in user_hand + computer_hand], 5)
    # Combine hands with community cards
    user_full_hand = user_hand + community_cards
    computer_full_hand = computer_hand + community_cards
    # Determine the best 5 card hand for both players
    user_best_hand = max(combinations(user_full_hand, 5), key=evaluate_hand)
    computer_best_hand = max(combinations(computer_full_hand, 5), key=evaluate_hand)
    # Compare hands and determine winner
    return compare_hands(user_best_hand, computer_best_hand)

# Main function to run the simulation
def main():
    user_wins = 0
    computer_wins = 0
    ties = 0
    # Allow user to pick their hand
    user_hand = []
    while len(user_hand) < 2:
        card = input("Enter a card for your hand (e.g. 'AS' for Ace of Spades): ").upper()
        if card in DECK and card not in user_hand:
            user_hand.append(card)
        else:
            print("Invalid card. Please try again.")
    # Simulate 1000 games
    for _ in range(10000):
        result = simulate_game(user_hand)
        if result == 1:
            user_wins += 1
        elif result == 2:
            computer_wins += 1
        else:
            ties += 1
    # Print results
    print(f"User wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Ties: {ties}")
    print(f"User win rate: {user_wins / 10000:.2%}")

# testing the code
if __name__ == "__main__":
    main()