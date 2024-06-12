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

        # Si tous les joueurs ont checké
        if all(player.status == "check" for player in self.players if player.in_game):
            print("All players checked. End of the betting round.")
            return True

        # Si tous les joueurs se sont couchés
        if all(player.status == "fold" for player in self.players if player.in_game):
            print("All players folded. End of the betting round.")
            return True

        # Si un joueur a misé ou relancé
        if any(player.status in ["bet", "raise"] for player in self.players if player.in_game):
            for player in self.players:
                if player.status in ["call", "raise", "fold"]:
                    continue  # Passer les joueurs qui ont déjà pris une action appropriée
                if player.status == "bet":
                    for other_player in self.players:
                        if other_player != player and other_player.in_game:
                            action = input(f"{other_player.name}, choose an action (call, raise, fold): ").lower()
                            if action == "call":
                                other_player.call(self.current_bet)
                                self.pot.add(self.current_bet)
                                other_player.status = "call"
                            elif action == "raise":
                                amount = int(input("Enter the raise amount: "))
                                other_player.raise_bet(self.current_bet+amount)
                                self.pot.add(self.current_bet + amount)
                                self.current_bet += amount
                                other_player.status = "raise"
                            elif action == "fold":
                                other_player.fold()
                                other_player.status = "fold"
                            else:     
                                raise ValueError("Invalid action.")
                    return False

        return False

    def round(self):
        for player in self.players:
            if not player.in_game:
                continue
            action = input(f"{player.name}, choose an action (bet, check, fold): ").lower()
            if action == "bet":
                amount = int(input("Enter the bet amount: "))
                player.bet(amount)
                self.current_bet = amount
                self.pot.add(amount)
                player.status = "bet"
                break
            elif action == "check":
                player.check()
                player.status = "check"
            elif action == "fold":
                player.fold()
                player.status = "fold"
            else:
                raise ValueError("Invalid action.")
            if self.check_player_status():
                break

        # Après la première action, vérifier les réponses des autres joueurs
        for player in self.players:
            if player.status in ["bet", "call", "raise", "fold"]:
                continue
            if self.check_player_status():
                break
            
        # Réinitialiser le statut des joueurs après la fin du tour de mise
        self.reset_players_status()

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
