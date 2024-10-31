class Status:
    """All the variable of the shop"""
    def __init__(self, shop):
        self.machine_switch = False
        self.coinIN = -1
        self.cup_added = -1
        self.coffeeIN = -1
        self.milkIN = -1
        self.sugerIN = True
        self.profit = 0
        self.water = 1000
        self.coffee = True