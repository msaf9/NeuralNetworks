#Using for loop
inputs = [2.1,7.3,5.9,6.8]
weight = [[-6.2,7.1,9.4,2.8],
 			[7.2,8.4,-6.6,7.9],
				[4.1,-2.9,3.9,8.3]]
biases = [3.5,0.8,1.3]

layer_output=[]
for weights, bias in zip(weight, biases):
	output=0
	for new_in, new_wei in zip(inputs,weights):
		output+=new_in*new_wei
	output+=bias
	layer_output.append(output)

print(layer_output)