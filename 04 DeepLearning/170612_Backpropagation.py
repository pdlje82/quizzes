import numpy as np


def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))


x = np.array([0.5, 0.1, -0.2])
target = 0.6
learnrate = 0.5

weights_input_hidden = np.array([[0.5, -0.6],
                                 [0.1, -0.2],
                                 [0.1, 0.7]])

weights_hidden_output = np.array([0.1, -0.3])

## Forward pass
hidden_layer_input = np.dot(x, weights_input_hidden)
hidden_layer_output = sigmoid(hidden_layer_input)

#print(hidden_layer_output)

output_layer_in = np.dot(hidden_layer_output, weights_hidden_output)
#print(output_layer_in)
output = sigmoid(output_layer_in)
#print(output)

## Backwards pass
## TODO: Calculate output error
error = target - output

# TODO: Calculate error term for output layer
output_error_term = error * output * ( 1 - output )

# TODO: Calculate error term for hidden layer
hidden_error_term = np.dot(weights_hidden_output, output_error_term) * hidden_layer_output * (1 - hidden_layer_output)
#print(hidden_error_term)

# TODO: Calculate change in weights for hidden layer to output layer
delta_w_h_o = learnrate * output_error_term * hidden_layer_output

# TODO: Calculate change in weights for input layer to hidden layer
'''Also, w​_ij​​ is a matrix now, so the right side of the assignment must have the same shape as the left side. Luckily, 
Numpy takes care of this for us. If you multiply a row vector array with a column vector array, it will multiply the 
first element in the column by each element in the row vector and set that as the first row in a new 2D array. This 
continues for each element in the column vector, so you get a 2D array that has 
shape (len(column_vector), len(row_vector)).'''

delta_w_i_h = learnrate * hidden_error_term * x[:, None]

print(hidden_error_term)
print(x[:, None])
print(hidden_error_term * x[:, None])

#print('Change in weights for hidden layer to output layer:')
#print(delta_w_h_o)
#print('Change in weights for input layer to hidden layer:')
#print(delta_w_i_h)
