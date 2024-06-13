# Definition of the PreFlop class
class PreFlop:
    def __init__(self, dealer, players):
        self.dealer = dealer
        self.players = players
        self.deal_cards()

    def deal_cards(self):
        for player in self.players:
            self.dealer.deal(player, 2)
