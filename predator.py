class Predator:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
        self.health = 100

    def hunt(self):
        print(f'{self.name} is hunting.')

    def attack(self, prey):
        print(f'{self.name} attacks {prey}!')
        prey.health -= self.strength

    def move(self, direction):
        print(f'{self.name} moves {direction}.')


class PredatorManager:
    def __init__(self):
        self.predators = []

    def add_predator(self, predator):
        self.predators.append(predator)
        print(f'{predator.name} has been added to the ecosystem.')

    def manage_hunting(self):
        for predator in self.predators:
            predator.hunt()