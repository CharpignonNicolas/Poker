import pygame
import sys
#from pot import Pot  # Assurez-vous que ce fichier existe et est correct


# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

# Initialisation de pygame
pygame.init()
font = pygame.font.Font(None, 36)

class BettingRound:
    def __init__(self, players, pot, initial_bet=0):
        self.players = players
        self.pot = pot
        self.current_bet = initial_bet
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Poker Game")

    def draw_button(self, text, rect):
        pygame.draw.rect(self.screen, gray, rect)
        text_surface = font.render(text, True, black)
        self.screen.blit(text_surface, (rect.x + 10, rect.y + 10))

    def check_player_status(self):
        for player in self.players:
            if not player.in_game:
                print(f"{player.name} folded. {player.name} loses.")
                sys.exit()

        if all(player.status == "check" for player in self.players if player.in_game):
            print("All players checked. End of the betting round.")
            return True

        if all(player.status == "fold" for player in self.players if player.in_game):
            print("All players folded. End of the betting round.")
            return True

        if any(player.status in ["bet", "raise"] for player in self.players if player.in_game):
            for player in self.players:
                if player.status in ["call", "raise", "fold"]:
                    continue
                if player.status == "bet":
                    for other_player in self.players:
                        if other_player != player and other_player.in_game:
                            return False
        return False

    def handle_action(self, player, action):
        if action == "call":
            player.call(self.current_bet)
            self.pot.add(self.current_bet)
            player.status = "call"
        elif action == "raise":
            amount = 10  # Vous pouvez adapter pour obtenir l'entrée de l'utilisateur via l'interface
            player.raise_bet(self.current_bet + amount)
            self.pot.add(self.current_bet + amount)
            self.current_bet += amount
            player.status = "raise"
        elif action == "fold":
            player.fold()
            player.status = "fold"

    def betting_round(self):
        buttons = {
            "bet": pygame.Rect(50, 500, 100, 50),
            "check": pygame.Rect(200, 500, 100, 50),
            "fold": pygame.Rect(350, 500, 100, 50),
            "call": pygame.Rect(500, 500, 100, 50),
            "raise": pygame.Rect(650, 500, 100, 50)
        }

        current_player_index = 0

        while True:
            self.screen.fill(white)

            for button_text, button_rect in buttons.items():
                self.draw_button(button_text, button_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button_text, button_rect in buttons.items():
                        if button_rect.collidepoint(event.pos):
                            current_player = self.players[current_player_index]
                            self.handle_action(current_player, button_text)
                            current_player_index = (current_player_index + 1) % len(self.players)
                            if self.check_player_status():
                                return

            pygame.display.flip()

    def reset(self):
        self.reset_current_bet()
        self.reset_players_current_bets()
        self.reset_players_in_game()
        self.reset_pot()
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
