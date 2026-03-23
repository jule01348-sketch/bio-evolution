import numpy as np

class MLP:
    def __init__(self, layers):
        self.layers = layers
        self.weights = [np.random.randn(layers[i], layers[i+1]) for i in range(len(layers)-1)]
        self.biases = [np.random.randn(1, layers[i+1]) for i in range(len(layers)-1)]

    def activation(self, x):
        return 1 / (1 + np.exp(-x))  # Sigmoid activation

    def forward(self, x):
        for w, b in zip(self.weights, self.biases):
            x = self.activation(np.dot(x, w) + b)
        return x

    def predict(self, x):
        return self.forward(x)

# Example usage
if __name__ == '__main__':
    mlp = MLP([3, 5, 1])  # Input layer of size 3, hidden layer of size 5, output layer of size 1
    sample_input = np.array([[0.1, 0.2, 0.3]])  # Sample input for the neural network
    output = mlp.predict(sample_input)
    print("Predicted output:", output)