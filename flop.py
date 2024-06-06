# Definition of the Flop class
class Flop:
    def __init__(self, dealer):
        self.dealer = dealer
        self.deal_cards()

    def deal_cards(self):
        self.dealer.burn()
        for _ in range(3):
            self.dealer.add_community_card()
