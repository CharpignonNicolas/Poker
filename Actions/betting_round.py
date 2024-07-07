import pygame
from buttons import Button
from pot import Pot

class BettingRound:
    def __init__(self, players, pot, screen, font, buttons, initial_bet=0):
        self.players = players
        self.pot = pot
        self.current_bet = initial_bet
        self.screen = screen
        self.font = font
        self.buttons = buttons

    def handle_bet_event(self, player):
        amount = int(input("Enter the bet amount: "))  # Replace with your input method
        player.bet(amount)
        self.current_bet = amount
        self.pot.add(amount)
        player.status = "bet"

    def handle_call_event(self, player):
        player.call(self.current_bet)
        self.pot.add(self.current_bet)
        player.status = "call"

    def handle_buttons_event(self, event, player):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.is_clicked(event):
                    if button.text == "Raise":
                        amount = int(input("Enter the raise amount: "))  # Replace with your input method
                        player.raise_bet(self.current_bet + amount)
                        self.pot.add(self.current_bet + amount)
                        self.current_bet += amount
                        player.status = "raise"
                    elif button.text == "Check":
                        player.check()
                        player.status = "check"
                    elif button.text == "Fold":
                        player.fold()
                        player.status = "fold"
                    elif button.text == "Bet":
                        self.handle_bet_event(player)
                    elif button.text == "Call":
                        self.handle_call_event(player)
                    return True
        return False

    def draw_current_player(self, player):
        # Draw the current player's name on the screen
        player_text = self.font.render(f"Current Player: {player.name}", True, (255, 255, 255))
        self.screen.blit(player_text, (10, 10))

    def round(self):
        for player in self.players:
            if not player.in_game:
                continue
            action_taken = False
            while not action_taken:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    action_taken = self.handle_buttons_event(event, player)

                # Draw buttons and current player
                self.screen.fill((0, 105, 0))
                self.draw_current_player(player)
                for button in self.buttons:
                    button.draw(self.screen, self.font)
                pygame.display.flip()

            if self.check_player_status():
                break

        # Check status for other players
        for player in self.players:
            if player.status in ["bet", "call", "raise", "fold"]:
                continue
            if self.check_player_status():
                break

        # Reset player statuses after betting round
        self.reset_players_status()

    def check_player_status(self):
        active_players = [player for player in self.players if player.in_game]
        if len(active_players) == 0:
            print("All players folded. Game over.")
            pygame.quit()
            exit()
        elif len(active_players) == 1:
            print(f"{active_players[0].name} wins!")
            pygame.quit()
            exit()
        
        # Check if all active players have checked
        if all(player.status == "check" for player in active_players):
            print("All players checked. End of the betting round.")
            return True

        # Check if all active players have either called or checked
        if all(player.status in ["check", "call"] for player in active_players):
            print("All players have either called or checked. End of the betting round.")
            return True
        
        return False

    def reset_players_status(self):
        for player in self.players:
            player.status = None

    def reset(self):
        self.current_bet = 0
        self.reset_players_status()
