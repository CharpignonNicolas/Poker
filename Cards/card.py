import random

# Definition of the Card class
class Card:
    # The suits of the cards
    suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
    # The ranks of the cards (2-10, Jack, Queen, King, Ace)
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # 11: Jack, 12: Queen, 13: King, 14: Ace

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
