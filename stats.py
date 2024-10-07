class Status:
    """All the variable of the shop"""
    def __init__(self, shop):
        self.machine_switch = False
        self.cup_added = 1
        self.coinIN = -1
        self.coffeeIN = 1
        self.milkIN = -1
        self.sugerIN = True
        self.profit = 100
        self.water = 600
        self.coffee = True