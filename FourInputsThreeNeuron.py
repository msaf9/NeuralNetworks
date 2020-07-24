#Three neuron and four inputs
inputs = [2.3,5.4,1.8,-0.5]
weight1 = [-6.2,7.1,9.4,2.8]
weight2 = [7.2,8.4,-6.6,7.9]
weight3 = [4.1,-2.9,3.9,8.3]

bias1 = 3
bias2 = 2
bias3 = 0.8

outputs = [inputs[0]*weight1[0] + inputs[1]*weight1[1] + inputs[2]*weight1[2] + inputs[3]*weight1[3] + bias1,
			inputs[0]*weight2[0] + inputs[1]*weight2[1] + inputs[2]*weight2[2] + inputs[3]*weight2[3] + bias2,
				inputs[0]*weight3[0] + inputs[1]*weight3[1] + inputs[2]*weight3[2] + inputs[3]*weight3[3] + bias3]

print(outputs)