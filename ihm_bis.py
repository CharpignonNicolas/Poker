import pygame
import pygame.font
from party import Party

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Screen")
GREEN = (0, 105, 0)

player_names = ["Player 1", "Player 2"]
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


# Set up fonts
font = pygame.font.Font(None, 32)

# Button class
class Button:
    def __init__(self, x, y, w, h, color, text, action=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        txt_surface = font.render(self.text, True, (255, 255, 255))
        screen.blit(txt_surface, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, event):
        return self.rect.collidepoint(event.pos)

# Input box class
class InputBox:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = ''
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        # Render the current text.
        txt_surface = font.render(self.text, True, self.color)
        width = max(200, txt_surface.get_width() + 10)
        self.rect.w = width
        # Blit the text.
        screen.fill((30, 30, 30), self.rect)
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

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
    button1.draw(screen)
    button2.draw(screen)
    input_box.draw(screen)
    
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

    # Afficher les cartes des joueurs
    for player_index, hand_images in enumerate(player_card_images):
        for card_index, img in enumerate(hand_images):
            screen.blit(img, (50 + card_index * (new_width + 10), 50 + player_index * (new_height + 10)))

    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
