import numpy as np
from utils import *
    
arr = np.array([
            [-1,2,0,4,5],
            [4,-5,6,0,6],
            [2,0,7,8,7],
            [3,-7,4,2,8]
        ])

#create a temp arr with first two rows and n columns - column 1 and then 4th , then 7th an so on
temp = arr[:2,::3]

#create a temp2 array , by choosing what rows u want, and what specific column you want in each of that row
#Note that this will be single dimensional array
temp2 = arr[[3,2,1,0,0],[0,1,2,3,4]]

#create a temp3 array this time having only positive values
#Note that this will be single dimensional array
cond = arr > 0
temp3 = arr[cond]


print("original array:\n",arr)
describe_np_array(arr)

print("arr with first two rows and first and fourth columns :\n", temp)
describe_np_array(temp)

print("arr which is cherry picked:", temp2)
describe_np_array(temp2)

print("arr with only positive alues:", temp3)
describe_np_array(temp3)





