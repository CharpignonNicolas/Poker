import pygame
import sys
import time
from party import Party
from Actions.betting_round import BettingRound
from pot import Pot
from Players.player import Player


# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
WIDTH, HEIGHT = 1280, 720
GREEN = (0, 105, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nom de votre jeu")

# Création de la ronde de mise
players = [Player("Player 1"), Player("Player 2")]
pot = Pot()
round = BettingRound(players, pot)

# Lancer la ronde de mise
round.betting_round()

player_names = ["Player 1", "Player 2"]
game = Party(player_names)
game.start()
game.test()
game.test2()
game.test3()

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

#charger les images des community cards
community_card_images = []
for card in game.dealer.community_cards.cards:  
    community_card_images.append(load_card_image(card))

# Redimensionner les images des cartes si nécessaire
community_card_images = [pygame.transform.scale(img, (new_width, new_height)) for img in community_card_images]

# Boucle de jeu Pygame
running = True
clock = pygame.time.Clock()
stage_time = time.time()
stage_duration = 5  # Durée de chaque étape en secondes

while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessin du fond
    screen.fill(GREEN)

    # Afficher les cartes des joueurs
    for player_index, hand_images in enumerate(player_card_images):
        for card_index, img in enumerate(hand_images):
            screen.blit(img, (50 + card_index * (new_width + 10), 50 + player_index * (new_height + 10)))

    # Afficher les cartes de la communauté
    for card_index, img in enumerate(community_card_images):
        screen.blit(img, (50 + card_index * (new_width + 10), 300))


    # Mise à jour de l'écran
    pygame.display.flip()

    # Limiter le taux de rafraîchissement
    clock.tick(30)

# Quitter Pygame proprement
pygame.quit()
sys.exit()
