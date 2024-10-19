import numpy as np

#generate a random 2-d array with 5 rows and 8 columns and elements in range 10 to 50
arr1 = np.random.randint(10,50,size=(5,8))

#generate a random 3-d array with 2 arrays of size 3 rows and 6 columns and elements in range 1 to 20
arr2 = np.random.randint(1,20,size=(2,3,6))

print("arr1=\n", arr1)
print("arr2=\n", arr2)
