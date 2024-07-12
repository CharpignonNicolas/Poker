import pygame
import sys
from Assets import *

pygame.init()

# Configuration de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Poker Game")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

class InputBox:
    def __init__(self, x, y, width, height, text='', action=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = pygame.Color('white')
        self.color_active = pygame.Color('yellow')
        self.color = self.color_inactive
        self.text = text
        self.action = action
        self.txt_surface = font.render(text, True, pygame.Color('black'))
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = font.render(self.text, True, pygame.Color('black'))
    
    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, pygame.Color('black'), self.rect, 2)

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, 36)
        self.txt_surface = self.font.render(text, True, pygame.Color('black'))
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_rect = self.txt_surface.get_rect(center=self.rect.center)
        screen.blit(self.txt_surface, text_rect)
    
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

def get_user_action():
    input_box_bet = InputBox(200, 100, 100, 50, '', 'bet')
    input_box_raise = InputBox(200, 200, 100, 50, '', 'raise')
    button_check = Button(50, 300, 100, 50, "Check", pygame.Color('green'), "check")
    button_fold = Button(50, 400, 100, 50, "Fold", pygame.Color('red'), "fold")
    button_call = Button(50, 500, 100, 50, "Call", pygame.Color('blue'), "call")

    input_boxes = [input_box_bet, input_box_raise]
    buttons = [button_check, button_fold, button_call]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for box in input_boxes:
                result = box.handle_event(event)
                if result is not None:
                    return box.action, result

            for button in buttons:
                if button.is_clicked(event):
                    return button.action, None

        screen.fill((0, 105, 0))  # Fond vert foncé

        for box in input_boxes:
            box.update()
            box.draw(screen)

        for button in buttons:
            button.draw(screen)

        pygame.display.flip()
        clock.tick(30)

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
            print("All players checked. End of the betting round.")
            return True

        if all(player.status == "fold" for player in self.players if player.in_game):
            print("All players folded. End of the betting round.")
            return True

        return False
    
    def round(self):
        for player in self.players:
            if not player.in_game:
                continue
            while True:
                action, amount = get_user_action()
                try:
                    if action == "bet":
                        amount = int(amount)
                        player.bet(amount)
                        self.current_bet = amount
                        self.pot.add(amount)
                        player.status = "bet"
                        break
                    elif action == "check":
                        player.check()
                        player.status = "check"
                        break
                    elif action == "fold":
                        player.fold()
                        player.status = "fold"
                        break
                    elif action == "call":
                        player.call(self.current_bet)
                        self.pot.add(self.current_bet)
                        player.status = "call"
                        break
                    elif action == "raise":
                        amount = int(amount)
                        player.raise_bet(self.current_bet + amount)
                        self.pot.add(self.current_bet + amount)
                        self.current_bet += amount
                        player.status = "raise"
                        break
                    else:
                        raise ValueError("Invalid action.")
                except ValueError as e:
                    print(e)
                    continue
            if self.check_player_status():
                break

        # Si un joueur a misé ou relancé
        if any(player.status in ["bet", "raise"] for player in self.players if player.in_game):
            for player in self.players:
                if player.status in ["call", "raise", "fold"]:
                    continue  # Passer les joueurs qui ont déjà pris une action appropriée
                if player.status == "bet":
                    for other_player in self.players:
                        if other_player != player and other_player.in_game:
                            while True:
                                action, amount = get_user_action()
                                try:
                                    if action == "call":
                                        other_player.call(self.current_bet)
                                        self.pot.add(self.current_bet)
                                        other_player.status = "call"
                                        break
                                    elif action == "raise":
                                        amount = int(amount)
                                        other_player.raise_bet(self.current_bet + amount)
                                        self.pot.add(self.current_bet + amount)
                                        self.current_bet += amount
                                        other_player.status = "raise"
                                        break
                                    elif action == "fold":
                                        other_player.fold()
                                        other_player.status = "fold"
                                        break
                                    else:
                                        raise ValueError("Invalid action.")
                                except ValueError as e:
                                    print(e)
                                    continue
                    return False

        return False

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

