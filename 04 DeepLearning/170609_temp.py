a = ['a1', 'a2', 'a3']
b = ['b1', 'b2']

# will iterate 2 times,
# the third value of a will not be used
print("Zip:")
i=0
for x, y in zip(a, b):
  print(x, y)
  print(i)
  i+=1


import numpy as np
from data_prep import features, targets, features_test, targets_test


def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))

# TODO: We haven't provided the sigmoid_prime function like we did in
#       the previous lesson to encourage you to come up with a more
#       efficient solution. If you need a hint, check out the comments
#       in solution.py from the previous lecture.

# Use to same seed to make debugging easier
np.random.seed(42)

n_records, n_features = features.shape
last_loss = None

# Initialize weights
weights = np.random.normal(scale=1 / n_features**.5, size=n_features)
print(weights.shape)

# Neural Network hyperparameters
epochs = 1000
learnrate = 0.5

print(weights)