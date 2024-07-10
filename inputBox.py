import pygame
import pygame.font

class InputBox:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 255, 255)
        self.text = text
        self.font = pygame.font.Font(None, 32)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return self.get_action()
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def get_action(self):
        action = self.text.split()[0].lower()  # Get the first word as action
        amount_str = self.text.split()[1] if len(self.text.split()) > 1 else '0'
        amount = int(amount_str) if amount_str.isdigit() else 0
        return action, amount

    def update(self):
        width = max(200, self.font.size(self.text)[0] + 10)
        self.rect.w = width

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
