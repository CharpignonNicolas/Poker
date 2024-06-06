# Definition of the River class
class River:
    def __init__(self, dealer):
        self.dealer = dealer
        self.deal_card()

    def deal_card(self):
        self.dealer.burn()
        self.dealer.add_community_card()
