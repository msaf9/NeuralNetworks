#Using for Numpy
import numpy as np
inputs = [2.1,7.3,5.9,6.8]
weight = [[-6.2,7.1,9.4,2.8],
 			[7.2,8.4,-6.6,7.9],
				[4.1,-2.9,3.9,8.3]]
biases = [3.5,0.8,1.3]

output=np.dot(weight,inputs) + biases
print(output)