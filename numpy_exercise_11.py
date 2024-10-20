import numpy as np
import numpy.ma as np_mask

arr1 = np.zeros((4,4),dtype=int)
arr1[2,2] = 1 #set 3rd row 3rd column to 1
arr1[3,0] = 1 #set 4th row 1st column to 1
print("arr1=\n{}".format(arr1))

arr2 = np_mask.masked_equal(arr1, 1)
print("arr2=\n{}".format(arr2))

arr3 = np_mask.mask_rows(arr2) #mask rows which has atleast one masked column
print("arr3=\n{}".format(arr3))