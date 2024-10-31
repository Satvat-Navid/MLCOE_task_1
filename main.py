import sys
import pygame
from settings import Setting
from machine import Machine
from cup import Cup
from resourses import Resources
from buttons import Buttons
from stats import Status


class Shop:
    """This represent the shop and all its functions"""
    def __init__(self):
        """It initialize the machine components and funtions"""
        pygame.init()
        self.settings = Setting(self)
        self.screen = pygame.display.set_mode((self.settings.display_width, self.settings.display_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("COFFEE SHOP")
        self.state = Status(self)
        self.machine = Machine(self)
        self.cup = Cup(self)
        self.buttons = Buttons(self)
        self.reso = Resources(self)

    def run_machine(self):
        """Loop for runing machine"""
        while True:
            self._check_events()
            self.reso.check_veriable()
            self.cup._check_cup()
            self.buttons._check_BGcolor()
            self._update_screen()
            

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse = pygame.mouse.get_pos()
                self.click(self.mouse)

    def click(self, mouse):
        if self.buttons.coin_rect.collidepoint(mouse):
            self.state.coinIN = (-1)*(self.state.coinIN)

        if self.buttons.milk_rect.collidepoint(mouse):
            self.state.milkIN = (-1)*(self.state.milkIN)

        if self.buttons.suger_rect.collidepoint(mouse):
            self.state.sugerIN = (-1)*(self.state.sugerIN)
        
        if self.buttons.power_rect.collidepoint(mouse) and self.state.cup_added > 0:
            self.state.coffeeIN = (-1)*(self.state.coffeeIN)
            if self.state.coffeeIN == 1 and self.state.water > 0:
                self.state.profit += 50
                self.state.water -= 100
                self.reso.prep_water()
        
        if self.buttons.cup_rect.collidepoint(mouse) and self.state.coinIN > 0:
            self.state.cup_added = (-1)*(self.state.cup_added)
            # self.state.coinIN = -1
        

    def _keydown_event(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP and self.state.water < 1000:
            self.state.water += 100
            self.reso.prep_water()
        elif event.key == pygame.K_DOWN and self.state.water > 0:
            self.state.water -= 100
            self.reso.prep_water()

    def _keyup_event(self, event):
        pass

    def cup_available(self):
        pass

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.machine.draw_bg()
        self.reso.draw_resource()
        self.buttons.draw_buttons()
        if self.state.coinIN > 0:
            self.screen.blit(self.buttons.cup_image, self.buttons.cup_rect)
        if self.state.cup_added > 0:
            self.cup.draw_cup()
        pygame.display.flip()

if __name__ == "__main__":
    """Make the machine instance and run the machine"""
    shop = Shop()
    shop.run_machine()