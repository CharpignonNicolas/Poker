import pygame
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def reset(self):
        self.cards = []

    def __repr__(self):
        return f"Hand: {self.cards}"

    def load_card_image(self, card):
        image_path = f'Assets/{card.image_name()}'
        card_image = pygame.image.load(image_path)
        self.card_images.append(card_image)

    def draw(self, screen, x, y):
        for i, card_image in enumerate(self.card_images):
            screen.blit(card_image, (x + i * 30, y))