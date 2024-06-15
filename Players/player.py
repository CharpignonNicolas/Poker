from Players.hand import Hand

# Definition of the Player class
class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = Hand()
        self.in_game = True
        self.status = None
        self.current_bet = 0

    def __repr__(self):
        return f"{self.name} - Main: {self.hand}, Jetons: {self.chips}"

    def bet(self, amount):
        if amount <= self.chips:
            self.chips -= amount
            self.current_bet += amount
        else:
            raise ValueError("Pas assez de jetons pour miser cette somme.")

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

    def status(self):
        return self.status