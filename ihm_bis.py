import pygame
import pygame.font
from buttons import Button  # Import the Button class from buttons.py
from Actions.betting_round import BettingRound  # Assume BettingRound is modified to work with buttons
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
button_raise = Button(100, 500, 100, 50, (0, 255, 0), "Raise")
button_check = Button(250, 500, 100, 50, (0, 255, 0), "Check")
button_fold = Button(400, 500, 100, 50, (255, 0, 0), "Fold")
button_bet = Button(550, 500, 100, 50, (255, 255, 0), "Bet") 

buttons = [button_raise, button_check, button_fold, button_bet]  
# Ajout du bouton Bet à la liste

# Create the Party instance
player_names = ["Player 1", "Player 2"]
party = Party(player_names, screen, font, buttons)  # Pass the buttons to the Party
print(f"Party Screen: {party.screen}, Party Font: {party.font}")  # Debugging line

# Start the game
party.start()

# Game loop
running = True
while running:
    # Fill the background
    screen.fill(GREEN)

    # Draw buttons
    for button in buttons:
        button.draw(screen, font)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Pass events to the Party instance
        party.handle_event(event)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()