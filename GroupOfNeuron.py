#Using for Group of neuron inputs
import numpy as np
inputs = [[2.1, 7.3, 5.9, 6.2],
			[8.5, -0.3, 7.1, 4.21],
				[5.2, -2.1, 4.6, -0.29]]

weight = [[-6.2, 7.1, 9.4, 2.8],
 			[7.2, 8.4, -6.6, 7.9],
				[4.1, -2.9, 3.9, 8.3]]
biases = [3.5,0.8,1.3]

output = np.dot(inputs, np.array(weight).T) + biases
print(output)