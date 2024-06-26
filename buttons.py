import pygame

class Button:
    def __init__(self, x, y, w, h, color, text, action=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text
        self.action = action

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        txt_surface = font.render(self.text, True, (255, 255, 255))
        screen.blit(txt_surface, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, event):
        return self.rect.collidepoint(event.pos)

class InputBox:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = ''
        self.active = False

    def draw(self, screen, font):
        txt_surface = font.render(self.text, True, self.color)
        width = max(200, txt_surface.get_width() + 10)
        self.rect.w = width
        screen.fill((30, 30, 30), self.rect)
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
