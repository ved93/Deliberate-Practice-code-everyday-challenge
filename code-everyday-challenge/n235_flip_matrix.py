# Flip a matrix along one diagonal (without using any library) 
# Sample input =  
# [0, 0, 0, 0, 0] 
# [0, 0, 0, 0, 0] 
# [1, 0, 0, 0, 0] 
# [0, 0, 0, 0, 2] 
# [0, 0, 0, 0, 0] 

# Sample output =  
# [0, 0, 1, 0, 0] 
# [0, 0, 0, 0, 0] 
# [0, 0, 0, 0, 0] 
# [0, 0, 0, 0, 0] 
# [0, 0, 0, 2, 0] 
# Initialize a matrix n*n matrix  
# Populate random values 
# Flip the matrix 



import numpy as np

# m=np.random((3,2))
m=np.random.randint(25, size=(4,4))
print(m,m[0], m.shape, ' ')

print(m.transpose())

t = [[row[i] for row in m] for i in range(len(m))]
print(t)


