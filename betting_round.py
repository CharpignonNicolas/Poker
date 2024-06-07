from pot import Pot

# Class to manage a betting round
class BettingRound:
    def __init__(self, players, pot, initial_bet=0):
        self.players = players
        self.pot = pot
        self.current_bet = initial_bet

    def round(self):
        for player in self.players:
            if player.in_game:
                action = input(f"{player.name}, choose an action (fold, check, bet, raise): ").lower()
                if action == "fold":
                    player.fold()
                elif action == "check":
                    player.check()
                elif action == "bet":
                    amount = int(input("Enter the bet amount: "))
                    player.bet(amount)
                    self.current_bet = amount
                    self.pot.add(amount)
                elif action == "raise":
                    amount = int(input("Enter the raise amount: "))
                    player.raise_bet(amount - player.current_bet)
                    self.current_bet = amount
                    self.pot.add(amount)
