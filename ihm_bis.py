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
button_check = Button(250, 500, 100, 50, (0, 255, 0), "Check")
button_fold = Button(400, 500, 100, 50, (255, 0, 0), "Fold")
button_call = Button(700, 500, 100, 50, (0, 0, 255), "Call")

buttons = [button_check, button_fold, button_call]  # Only add the buttons here

# Create input boxes for Bet and Raise
input_box_bet = InputBox(100, 500, 100, 50, '')
input_box_bet.action = "Bet"
input_box_raise = InputBox(550, 500, 100, 50, '')
input_box_raise.action = "Raise"

input_boxes = [input_box_bet, input_box_raise]

# Create the Party instance
player_names = ["Player 1", "Player 2"]
party = Party(player_names, screen, font, buttons, input_boxes)  # Pass the buttons and input boxes to the Party
print(f"Party Screen: {party.screen}, Party Font: {party.font}")  # Debugging line

# Start the game
party.start()

    # Fonction pour charger les images des cartes
def load_card_image(card):
    image_path = f'Assets/{card.image_name()}'
    return pygame.image.load(image_path)

# Charger les images des cartes des joueurs
player_card_images = []
for player in party.players:
    player_card_images.append([load_card_image(card) for card in player.hand.cards])

# Redimensionner les images des cartes si nécessaire
new_width, new_height = 100, 150
player_card_images = [[pygame.transform.scale(img, (new_width, new_height)) for img in hand_images] for hand_images in player_card_images]

# Game loop
running = True
while running:
    # Fill the background
    screen.fill(GREEN)

        # Afficher les cartes des joueurs
    for player_index, hand_images in enumerate(player_card_images):
        for card_index, img in enumerate(hand_images):
            screen.blit(img, (50 + card_index * (new_width + 10), 50 + player_index * (new_height + 10)))


    # Draw buttons
    for button in buttons:
        button.draw(screen, font)

    # Draw input boxes
    for box in input_boxes:
        box.draw(screen)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Pass events to the Party instance
        party.handle_event(event)

    # Update the display
    pygame.display.flip()

# Quit Pygame
