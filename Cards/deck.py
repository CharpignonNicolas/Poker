from Cards.card import Card
import random

# Definition of the Deck class
class Deck:
    def __init__(self):
        # Create a deck of cards with all combinations of suits and ranks
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def __len__(self):
        return len(self.cards)
