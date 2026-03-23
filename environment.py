# Environment Module

## Biome Generation

class Biome:
    def __init__(self, name, climate, resources):
        self.name = name
        self.climate = climate
        self.resources = resources

    def generate_resources(self):
        # Logic for generating resources based on biome type
        return self.resources


class BiomeGenerator:
    def __init__(self):
        self.biomes = []

    def add_biome(self, biome):
        self.biomes.append(biome)

    def generate_biomes(self):
        # Logic for biome generation
        return self.biomes


## Day/Night Cycle

class DayNightCycle:
    def __init__(self, duration):
        self.duration = duration  # Total duration of the cycle in seconds
        self.is_day = True

    def update(self, time_passed):
        # Logic to update the time and switch between day and night
        # For example, every `duration / 2` seconds switch state
        if time_passed >= self.duration / 2:
            self.is_day = not self.is_day


## Resource Management

class ResourceManager:
    def __init__(self):
        self.resources = {}

    def add_resource(self, name, amount):
        self.resources[name] = amount

    def consume_resource(self, name, amount):
        if name in self.resources:
            self.resources[name] -= amount
            if self.resources[name] < 0:
                self.resources[name] = 0  # Prevent negative resources

    def get_resources(self):
        return self.resources
