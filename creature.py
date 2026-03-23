class Creature:
    def __init__(self, energy_level=100, metabolism_rate=1, learning_ability=1, gestation_period=9):
        self.energy_level = energy_level
        self.metabolism_rate = metabolism_rate
        self.learning_ability = learning_ability
        self.gestation_period = gestation_period
        self.neural_pathways = []

    def consume_energy(self, amount):
        self.energy_level -= amount
        if self.energy_level < 0:
            self.energy_level = 0

    def regenerate_energy(self):
        self.energy_level += self.metabolism_rate
        if self.energy_level > 100:
            self.energy_level = 100

    def process_stimulus(self, stimulus):
        # Process environmental stimulus
        pass

    def learn(self):
        # Improve learning ability
        self.learning_ability += 1

    def reproduce(self):
        if self.energy_level > 50:  # Must have enough energy to reproduce
            return Creature(self.energy_level // 2)  # Example of offspring creation
        else:
            raise Exception("Not enough energy to reproduce.")

    def give_birth(self):
        # Logic for giving birth
        pass
