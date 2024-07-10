import pygame
from buttons import Button
from inputBox import InputBox
from pot import Pot

class BettingRound:
    def __init__(self, players, pot, screen, font, initial_bet=0):
        self.players = players
        self.pot = pot
        self.current_bet = initial_bet
        self.screen = screen
        self.buttons = [
            Button(250, 500, 100, 50, (0, 255, 0), "Check"),
            Button(400, 500, 100, 50, (255, 0, 0), "Fold"),
            Button(700, 500, 100, 50, (0, 0, 255), "Call")
        ]
        self.input_box_bet = InputBox(100, 500, 100, 50, 'Bet 0')
        self.input_box_raise = InputBox(550, 500, 100, 50, 'Raise 0')

    def handle_buttons_event(self, event):
        for button in self.buttons:
            if button.is_clicked(event):
                action = button.get_action()
                if action == "check":
                    print("Player checks.")
                    # Handle check logic
                elif action == "fold":
                    print("Player folds.")
                    # Handle fold logic
                elif action == "call":
                    print("Player calls.")
                    # Handle call logic

    def handle_input_boxes_event(self, event):
        action_bet, amount_bet = self.input_box_bet.handle_event(event)
        if action_bet == "bet":
            print(f"Player bets {amount_bet}.")
            # Handle bet logic

        action_raise, amount_raise = self.input_box_raise.handle_event(event)
        if action_raise == "raise":
            print(f"Player raises to {amount_raise}.")
            # Handle raise logic

    def update(self):
        self.input_box_bet.update()
        self.input_box_raise.update()

    def draw(self):
        for button in self.buttons:
            button.draw(self.screen, self.font)
        self.input_box_bet.draw(self.screen)
        self.input_box_raise.draw(self.screen)

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
        
        if all(player.status == "check" for player in active_players):
            print("All players checked. End of the betting round.")
            return True

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
                    self.handle_input_boxes_event(event)
                    self.handle_custom_events(event)  # Gérer les événements personnalisés ici

                self.screen.fill((0, 105, 0))
                self.draw_current_player(player)
                for button in self.buttons:
                    button.draw(self.screen, self.font)
                for box in self.inputBoxes:
                    box.draw(self.screen)
                pygame.display.flip()

            if self.check_player_status():
                break

        for player in self.players:
            if player.status in ["bet", "call", "raise", "fold"]:
                continue
            if self.check_player_status():
                break

        self.reset_players_status()
