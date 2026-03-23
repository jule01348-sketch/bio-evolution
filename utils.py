import logging
import matplotlib.pyplot as plt
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def log_info(message):
    """Logs an information message."""  
    logging.info(message)


def log_error(message):
    """Logs an error message."""  
    logging.error(message)


class StatisticsTracker:
    def __init__(self):
        self.data = []

    def add_data(self, value):
        self.data.append(value)
        log_info(f'Added data: {value}')

    def mean(self):
        return np.mean(self.data)

    def median(self):
        return np.median(self.data)

    def std_dev(self):
        return np.std(self.data)


def visualize_data(data):
    """Visualizes the given data using a histogram."""  
    plt.hist(data, bins=10, alpha=0.7, color='blue')
    plt.title('Data Visualization')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()  
