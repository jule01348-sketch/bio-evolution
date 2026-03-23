import random
import numpy as np
from creature import Creature
from environment import Biome, BiomeGenerator, DayNightCycle, ResourceManager
from predator import Predator, PredatorManager
from utils import StatisticsTracker, log_info, log_error
import matplotlib.pyplot as plt

class Simulation:
    def __init__(self, width=50, height=50, num_creatures=10, num_predators=3, simulation_time=3600):
        self.width = width
        self.height = height
        self.time = 0
        self.simulation_time = simulation_time
        
        # Initialize creatures
        self.creatures = []
        for _ in range(num_creatures):
            x = random.uniform(0, width)
            y = random.uniform(0, height)
            self.creatures.append(Creature())
        
        # Initialize environment
        self.biome_generator = BiomeGenerator()
        self.resource_manager = ResourceManager()
        self.day_night_cycle = DayNightCycle(240)  # 240 ticks for full day/night cycle
        
        # Initialize predators
        self.predator_manager = PredatorManager()
        for _ in range(num_predators):
            predator = Predator(f'Predator_{_}', strength=random.uniform(10, 20))
            self.predator_manager.add_predator(predator)
        
        # Statistics tracking
        self.stats = StatisticsTracker()
        self.population_history = []
        self.energy_history = []
        
        log_info(f'Simulation initialized with {num_creatures} creatures and {num_predators} predators')

    def step(self):
        """Execute one simulation step"""
        self.time += 1
        
        # Update day/night cycle
        self.day_night_cycle.update(self.time)
        
        # Update creatures
        alive_creatures = []
        for creature in self.creatures:
            creature.update(self.time)
            
            # Check for reproduction
            if creature.energy_level > 70:
                if random.random() < 0.05:  # 5% chance to reproduce
                    offspring = creature.reproduce()
                    if offspring:
                        alive_creatures.append(offspring)
            
            if creature.energy_level > 0:
                alive_creatures.append(creature)
        
        self.creatures = alive_creatures
        
        # Update predators
        self.predator_manager.manage_hunting()
        
        # Track statistics
        avg_energy = np.mean([c.energy_level for c in self.creatures]) if self.creatures else 0
        self.stats.add_data(avg_energy)
        self.population_history.append(len(self.creatures))
        self.energy_history.append(avg_energy)
        
        if self.time % 100 == 0:
            log_info(f'Time: {self.time}, Population: {len(self.creatures)}, Avg Energy: {avg_energy:.2f}')

    def run(self):
        """Run the full simulation"""
        log_info('Starting simulation...')
        
        while self.time < self.simulation_time:
            self.step()
            
            # Stop if population dies out
            if len(self.creatures) == 0:
                log_info('Population extinct!')
                break
        
        log_info(f'Simulation complete. Final population: {len(self.creatures)}')

    def visualize_results(self):
        """Visualize simulation results"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
        
        # Population over time
        ax1.plot(self.population_history)
        ax1.set_xlabel('Time (ticks)')
        ax1.set_ylabel('Population')
        ax1.set_title('Population Over Time')
        ax1.grid(True)
        
        # Average energy over time
        ax2.plot(self.energy_history)
        ax2.set_xlabel('Time (ticks)')
        ax2.set_ylabel('Average Energy')
        ax2.set_title('Average Energy Over Time')
        ax2.grid(True)
        
        plt.tight_layout()
        plt.show()

    def save_stats(self, filename='simulation_stats.txt'):
        """Save statistics to file"""
        with open(filename, 'w') as f:
            f.write(f'Final Population: {len(self.creatures)}\n')
            f.write(f'Mean Energy: {self.stats.mean():.2f}\n')
            f.write(f'Median Energy: {self.stats.median():.2f}\n')
            f.write(f'Std Dev: {self.stats.std_dev():.2f}\n')
        log_info(f'Statistics saved to {filename}')


if __name__ == '__main__':
    # Create and run simulation
    sim = Simulation(width=50, height=50, num_creatures=10, num_predators=3, simulation_time=3600)
    sim.run()
    sim.visualize_results()
    sim.save_stats()