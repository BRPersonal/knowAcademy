import numpy as np
original = np.array(
    [
        [3,2,1],
        [5,4,6],
        [0,1,3]
    ]
)
transpose = original.T
print("Original array:\n",original)
print("Transposed array:\n", transpose)

b = np.array([4,6,8,5])
print("b:", b)
print("b+1:", b + 1) #This will create new array. does not modify the original
print("b-2:", b - 2)
print("b*10:", b * 10)

#This modifies the array because we assign it back
b += 1
print("b:", b)
