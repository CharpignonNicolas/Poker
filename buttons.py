import pygame

class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

    def get_action(self):
        if self.text == "Check":
            return "check"
        elif self.text == "Fold":
            return "fold"
        elif self.text == "Call":
            return "call"
        return None
