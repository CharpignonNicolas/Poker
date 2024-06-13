# Definition of the Turn class
class Turn:
    def __init__(self, dealer):
        self.dealer = dealer
        self.deal_card()

    def deal_card(self):
        self.dealer.burn()
        self.dealer.add_community_card()
