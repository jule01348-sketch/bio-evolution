# Configuration for the Simulator

# Simulation Speed
simulation_speed = 1.0  # Speed of the simulation (1.0 is normal speed)

# Environment Parameters
environment = {
    'temperature': 22.0,  # Degrees Celsius
    'humidity': 50,       # Percentage
    'resources': {
        'food': 1000,     # Amount of food available
        'water': 500      # Amount of water available
    }
}

# Creature Defaults
creature_defaults = {
    'size': 1.0,          # Default size of creatures
    'speed': 1.0,         # Default movement speed
    'lifespan': 10,       # Lifespan in years
}

# Metabolism Rates
metabolism_rates = {
    'base_rate': 0.1,     # Base metabolism rate
    'activity_multiplier': 2.0  # Multiplier based on activity level
}

# Reproduction Settings
reproduction_settings = {
    'max_offspring': 3,    # Maximum offspring per reproduction
    'maturity_age': 2      # Age at which creatures can reproduce
}

# Logging Options
logging_options = {
    'log_level': 'INFO',   # Logging level of detail: DEBUG, INFO, WARNING, ERROR
    'log_file': 'simulation.log'  # File to log outputs
}