import sys
import pygame
from settings import Setting


class CoffeeMachine:
    """This represent the coffee machine and all functions"""
    def __init__(self):
        """It initialize the machine components and funtions"""
        pygame.init()
        self.settings = Setting(self)
        self.screen = pygame.display.set_mode(self.settings.display_height, self.settings.display_width)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("COFFEE MACHINE")

    def run_machine(self):
        """Loop for runing machine"""
        while True:
            pass
