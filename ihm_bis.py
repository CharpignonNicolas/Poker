import pygame
from party import Party
from buttons import Button, InputBox


pygame.init()

WIDTH, HEIGHT = 800, 600
GREEN = (0, 105, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Poker")

font = pygame.font.Font(None, 32)

button1 = Button(100, 200, 200, 50, (0, 255, 0), "bet")
button2 = Button(500, 200, 200, 50, (255, 0, 0), "check")
button3 = Button(700, 200, 200, 50, (0, 255, 0), "fold")
input_box = InputBox(300, 300, 200, 50)

def handle_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button1.is_clicked(event):
            print("bet")
            return "bet"
        elif button2.is_clicked(event):
            return "check"
        elif button3.is_clicked(event):
            return "fold"
        else:
            return input_box.handle_event(event)

player_names = ["Player 1", "Player 2"]
game = Party(player_names)
game.start()

running = True

while running:

    screen.fill(GREEN)

    button1.draw(screen, font)
    button2.draw(screen, font)
    button3.draw(screen, font)
    input_box.draw(screen, font)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        handle_event(event)
    
    pygame.display.flip()

pygame.quit()