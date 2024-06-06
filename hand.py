# Definition of the Hand class
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def reset(self):
        self.cards = []

    def __repr__(self):
        return f"Hand: {self.cards}"
