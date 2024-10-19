import numpy as np

arr = np.array(
    [
        [6,5,1],
        [2,7,4],
        [9,1,3]
    ]
)

print("Largest element in array: ", arr.max())

#axis=0  means column-wise; axis=1 means row-wise
print("row-wise maximum: ", arr.max(axis = 1)) #This will be an 1-d array having max in each row
print("column-wise minimum: ", arr.min(axis = 0)) #This will be an 1-d array hacing min in each column

#These two will produce 3*3 array only.

#output will be [[6,6+5,6+5+1]...]
print("cumulative sum of each row:\n ", arr.cumsum(axis = 1))

#output will be [[6,5,1],[6+2,5+7,1+4],[6+2+9,5+7+1,1+4+3]]
print("cumulative sum of each column:\n ", arr.cumsum(axis = 0))
