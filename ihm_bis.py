import pygame
import pygame.font
from buttons import Button  # Import the Button class from buttons.py
from Actions.betting_round import BettingRound  # Assume BettingRound is modified to work with buttons
from inputBox import InputBox  # Import the InputBox class
from pot import Pot
from party import Party

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Poker Game")
GREEN = (0, 105, 0)

# Set up fonts
font = pygame.font.Font(None, 32)
if font is None:
    print("Font initialization failed")

# Create buttons
"""
button_check = Button(250, 500, 100, 50, (0, 255, 0), "Check")
button_fold = Button(400, 500, 100, 50, (255, 0, 0), "Fold")
button_call = Button(700, 500, 100, 50, (0, 0, 255), "Call")

buttons = [button_check, button_fold, button_call]  # Only add the buttons here

# Création des InputBox pour Bet et Raise
input_box_bet = InputBox(100, 500, 100, 50, '')
input_box_bet.get_action("Bet")  # Définition de l'action associée à Bet

input_box_raise = InputBox(550, 500, 100, 50, '')
input_box_raise.get_action("Raise")  # Définition de l'action associée à Raise

# Liste des InputBox
input_boxes = [input_box_bet, input_box_raise]
"""

# Create the Party instance
player_names = ["Player 1", "Player 2"]
party = Party(player_names, screen, font)  # Pass the buttons and input boxes to the Party
print(f"Party Screen: {party.screen}, Party Font: {party.font}")  # Debugging line

# Start the game
party.start()

# Function to load card images
"""
def load_card_image(card):
    image_path = f'Assets/{card.image_name()}'
    return pygame.image.load(image_path)

# Load player card images
player_card_images = []
for player in party.players:
    player_card_images.append([load_card_image(card) for card in player.hand.cards])

# Resize card images if necessary
new_width, new_height = 100, 150
player_card_images = [[pygame.transform.scale(img, (new_width, new_height)) for img in hand_images] for hand_images in player_card_images]
"""
# Game loop
running = True
while running:
    screen.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN:
            # Handle events in BettingRound
            betting_round.handle_buttons_event(event)
            betting_round.handle_input_boxes_event(event)

    pygame.display.flip()

# Quit Pygame
pygame.quit()