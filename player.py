from hand import Hand

# Definition of the Player class
class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = Hand()
        self.in_game = True
        self.current_bet = 0

    def __repr__(self):
        return f"{self.name} - Hand: {self.hand}, Chips: {self.chips}"

    def bet(self, amount):
        if amount <= self.chips:
            self.chips -= amount
            self.current_bet += amount
        else:
            raise ValueError("Not enough chips to bet this amount.")

    def call(self, amount):
        self.bet(amount)

    def raise_bet(self, amount):
        self.bet(amount)

    def fold(self):
        self.in_game = False
        
    def all_in(self):
        self.chips = 0
        
    def check(self):
        pass
