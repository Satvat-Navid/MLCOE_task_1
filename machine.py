import pygame

class Machine:
    """Funtionality of the coffee machine"""
    def __init__(self, shop):
        self.screen = shop.screen
        self.settings = shop.settings
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/machine.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = (1/6)*(self.settings.display_width)
        self.rect.y = (1/3)*(self.settings.display_height)
        self.draw_bg()

    def draw_bg(self):
        self.screen.blit(self.image, self.rect)