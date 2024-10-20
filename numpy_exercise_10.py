import numpy as np

#create a 5*5 array prefilled with elements 1 to 24
arr1 = np.reshape(np.arange(25),(5,5))

#identify elements greater than 10.Will create boolean array
arr2 = (arr1 > 10)

#identify even elements . Will create boolean array
arr3 = (arr1 % 2 == 0)

#negate arr2
inverted_arr2 = ~arr2;

#identify whether elements are divisible by2 or 3
arr4 = (arr1 % 2 == 0) | (arr1 % 3 == 0)

#identify whether elements are divisible by2 or 3
arr5 = (arr1 % 2 == 0) & (arr1 % 3 == 0)


print("arr1=\n{}".format(arr1))
print("arr2=\n",arr2)
print("inverted_arr2=\n",inverted_arr2)
print("arr3=\n",arr3)
print(f"arr4=\n{arr4}")
print(f"arr5=\n{arr5}")



