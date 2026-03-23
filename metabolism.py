class Metabolism:
    def __init__(self):
        self.hunger = 100  # 100 means full, 0 means starving
        self.thirst = 100  # 100 means hydrated, 0 means dehydrated
        self.health = 100   # 100 means healthy, 0 means deceased
        self.loneliness = 0  # 0 means not lonely, 100 means very lonely

    def update_hunger(self, amount):
        self.hunger = max(0, min(100, self.hunger - amount))

    def update_thirst(self, amount):
        self.thirst = max(0, min(100, self.thirst - amount))

    def update_health(self, amount):
        self.health = max(0, min(100, self.health + amount))

    def update_loneliness(self, amount):
        self.loneliness = max(0, min(100, self.loneliness + amount))

    def __str__(self):
        return f'Hunger: {self.hunger}, Thirst: {self.thirst}, Health: {self.health}, Loneliness: {self.loneliness}'
