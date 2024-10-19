import numpy as np
a1 = np.array([ 
    [2,1],
    [4,3]
])

a2 = np.array([ 
    [3,4],
    [1,2]
])

print ("2-d array addition:\n", a1 + a2)
print("2-d array multiplication:\n", a1 * a2)

#r(1,1) = first row of a1 multiplied by first column of a2 and summed up
#r(1,2) = first row of a1 multiplied by second column of a2 and summed up
#r(2,1) = second row of a1 multiplied by first column of a2 and summed up
#r(2,2) = second row of a1 multiplied by second column of a2 and summed up
print("matrix multiplication:\n", a1.dot(a2))

#Has a1 changed? No
print("a1:\n", a1)
