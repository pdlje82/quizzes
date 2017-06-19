import numpy as np

def sigmoid(x):
    # TODO: Implement sigmoid function
    return 1 / (1 + np.exp(-x))

inputs = np.array([0.7, -0.3])
weights = np.array([0.1, 0.8])
bias = -0.1

# TODO: Calculate the output
assert len(inputs) == len(weights)
sum = 0
for i in range(0, len(inputs)):
    sum += inputs[i] * weights[i]

output = sigmoid(sum + bias )

print('Output:')
print(output)
