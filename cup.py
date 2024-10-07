import pygame
from stats import Status

class Cup:
    """Represent the coffee cup and its funtions"""
    def __init__(self, shop) -> None:
        self.shop = shop
        self.state = Status()
        self.screen = shop.screen
        self.screen_rect = self.screen.get_rect
        self._check_cup()
        self.rect = self.image.get_rect()
        self.rect.x = self.shop.machine.rect.x + 120
        self.rect.y = self.shop.machine.rect.y + 160

    

    def _check_cup(self):
        if self.state.coffeeIN > 0:
            self.image = pygame.image.load("images/cup_coffee.png")
        elif self.state.milkIN > 0:
            self.image = pygame.image.load("images/cup_milk.png")
        else :
            self.image = pygame.image.load("images/cup_empty.png")


    def draw_cup(self):
        self.screen.blit(self.image, self.rect)