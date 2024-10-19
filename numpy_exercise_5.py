import numpy as np

arr1 = np.array([11,21,31,41,49])
arr2 = np.array([[1,9,21],[29,41,51],[58,72,9]])
arr3 = np.array([[15,7,10,-11,20,75],[-3,9,24,1,100,-14]])

print("column-wise sum of arr1=", arr1.sum(axis=0)) #type is np.int64
print("column-wise sum of arr2=",arr2.sum(axis=0)) #type is np.ndarray
print("column-wise average of arr2=",np.average(arr2,axis=0))
print("column-wise average of arr3=",np.average(arr3,axis=0))
print("index of minimum element in arr3=", np.argmin(arr3)) #treating as 1-d array 

print("row-wise minimum in arr2=", np.min(arr2,axis=1))
print("row-wise minimum in arr3=", np.min(arr3,axis=1))

computation on Arrays:BroadCasting



