import pygame
import pygame.font
from party import Party
from buttons import Button, InputBox

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Screen")
GREEN = (0, 105, 0)

"""player_names = ["Player 1", "Player 2"]
game = Party(player_names)
game.start()

# Fonction pour charger les images des cartes
def load_card_image(card):
    image_path = f'Assets/{card.image_name()}'
    return pygame.image.load(image_path)

# Charger les images des cartes des joueurs
player_card_images = []
for player in game.players:
    player_card_images.append([load_card_image(card) for card in player.hand.cards])

# Redimensionner les images des cartes si nécessaire
new_width, new_height = 100, 150
player_card_images = [[pygame.transform.scale(img, (new_width, new_height)) for img in hand_images] for hand_images in player_card_images]
"""

# Set up fonts
font = pygame.font.Font(None, 32)

# Create buttons
button1 = Button(100, 200, 200, 50, (0, 255, 0), "Button 1")
button2 = Button(500, 200, 200, 50, (255, 0, 0), "Button 2")
input_box = InputBox(300, 300, 200, 50)

# Game loop
running = True
while running:
    # Dessin du fond
    screen.fill(GREEN)

    # Draw buttons and input box
    button1.draw(screen, font)
    button2.draw(screen, font)
    input_box.draw(screen, font)
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.is_clicked(event):
                print("Button 1 clicked")
            elif button2.is_clicked(event):
                print("Button 2 clicked")
        input_box.handle_event(event)

    """# Afficher les cartes des joueurs
    for player_index, hand_images in enumerate(player_card_images):
        for card_index, img in enumerate(hand_images):
            screen.blit(img, (50 + card_index * (new_width + 10), 50 + player_index * (new_height + 10)))"""
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
