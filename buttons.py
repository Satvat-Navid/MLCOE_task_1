import pygame

class Buttons:
    """Contain the funtionality of the buttons of the machine """
    def __init__(self, shop) -> None:
        self.shop = shop
        self.screen = shop.screen
        self.screen_rect = self.screen.get_rect()
        self.font_color = (0, 0, 255)
        self.coinBG_color = (255, 0, 0)
        self.milkBG_color = (255, 0, 0)
        self.sugerBG_color = (255, 0, 0)
        self.powerBG_color = (255, 0, 0)
        self.cupBG_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_coin()
        self.prep_milk()
        self.prep_suger()
        self.prep_power()
        self.prep_cup()

    def _check_BGcolor(self):
        if self.shop.state.coinIN > 0:
            self.coinBG_color = (0, 255, 0)
            self.prep_coin()
        if self.shop.state.coinIN < 0:
            self.coinBG_color = (255, 0, 0)
            self.prep_coin()

        if self.shop.state.milkIN > 0:
            self.milkBG_color = (0, 255, 0)
            self.prep_milk()
        if self.shop.state.milkIN < 0:
            self.milkBG_color = (255, 0, 0)
            self.prep_milk()

        if self.shop.state.sugerIN > 0:
            self.sugerBG_color = (0, 255, 0)
            self.prep_suger()
        if self.shop.state.sugerIN < 0:
            self.sugerBG_color = (255, 0, 0)
            self.prep_suger()

        if self.shop.state.coffeeIN > 0:
            self.powerBG_color = (0, 255, 0)
            self.prep_power()
        if self.shop.state.coffeeIN < 0:
            self.powerBG_color = (255, 0, 0)
            self.prep_power()

        if self.shop.state.cup_added > 0:
            self.cupBG_color = (0, 255, 0)
            self.prep_cup()
        if self.shop.state.cup_added < 0:
            self.cupBG_color = (255, 0, 0)
            self.prep_cup()

    def prep_coin(self):
        coin_str = "COIN"
        self.coin_image = self.font.render(coin_str, True, self.font_color, self.coinBG_color)
        self.coin_rect = self.coin_image.get_rect()
        self.coin_rect.right = self.screen_rect.right - 10
        self.coin_rect.top = self.screen_rect.top + 10

    def prep_milk(self):
        milk_str = "MILK"
        self.milk_image = self.font.render(milk_str, True, self.font_color, self.milkBG_color)
        self.milk_rect = self.milk_image.get_rect()
        self.milk_rect.right = self.screen_rect.right - 10
        self.milk_rect.top = self.coin_rect.bottom + 10
        
    def prep_suger(self):
        suger_str = "SUGER"
        self.suger_image = self.font.render(suger_str, True, self.font_color, self.sugerBG_color)
        self.suger_rect = self.suger_image.get_rect()
        self.suger_rect.right = self.screen_rect.right -10
        self.suger_rect.top = self.milk_rect.bottom + 10
        
    def prep_cup(self):
        cup_str = "ADD CUP"
        self.cup_image = self.font.render(cup_str, True, self.font_color, self.cupBG_color)
        self.cup_rect = self.cup_image.get_rect()
        self.cup_rect.right = self.screen_rect.right - 10
        self.cup_rect.top = self.suger_rect.bottom + 10
        
    def prep_power(self):
        power_str = "POWER"
        font = pygame.font.SysFont(None, 30)
        self.power_image = font.render(power_str, True, self.font_color, self.powerBG_color)
        self.power_rect = self.power_image.get_rect()
        self.power_rect.left = self.shop.machine.rect.left + 47
        self.power_rect.top = self.shop.machine.rect.top + 47

    def draw_buttons(self):
        self.screen.blit(self.coin_image, self.coin_rect)
        self.screen.blit(self.milk_image, self.milk_rect)
        self.screen.blit(self.suger_image, self.suger_rect)
        self.screen.blit(self.power_image, self.power_rect)