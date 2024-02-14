#Transpose
import numpy as np

weight = [[-6.2, 7.1, 9.4, 2.8],
 			[7.2, 8.4, -6.6, 7.9],
			[4.1, -2.9, 3.9, 8.3]]
			
output = np.array(weight).T
print(output)