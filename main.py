import sys
import pygame
from settings import Setting
from machine import Machine
from resourses import Resources


class Shop:
    """This represent the shop and all its functions"""
    def __init__(self):
        """It initialize the machine components and funtions"""
        pygame.init()
        self.settings = Setting(self)
        self.screen = pygame.display.set_mode((self.settings.display_width, self.settings.display_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("COFFEE SHOP")
        self.machine = Machine(self)
        self.reso = Resources(self)

    def run_machine(self):
        """Loop for runing machine"""
        while True:
            self._check_events()
            self.reso.check_veriable()
            self._update_screen()
            

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._keyup_event(event)

    def _keydown_event(self, event):
        
        pass

    def _keyup_event(self, event):
        pass

    def _update_screen(self):
        self.machine.draw_bg()
        self.reso.draw_resource()
        pygame.display.flip()

if __name__ == "__main__":
    """Make the machine instance and run the machine"""
    shop = Shop()
    shop.run_machine()