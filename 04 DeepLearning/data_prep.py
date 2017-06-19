import numpy as np
import pandas as pd

admissions = pd.read_csv('binary.csv')

# Make dummy variables for rank
data = pd.concat([admissions, pd.get_dummies(admissions['rank'], prefix='rank')], axis=1)
data = data.drop('rank', axis=1)

# Standarize features
'''We'll need to standardize the GRE and GPA data, which means to scale the values such they have zero mean and 
a standard deviation of 1. This is necessary because the sigmoid function squashes really small and really large inputs. 
The gradient of really small and large inputs is zero, which means that the gradient descent step will go to zero too. 
Since the GRE and GPA values are fairly large, we have to be really careful about how we initialize the weights or the 
gradient descent steps will die off and the network won't train. Instead, if we standardize the data, we can initialize 
the weights easily and everyone is happy.'''

for field in ['gre', 'gpa']:
    mean, std = data[field].mean(), data[field].std()
    data.loc[:, field] = (data[field] - mean) / std

# Split off random 10% of the data for testing
np.random.seed(43)
sample = np.random.choice(data.index, size=int(len(data) * 0.9), replace=False)
data, test_data = data.ix[sample], data.drop(sample)

# Split into features and targets
features, targets = data.drop('admit', axis=1), data['admit']
features_test, targets_test = test_data.drop('admit', axis=1), test_data['admit']