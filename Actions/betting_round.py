from pot import Pot

class BettingRound:
    def __init__(self, players, pot, initial_bet=0):
        self.players = players
        self.pot = pot
        self.current_bet = initial_bet
        self.bets_matched = {player: False for player in players}

    def check_player_status(self):
        # Si tous les joueurs ont checké ou se sont couchés
        if all(player.status in ["check", "se coucher"] for player in self.players if player.in_game):
            print("Fin du tour de mise.")
            return True
        return False

    def player_action(self, player):
        if not player.in_game:
            return

        if self.current_bet == 0:
            action = input(f"{player.name}, choisissez une action (miser, check, se coucher): ").lower()
            if action == "miser":
                amount = int(input("Miser : "))
                player.bet(amount)
                self.current_bet = amount
                self.pot.add(amount)
                player.status = "miser"
                self.bets_matched[player] = True
            elif action == "check":
                player.check()
                player.status = "check"
                self.bets_matched[player] = True
            elif action == "se coucher":
                player.fold()
                player.status = "se coucher"
            else:
                raise ValueError("Invalid action.")
        else:
            action = input(f"{player.name}, choisissez une action (suivre, relancer, se coucher): ").lower()
            if action == "suivre":
                player.call(self.current_bet)
                self.pot.add(self.current_bet)
                player.status = "suivre"
                self.bets_matched[player] = True
            elif action == "relancer":
                amount = int(input("Relancer de : "))
                player.raise_bet(self.current_bet + amount)
                self.pot.add(self.current_bet + amount)
                self.current_bet += amount
                player.status = "relancer"
                # Reset the matched bets as there's a new raise
                for p in self.players:
                    if p != player:
                        self.bets_matched[p] = False
                self.bets_matched[player] = True
            elif action == "se coucher":
                player.fold()
                player.status = "se coucher"
            else:
                raise ValueError("Invalid action.")

    def round(self):
        # Loop until all active players have matched the current bet
        while not all(self.bets_matched[player] or not player.in_game for player in self.players):
            for player in self.players:
                if not player.in_game or self.bets_matched[player]:
                    continue
                self.player_action(player)
                if self.check_player_status():
                    return

        # Réinitialiser le statut des joueurs après la fin du tour de mise
        self.reset_players_status()
        self.reset_bets_matched()

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

    def reset_bets_matched(self):
        self.bets_matched = {player: False for player in self.players}

    def reset(self):
        self.reset_current_bet()
        self.reset_players_current_bets()
        self.reset_players_in_game()
        self.reset_pot()
        self.reset_players_status()
        self.reset_bets_matched()
