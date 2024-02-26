#  here we have only 1 neurone and get unput of 3 
# input = [1,2,3, 2.5]
# weights = [0.2 , 0.8 , -0.5,1-0]
# bias = 2

# output = input[0]*weights[0] + input[1]*weights[1] +input[2]*weights[2] +input[3]*weights[3]+ bias
# print(output)



# what if we have 3 neurons and get input that is output of 4 neuron layer
# input = [1,2,3, 2.5]
# weights1 = [0.2 , 0.8 , -0.5,1-0]
# weights2 = [0.5, -0.91, 0.26 ,- 0.5]

# weights3 = [-0.26, -0.27 , 0.17 , 0.87]

# bias1 = 2 
# bias2 = 3
# bias3 = 0.5

# output1 = input[0]*weights1[0] + input[1]*weights1[1] + input[2]*weights1[2]+ input[3]*weights1[3] + bias1
# output2 = input[0]*weights2[0] + input[1]*weights2[1] + input[2]*weights2[2]+ input[3]*weights2[3] + bias2
# output3 = input[0]*weights3[0] + input[1]*weights3[1] + input[2]*weights3[2]+ input[3]*weights3[3] + bias3

# print(output1)
# print(output2)
# print(output3)



################### Now we are using vectors and metrics  dont raw python #################
# import numpy as np 
# input = [1,2,3, 2.5]


# weights =  [[0.2 , 0.8 , -0.5,1-0],[0.5, -0.91, 0.26 ,- 0.5],[-0.26, -0.27 , 0.17 , 0.87] ]
# weights_array = np.array(weights)
# input_array = np.array(input)
# bias = [2, 3, 0.5]

# import numpy as np

# # output = np.dot(weights, input_array.T) + bias
# # print(output)
# print(weights_array.T)
# print(input_array.shape)


#######################

# batch of input values and modeling a 2 layers of neurons 
# import numpy as np
# input = [[1,2,3, 2.5],
#          [2.0,5.0,-1.0,2.0],
#          [-1.5,2.7,3.3,-0.8]]
# input_array = np.array(input)
# weights = [[0.2 , 0.8 , -0.5,1-0],
#            [0.5, -0.91, 0.26 ,- 0.5],
#            [-0.26, -0.27 , 0.17 , 0.87] ]

# bias = [2, 3, 0.5]

# weights2 = [[0.1 , -0.14 , 0.5],
#            [-0.5, 0.12,-0.33 ],
#            [-0.44, 0.73 , -0.13] ]

# bias2 = [-1 , 2 , -0.5]

# layer1 = np.dot(input , np.array(weights).T) + bias
# layer2 = np.dot(layer1 , np.array(weights2).T) + bias2

# print(layer2)


##  now we gonna do the things in objects 

X = [[1,2,3, 2.5],
     [2.0,5.0,-1.0,2.0],
     [-1.5,2.7,3.3,-0.8]]




class Layer_Dense:
    def __init__(self):
        pass
    def forward(self):
        pass