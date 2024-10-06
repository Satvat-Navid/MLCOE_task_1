import pygame
from stats import Status

class Resources:
    """All the available resources in the shop"""
    def __init__(self, shop) -> None:
        self.screen = shop.screen
        self.screen_rect = self.screen.get_rect()
        self.shop = shop
        self.stats = Status()
        self.font = pygame.font.SysFont(None, 36)
        self.text_color = (0, 0, 255)
        self.profitBG_color = (255, 0, 0)
        self.waterBG_color = (0, 255, 0)
        self.coffeeBG_color = (255, 0, 0)
        self.prep_profit()
        self.prep_water()
        
    def check_veriable(self):
        if self.stats.profit != 0:
            self.profitBG_color = (0,255, 0)
            self.prep_profit()
        if self.stats.water < 400:
            self.waterBG_color = (255, 0, 0)
            self.prep_water()
        if self.stats.coffee:
            self.coffeeBG_color = (0, 255, 0)
            self.coffee_str = "Coffee IN"
            self.prep_coffee()
        else: 
            self.coffee_str = "NO Coffee"
            self.prep_coffee()


    def prep_profit(self):
        str1 = self.stats.profit
        value_str = "Profit : {:,}".format(str1)
        self.profit_image = self.font.render(value_str, True, self.text_color, self.profitBG_color)
        self.profit_rect = self.profit_image.get_rect()
        self.profit_rect.x = 10
        self.profit_rect.top = self.screen_rect.top + 10

    def prep_water(self):
        str2 = self.stats.water
        water_str = "Water : {:,}".format(str2)
        self.water_image = self.font.render(water_str, True, self.text_color, self.waterBG_color)
        self.water_rect = self.water_image.get_rect()
        self.water_rect.x = 10
        self.water_rect.top = self.profit_rect.bottom + 10
        
    def prep_coffee(self):
        self.coffee_image = self.font.render(self.coffee_str, True, self.text_color, self.coffeeBG_color)
        self.coffee_rect = self.coffee_image.get_rect()
        self.coffee_rect.x = 10
        self.coffee_rect.top = self.water_rect.bottom + 10

    def draw_resource(self):
        self.screen.blit(self.profit_image, self.profit_rect)
        self.screen.blit(self.water_image, self.water_rect)
        self.screen.blit(self.coffee_image, self.coffee_rect)
