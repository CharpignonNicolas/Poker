import pygame
from buttons import Button
from inputBox import InputBox
from pot import Pot

class BettingRound:
    def __init__(self, players, pot, screen, font, buttons, inputBox, initial_bet=0):
        self.players = players
        self.pot = pot
        self.current_bet = initial_bet
        self.screen = screen
        self.font = font
        self.buttons = buttons
        self.inputBox = inputBox

    def handle_bet_event(self, player, amount):
        player.bet(amount)
        self.current_bet = amount
        self.pot.add(amount)
        player.status = "bet"

    def handle_raise_event(self, player, amount):
        player.raise_bet(self.current_bet + amount)
        self.pot.add(self.current_bet + amount)
        self.current_bet += amount
        player.status = "raise"

    def handle_call_event(self, player):
        player.call(self.current_bet)
        self.pot.add(self.current_bet)
        player.status = "call"

    def handle_buttons_event(self, event, player):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.is_clicked(event):
                    if button.text == "Raise":
                        amount = self.get_input_box_value("Raise")
                        self.handle_raise_event(player, amount)
                    elif button.text == "Check":
                        player.check()
                        player.status = "check"
                    elif button.text == "Fold":
                        player.fold()
                        player.status = "fold"
                    elif button.text == "Bet":
                        amount = self.get_input_box_value("Bet")
                        self.handle_bet_event(player, amount)
                    elif button.text == "Call":
                        self.handle_call_event(player)
                    return True
        return False

    def handle_input_boxes_event(self, event):
        for box in self.inputBox:
            box.handle_event(event)

    def get_input_box_value(self, action):
        for box in self.inputBox:
            if box.action == action:
                return int(box.text) if box.text.isdigit() else 0
        return 0

    def draw_current_player(self, player):
        # Draw the current player's name on the screen
        player_text = self.font.render(f"Current Player: {player.name}", True, (255, 255, 255))
        self.screen.blit(player_text, (10, 10))

    def update_buttons_and_inputs(self, actions):
        self.buttons = [button for button in self.buttons if button.text in actions]
        self.inputBox = [box for box in self.inputBox if box.action in actions]

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
                    self.handle_input_boxes_event(event)

                # Draw buttons, input boxes, and current player
                self.screen.fill((0, 105, 0))
                self.draw_current_player(player)
                for button in self.buttons:
                    button.draw(self.screen, self.font)
                for box in self.inputBox:
                    box.draw(self.screen)
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
