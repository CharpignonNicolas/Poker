from deck import Deck
from community_cards import CommunityCards
from pot import Pot

# Definition of the Dealer class
class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.community_cards = CommunityCards()
        self.pot = Pot()

    def deal(self, player, num_cards):
        for _ in range(num_cards):
            player.hand.add_card(self.deck.draw())

    def burn(self):
        self.deck.draw()

    def add_community_card(self):
        self.community_cards.add_card(self.deck.draw())
        
    def award_pot(self, player):
        player.chips += self.pot.amount
        self.pot.reset()

    def __len__(self):
        return len(self.deck)