from Players.player import Player
from dealer import Dealer
from pot import Pot
from Rounds.pre_flop import PreFlop
from Rounds.flop import Flop
from Rounds.turn import Turn
from Rounds.river import River
from Actions.main_evaluator import evaluate_hand, compare_hands

class Party:
    def __init__(self, player_names, initial_stack=1000):
        self.players = [Player(name, initial_stack) for name in player_names]
        self.pot = Pot()
        self.dealer = Dealer()
    
    def start(self):
        preflop = PreFlop(self.dealer, self.players)
        print("Starting the game...")  # Ajout d'un message de débogage
        self.load_card_images()
        print("Cards loaded!")  # Ajout d'un message de débogage
        print("Preflop")
        self.display_hands()
        self.betting_round()
        self.check_player_status()

        flop = Flop(self.dealer)
        print("Flop")
        self.display_community_cards()
        self.betting_round()
        self.check_player_status()

        turn = Turn(self.dealer)
        print("Turn")
        self.display_community_cards()
        self.betting_round()
        self.check_player_status()

        river = River(self.dealer)
        print("River")
        self.display_community_cards()
        self.betting_round()
        self.check_player_status()

        self.evaluate_hands()
        self.compare_hands()
        
    def display_hands(self):
        screen.fill((0, 105, 0))  # Fond vert foncé pour l'affichage des cartes
        for i, player in enumerate(self.players):
            print(f"Displaying cards for {player.name}")  # Debug
            for j, card_image in enumerate(self.player_card_images[i]):
                print(f"Displaying card {j+1} for {player.name}")  # Debug
                if card_image:
                    screen.blit(card_image, (100 + j * 110, 100 + i * 170))
                else:
                    print(f"Card image not found for {player.name}, card {j+1}")  # Debug
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds to display the cards
        #print(self.pot)

    def display_community_cards(self):
        print(self.dealer.community_cards)
    
    def betting_round(self):
        betting_round = BettingRound(self.players, self.pot)
        betting_round.round()

    def check_player_status(self):
        active_players = [player for player in self.players if player.in_game]
        if len(active_players) == 0:
            print("All players folded. Game over.")
            exit()
        elif len(active_players) == 1:
            print(f"{active_players[0].name} wins!")
            exit()

    def evaluate_hands(self):
        for player in self.players:
            eval_hand = evaluate_hand(player.hand.cards, self.dealer.community_cards.cards)
            print(f"{player.name}'s hand: {eval_hand[1]} ({eval_hand[0]})")

    def compare_hands(self):
        player1, player2 = self.players
        winner = compare_hands(player1, player2, self.dealer.community_cards.cards)
        winner.chips += self.pot.amount
        print(f"{winner.name} wins!")

    def load_card_images(self):
        print("Loading card images...")  # Ajout d'un message de débogage

        def load_card_image(card):
            image_path = f'Assets/{card.image_name()}'
            try:
                image = pygame.image.load(image_path)
                print(f"Loaded image: {image_path}")  # Debug
                return image
            except pygame.error as e:
                print(f"Failed to load image {image_path}: {e}")
                return None

        self.player_card_images = []
        for player in self.players:
            player_images = []
            for card in player.hand.cards:
                img = load_card_image(card)
                if img is not None:
                    player_images.append(img)
            self.player_card_images.append(player_images)

        # Resize card images if necessary
        new_width, new_height = 100, 150
        self.player_card_images = [[pygame.transform.scale(img, (new_width, new_height)) for img in hand_images if img] for hand_images in self.player_card_images]

        # Debug: print player card images list
        for i, hand_images in enumerate(self.player_card_images):
            print(f"Player {i+1} card images: {hand_images}")

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def image_name(self):
        return f"{self.rank}_of_{self.suit}.png"

# Initialisation des joueurs et début de la partie
player_names = ["Player 1", "Player 2"]
game = Party(player_names)
game.start()
