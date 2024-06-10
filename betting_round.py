from pot import Pot

class BettingRound:
    def __init__(self, players, pot, initial_bet=0):
        self.players = players
        self.pot = pot
        self.current_bet = initial_bet

    def check_player_status(self):
        for player in self.players:
            if not player.in_game:
                print(f"{player.name} folded. {player.name} loses.")
                exit()

        if all(player.status == "check" for player in self.players if player.in_game):
            print("Both players checked. End of the betting round.")
            return True
        if all(player.status == "fold" for player in self.players if player.in_game):
            print("Both players folded. End of the betting round.")
            return True

        if any(player.status == "bet" for player in self.players if player.in_game):
            for player in self.players:
                if player.status == "bet":
                    continue
                player.status = input(f"{player.name}, choose an action (call, raise, fold): ").lower()
                if player.status == "call":
                    player.call(self.current_bet - player.current_bet)
                    self.pot.add(self.current_bet - player.current_bet)
                elif player.status == "raise":
                    amount = int(input("Enter the raise amount: "))
                    player.raise_bet(amount)
                    self.current_bet = amount
                    self.pot.add(amount)
                elif player.status == "fold":
                    player.fold()
                else:
                    raise ValueError("Invalid action.")
            return False
        return False

    def round(self):
        for player in self.players:
            if not player.in_game:
                continue
            player.status = input(f"{player.name}, choose an action (bet, check, fold): ").lower()
            if player.status == "bet":
                amount = int(input("Enter the bet amount: "))
                player.bet(amount)
                self.current_bet = amount
                self.pot.add(amount)
                break
            elif player.status == "check":
                player.check()
            elif player.status == "fold":
                player.fold()
            else:
                raise ValueError("Invalid action.")
            if self.check_player_status():
                break

        # After the first player has made a move, check for other players' responses
        for player in self.players:
            if player.status == "bet":
                continue
            self.check_player_status()
            if self.check_player_status():
                break

    def reset_current_bet(self):
        self.current_bet = 0

    def reset_players_current_bets(self):
        for player in self.players:
            player.current_bet = 0

    def reset_players_in_game(self):
        for player in self.players:
            player.in_game = True
            
    def reset_players_status(self):
        for player in self.players:
            player.status = None

    def reset_pot(self):
        self.pot.reset()

    def reset(self):
        self.reset_current_bet()
        self.reset_players_current_bets()
        self.reset_players_in_game()
        self.reset_pot()
        self.reset_players_status()
