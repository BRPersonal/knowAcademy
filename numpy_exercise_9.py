import numpy as np
from utils import *

arr1 = np.array([0,2,3,0,1,6,5,2])
arr2 = np.greater(arr1,0)

print("arr1=\n", arr1)
print("arr2=\n", arr2)

arr3 = np.random.randint(1,20,size=(2,3,6))
arr4 = np.not_equal(arr3,5)

print("arr3=\n", arr3)
print("arr4=\n", arr4)


describe_np_array(arr2)
describe_np_array(arr4)