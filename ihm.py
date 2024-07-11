import pygame
import sys
from party import Party

# Initialisation des joueurs et début de la partie
player_names = ["Player 1", "Player 2"]
game = Party(player_names)
game.start()

class Card:
    def __init__(self, image_path, position):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class PokerGame:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Poker Game")
        self.GREEN = (0, 255, 0)
        self.clock = pygame.time.Clock()
        
        # Charger les cartes avec des positions initiales
        self.cards = [
            Card('card1.png', (self.WIDTH // 2 - 100, self.HEIGHT // 2)),
            Card('card2.png', (self.WIDTH // 2, self.HEIGHT // 2)),
            Card('card3.png', (self.WIDTH // 2 + 100, self.HEIGHT // 2)),
        ]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.GREEN)
            
            # Dessiner les cartes
            for card in self.cards:
                card.draw(self.screen)
                
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


game = PokerGame()
game.run()
